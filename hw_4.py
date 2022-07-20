
def input_number(number: str) -> int:
    """return input of number"""
    result = ''
    while not result.isdigit():
        result = input(number)
    return int(result)