use rocket::response::stream::TextStream;
use rocket::{fs::FileServer, State, Shutdown};
use rocket::tokio::sync::broadcast::{channel, Sender, error::RecvError};
use rocket::tokio::select;

#[macro_use] extern crate rocket;


#[get("/count")]
async fn count(queue: &State<Sender<&'static str>>, mut end: Shutdown) -> TextStream![&'static str] {
    let mut rx = queue.subscribe();
    TextStream! {
        loop {
            let num = select! {
                num = rx.recv() => match num {
                    Ok(num) => num,
                    Err(RecvError::Closed) => break,
                    Err(RecvError::Lagged(_)) => continue,
                },
                _ = &mut end => break,
            };

            yield num;
        }
    }
}

#[get("/add/<num>")]
fn add(num: u32, queue: &State<Sender<&'static str>>) {
    let msg = (num + 1).to_string().into_boxed_str();
    let _res = queue.send(Box::leak(msg));
}

#[launch]
fn rocket() -> _ {
    rocket::build()
        .manage(channel::<&'static str>(1024).0)
        .mount("/", routes![add, count])
        .mount("/", FileServer::from("public/"))
}