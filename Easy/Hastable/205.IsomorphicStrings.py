class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s = {}  # Maps characters from s -> t
        map_t = {}  # Maps characters from t -> s
        
        for char_s, char_t in zip(s, t):
            if char_s in map_s:
                if map_s[char_s] != char_t:  # Mismatch in mapping
                    return False
            else:
                map_s[char_s] = char_t  # Create mapping
            
            if char_t in map_t:
                if map_t[char_t] != char_s:  # Mismatch in reverse mapping
                    return False
            else:
                map_t[char_t] = char_s  # Create reverse mapping
        
        return True  # If all mappings are consistent