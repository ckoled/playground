function twoSum(nums: number[], target: number): number[] {
  const pNums: number[] = []
  for (let i=0;i<nums.length;i++) {
    const idx = pNums.indexOf(target-nums[i])
    if (idx >= 0)
      return [idx, i]
    pNums.push(nums[i])
  }
  return []
};

const target = 9
const nums = [2,7,11,15]
console.log(twoSum(nums, target))