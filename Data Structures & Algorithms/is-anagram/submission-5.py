class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False


        # New version: Try Hashmap

        s_count, t_count = {}, {} # two hashes

        # so make 
        # key : element of s
        # val : count of that key
        for i in range(len(s)):
            s_count[s[i]] = 1 + s_count.get(s[i], 0) # return 0 if get is unsuccessful
            t_count[t[i]] = 1 + t_count.get(t[i], 0) # return 0 if get is unsuccessful
        
        return s_count == t_count





        # s1 = "".join(sorted(s)) # resorted alphabetically
        # t1 = "".join(sorted(t))

        # return sorted(s) == sorted(t)

        # sorted() will sort them in increasing order of number or alphabet
        # however it will return a list
        # to make it back to a string, you must append a blank string before

        # join() method merges elements of an iterable into a single string, 
        # using a specified separator string between each element

        # example:
        # words = ["Python", "is", "awesome"]

        # Join with a SPACE (" ")
        # sentence = " ".join(words) # so space " " is the separator
        # print(sentence)  # Output: Python is awesome 




        