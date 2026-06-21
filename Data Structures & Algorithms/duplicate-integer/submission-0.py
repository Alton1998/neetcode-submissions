class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_dict = dict()
        for i in nums:
            count = count_dict.get(str(i),0)
            count  = count + 1
            count_dict[str(i)] = count
            if count > 2 or count==2:
                return True
        return False
        