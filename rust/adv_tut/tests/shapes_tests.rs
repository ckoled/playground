use adv_tut::*;
use rand::prelude::*;
use std::f64::consts::PI;

#[test]
fn it_circle() {
  let r: f64 = thread_rng().gen_range(0.0..101.0);
  let circle = Circle::new(r);
  assert_eq!(circle.get_feature(Feature::Area), PI * r.powi(2));
  assert_eq!(circle.get_feature(Feature::Perimeter), PI * r * 2.);
}

#[test]
fn it_rectangle() {
  let w: f64 = thread_rng().gen_range(0.0..101.0);
  let h: f64 = thread_rng().gen_range(0.0..101.0);
  let rect = Rectangle::new(w, h);
  assert_eq!(rect.get_feature(Feature::Area), w * h);
  assert_eq!(rect.get_feature(Feature::Perimeter), 2. * w + 2. * h);
}