def count_matching_numbers(numbers, winning_numbers):
    # 여기에 코드를 작성하세요
    i = 0
    stack_number = 0
    
    while(i < len(numbers)):
        j = 0
        while(j < len(winning_numbers)):
            if(numbers[i] == winning_numbers[j]):
                stack_number += 1
            j += 1
        i += 1
    
    return stack_number

# 테스트 코드
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))