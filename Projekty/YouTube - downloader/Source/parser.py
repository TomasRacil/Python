import argparse

def vlajky():  
	parser = argparse.ArgumentParser(description='Odkaz youtube videa')
	parser.add_argument('-odkaz', metavar='odkaz', help='Zde zadejte odkaz')
	parser.add_argument('-rozliseni', metavar='rozliseni', help='Zde zadejte pozadovane rozliseni (napr. "360p", "480p"...) ', default='nezadano')
	parser.add_argument('-titulky', metavar='titulky', help='Pokud chcete stáhnout i tutlky zadejte "ano" ', default='ne')
	args = parser.parse_args()

	return(args)

