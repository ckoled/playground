// really bad
function getSkyline(buildings: number[][]): number[][] {

  const solutions = new Map<number, number>();
  const ends: number[] = []

  const inRange = (point: number, height: number) => {
    for (const b of buildings) {
      if (b[0] <= point && b[1] >= point) {
        if (height > b[2])
          solutions.set(point, height)
        return true
      }
      return false
    }
  }

  solutions.set(buildings[0][0], buildings[0][2])
  solutions.set(buildings[0][1], buildings[0][2])
  ends.push(buildings[0][1])
  for (let i = 1; i < buildings.length; i++) {
    inRange(buildings[i][0], buildings[i][2])
    if (!inRange(buildings[i][1], buildings[i][2])) ends.push()
  }

  const temp: number[][] = []

  solutions.forEach((v, k) => {
    if (k+1 == 3) console.log("nope")
  })

  return temp;

  // let solutions: number[][] = [[buildings[0][0], buildings[0][2]]]
  // let height = buildings[0][2]
  // for (const b of buildings) {
  //   for (let i = b[0]; i != b[1]; i = b[1]) {
  //     let softMax = 0
  //     for (const building of buildings) {
  //       if (building[0] <= i && building[1] >= i && softMax < building[2])
  //         softMax = building[2]
  //     }
  //     if (softMax != height) {
  //       solutions.push([softMax<height?i-1:i, softMax])
  //       height = softMax
  //     }
  //   }
  // }
  // solutions.push([buildings[buildings.length-1][1], 0])
  // return solutions
}