class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        d=0
        n=len(word)
        for i in range(n):
            if word[i]==ch:
                d=i
                break
        print(d)
        g=list(word)
        i=0
        j=d
        while i<j:
            g[i],g[j]=g[j],g[i]
            i+=1
            j-=1
        return ''.join(g)
        
        
