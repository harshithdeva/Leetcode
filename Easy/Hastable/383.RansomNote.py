def canConstruct(ransomNote: str, magazine: str) -> bool:
        ransom = {}
        for r in ransomNote:
            if ransom.get(r):
                ransom[r] += 1
            else:
                ransom.update({r:1})
        
        mags  = {}
        for m in magazine:
            if  mags.get(m):
                mags[m] += 1
            else:
                mags.update({m:1})

        for key in ransom:
            if mags.get(key):
                if mags[key]>= ransom[key]:
                    continue
                else:
                    return False
            else:
                return False
        return True


# Solved on my own