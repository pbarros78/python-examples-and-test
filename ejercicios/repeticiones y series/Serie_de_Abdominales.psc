Proceso Serie_de_Abdominales
	Definir serie,repeticiones Como Entero;
	serie <- 1;
	Mientras serie<4 Hacer
		Escribir 'Serie: '+ConvertirATexto(serie);
		repeticiones <- 1;
		Mientras repeticiones<6 Hacer
			Escribir 'Repeticion: '+ConvertirATexto(repeticiones);
			repeticiones <- repeticiones+1;
		FinMientras
		serie <- serie+1;
	FinMientras
FinProceso
