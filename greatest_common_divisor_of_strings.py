class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        idx = gcd(len(str1), len(str2))
        
        return str1[:idx]
        

a = Solution()
str1 = "ABCABC"
str2 = "ABC"

print(a.gcdOfStrings(str1, str2))

str1 = "ABABAB" 
str2 = "ABAB"

print(a.gcdOfStrings(str1, str2))

str1 = "LEET"
str2 = "CODE"

print(a.gcdOfStrings(str1, str2))



