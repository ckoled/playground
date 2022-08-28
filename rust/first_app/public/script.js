let count = document.getElementById("count");

function increment() {
  fetch("/add/1")
}

function subscribe(uri) {
  function connect(uri) {
    const events = new EventSource(uri);

    events.addEventListener("message", (ev) => {
      console.log(ev.data)
      count.innerText = ev.data
    })

    events.addEventListener("open", () => {
      console.log("connected")
    })

    events.addEventListener("error", () => {
      events.close()
      console.error("error")
    })
  }
  connect(uri);
}

function init() {
  subscribe("/count");
}
init()