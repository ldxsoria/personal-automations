import os
import pathlib

path = pathlib.Path(__file__).parent.resolve()

numero = input('Numero de la version >')

os.mkdir(f'path/{numero}')

dir = f'path/{numero}'

os.system(f'pyinstaller {dir}/pdf-name-csv.py')