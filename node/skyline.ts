// really bad
function getSkyline(buildings: number[][]): number[][] {
  let solutions: number[][] = [[buildings[0][0], buildings[0][2]]]
  let height = buildings[0][2]
  for (const b of buildings) {
    for (let i = b[0]; i != b[1]; i = b[1]) {
      let softMax = 0
      for (const building of buildings) {
        if (building[0] <= i && building[1] >= i && softMax < building[2])
          softMax = building[2]
      }
      if (softMax != height) {
        solutions.push([softMax<height?i-1:i, softMax])
        height = softMax
      }
    }
  }
  solutions.push([buildings[buildings.length-1][1], 0])
  return solutions
}