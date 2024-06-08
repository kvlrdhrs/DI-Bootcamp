import random

list_of_numbers = [random.randint(0, 10000) for _ in range(20000)]
target_number = 3728

def count_pairs_with_sum(numbers, target):
    count = 0
    num_dict = {}
    
    for number in numbers:
        complement = target - number
        if complement in num_dict:
            count += num_dict[complement]
        if number in num_dict:
            num_dict[number] += 1
        else:
            num_dict[number] = 1
            
    return count

pairs_count = count_pairs_with_sum(list_of_numbers, target_number)
print(f"Number of pairs that sum to {target_number}: {pairs_count}")