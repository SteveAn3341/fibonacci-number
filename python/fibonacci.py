def fibonacci(n):
  a = 0
  b = 1
  c = a + b
  cycle = 2
  while n > cycle:
    a = b
    b = c
    c = a + b
    cycle += 1
  return c

print(fibonacci(8))

# def fibonacci(n):
#   if n <= 0:
#     return 0
#   elif n == 1:
#     return 1
#   else:
#     a = 0
#     b = 1
#     for i in range(2, n+1):
#       c = a + b
#       a = b
#       b = c
#     return c

# print(fibonacci(8))