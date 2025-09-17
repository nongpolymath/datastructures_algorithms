import re
def is_palindrome(input_str):
    clean_str = re.sub(r"[^a-zA-Z0-9]","", input_str)
    input_str = clean_str.lower()
    left = 0
    right = len(input_str)-1
    while left<right:
        if input_str[left] != input_str[right]:
            return False
        left +=1
        right-=1
    return True
        

print(is_palindrome("A man, a plan, a canal – Panama!"))