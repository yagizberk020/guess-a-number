import random

max_sayi = 120
min_sayi = -20

say = random.randint(min_sayi, max_sayi)
saytahsay = 0
saytah = 0

def is_input_valid(sayi, sayi_min, sayi_max):

    if not sayi.lstrip("-").isnumeric():
        print('Lutfen gecerli bir sayi giriniz!')
        return False
    elif not (min_sayi <= int(sayi) < sayi_max):
        print(f'Lutfen {sayi_min} ile {sayi_max} arasinda bir sayi giriniz!')
        return False

    return True

while  saytah != say:

    saytah = input(f"{min_sayi} ile {max_sayi} arasında bir sayı girin: ")

    if not is_input_valid(saytah, min_sayi, max_sayi):
        continue
    
    saytah = int(saytah)

    saytahsay += 1
    
    if saytah < say:
        print("daha büyük")
        min_sayi = saytah
    elif saytah > say:
        print("daha küçük")
        max_sayi = saytah
    
