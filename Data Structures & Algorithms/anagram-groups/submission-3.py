class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 1. Go over one string and make it into its own group
        # 2. Grab any other words that are anagram and add them (remove them from the pool)
        # 3. repeat till no more words are left in the pool

        result = []

        while (len(strs) > 0):
            curr = strs[0];
            # print(curr)
            group = []
            group.append(curr)

            for other in strs[1:]:
                # print(other)
                if self.isAnagram(curr, other):
                    
                    group.append(other)
            
            for word in group:
                strs.remove(word)
            
            result.append(group)


        
        return result


    # stole this from previous question (but I made it so no shame)
    def isAnagram(self, s: str, t: str) -> bool:

        if (s == t):
            return True # dealing with trivial case

        s1 = "".join(sorted(s)) # resorted alphabetically
        t1 = "".join(sorted(t))

        return s1 == t1

    
    

    