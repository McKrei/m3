# 2. Напиши программу, которая находит во введенной строке число с максимальной суммой цифр.
# Строка может содержать как числа, так и слова.
# Используй функцию max() с необязательным аргументом key в виде анонимной функции и функцию filter().


# s = input().split()
s = '123 abc 65 abc 1000 hello 91'
print(max(filter(str.isdigit, s), key=lambda n: sum(map(int, list(n)))))




# s = input().split()
s = '123 aba cdc 234 xx'
print(all(map(lambda x: x == x[::-1], filter(str.isalpha, s))))



def power(n, k):
    if k == 0:
        return 1
    return n * power(n, k - 1)


# n, k = map(int, input().split())
n, k = 2, 5
print(power(n, k))


def fib(n):
   if n <= 2:
       return 1
   return fib(n - 1) + fib(n - 2)


# n = int(input())
n = 5
print(fib(n))
