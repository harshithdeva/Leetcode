def canPlaceFlowers(flowerbed, n: int) -> bool:
        
        prev = 0
        next = 0
        count = 0
        if len(flowerbed) == 0:
            return False
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                if n >=1:
                    count += 1
                if n == count:
                    return True
                else:
                    return False
            if flowerbed[0] == 1:
                if n == 0:
                    return True
                else:
                    return False

        for i in range (len(flowerbed)):
            if i == 0:
                prev = flowerbed[i]
                next = flowerbed[i+1]
                if prev == 0 and next == 0:
                    count+=1
                    flowerbed[i] = 1
                    prev = 1
                continue
            else:
                try:
                    next = flowerbed[i+1]
                except:
                    next = 0
                if flowerbed[i] == 0 and next == 0 and prev == 0:
                    count+=1
                    prev = 1
                    continue
                prev = flowerbed[i]
        
        if count >= n:
            return True
        else:
            return False
        
    

    # Solved on my own