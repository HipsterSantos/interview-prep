"""20. Valid Parentheses
Easy
Topics
Companies
Hint

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

 

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.

"""
#this code satify these usecases () [] {}, [), {) ([] ()[} 
#but not this one {[]}, {[]()} ,{[()]}

class Solution: 
    def isValid(self,s:str)->bool:
        rules = {
            '(': ')',
            '{':'}',
            '[':']'
        }
        for index,ch in enumerate(s):
            nextIndex = index+1
            if rules.get(ch) == s[nextIndex]: return True 
            else: return False