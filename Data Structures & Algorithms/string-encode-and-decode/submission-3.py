class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        if not strs:
            return ""
        for word in strs:
            encoded_str = encoded_str + "#" +str(len(word)) + "!" + word
        return encoded_str


    def decode(self, s: str) -> List[str]:
        if not s:
            return list()
        i = 0
        original_list = []
        while i < len(s):
            if s[i]=="#":
                length_word = ""
                j = i + 1
                while s[j]!="!":
                    try:
                        length_word = length_word + str(int(s[j]))
                        j = j + 1
                    except Exception as e:
                        break
                i = j + 1
                word = s[i:i+int(length_word)]
                original_list.append(word)
                i = i + int(length_word)
        return original_list