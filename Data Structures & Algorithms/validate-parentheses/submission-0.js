class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        let t = {
            "(":0,
            "{":0,
            "[":0
        }
        let open = ["(","{","["]
        

        for (let ch of s){

            if (open.includes(ch)){
                t[ch] += 1
            } else{
                if (ch == ")"){
                    t["("]--
                }
                if (ch == "}"){
                    t["{"]--
                }
                if (ch == "]"){
                    t["["]--
                }
            }

        }


        if (t["("] != 0 || t["{"] != 0  || t["["] != 0 ){
            return false
        } else {
            return true
        }
    }
}
