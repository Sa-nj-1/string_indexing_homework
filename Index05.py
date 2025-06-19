def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    raqamlar=0
    if s[0]== (1,2,3,4,5,6,7,8,9,):
        raqamlar += 1
        return raqamlar 
    if s[1]== (1,2,3,4,5,6,7,8,9,):
        raqamlar += 1
        return raqamlar 
    if s[2]== (1,2,3,4,5,6,7,8,9,):
        raqamlar += 1
        return raqamlar 
    if s[3]== (1,2,3,4,5,6,7,8,9,):
        raqamlar += 1
        return raqamlar 
    if s[4]== (1,2,3,4,5,6,7,8,9,):
        raqamlar += 1
        return raqamlar

print(main('a1bcd')) 
    