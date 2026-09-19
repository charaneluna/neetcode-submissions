class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for word in strs:
            s+= word + 'lina'

        return s
    def decode(self, s: str) -> List[str]:

        li = s.split('lina')
        return(li[:len(li)-1])

