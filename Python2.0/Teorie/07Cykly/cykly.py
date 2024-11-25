# Cyklus while
i = 0
while i < 5:
  print(i)
  i += 1

# Cyklus while s break
i = 0
while True:  # Nekonečný cyklus
  print(i)
  i += 1
  if i >= 5:
    break

# Cyklus for
seznam = ["jablko", "hruška", "banán"]
for ovoce in seznam:
  print(ovoce)

# Cyklus for s range()
for i in range(5):
  print(i)

for i in range(2, 8, 2):
  print(i)

# Vnořené cykly
for i in range(3):
  for j in range(2):
    print(f"i = {i}, j = {j}")