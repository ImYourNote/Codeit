def count_matching_numbers(numbers, winning_numbers):
    # 지난 실습의 코드를 여기에 붙여 넣으세요
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

def check(numbers, winning_numbers):
    # 여기에 코드를 작성하세요
    check_number = count_matching_numbers(numbers, winning_numbers)
    if(check_number == 6):
        if(winning_numbers[-1] in numbers):
            return 50000000
        return 1000000000
    elif(check_number == 5):
        return 1000000
    elif(check_number == 4):
        return 50000
    elif(check_number == 3):
        return 5000
        
    

# 테스트 코드
print(check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6]))
print(check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25]))