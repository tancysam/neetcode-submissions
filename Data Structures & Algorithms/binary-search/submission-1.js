class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let i = -1

        let mid = Math.floor(nums.length/2)
        if (target >= nums[mid]){
            for (i = mid; i < nums.length; i++){
                if (nums[i] == target){
                    return i
                }
            }
        }

        if (target < nums[mid]){
            for (i = 0; i < mid; i++){
                if (nums[i] == target){
                    return i
                }
            }
        }

        return -1
    }
}
