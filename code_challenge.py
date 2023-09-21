def lookForTwoSum2(numbers_list, target):
    nums = {}
    flag = False
    for num in numbers_list:
        difference = target - num
        if difference in nums:
            print(num, ",", difference)
            flag = True
        else:
            nums[num] = "number"
            continue
    if flag == False:
        print("There are no pairs of numbers in that list for which the addition results in " + str(target))

file_path = "./data.txt"
with open(file_path, "r") as file:
    line = file.readline()
    data = []
    while line:
        data.append(line)
        line = file.readline()
    numbers = eval(data[0].strip("numbers="))
    target = int(data[1].strip("target="))

lookForTwoSum2(numbers, target)
