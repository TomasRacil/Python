import argparse

def vlajky():  
	parser = argparse.ArgumentParser(description='Odkaz youtube videa')
	parser.add_argument('-o', metavar='odkaz', help='Zde zadejte odkaz')
	parser.add_argument('-r', metavar='rozliseni', help='Zde zadejte pozadovane rozliseni (napr. "360p", "480p"...) ', default='nezadano')
	parser.add_argument('-t', metavar='titulky', help='Pokud chcete stáhnout i tutlky zadejte "ano" ', default='ne')
	args = parser.parse_args()

<<<<<<< HEAD
	return(args)

=======
	return(args)
>>>>>>> 580955f5df2223cb1f7e8204e5b77bfd6b71739a
