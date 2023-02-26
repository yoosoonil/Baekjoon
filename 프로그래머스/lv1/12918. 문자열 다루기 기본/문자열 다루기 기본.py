def solution(s):
    # isdigit()는 문자열이 숫자로만 이루어져있는 판단하는 메서드.
    if (len(s) == 4 or len(s) ==6) and s.isdigit():
        return True
    else:
        return False