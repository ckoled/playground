fn main() {
  let hello = ['h', 'e', 'l', 'l', 'o'];
  for (i, ch) in hello.iter().rev().enumerate() {
    println!("{ch} at pos {i}");
  }
}