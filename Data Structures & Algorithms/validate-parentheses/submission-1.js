class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let t = []
        let open = ["(", "{", "["]


        for (let ch of s) {
            if (open.includes(ch)) {
                t.push(ch)
            } else {
                let l = t.pop()
                if (ch == ")" && l == "(") {

                } else if (ch == "}" && l == "{") {

                } else if (ch == "]" && l == "[") {

                } else {
                    return false
                }
            }
        }
        if (t.length == 0) {
            return true
        } else {
            return false
        }
    }
}
