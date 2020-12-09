seznam1=[cislo for cislo in range(1,101) if cislo%3==0]
seznam=[cislo if cislo%2==0 else 0 for cislo in [cislo for cislo in range(1,101) if cislo%3==0]]

"""for cislo in range(1,101):
	seznam.append(cislo)"""

print(seznam)