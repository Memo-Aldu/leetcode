

'''
    Given two strings s and t , write a function to determine if t is an anagram of s.
    Example 1:
        Input: s = "anagram", t = "nagaram"
        Output: true
    Example 2:
        Input: s = "rat", t = "car"
        Output: false
    
    t is an anagram of s if t is a rearrangement of s.
'''

def solution_1(s: str, t: str) -> bool:
    t_sorted = "".join(sorted(list(t)))
    s_sorted = "".join(sorted((list(s))))
    return s_sorted == t_sorted


'''
    using a dict (Key value pair)
    - key is the char 
    - value is the frequency
    Time complexity: O(s + t)
    Space Complexity: O(s + t)
'''
def solution_2(s: str, t: str) -> bool:
    s_dict = {}
    t_dict = {}
    
    if len(s) != len(t):
        return False
    
    for char in s:
        s_dict[char] = s_dict.get(char, 0) + 1
        
    for char in t:
        t_dict[char] = t_dict.get(char, 0) + 1
    
    return t_dict == s_dict
    
        