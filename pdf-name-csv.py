import os
import csv
import pathlib


#Obtener nombre de todos los archivos en Orden
ejemplo_dir = '.'
original_names = []
directorio = pathlib.Path(ejemplo_dir)
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
	os.system("mv %s" % comando)
	#print(comando)