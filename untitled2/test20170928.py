"""
변수와 입출력 테스트
print, input
연산자 테스트
"""
a = 1
b = 2
print(a, "\n", b)
print(a + b)

a = input("a : ")
b = input("b : ")
print(a, b) , print(a) , print(b)
print(a + b)
print(int(a) + int(b))

a = int(input())
b = int(input())

c = a + b
d = a - b
e = a * b
f = a ** b
g = a / b
print(a, b, c, d, e, f, g)