import sys
input = sys.stdin.readline
a = input()
cnt = 0
def recursion(s, l, r):
    global cnt
    cnt += 1
    if l >= r:
        return "1 "+str(cnt)
    elif s[l] != s[r]:
        return "0 "+str(cnt)
    else:
        return recursion(s, l+1, r-1)
def isPalindrome(s):
    global cnt
    cnt = 0
    return recursion(s, 0, len(s)-1)

for i in range(1,int(a)+1):
    print(isPalindrome(input().rstrip()))
