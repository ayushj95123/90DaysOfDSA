def checkPalindrome(str, start = 0):
    if start >= len(str)/2:
        return True
    if str[start] != str[len(str)-start-1]:
        return False
    else:
        return checkPalindrome(str, start+1)

print(checkPalindrome("aba"))
print(checkPalindrome("a"))
print(checkPalindrome("abd"))
print(checkPalindrome("abaaba"))
