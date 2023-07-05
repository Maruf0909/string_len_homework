def main(a):
    """
    A string type variable is given. Return True if its length is even. Return False if its length is odd.
    Args:
        a: string
    Returns:
        True or False
    """
    if len(a)%2==0:
        s="true"
    if len(a)%2==1:
        s="false"
    
    
    
    return s
print(main("python"))