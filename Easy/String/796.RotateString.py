def rotateString(s: str, goal: str) -> bool:
        concat_s = s+s
        if len(s)>len(goal):
            return False
        if goal in concat_s:
            return True
        else:
            return False