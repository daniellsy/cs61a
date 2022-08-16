from curses import endwin


def sum_digits_itr(n):
    """
    calculate the summation of all digits in n
    >>> sum_digits_itr(2019)
    12
    """
    sum=0
    while n>0:
        sum+=n%10
        n//=10
    # iteration invatiant
    return sum
    
def sum_digits_rec(n):
    if n<10:
        return n
    former,last=n//10,n%10
    return sum_digits_rec(former)+last

def print_move(origin,destination):
    """
    pirnt instructions to move a desk
    """
    print("Move the top disk from rod",origin,"to",destination)

def move_stack(n,start,end):
    """print the moves requirement
    There are exacly three poles,and start and end must be different
    """
    if n==1:
        print_move(start,end)
    else:
        bridge=6-start-end
        move_stack(n-1,start,bridge)
        print_move(start,end)
