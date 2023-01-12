def process(rut):
    def readFiles(file, lines):
        f = open (file,'r')
        if lines:
            texto = f.readlines()
        else:
            texto = f.read()
        f.close()
        return texto

    def clearNewLines(list):
        listAux = []
        for item in list:
            listAux.append(item.replace('\n', ''))
        return listAux

    def decodeNotes(listNotes, text, rut):
        notasDeco = []

        i = 0
        while i < len(listNotes):
            notasDeco.append("")
            j = 0
            while j < len(listNotes[i]):
                k = j
                if j >= 8:
                    k = j - 8
                pos = int(rut[k])
                letra = listNotes[i][j]
                deco = text[text.find(letra) - pos]
                notasDeco[i] += deco
                j += 1
            i += 1
        return notasDeco

    def showNote(listNotes, rut):
        i = 0
        while i < len(listNotes):
            print(listNotes[i])
            if listNotes[i].find(rut) == 0:
                datos = listNotes[i].split(';')
                print("Rut:", datos[0])
                j = 1
                while j < len(datos):
                    print("Nota " + str(j) + ":", datos[j])
                    j += 1
                break
            i += 1

    texto = readFiles('Texto deco.txt', False)
    texto = texto.replace("texto = \"", "").replace("\"", "")
    notasEnc = readFiles('notas_raro.txt', True)
    notas = clearNewLines(notasEnc)
    notasDeco = decodeNotes(notas, texto, rut)
    showNote(notasDeco, rut)

rut = "24326475"

process(rut)