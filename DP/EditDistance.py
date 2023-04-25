def editDistance(str1, str2) :
    
    # Your code goes here
    #return editRec(str1,str2, len(str1)-1, len(str2)-1)
    # dp = dp = [[-1 for ti in range(len(str2)+1)]for si in range(len(str1)+1)]
    # return editMemo(str1,str2, len(str1)-1, len(str2)-1, dp)
    return editDP(str1,str2)


def editRec(s,t, si, ti):
    if si < 0 and ti< 0:
        return 0
    if si < 0 or ti < 0:
        return abs(si-ti)

    if s[si] == t[ti]:
        return editRec(s,t,si-1, ti-1)
    else:
        delete =  editRec(s,t,si, ti-1) +1
        replace = editRec(s,t,si-1, ti-1)+1
        insert = editRec(s,t,si-1, ti)+1
        return min(delete, replace, insert)

def editMemo(s,t, si, ti, dp):
    if si < 0 and ti< 0:
        return 0
    if si < 0 or ti < 0:
        return abs(si-ti)
    
    if dp[si][ti] != -1:
        return dp[si][ti]

    if s[si] == t[ti]:
        dp[si][ti] = editMemo(s,t,si-1, ti-1, dp)
    else:
        delete =  editMemo(s,t,si, ti-1, dp) +1
        replace = editMemo(s,t,si-1, ti-1, dp)+1
        insert = editMemo(s,t,si-1, ti, dp)+1
        dp[si][ti] = min(delete, replace, insert)
    return dp[si][ti]

def editDP(s,t):
    dp = dp = [[0 for ti in range(len(t)+1)]for si in range(len(s)+1)]

    for si in range(len(s)+1):
        for ti in range(len(t)+1):
            if si == 0 and ti == 0:
                dp[si][ti] = 0
            elif si == 0 or ti == 0:
                dp[si][ti] = abs(si-ti)
            else:
                if s[si-1] == t[ti-1]:
                    dp[si][ti] = dp[si-1][ti-1]
                else:
                    delete =  dp[si][ti-1] +1
                    replace = dp[si-1][ti-1]+1
                    insert = dp[si-1][ti]+1
                    dp[si][ti] = min(delete, replace, insert)
    return dp[len(s)][len(t)]