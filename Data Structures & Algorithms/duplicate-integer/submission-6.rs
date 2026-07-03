
impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let mut present_set:HashSet<i32> = HashSet::new();
        for num in nums.iter() {
            if !present_set.insert(*num){
                return true;
            }
        }
        return false;
    }
}