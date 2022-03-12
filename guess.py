import random

max_sayi = 120
min_sayi = -20

say = random.randint(min_sayi, max_sayi)
saytahsay = 0
saytah = 0

def is_input_valid(sayi, sayi_min, sayi_max):

    if not sayi.lstrip("-").isnumeric():
        print('Please enter a valid number!')
        return False
    elif not (min_sayi <= int(sayi) < sayi_max):
        print(f'Please enter a number between {sayi_min} and {sayi_max} !')
        return False

    return True

while  saytah != say:

    saytah = input(f"Please enter a number between {min_sayi} and {max_sayi} : ")

    if not is_input_valid(saytah, min_sayi, max_sayi):
        continue
    
    saytah = int(saytah)

    saytahsay += 1
    
    if saytah < say:
        print("Larger")
        min_sayi = saytah
    elif saytah > say:
        print("Smaller")
        max_sayi = saytah
    
