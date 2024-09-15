def largestPerimeter(nums):        
        
        nums.sort()
        i = len(nums) - 1
        ans = []
        while i >= 2:
            if nums[i-1]+nums[i-2] > nums[i]:
                ans.append((nums[i]+nums[i-1]+nums[i-2]))
            i -= 1
        if not ans:
             ans.append(0)
        max_ans = max(ans)
        return(max_ans)
            
print(largestPerimeter(nums =[1,2,1,10]))

    # Solved on my own with some hints from the comments
# .sort() modifies the og list
# sorted() creates a new list and does not modify the original list