# #과제39
# a = int(input("숫자 입력 : "))
# def odd():
#     for i in range(a):
#         if i % 2 == 1:
#             print(i)
# odd()


# #과제40
# a = int(input("숫자 입력 : "))
# def mul():
#     if a % 3 == 0:
#         print(a)
# mul()


# #과제41
# a = list(map(int, input().split()))

# def numbers(*args):
#     maximum = a[0] 
#     minimum = a[0]
#     for i in args:
#         if maximum <= i:
#             maximum = i
#         if minimum >= i:
#             minimum = i
#     return(maximum, minimum)

# print(numbers(*a))


# #과제43
# a = int(input("숫자 입력 : "))
# def fact(args):
#     b = 1
#     for i in range(1,args+1):
#         b *= i
#     return(b)

# print(a)
# print(fact(a))


# #과제44
# a, b = map(int, input("숫자 두개 입력 : ").split())
# def c(num1, num2):
#     x = 0
#     for i in range(1, num1+1):
#         for j in range(1, num2+1):
#             if i * j >= 30:
#                 x += i * j
#             else :
#                 continue
#     return(x)
           
    
# print(c(a, b))


# #과제45
# def b(args):
#     c = 0
#     for i in args:
#         c += i
#     return(c)

# a = [1, 2, 3, 4, 5]
# print(b(a))