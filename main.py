def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n > 2 and n % 2 != 0:
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i = i + 2
        return True
    else:
        return False


def get_product(list):
    prod = 1
    for num in list:
        prod = prod * num
    return prod


def get_cmmdc_v1(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1


def get_cmmdc_v2(num1, num2):
    while num2 != 0:
        r = num1 % num2
        num1 = num2
        num2 = r
    return num1


def main():
    finish = False
    while finish != True:
        print("Tastati:")
        print("1 Pentru a verifica daca un numar este prim ")
        print("2 Pentru a calcula un produs de numere ")
        print("3 Pentru a calcula cel mai mare divizor comun a doua numere (metoda 1) ")
        print("4 Pentru a calcula cel mai mare divizor comun a doua numere (metoda 2) ")
        print("x Pentru a iesi ")
        s=input()
        if s == '1':
            n = int(input("Verificati numarul: "))
            print(is_prime(n))
        elif s == '2':
            list = input("Introduceti numerele separandu-le printr-o virgula")
            string = list.split(',')
            for i, x in enumerate(string):
                string[i] = int(x)
            print(get_product(string))
        elif s == '3':
            cmmdc1 = int(input("introduceti primul numar: "))
            cmmdc2 = int(input("introduceti al doilea numar: "))
            print(get_cmmdc_v1(cmmdc1,cmmdc2))
        elif s == '4':
            cmmdc1 = int(input("introduceti primul numar: "))
            cmmdc2 = int(input("introduceti al doilea numar: "))
            print(get_cmmdc_v2(cmmdc1, cmmdc2))
        elif s == 'x':
            finish = True
        else:
            print("Ati introdus o valoare gresita. ")

if __name__ == '__main__':
    main()