"""
Task
The provided code stub reads two integers,  and , from STDIN.
Add logic to print two lines. The first line 
should contain the result of integer division,  // . 
The second line should contain the result of float division,  / .
"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b,a/b, sep='\n')