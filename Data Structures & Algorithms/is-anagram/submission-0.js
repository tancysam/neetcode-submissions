class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        s = s.split("")
        t = t.split("")
        s = s.sort().join("")
        t = t.sort().join("")


        if (s == t){
            return true
        } else {
            return false
        }
    }
}
