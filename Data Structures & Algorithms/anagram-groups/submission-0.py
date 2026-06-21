

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_groups = dict()
        for word in strs:
            count_char = dict()
            for my_char in word:
                count = count_char.get(my_char,0)
                count = count + 1
                count_char[my_char] = count   
            hash_word = ""  
            for key in sorted(count_char.keys()):
                hash_word = hash_word + key + str(count_char[key])
            word_group = word_groups.get(hash_word,list())
            word_group.append(word)
            word_groups[hash_word] = word_group
        groups = list()
        for group in word_groups.values():
            groups.append(group)
        return groups

                

            



        