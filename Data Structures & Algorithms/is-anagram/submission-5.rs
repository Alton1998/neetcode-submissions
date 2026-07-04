impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let s:Vec<char> = s.chars().collect();
        let t:Vec<char> = t.chars().collect();
        if s.len() != t.len(){
            return false
        }
        let mut s_count_map:HashMap<char,u32>= HashMap::new();
        let mut t_count_map:HashMap<char,u32>=HashMap::new();
        let mut i:usize = 0 ;
        while i < s.len() {
            if let Some(a) = s_count_map.get_mut(&s[i]) {
                *a = *a + 1;
            }
            else {
                s_count_map.insert(s[i], 1);
            }
            if let Some(b) = t_count_map.get_mut(&t[i]) {
                *b = *b + 1;
            }
            else {
                t_count_map.insert(t[i], 1);
            }
            i = i + 1
        }
        return s_count_map == t_count_map;
    }
}