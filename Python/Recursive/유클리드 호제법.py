def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a = int(input("Enter the integer a : "))
b = int(input("Enter the integer b : "))
print("a와 b의 최대 공약수는 : ", gcd(a,b))