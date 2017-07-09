from sys import exit, argv

theta0 = 0.0
theta1 = 0.0

def main():
	global theta0
	global theta1
	try:
		fd = open("theta_data.csv")
	except IOError:
		print('Erreur ouverture fichier')
		exit(1)
	donnee = list(fd)
	infoDonnee = donnee[0].replace('\n', '').split(',')
	thetas = donnee[1].replace('\n', '').split(',')
	theta0 = thetas[0]
	theta1 = thetas[1]
	kilometrage = input('Entrer un (%s)\n' % infoDonnee[0])
	if (not kilometrage.isnumeric()):
		print('Mauvais format!')
		exit()
	valeurKilometrage = float(kilometrage)
	prix = int(float(theta0) + float(theta1) * float(kilometrage))
	print('Resultat: (prix, kilometrage)\n(%d, %s)' % (prix, kilometrage))

if __name__ == '__main__':
  main()
