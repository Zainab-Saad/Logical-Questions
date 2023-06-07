''''
Write a function which will take a string as input, check and return if it is palindrome or not. For
example, if the string is “madam” the function should return true and if the string is “doctor” it should
return false.'''


def palindrome(inp):
    
    # get the length of the input string -- substitute for built in len function
    length = 0
    for i in inp:
        length += 1
    for i in range(0, length//2):
        if inp[i] == inp[len(inp)-1-i]:
            continue
        else:
            return False
    return True


isPalindrome = palindrome('madam')
print(isPalindrome)
