"""
You are given a string and your task is to swap cases. 
In other words, convert all lowercase letters to uppercase letters and vice versa.
"""
def swap_case(s):
    ans = ''
    for i in range(len(s)):
        Char_ascii = ord(s[i])
        if( 65<=Char_ascii<=90):
            ans+= chr(ord(s[i])+32)
        elif (97<=Char_ascii<=122):
            ans+= chr(ord(s[i])-32)
        else:
            ans+= s[i]
       
    return ans

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)