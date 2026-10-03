class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"

        result = []
        for word in words:
            lower_word = word.lower()

            if all(char in row1 for char in lower_word) or \
               all(char in row2 for char in lower_word) or \
               all(char in row3 for char in lower_word):
                result.append(word)

        return result