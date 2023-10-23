# reverse an integer
# num = 1231246
# rev = 0
# while num != 0:
#     temp = num % 10
#     rev = rev * 10 + temp
#     num //= 10
#
# print(rev)


# armstrong number
#
# num = 15
# check = num
# summ = 0
# while num != 0:
#     t = num % 10
#     summ = summ + (t * t * t)
#     num //= 10
#
# if summ == check:
#     print("armstrong")
# else:
#     print("not armstrong")


# # prime number
#
# num=13
# count = 0
# for i in range(2,(num//2)):
#     if num%i==0:
#         count=1
#         break
#
# if count == 1:
#     print("not prime)")
# else:
#     print("prime")

# # fibonacci series
#
# num = 5
# first, second = 0, 1
# for i in range(0, num):
#     if i >= num:
#         result = 1
#         break
#     else:
#         result = first + second
#         first = second
#         second = result
#     print(result)


# # fibonacci with recursion
#
# num = 5
# first, second = 0, 1
#
#
# def fibo(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return fibo(num - 1) + fibo(num - 2)
#
#
# for i in range(num):
#     print(fibo(i))

# # check if the number is plaindrom
#
# num = 131
# check = num
# rev = 0
# while num != 0:
#     temp = num % 10
#     rev = rev * 10 + temp
#     num //= 10
#
# if rev == check:
#     print("palindrome")
# else:
#     print("NOT palindrome")


# # # check if the number is plaindrom using recursion
#
# num = 131
# check = num
# rev = 0
# def palindrome(num):
#     while num != 0:
#     temp = num % 10
#     rev = rev * 10 + temp
#     num //= 10


# # max num
#
# n1= int(input("enter num 1: "))
# n2= int(input("enter num 2: "))
# n3= int(input("enter num 3: "))
# m = 0
#
# if n1 > n2 and n1 > n3:
#     print(f"the biggest is {n1} ")
# elif n2 > n3 and n2 > n1:
#     print(f"the biggest is {n2} ")
# else:
#     print(f"the biggest is {n3} ")

# # check binary
# num = int(input("please give a number : "))
# while(num>0):
#     j=num%10
#     if j!=0 and j!=1:
#         print("num is not binary")
#         break
#     num=num//10
#     if num==0:
#         print("num is binary")
# # swapping two num
# a,b=3,1
# print(a)
# print(b)
# print("swapped")
# a,b=b,a
# print(a)
# print(b)

# # swapping with 3rd variable
# a, b = 1, 10
# temp = a
# a = b
# b = temp
# print(a)
# print(b)

# # prime factors
#
# num = int(input("enter num: "))
# for i in range(2,num):
#     if num % i == 0:
#         print(i)

# # check if teh number is perfect
#
# num = int(input("enter num: "))
# summ = 0
# for i in range(1, num):
#     if num % i == 0:
#         summ += i
#
# if summ == num:
#     print("num is perfect")
# else:
#     print("num is NOT perfect")

# # find the average
#
# num=int(input("enter the total num of elements: "))
# lis=[]
# tot=0
# for i in range(num):
#     lis.append(int(input("enter element: ")))
# for i in lis:
#     tot=tot+i
# avg=tot/num
#
#
# print(avg)
#
#


# # factioriall
#
# num = int(input("enter total num: "))
# fact = 1
# for i in range(1, num+1):
#     fact = fact*i
# print(fact)


# # Factorial using recursion
#
# def fact(num):
#     facto = 1
#     if num == 1 or num == 0:
#         return 1
#     else:
#         return num*fact(num-1)
#

#
# num = int(input("enter total num: "))
# if num<0:
#     print("cant find factorial of negetive number")
# else:
#     print(fact(num))


# # even odd
# num = int(input("enter total num: "))
#
# if num%2==0:
#     print("even")
# else:
#     print("odd")

# ## first n prime numbers
#
#
# def is_prime(num):
#     if num <= 1:
#         return False
#     if num == 2:
#         return True
#     if num % 2 == 0:
#         return False
#     for i in range(3, int(num ** 0.5) + 1, 2):
#         if num % i == 0:
#             return False
#     return True
#
#
# def generate_primes(n):
#     prime_list = []
#     num = 2  # Start with the first prime number, 2
#     while len(prime_list) < n:
#         if is_prime(num):
#             prime_list.append(num)
#         num += 1
#     return prime_list
# n = int(input("enter total num: "))
# prime_numbers = generate_primes(n)
# print(f"The first {n} prime numbers are: {prime_numbers}")


# prime numbers in a given range
# num=4
# for i in range(num):
#     for n in range(i+1):
#         print("*", end=" ")
#     print()


# # to check if string contains vowels and how many
# s = input("enter:")
# s = s.lower()
# count = 0
# vov = ['a', 'e', 'o', 'i', 'u']
# for i in s:
#     # if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#     for n in vov:
#         if i == n:
#             count += 1
#
# print(count)


# # calculating power using POW method
# import math
# n1 = int(input("enter num1: "))
# n2= int(input("enter num2: "))
#
# p=math.pow(n1, n2)
# print(p
#
# # calculating power using POW method
#
# def poww(base, expo):
#     result = 1
#     while expo != 0:
#         result = base * result
#         expo-=1
#     return result
# base = int(input("enter base: "))
# expo = int(input("enter expo: "))
# print(poww(base,expo))

# # square of a gicen number
#
# num = int(input("enter num: "))
# print(num*num)

# # cuve of a gicen number
#
# num = int(input("enter num: "))
# print(num*num*num)

# # # sqrt of a gicen number
#
# import math
# num = int(input("enter num: "))
# print(math.sqrt(num))

# # program to find teh lcm
# n1 = int(input("enter num1: "))
# n2= int(input("enter num2: "))
# greater=0
# if n1>n2:
#     greater= n1
# else:
#     greater= n2
#
# while (True) :
#


# n1 = int(input("enter num1: "))
# count = 0
# for i in range(2, n1):
#     if n1 % i == 0:
#         count += 1
# print(count)


# # delete vowvels from string
#
# st = input("enetr string: ")
# vow = ['a', 'e', 'i', 'o', 'u']
# print(st)
#
# for i in st:
#     for n in vow:
#         if i == n:
#             st = st.replace(n, "")
# print(st)

#
# # check th enumber of vowel and consonent
# st = input("enetr string: ")
# voww = "aeiouAEIOU"
# num= "1234567890"
# spec = "!@#$%^&*()_-+=[]{}|;:'\",.<>?`~"
#
# vov_c = 0
# con_c = 0
# spl = 0
# numb=0
#
# for i in st:
#     if i.isalpha():
#         if i in voww:
#             vov_c += 1
#         else:
#             con_c += 1
#     elif i in spec:
#             spl += 1
#     elif i in num:
#             numb += 1
#
# print(f"vowels: ", vov_c, " consonants: ", con_c, " spl char", spl, " num: ", numb)

# # check if strings are anagram
# st1=input("enter first string: ")
# st2=input("enter second string: ")
#
# if sorted(st1) == sorted(st2):
#     print("the strings are anagram")
# else:
#     print("not anagaram")


# check if strings are palindrome
st1=input("enter first string: ")
st2=input("enter second string: ")

if st1 == st2[::-1]:
    print("the strings are palindrome")
else:
    print("not palindrome")
