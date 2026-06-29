class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let countDict = {}
        for (let num of nums){
            if (num in countDict){
                return true
            } else {
                countDict[num] = 1
            }
        }
        return false
    }
}
