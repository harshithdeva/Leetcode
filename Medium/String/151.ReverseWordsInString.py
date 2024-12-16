def reverseWords(s: str) -> str:
        new_str = s.split()
        for i  in range(len(new_str)):
            new_str[i] = new_str[i].strip()
        new_str.reverse()
        result = " ".join(new_str)
        return result