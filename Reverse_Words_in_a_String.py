
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        for i in s:
            if i == ' ':
                s.remove(i)
        
        return ' '.join(s[::-1])
        

# a = Solution()
# s = "the sky is blue" 
# s = " hello world "
# s = "a good example"
# print(a.reverseWords(s))


