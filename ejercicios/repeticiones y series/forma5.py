"""
Forma cinco:
Sólo con for
para mostrar (imprimir) un valor usado con for, se le suma 1 porque toma como primer índice el 0
"""
print("Quinta Forma")

for serie in range(3):
    print("Serie: ", serie + 1)
    for repeticion in range(5):
        print("Repetición: ", repeticion + 1)
