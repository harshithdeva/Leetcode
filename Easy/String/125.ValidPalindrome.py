def isPalindrome(s: str) -> bool:

    if s == "":
        return False
    if s == " ":
        return True
    s = s.lower()   
    new_str = ''.join(e for e in s if e.isalpha())
    reversed_str = new_str[::-1]
    if new_str == reversed_str:
        return True
    else:
        return False
isPalindrome("A man, a plan, a canal: Panama")