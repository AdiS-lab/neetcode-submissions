import random
class Solution:

    def encode(self, strs: List[str]) -> str:
        key = str(random.random()+1)
        encodedStr = "" + str(len(key)) + key
        if len(strs) > 0:
            encodedStr += key.join(strs)
            return encodedStr
        return ""

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        lenKey = int(s[0]) * 10 + int(s[1])
        key = s[2: 2+lenKey]
        print(lenKey)
        print(s)
        print(key)
        return s[2:].split(key)[1:]
