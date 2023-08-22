def kalkulyator():
    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Выход")
        
        choice = input("Введите номер операции: ")
        
        if choice == '5':
            break

        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if choice == '1':
            result = num1 + num2
            print(f"Результат: {num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"Результат: {num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"Результат: {num1} * {num2} = {result}")
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print(f