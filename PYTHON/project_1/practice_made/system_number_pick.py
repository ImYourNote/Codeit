from random import randint


def generate_numbers(n):
    # 지난 실습의 코드를 여기에 붙여 넣으세요
    i = 1
    picked_numbers = []
    
    while(i <= 6):
        number = randint(1,45)
        if(number not in picked_numbers):
            picked_numbers.append(number)
        i += 1
        
    return picked_numbers

def draw_winning_numbers():
    # 여기에 코드를 작성하세요
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

# 테스트 코드
print(draw_winning_numbers())