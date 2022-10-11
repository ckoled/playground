pub enum Feature {
  Area,
  Perimeter
}

pub struct Circle {
  radius: f64
}

impl Circle {
  pub fn new(radius: f64) -> Circle {
      Circle {radius}
  }

  pub fn get_feature(&self, feature: Feature) -> f64 {
      match feature {
          Feature::Area => self.calc_area(),
          Feature::Perimeter => self.calc_circumference()
      }
  }

  fn calc_area(&self) -> f64 {
      std::f64::consts::PI * self.radius.powi(2)
  }

  fn calc_circumference(&self) -> f64 {
      2.0 * std::f64::consts::PI * self.radius
  }
}

pub struct Rectangle {
  width: f64,
  height: f64
}

impl Rectangle {
  pub fn new(width: f64, height: f64) -> Rectangle {
      Rectangle {width, height}
  }

  pub fn get_feature(&self, feature: Feature) -> f64 {
      match feature {
          Feature::Area => self.calc_area(),
          Feature::Perimeter => self.calc_perimeter()
      }
  }

  fn calc_area(&self) -> f64 {
      self.width * self.height
  }

  fn calc_perimeter(&self) -> f64 {
      2.0 * self.width + 2.0 * self.height
  }
}

pub fn highest_divisor(n: u32) -> u32 {
  let n_sqrt = (n as f32).sqrt().floor() as u32;
  for i in (1..=((n as f32/2.).floor() as u32)).rev() {
    for j in 1..n_sqrt {
      if i*j == n {
        return i;
      }
    }
  }
  return 0;
}

#[cfg(test)]
mod tests {
  use super::*;
  use std::f64::consts::PI;
  
  #[test]
  fn ut_circle() {
    let circle = Circle::new(1.);
    assert_eq!(circle.get_feature(Feature::Area), PI);
    assert_eq!(circle.calc_area(), PI);
    assert_eq!(circle.get_feature(Feature::Perimeter), 2. * PI);
    assert_eq!(circle.calc_circumference(), 2. * PI);
  }

  #[test]
  fn ut_rectangle() {
    let rectangle = Rectangle::new(1., 2.);
    assert_eq!(rectangle.get_feature(Feature::Area), 2.);
    assert_eq!(rectangle.calc_area(), 2.);
    assert_eq!(rectangle.get_feature(Feature::Perimeter), 6.);
    assert_eq!(rectangle.calc_perimeter(), 6.);
  }
}