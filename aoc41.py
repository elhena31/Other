from fileinput import close
import numpy as np  #for working with arrays
import array as arr

with open('bingoexample.txt', 'r') as file:
    all_file = file.read().strip()  # Read and remove any extra new line
    all_file_list = all_file.split('\n')  # make a list of lines
    final_data = [[int(each_int) for each_int in line.split()] for line in all_file_list]  # make list of list and convert to int 
    lista_balotas=final_data[0]
    tableros_iniciales = final_data[2:]

file.close()

    print("balotas",lista_balotas)
    print("tableros:",tableros_iniciales)