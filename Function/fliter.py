#1~200之间的回数
# -*- coding: utf-8 -*-
def is_palindrome(num):
    s=str(num)
    str_length=len(s)
    if s[0]==s[-1]:
        return True
    return False

output = filter(is_palindrome, range(1, 200))
print('1~200:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
