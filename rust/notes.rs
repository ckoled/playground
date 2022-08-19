// use std::fmt;

// enum Location {
//     Unknown,
//     Anonymous,
//     Known(f64, f64)
// }
// impl fmt::Display for Location {
//     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
//         match self {
//             Self::Unknown => write!(f, "idk bruh"),
//             Self::Anonymous => write!(f, "its over there"),
//             Self::Known(lat, long) => write!(f, "latitude: {lat}, longitude: {long}")
//         }
//     }
// }

// fn main() {
//     let address = Location::Unknown;
//     println!("address is {address}");
//     let address = Location::Anonymous;
//     println!("address is {address}");
//     let address = Location::Known(28.608295, -80.604177);
//     println!("address is {address}");
// }


// use std::fmt;

// struct Satellite {
//     name: String,
//     velocity: f64
// }
// impl fmt::Display for Satellite {
//     fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
//         write!(f, "{} is going {} mi/s", self.name, self.velocity)
//     }
// }

// fn main() {
//     let hubble = Satellite {
//         name: String::from("Hubble Telescope"),
//         velocity: 4.72
//     };
//     println!("hubble is {hubble}");
// }


// use std::ops::Add;

// fn sum_boxes<T: Add<Output=T>>(a: Box<T>, b: Box<T>) -> Box<T> {
//     Box::new(*a + *b)
// }

// fn main() {
//     let one = Box::new(1);
//     let two = Box::new(2);
//     assert_eq!(*sum_boxes(one, two), 3);

//     let pi = Box::new(3.14159);
//     let e = Box::new(2.71828);
//     assert_eq!(*sum_boxes(pi, e), 5.85987);

//     println!("Tests passed!");
// }


// #[derive(PartialEq, PartialOrd)]
// struct Rectangle {
//     width: f64,
//     height: f64
// }
// impl Rectangle {
//     fn get_area(&self) -> f64 {
//         self.width * self.height
//     }
//     fn scale(&mut self, val: f64) {
//         self.width *= val;
//         self.height *= val;
//     }
//     fn new(width: f64, height: f64) -> Rectangle {
//         Rectangle { width, height }
//     }
// }
// trait Description {
//     fn describe(&self) -> String {
//         format!("This is an object")
//     }
// }
// impl Description for Rectangle {
//     fn describe(&self) -> String {
//         format!("width: {}, height: {}", self.width, self.height)
//     }
// }

// fn main() {
//     let mut rect = Rectangle::new(1.2, 3.4);
//     assert_eq!(rect.get_area(), 4.08);
//     rect.scale(0.5);
//     assert_eq!(rect.get_area(), 1.02);
//     let rect2 = Rectangle::new(1., 4.);
//     println!("Rect > Rect2: {}", rect>rect2);
//     println!("Rectangle is {}", rect.describe());
//     println!("Tests passed!");
// }


// use std::io;
// use rand::{thread_rng, Rng};

// fn main() {
//     let num = thread_rng().gen_range(1..101);
//     println!("generated random number ***");
//     loop {
//         let mut buf = String::new();
//         println!("Enter guess (1-100):");
//         match io::stdin().read_line(&mut buf){
//             Ok(_) => (),
//             Err(_) => {
//                 println!("Could not read input");
//                 continue;
//             }
//         };
//         let guess = match buf.trim().parse::<i32>() {
//             Ok(s) => s,
//             Err(_) => {
//                 println!("Not an integer");
//                 continue;
//             }
//         };
//         if guess == num { break; }
//         else if guess > num { println!("Lower!") }
//         else { println!("Higher!") }
//     }
//     println!("Correct! 😁");
// }


// fn main() {
//     let mut buf = String::new();
//     println!("Enter first number: ");
//     io::stdin().read_line(&mut buf).unwrap();
//     let num1: f32 = buf.trim().parse().unwrap();
//     buf.clear();
//     println!("Enter second number: ");
//     io::stdin().read_line(&mut buf).unwrap();
//     let num2: f32 = buf.trim().parse().unwrap();
//     buf.clear();
//     println!("Enter operation(+, -, *, /): ");
//     io::stdin().read_line(&mut buf).unwrap();
//     match buf.trim() {
//         "+" => println!("{}", num1 + num2),
//         "-" => println!("{}", num1 - num2),
//         "*" => println!("{}", num1 * num2),
//         "/" => println!("{}", num1 / num2),
//         _ => panic!("invalid operation")
//     }
// }


// fn main() {

//     // Stack
//     let mut msg = ['h', 'e', 'l', 'l', 'o'];

//     // Heap, str(slice) type contains ptr and len
//     let message = String::from("World");

//     // str works with String

//     for item in msg.iter_mut() {
//         println!("item {}", item);
//         if *item == 'e' {
//             *item = '3';
//         }
//     }

//     println!("{:?}", msg);
//     // Scope
//     {
//         let message = String::from("Hello");
//         println!("{message}")
//     }
//     println!("{message}");

// }
