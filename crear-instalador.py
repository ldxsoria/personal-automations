import os
import pathlib

#path = pathlib.Path(__file__).parent.resolve()

numero = input('Numero de la version >')

os.mkdir(f'{numero}')

dir = f'{numero}'

os.system(f'pyinstaller --onefile pdf-name-csv.py')