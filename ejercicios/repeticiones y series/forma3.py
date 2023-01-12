"""
Forma tres:
1 while con aumento "manual" de repeticiones
"""
print("Tercera Forma")

serie = 1 # primera serie
repeticion = 1 # primera repeticion
print("Serie: ", serie)
while (serie < 4):
    print("Repetición: ", repeticion)
    repeticion += 1 # siguiente repeticion
    if (repeticion == 6):
        serie += 1 # siguiente serie
        repeticion = 1 # primera repeticion (para la nueva serie)
        if (serie < 4): # si la serie es menor a 4 (todavía no nos pasamos) se imprime la serie
            print("Serie: ", serie)
    
