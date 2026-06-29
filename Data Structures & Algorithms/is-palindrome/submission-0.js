class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        s = s.replace(/[^a-z0-9]/gi, '').toLowerCase()

        for (let i = 0; i < (s.length/2 + 1); i++){
            let a = s[i]
            let b = s[s.length - 1 -i]

            if (a != b){
                console.log(a,b)
                return false
            }
        }

        return true
    }
}
