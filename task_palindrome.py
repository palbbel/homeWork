def is_palindrome(s):
    revers_s = ''

    s = str(s)
    for i in s[::-1]:
        revers_s += i

    s = "".join(s.lower().split())
    revers_s = "".join(revers_s.lower().split())
    if s == revers_s:
        return True
    else:
        return False



