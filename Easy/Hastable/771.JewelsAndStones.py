
def numJewelsInStones(jewels: str, stones: str) -> int:
        str_jewel = []
        for j in jewels:
            str_jewel.append(j)
        count = 0
        for s in stones:
            if s in str_jewel:
                count+=1
        return count
    
    
    # Solved on my own