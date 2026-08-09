impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut result: Vec<i32> = Vec::new();

        for i_index in 0..nums.len() - 1 {
            let i = nums[i_index];

            for j_index in i_index + 1..nums.len() {
                let j = nums[j_index];

                let sum = i + j;

                if sum == target {
                    result.push(i_index as i32);
                    result.push(j_index as i32);
                    return result;
                }
            }
        }

        result
    }
}
