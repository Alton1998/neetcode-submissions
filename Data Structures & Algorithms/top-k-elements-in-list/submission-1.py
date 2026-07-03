class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = dict()
        for i in nums:
            count = count_dict.get(i, 0)
            count = count + 1
            count_dict[i] = count
        top_k_dict = dict()
        for key, value in count_dict.items():
            top_k_list = top_k_dict.get(value, list())
            top_k_list.append(key)
            top_k_dict[value] = top_k_list
        element_list = []
        top_k_dict_keys = sorted(top_k_dict.keys(), reverse=True)
        j = 0
        while len(element_list) < k and j < len(top_k_dict_keys):
            element_list.extend(top_k_dict.get(top_k_dict_keys[j])[:k])
            j = j + 1
        return element_list