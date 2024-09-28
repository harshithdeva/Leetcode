def lengthOfLastWord(s: str) -> int:
        new_str = s.split()
        for i  in range(len(new_str)):
            new_str[i] = new_str[i].strip()
        return len(new_str[-1])