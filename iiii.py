def calculate():
  # Запрашиваем у пользователя два числа и операцию

  num1 = float(input("Введите первое число: "))
  num2 = float(input("Введите второе число: "))
  operation = input("Введите операцию (+, -, *, /): ")

  # Выполняем операцию в зависимости от выбора пользователя
  if operation == "+":
    result = num1 + num2

    print(result)