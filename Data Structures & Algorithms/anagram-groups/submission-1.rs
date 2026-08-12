impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut group_map: HashMap<String, Vec<String>> = HashMap::new();

        for word in strs.iter() {
            let mut character_count_map: HashMap<char, i32> = HashMap::new();

            for character in word.chars() {
                match character_count_map.get_mut(&character) {
                    Some(x) => *x = *x + 1,
                    None => {
                        character_count_map.insert(character, 1);
                    }
                }
            }

            let mut character_keys: Vec<char> =
                character_count_map.keys().copied().collect();

            character_keys.sort();

            let mut hash_word = String::new();

            for key in character_keys {
                if let Some(x) = character_count_map.get(&key) {
                    hash_word.push_str(&key.to_string());
                    hash_word.push_str(&x.to_string());
                }
            }

            match group_map.get_mut(&hash_word) {
                Some(x) => {
                    x.push(word.clone());
                }
                None => {
                    group_map.insert(hash_word, vec![word.clone()]);
                }
            }
        }

        group_map.into_values().collect()
    }
}