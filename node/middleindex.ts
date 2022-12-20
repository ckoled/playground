function findMiddleIndex(nums: number[]): number {
  let middleIndex = -1
  let current = Math.floor(nums.length/2)
  let leftSum, rightSum
  let direction
  do {
    leftSum = nums.reduce((prev, v, i, arr) => {
      if (i>current) return prev;
      return prev + v
    }, 0)
    rightSum = nums.reduce((prev, v, i, arr) => {
      if (i<current) return prev;
      return prev + v
    }, 0)

    if (leftSum > rightSum) {
      if (!direction) direction = 0
      if (direction == 1) break
      current--
    }
    else if (leftSum < rightSum) {
      if (!direction) direction = 1
      if (direction == 0) break
      current++
    } else {
      middleIndex = current
      if (!direction) direction = 0
      if (direction == 1) break
      current--
    }
    
  } while (current >= 0 && current < nums.length)

  return middleIndex
};