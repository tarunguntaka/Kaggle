
#s = "abcabcbb"
#output = 3
# def lsub(s:str) -> int:

#     charset = set()
#     l = 0 
#     res = 0 
#     for r in range(len(s)):
#         while s[r] in charset:
#             charset.remove(s[l])
#             l+=1 
#         charset.add(s[r])
#         res = max(res, r-l+1)
    
#     return res 




'''best solution approach'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        n = len(s)
        
        l = 0 
        res = 0 
        
        d = {}
        
        for r in range(n):
            if s[r] in d:
                l = max(l,d[s[r]])
            res = max(res,r-l+1)
            
            d[s[r]] = r + 1
        return res 
            
s1 = Solution()
print(s1.lengthOfLongestSubstring("abcabcbb"))



'''solution idea is sliding window and how a window is managed, '''