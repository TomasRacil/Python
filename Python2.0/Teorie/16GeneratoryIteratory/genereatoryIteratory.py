def fibonacci(n):
  a, b = 0, 1
  for _ in range(n):
    yield a
    a, b = b, a + b

for cislo in fibonacci(10):
  print(cislo)