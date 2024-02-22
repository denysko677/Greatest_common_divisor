def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    print("Введіть два числа для знаходження найбільшого спільного дільника:")
    num1 = int(input("Перше число: "))
    num2 = int(input("Друге число: "))
    
    result = gcd(num1, num2)
    print("Найбільший спільний дільник:", result)

if __name__ == "__main__":
    main()
