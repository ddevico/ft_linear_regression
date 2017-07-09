import matplotlib.pyplot as plt
import copy
from re 	import compile as re_compile
from sys	import argv
from sys	import exit

theta0 = 0.0
theta1 = 0.0
echelle = 1.0
echelleMin = 0.0
infoData = ""
Origindata = []

def estimation(kilometrage):
	return (theta1 * kilometrage + theta0)

def parse(file_name):
	global infoData
	global Origindata
	tabData = []
	try:
		fd = open(file_name, 'r')
	except IOError:
		print('Could not open file!')
		exit()
	data = list(fd)
	infoData = data[0]
	for line in data[1:]:
		line = line.replace('\n', '')
		split = line.split(',')
		tabData.append((float(split[0]), float(split[1])))
	fd.close()
	Origindata = copy.deepcopy(tabData)
	return tabData

def minimiseValeur(data):
	global echelle
	global echelleMin
	x_set = [x[0] for x in data]
	min_x = min(x_set)
	max_x = max(x_set)
	echelle = max_x - min_x
	echelleMin = min_x / echelle
	data = [((x[0] - min_x) / echelle, x[1]) for x in data]
	return data

def calculThetas(data):
	global theta0
	global theta1
	data = minimiseValeur(data)
	tmp_theta0 = 1.0
	tmp_theta1 = 1.0
	learning_rate = 0.1
	while (abs(tmp_theta0) > 0.001 and abs(tmp_theta1) > 0.001):
		theta0Sum = sum([estimation(data[i][0]) - data[i][1] for i in range(len(data))])
		theta1Sum = sum([(estimation(data[i][0]) - data[i][1]) * data[i][0] for i in range(len(data))])
		tmp_theta0 = learning_rate * theta0Sum * (1.0 / len(data))
		tmp_theta1 = learning_rate * theta1Sum * (1.0 / len(data))
		theta0 -= tmp_theta0
		theta1 -= tmp_theta1
	theta1 /= echelle
	return data

def fileThetas(file_name):
	fd = open("theta_data.csv", "w+")
	data = infoData + str(theta0) + ',' + str(theta1)
	fd.write(data)
	fd.close()

def Affichage(data):
	x_set = [x[0] for x in Origindata]
	y_set = [y[1] for y in Origindata]
	plt.plot(x_set, y_set, 'ro')
	min_x = int(min(x_set))
	max_x = int(max(x_set))
	data = range(min_x, max_x)
	plt.plot(data, [estimation(x) for x in data], 'black')
	plt.show()

def main():
	if (len(argv) != 2):
		print('Usage: %s [data_file.csv]' % argv[0])
		exit()
	data = parse(argv[1])
	data = calculThetas(data)
	fileThetas(argv[1])
	Affichage(data)

if __name__ == '__main__':
  main()
