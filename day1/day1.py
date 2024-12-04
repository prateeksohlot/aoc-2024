def load_input(path:str)->list:

    files = open(path, 'r+')

    left_list = [line.strip().split()[0] for line in files]
    right_list = [line.strip().split()[1] for line in files]
    
    
    return left_list, right_list


def part_1(path:str)->int:
    
    left_list, right_list = load_input(path)

    left_list.sort()
    right_list.sort()

    location_diff = []

    for l,r in zip(left_list, right_list):
        diff = abs(int(l) - int(r))
        location_diff.append(diff)

    return sum(location_diff)

def part_2(path:str)->int:
    left_list, right_list = load_input(path)

    total = 0
    for ele in left_list:
        count = right_list.count(ele)
        total += count * int(ele)
    
    return total

#Doc Test
if __name__ == "__main__":

    print("***** Part 1 *****")
    print(part_1('day1_input.txt'))
    print("*"*18)

    print("***** Part 2 *****")
    print(part_2('day1_input.txt'))
    print("*"*18)