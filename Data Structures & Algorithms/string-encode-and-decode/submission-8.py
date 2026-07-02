class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "\0"
        text = "\t".join(strs)
        print(text)
        return text

    def decode(self, s: str) -> List[str]:
        if s == "\0":
            return []
        strs = s.split("\t")
        print(strs)
        return strs
