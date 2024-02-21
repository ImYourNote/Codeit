from random import randint


def generate_numbers(n):
    #번호 뽑기
    i = 1
    picked_numbers = []
    
    while(i <= 6):
        number = randint(1,45)
        if(number not in picked_numbers):
            picked_numbers.append(number)
        i += 1
        
    return picked_numbers


def draw_winning_numbers():
    #당첨 번호 뽑기
    winning_numbers = []
    
    while(len(winning_numbers) < 6):
        w_number = randint(1,45)
        
        if(w_number not in winning_numbers):
            winning_numbers.append(w_number)
        
        winning_numbers.sort()
    
    while True:    
        bonus_number = randint(1,45)
        if(bonus_number not in winning_numbers):
            winning_numbers.append(bonus_number)
            break
    
    return winning_numbers


def count_matching_numbers(numbers, winning_numbers):
    #겹치는 번호 개수
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
    #당첨 확인        
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
    else:
        return 0

