def is_decreasing(array:list) ->bool:
    """Check if the array is decreasing and difference is between 1 and 3."""
    return all(array[i] > array[i + 1] and \
               1<= array[i] - array[i+1]<=3 for i in range(len(array) - 1))
  

def is_increasing(array:list) ->bool:
    """Check if the array is Increasing and difference is between 1 and 3."""
    return all(array[i] < array[i + 1] and \
               1<= array[i+1] - array[i]<=3 for i in range(len(array) - 1))

def made_safe(array:list) ->bool:
     # Try removing each level to see if the sequence can be made safe
    for i in range(len(array)):
        new_array = array[:i] + array[i+1:]
        is_safe = is_increasing(new_array) or is_decreasing(new_array)
        if is_safe:
            return True
    return False

def part_1(path:str) -> int:
    '''
    Check if the input report contains a sequence of 
    increasing or decreasing numbers with a difference of  min 1 and max 3.
    '''

    files = open(path, 'r+')
    safe_reports = 0

    for lines in files:
        lines = lines.split()
        report = list(map(int, lines))

        result = is_decreasing(report) or is_increasing(report)
        
        if result:
            safe_reports += 1
    
    return safe_reports

def part_2(path:str) -> int:

    files = open(path, 'r+')

    safe_reports = 0
    for lines in files:
        lines = lines.split()
        report = list(map(int, lines))

        is_safe = is_increasing(report) or is_decreasing(report)
        if is_safe:
            safe_reports += 1
        else:
            msafe = made_safe(report)
            if msafe:
                safe_reports += 1
    
    return safe_reports

#Doc Test
if __name__ == "__main__":

    print("***** Part 1 *****")
    print(part_1('day2_input.txt'))
    print("*"*18)

    print("***** Part 2 *****")
    print(part_2('day2_input.txt'))
    print("*"*18)
