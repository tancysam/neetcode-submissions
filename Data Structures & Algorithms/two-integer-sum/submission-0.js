class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let calcSums = {}
        for (let i = 0; i < nums.length; i++){
            let diff = target - nums[i]

            if (diff in calcSums){
                return [calcSums[diff],i]
            } else {
                calcSums[nums[i]]= i
            }
            console.log(calcSums)
        }
        
    }
}
