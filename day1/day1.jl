files = open("day1_input.txt", "r")

function load_file(files)
    # Once the file is read, the pointer is placed at the end.
    # If you call it in multiple function it return nothing
    # So we need to call it in the main function
    seekstart(files) # Reset the file pointer to the beginning
    left_list = []
    right_list = []

    for lines in readlines(files)
        line = split(lines)
        # Julia is 1 based Index
        push!(left_list, line[1])
        push!(right_list, line[2])
    end
    # Converting list from str to Int
    left = parse.(Int, left_list)
    right = parse.(Int, right_list)

    return left, right
end

function part_1(files)
    left, right = load_file(files)

    sort!(left)
    sort!(right)
    position_diff = []

    for (l,r) in zip(left, right)
        push!(position_diff, abs(l-r))
    end

    return sum(position_diff)
    
end

function part_2(files)
    left, right = load_file(files)

    similarity = []
    for ele in left
        count_element = count(x -> x == ele, right)
        s =  count_element* ele
        if s != 0
            push!(similarity,s)
        end
        
    end

    return sum(similarity)
end

println("********* Part1 **********")
println(part_1(files))
println("********* Part2 **********")
println(part_2(files))


