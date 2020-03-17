//Source-https://leetcode.com/problems/longest-substring-without-repeating-characters/
//Author-Uditanshu

Question-
******************************************
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
*****************************************
Solution-
*****************************************
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        j=0
        a=""
        l=[]
        while i!=len(s):
            for j in range(i,len(s)):
                if s[j] not in a:
                    a+=s[j]

                else:
                    l.append(len(a))
                    a=""
                    i+=1
                    j=i
                    break
        return(max(l,default=0))

*****************************************
