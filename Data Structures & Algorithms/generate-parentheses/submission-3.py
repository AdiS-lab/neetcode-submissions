class Solution:
    def generateParenthesis(self, n):
        res = []
        def bt(s, open_, close):
            if len(s) == 2 * n:
                res.append(s); return
            if open_ < n:      
                bt(s + '(', open_ + 1, close)
            if close < open_: 
                 bt(s + ')', open_, close + 1)
        bt('', 0, 0)
        return res
        