# n = 1
# while n < 1000:
#     print(n)
#     n += 1
#
# for i in range(1000):
#     if i % 3 == 0:
#         print(i)

result = 0
for i in range(1, 1000):
    if i % 3 == 0 and i % 5 == 0:
        result += i
print(result)