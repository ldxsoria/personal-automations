import os
import csv
import pathlib

#os.system('clear')
print('Bienvenido, este Script fue desarrolado en python por ldxsoria\nsigueme en: https://github.com/ldxsoria\n')
print('REQUISITOS:')
print("1) Crear una nueva carpeta")
print('2) Copiar este script en esa nueva carpeta')
print('3) Copiar todos los pdf en la carpeta*')
print('4) Crear un .csv con todos los nombres a cambiar en el orden de los pdf')
print('5) Ejecuta el script')
print('\n*La finalidad de este script es que despues de separar un pdf por ejemplo')
print('diplomas.pdf en diploma-1.pdf, diploma-2.pdf, etc, y usar la misma relacion ')
print('de nombres de los diplomas para cambiar el nombre del archivo diploma1.pdf a') 
print('nombre1.pdf, diploma2.pdf a nombre2.pdf ...\n')
orden = input('Presiona "enter" para iniciar > ')

if orden != None:
	#Obtener nombre de todos los archivos en Orden
	#path = '.'
	path = pathlib.Path(__file__).parent.resolve()
	original_names = []
	directorio = pathlib.Path(path)
	for archivo in directorio.iterdir():
		if(archivo.name.endswith(".pdf")):
			original_names.append(archivo.name)

	#print(len(original_names))
	#print(original_names)



	#Obtener nuevos nombres de un txt
	with open('nombres.csv', 'r') as f:
		reader = csv.reader(f)
		new_name = list(reader)
	#print(len(new_name))
	#print(new_name)


	#Cambiar nombre a los archivos
	for i in range(0,len(original_names)):
		#print (original_names[i])
		#print (new_name[i])
		comando = '%s,"%s.pdf"' %(original_names[i],new_name[i])
		comando = comando.replace("[","")
		comando = comando.replace("]","")
		comando = comando.replace("'","")
		comando = comando.replace(","," ")
		os.system("rename %s" % comando)
		#print(comando)