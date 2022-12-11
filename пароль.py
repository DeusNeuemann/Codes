import random
import string
que = input("Сгенерировать новый пароль?\n 1. Да\n 2. Нет")
if que in ["1","да","Да","da","Da","lf"]:
    total = string.ascii_letters + string.digits
    length = 20
    password = "".join(random.sample(total, length))
    print(password)
elif que in ["2","Нет","нет","net","Net","ytn"]:
    exit(0)
input()