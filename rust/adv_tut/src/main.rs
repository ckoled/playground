use adv_tut::*;

fn main() {
    // let rect = Rectangle::new(1.0, 2.0);
    // let area = rect.get_feature(Feature::Area);
    // println!("rect area is {}", area);

    // let circ = Circle::new(3.0);
    // let perimeter = circ.get_feature(Feature::Perimeter);
    // println!("circ perimeter is {}", perimeter);
    let num = highest_divisor((2 as u32).pow(18)+1);
    println!("{num}");
}
