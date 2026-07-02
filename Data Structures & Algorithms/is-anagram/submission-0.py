class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

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


        s1 = "".join(sorted(s))
        t1 = "".join(sorted(t))

        return s1 == t1
        