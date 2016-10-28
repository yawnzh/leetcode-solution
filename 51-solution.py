class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        verticle=[False]*n
        diagonal_1=[False]*(2*n-1)
        diagonal_2=[False]*(2*n-1)
        board=[['.']*n for i in range(n)]
        self.res=[]
        self.helper(board,0,verticle,diagonal_1,diagonal_2)
        return self.res
        
        
    def helper(self,board,i,v,d1,d2):
        n=len(board)
        if i==n:
            self.res.append([''.join(board[i]) for i in range(n)])
        line=board[i]
        for j in range(n):
            if line[j]=='.' and not v[j] and not d1[i+j-1] and not d2[i-j+n-1]:
                line[j]='Q'
                v[j]=True
                d1[i+j-1]=True
                d2[i-j+n-1]=True
                self.helper(board,i+1,v,d1,d2)
                line[j]='.'
                v[j]=False
                d1[i+j-1]=False
                d2[i-j+n-1]=False