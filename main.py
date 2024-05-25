import check_key as check
import rsa


def get_chose():
    print()
    print("Опции программы:")
    print("1 - Проверить свои параметры для RSA.")
    print("2 - Зашифровать файл, сгенерированными параметрами.")
    print("3 - Выйти")

    chose = ''
    while chose not in ("1", "2", "3"):
        chose = input("Ваш выбор: ")
        if chose not in ("1", "2", "3"):
            print("Неправильно. Попробуйте заново.")

    return chose


while True:
    chose = get_chose()

    if chose == "1":
        check.check_key()
    elif chose == "2":
        rsa.rsa()
    else:
        exit()
