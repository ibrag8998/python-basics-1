start = int(input())
end = int(input())
# start = 4
# end = 17

all_numbers_between = list(range(start, end + 1))
filtered_numbers = list()
for number in all_numbers_between:
    str_number = str(number)

    if "5" not in str_number:  # str_number = "125"
        filtered_numbers.append(number)

print(len(filtered_numbers))
