print("Description: This program will find the biggest value from string of numbers")

#nums = input("Please input numbers (comma separated): ")
#nums = nums.split(",")

#if len(nums) == 0:
   # print("There's is no input numbers")
    #exit(0)

nums = []

while True:
    try:
        # \" is referred to escaping characteres in strings'
        input_val = input("Enter next number (type \"stop\" to stop input): ")
        if input_val == "stop":
            break
        nums.append(float(input_val))
    except Exception:
        print("Wrong number, please try again")


if len(num) == 0:
    print("there is no input")
    exit(0)

max_num = nums[0]
for num in nums:
    if num > max_num:
        max_num = num

print(f"Max value: {max_num} ")
