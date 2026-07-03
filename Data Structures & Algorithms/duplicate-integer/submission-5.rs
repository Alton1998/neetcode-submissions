impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let mut count_map:HashMap<i32,i32> = HashMap::new();
        for num in nums.iter() {
            if let Some(a) = count_map.get_mut(num) {
                *a = *a + 1;
                if *a > 2 || *a==2 {
                    return true;
                }
            }
            else {
                count_map.insert(*num, 1);
            }
        }
        return false;
    }
}