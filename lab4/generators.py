1.
def generate_squares(N):
    for i in range(1, N + 1):
        yield i ** 2

2.
def generate_even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

def main():
    n = int(input("Enter a value for n: "))
        
    even_numbers_generator = generate_even_numbers(n)
        
    even_numbers_str = ', '.join(map(str, even_numbers_generator))
        
    print(even_numbers_str)
main()

3.
def generate_divisible_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

def main():
    n = int(input("Enter a value for n: "))
     
    divisible_generator = generate_divisible_by_3_and_4(n)
        
    for num in divisible_generator:
        print(num)

main()

4.
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2
#Test:        
a = int(input('Enter a: '))
b = int(input('Enter b: '))
for square in squares(a, b):
    print(square)

5.
def countdown(n):
    while n >= 0:
        yield n
        n -= 1
# Test:
n = int(input('Enter n: '))
for num in countdown(n):
    print(num)
