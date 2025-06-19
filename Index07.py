def main(s,n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    if n >= 0 and n < len(s):
        return s[n]
    else:
        return False
    
print(main('salom',1))