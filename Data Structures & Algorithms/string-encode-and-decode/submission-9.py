class Solution:

    # TIP: for ASCII: 
    # use backward slash \ and then add a character after 
    # this is to indicate it is actually ONE character

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "\0" # null character
        text = "\t".join(strs) # tab character
        print(text)
        return text

    def decode(self, s: str) -> List[str]:
        if s == "\0":
            return []
        strs = s.split("\t")
        print(strs)
        return strs
