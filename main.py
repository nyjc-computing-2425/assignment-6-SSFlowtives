from datetime import datetime
import time


def clock(n: int):
    """
    
    This function takes in integer n and shows the time and updates it every second,
    for n number of seconds.

    Parameters
    ----------
    n: int
        Amount of times to update time

    Returns
    -------
    None

    Examples
    --------
    >>> clock(3)
    12:59:17
    """
    for i in range(n):
        current_time = datetime.now()
        print(f"{str(current_time.hour).zfill(2)}:{str(current_time.minute).zfill(2)}:{str(current_time.second).zfill(2)}", end='\r')
        time.sleep(1)
    pass


def lcm(a: int, b: int) -> int:
    """

    This function takes in 2 integers and outputs their lowest common multiple

    Parameters
    ----------
    a: int
        First number

    b: int
        Second number

    Returns
    -------
    int
        Lowest common multiple

    Examples
    --------
    >>> lcm(2, 3)
    6
    >>> lcm(12, 5)
    60
    """
    old_a = a
    old_b = b
  
    while a != b:
        if a < b:
            a += old_a
        else:
            b += old_b
          
    return a


def gcf(a: int, b: int) -> int:
    """

    This function takes in 2 integers and outputs their greatest common factor

    Parameters
    ----------
    a: int
        First number

    b: int
        Second number

    Returns
    -------
    int
        Greatest common factor

    Examples
    --------
    >>> gcf(60, 48)
    12
    >>> gcf(70, 14)
    14
    """
    while b != 0:
        r = a % b
        a = b
        b = r
      
    return a