def isPalindrome(s):
    sgood = "".join(ch.lower() for ch in s if ch.isalnum())
    # return sgood == sgood[::-1]
    print(sgood)
    print(sgood[::-1])

if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    isPalindrome(s)
