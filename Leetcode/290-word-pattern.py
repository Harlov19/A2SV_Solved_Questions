class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if(len(words) != len(pattern)):
            return False
        char_word = {}
        word_char = {}
        
        for char, word in zip(pattern,words):
            if(char not in char_word):
                char_word[char] = word
            elif(char_word[char] != word):
                return False
            
            if(word not in  word_char):
                word_char[word] =char
            elif( word_char[word] != char):
                return False
           
        return True
