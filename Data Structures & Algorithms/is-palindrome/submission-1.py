class Solution:
    def isPalindrome(self, s: str) -> bool:
        # how to filter ONLY alphaneumeric
        # https://www.geeksforgeeks.org/python/python-remove-all-characters-except-letters-and-numbers/
        
        s_simple = "".join(filter(str.isalnum, s))
        print(s_simple)

        # get the first half and the other half

        first_half = s_simple[0:len(s_simple)//2]
        print(first_half)

        second_half = s_simple[(len(s_simple)+1)//2:len(s_simple)]
        print(second_half[::-1])
        # To perform a case-insensitive string comparison in Python, 
        # the best practice is to use the str.casefold() method on both strings
        return first_half.casefold() == second_half[::-1].casefold() # reverse second half

