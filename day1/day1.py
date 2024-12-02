def load_input(files):
    left_list = []
    right_list = []

    for line in files:
        line = line.split()
        left_list.append(line[0])
        right_list.append(line[1])
    
    return left_list, right_list


def part_1(files):
    
    left_list, right_list = load_input(files)

    left_list.sort()
    right_list.sort()

    location_diff = []

    for l,r in zip(left_list, right_list):
        diff = abs(int(l) - int(r))
        location_diff.append(diff)

    return sum(location_diff)

# def part_2(files):
#     left_list, right_list = load_input(files)

#     total = 0
#     for ele in left_list:
#         count = right_list.count(ele)
#         total += (int(count) * int(ele))
    
#     return total
files = open('day1_input.txt', 'r+')
left_list, right_list = load_input(files)

total = 0

for ele in left_list:
    count = right_list.count(ele)
    # print(type(count))
    total += count*int(ele)
    print(count*int(ele))
    # print(f'{ele} appears {count} times')
print(total)
# #Doc Test
# if __name__ == "__main__":
#     #Reading Input txt file
#     files = open('day1_input.txt', 'r+')

#     print("***** Part 1 *****")
#     print(part_1(files))
#     print("*"*18)

#     print("***** Part 2 *****")
#     print(part_2(files))
#     print("*"*18)