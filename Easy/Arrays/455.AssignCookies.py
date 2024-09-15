def assign_cookies(g, s):
    # sort both lists in ascending order
    g.sort()
    s.sort()
    # keep track of the number of cookies we have given out
    num_cookies = 0
    # start at the beginning of both lists
    i = 0
    j = 0
    # continue until we reach the end of either list
    while i < len(g) and j < len(s):
        # if the current cookie is large enough to satisfy the current child, give it to the child and move on to the next child and cookie
        if s[j] >= g[i]:
            num_cookies += 1
            i += 1
            j += 1
        # if the current cookie is too small to satisfy the current child, move on to the next cookie
        else:
            j += 1
    # return the number of cookies we have given out
    return num_cookies



# Passed 15/25 testcases, looked up solution for complete answer