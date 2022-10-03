class Solution:
    def simplifyPath(self, path: str) -> str:
        s=[]
        p=path.split('/')
        for t in p:
            if t not in ['.','..','']:
                s.append('/'+t)
            elif t=='..' and s:
                s.pop()
        return ''.join(s) if s else '/'
