class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        counter_chars = Counter(chars)
        ans = 0
        for word in words:
            if( Counter(word)<= counter_chars):
                ans+=len(word)
        return ans