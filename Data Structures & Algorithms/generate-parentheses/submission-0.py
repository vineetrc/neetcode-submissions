class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        out = []

        def dfs(s, c , res):

            if s + c == 2 * n:
                out.append("".join(res.copy()))
                return
            
            if s < n:
                res.append("(")
                dfs(s+1, c, res)
                res.pop()

            if c < s :
                res.append(")")
                dfs(s,c+1,res)
                res.pop()
            
        dfs(0,0,[])
        print(out)
        return out