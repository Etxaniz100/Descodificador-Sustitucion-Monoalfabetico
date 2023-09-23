
textoSInDescifrar = ""
print("Texto:")
#textoSInDescifrar = input().str.lower()

textoSInDescifrar = "RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KxvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."

textoSInDescifrar = textoSInDescifrar.lower()

diccionarioFrecuencia = {}
numLetras = 0

#Definimos un diccionario con las letras del diccionario y su frecuencia en textos
diccionarioFrecuenciaReal = {"e":16.78, "a":11.96, "o":8.69, "l":8.37, "s":7.88, "n":7.01, "d":6.87, "r": 4.94, "u":4.8, "i":4.15, "t":3.31, "c":2.92, "p":2.776, "m":2.12, "y":1.54, "q":1.53, "b":0.92, "h": 0.89, "g":0.73, "f":0.52, "v": 0.39, "j": 0.3, "ñ":0.29, "z":0.15, "x":0.06, "k":0.0, "w":0.0}


#Creamos un nuevo diccionario con las letras del diccionario
for i in diccionarioFrecuenciaReal.keys():
    diccionarioFrecuencia[i] = 0


#Recorriendo el texto contamos cuantas letras hay de cada
for letra in textoSInDescifrar:
    if letra not in diccionarioFrecuenciaReal.keys():
        pass

    elif letra in diccionarioFrecuencia.keys():
        diccionarioFrecuencia[letra] += 1
        numLetras += 1


#Teniendo el numero de letras, calculamos su frecuencia en base al numero de letras totales
diccionarioPorcentajeFrecuencia = {}

for letra in diccionarioFrecuencia.keys():
    diccionarioPorcentajeFrecuencia[letra] = (diccionarioFrecuencia[letra]/numLetras)*100


def bubbleSort(diccionario):

    arrayLetras = []
    arrayFrecuencia = []

    for i in diccionario.keys():
        arrayLetras.append(i)
        arrayFrecuencia.append(diccionario[i])

    for i in range(len(arrayFrecuencia)):

        for j in range(0, len(arrayFrecuencia) - i - 1):

            if arrayFrecuencia[j] < arrayFrecuencia[j + 1]:

                temp = arrayFrecuencia[j]
                arrayFrecuencia[j] = arrayFrecuencia[j+1]
                arrayFrecuencia[j+1] = temp

                temp2 = arrayLetras[j]
                arrayLetras[j] = arrayLetras[j+1]
                arrayLetras[j+1] = temp2

    return(arrayLetras, arrayFrecuencia)


def solucionPoe(diccionarioPorcentajeFrecuencia, texto):

    def aumentarCont(diccionario, letra):
            if letra not in diccionario.keys():
                diccionario[letra] = 1
            else:
                diccionario[letra] += 1

    def contarLetra(diccionarioSolucion, diccionarioSolucionInverso, letraBuscada, listaPalabraBuscada, palabraDada, diccionarioTemporal):

        #Solo funciona si la letra buscada solo aparece una vez

        for palabraBuscada in listaPalabraBuscada:
            
            if len(palabraDada) == len(palabraBuscada):


                valido = True

                #Miramos en que posicion de la palabra esta la letra que buscamos
                posLetraBuscada = -1

                for i in range(0, len(palabraDada)):
                    if palabraBuscada[i] == letraBuscada:
                        posLetraBuscada = i
                        #Si la letra que esta en esa posicion ya la tenemos descifrada, no nos interesa seguir con esta palabra
                        if palabraDada[i] in diccionarioSolucion.keys():
                            valido = False
                
                if posLetraBuscada == -1:
                    valido = False

                cont = 0

                while valido and cont < len(palabraDada):
                    #Es importante saltaros la letra que buscamos
                    if(cont != posLetraBuscada):
                        valido = (palabraBuscada[cont] in diccionarioSolucionInverso.keys() and palabraDada[cont] == diccionarioSolucionInverso[palabraBuscada[cont]])
                    cont += 1


                if valido:
                    aumentarCont(diccionarioTemporal, palabraDada[posLetraBuscada])
                    return True

    def obtenerLetraCodificada(letra, listaPalabrasBuscar, listaPalabras, diccionarioSolucion, diccionarioSolucionInverso):

        diccionarioTemporal = {}

        for i in listaPalabras:
            contarLetra(diccionarioSolucion, diccionarioSolucionInverso, letra, listaPalabrasBuscar, i, diccionarioTemporal)
                
        (listaBuena, laOtra) = bubbleSort(diccionarioTemporal)
        if(len(listaBuena)) > 0: 
            print(listaBuena[0] + " --> " + letra)
            diccionarioSolucion[listaBuena[0]] = letra
            diccionarioSolucionInverso[letra] = listaBuena[0] 


    ret = ""
    (arrayLetras,arrayFrecuencia) = bubbleSort(diccionarioPorcentajeFrecuencia)
    #(arrayLetrasReal,arrayFrecuenciaReal) = bubbleSort(diccionarioFrecuenciaReal)
    
    diccionarioSol = {}
    diccionarioSolInverso = {}


    texto2 = texto.replace(",", "")
    texto2 = texto2.replace(".", "")
    texto2 = texto2.replace(":", "")
    texto2 = texto2.replace(";", "")
    texto2 = texto2.replace("(", "")
    texto2 = texto2.replace(")", "")
    texto2 = texto2.replace("0", "")
    texto2 = texto2.replace("1", "")
    texto2 = texto2.replace("2", "")
    texto2 = texto2.replace("3", "")
    texto2 = texto2.replace("4", "")
    texto2 = texto2.replace("5", "")
    texto2 = texto2.replace("6", "")
    texto2 = texto2.replace("7", "")
    texto2 = texto2.replace("8", "")
    texto2 = texto2.replace("9", "")

    preListaPalabras = texto2.split(" ")

    listaPalabras = []

    for i in preListaPalabras:
        if i != "":
            listaPalabras.append(i)

    descodificando = True

    while descodificando:

        if("e" not in diccionarioSolInverso.keys()):
            #SUPONER E
            diccionarioSol[arrayLetras[0]] = "e"
            diccionarioSolInverso["e"] = arrayLetras[0]
            print(arrayLetras[0] + " --> e")

        if("a" not in diccionarioSolInverso.keys()):
            #SUPONER A
            diccionarioSol[arrayLetras[1]] = "a"
            diccionarioSolInverso["a"] = arrayLetras[1]
            print(arrayLetras[1] + " --> a")

        if("l" not in diccionarioSolInverso.keys()):
            # INTENTO L
            obtenerLetraCodificada("l", ["el", "la"], listaPalabras, diccionarioSol, diccionarioSolInverso)
          
        if("r" not in diccionarioSolInverso.keys()):
            #INTENTO OBTENER R
            
            diccionarioTemp = {}
            for i in listaPalabras:
                aux = ""
                for j in i: #Para cada letra
                    if j == aux:
                        aumentarCont(diccionarioTemp, j)
                    aux = j

            (listaBuena, laOtra) = bubbleSort(diccionarioTemp)

            #Nos aseguramos de no solapar las ll
            #Es posible no encontrar ninguna doble r
            if(len(listaBuena)) > 0: 
                if(listaBuena[0] == diccionarioSolInverso["l"]):
                    diccionarioSol[listaBuena[1]] = "r"
                    print(listaBuena[1] + " --> s")
                    diccionarioSolInverso["r"] = listaBuena[1]
                else:
                    diccionarioSol[listaBuena[0]] = "r"
                    print(listaBuena[0] + " --> r")
                    diccionarioSolInverso["r"] = listaBuena[0]

            listaBuena = []
            diccionarioTemp = {}

        if("s" not in diccionarioSolInverso.keys()):
            #INTENTO OBTENER S 
            diccionarioTemp = {}
            cont = 0
            for i in listaPalabras:

                if (len(i) == 3) and i[0] == diccionarioSolInverso["l"]:

                    aumentarCont(diccionarioTemp, i[len(i)-1])

            (listaBuena, laOtra) = bubbleSort(diccionarioTemp)
            if(len(listaBuena)) > 0:     
                print(listaBuena[0] + " --> s")
                diccionarioSol[listaBuena[0]] = "s"
                diccionarioSolInverso["s"] = listaBuena[0]

            listaBuena = []
            diccionarioTemp = {}

        if("d" not in diccionarioSolInverso.keys()):
            # INTENTO D
            obtenerLetraCodificada("d", ["del", "de", "desde"], listaPalabras, diccionarioSol, diccionarioSolInverso)
            
        if("o" not in diccionarioSolInverso.keys()):
            # SUPOSICION O
            encontrado = False
            cont = 0
            while not encontrado:
                if arrayLetras[cont] not in diccionarioSol.keys():
                    encontrado = True
                cont += 1

            print(arrayLetras[cont-1] + " --> o")
            diccionarioSol[arrayLetras[cont-1]] = "o"
            diccionarioSolInverso["o"] = arrayLetras[cont-1]

        if("n" not in diccionarioSolInverso.keys()):
            # INTENTO N
            obtenerLetraCodificada("n", ["en", "no", "son", "nos", "sino", "nada"], listaPalabras, diccionarioSol, diccionarioSolInverso)
            
        if("u" not in diccionarioSolInverso.keys()):
            # INTENTO U
            obtenerLetraCodificada("u", ["un", "una", "su", "sus"], listaPalabras, diccionarioSol, diccionarioSolInverso)
            
        if("y" not in diccionarioSolInverso.keys()):
            # INTENTO Y
            obtenerLetraCodificada("y", ["y", "ya", "yo", "ayer", "ley", "soy"], listaPalabras, diccionarioSol, diccionarioSolInverso)
            
        if("p" not in diccionarioSolInverso.keys()):
            # INTENTO P
            obtenerLetraCodificada("p", ["por", "pero", "para", "puede", "despues"], listaPalabras, diccionarioSol, diccionarioSolInverso)
            
        if("q" not in diccionarioSolInverso.keys()):
            # INTENTO Q
            obtenerLetraCodificada("q", ["que", "porque", "aunque", "quien", "aquel", "aquella", "aquellos"], listaPalabras, diccionarioSol, diccionarioSolInverso)
            
        if("m" not in diccionarioSolInverso.keys()):
            # INTENTO M
            obtenerLetraCodificada("m", ["me", "mas", "muy", "menos", "mundo", "mayor", "ademas"], listaPalabras, diccionarioSol, diccionarioSolInverso)
            
        if("t" not in diccionarioSolInverso.keys()):
            # INTENTO T
            obtenerLetraCodificada("t", ["este", "te", "entre", "todo", "hasta", "todos", "parte", "otra", "tan", "ten"], listaPalabras, diccionarioSol, diccionarioSolInverso)

        if("c" not in diccionarioSolInverso.keys()):
            # INTENTO C
            obtenerLetraCodificada("c", ["con", "como", "cada", "cuando", "hace", "contra", "caso", "hacer", "poco"], listaPalabras, diccionarioSol, diccionarioSolInverso)

        if("i" not in diccionarioSolInverso.keys()):
            # INTENTO I
            obtenerLetraCodificada("i", ["si", "sin", "ahi", "asi", "mi", "ni", "tiene", "dia"], listaPalabras, diccionarioSol, diccionarioSolInverso)

        if("f" not in diccionarioSolInverso.keys()):
            # INTENTO F
            obtenerLetraCodificada("f", ["fue", "forma", "fueron", "fin", "frente", "fuera", "final", "informacion", "familia"], listaPalabras, diccionarioSol, diccionarioSolInverso)

        if("h" not in diccionarioSolInverso.keys()):
            # INTENTO H
            obtenerLetraCodificada("h", ["hasta", "han", "hay", "ahora", "hace", "hacer", "hacia", "hecho", "mucho", "hoy", "hombre", "he", "historia", "muchos", "noche", "haber", "habian", "hizo", "horas"], listaPalabras, diccionarioSol, diccionarioSolInverso)

        if("b" not in diccionarioSolInverso.keys()):
            # INTENTO B
            obtenerLetraCodificada("b", ["sobre", "tambien", "habia", "bien", "gobierno", "estaba", "hombre", "debe", "haber", "habian", "posible", "cambio", "obra", "problemas", "problema", "obras", "sobres", "posibles", "nombre", "obrera", "obrero", "publico"], listaPalabras, diccionarioSol, diccionarioSolInverso)

        if("g" not in diccionarioSolInverso.keys()):
            # INTENTO G
            obtenerLetraCodificada("g", ["gobierno", "gran", "segun", "general", "algo", "lugar", "algunos", "luego", "embargo", "grupo", "grandes", "guerra", "gente", "algunas", "siglo", "alguna", "segundo"], listaPalabras, diccionarioSol, diccionarioSolInverso)

        if("v" not in diccionarioSolInverso.keys()):
            # INTENTO V
            obtenerLetraCodificada("v", ["nivel", "tuvo", "varios", "voz", "van", "vista", "servicio", "servicios", "movimiento", "visto", "actividad", "joven", "nuevos", "valor", "investigacion", "nuevas"], listaPalabras, diccionarioSol, diccionarioSolInverso)

        if("j" not in diccionarioSolInverso.keys()):
            # INTENTO J
            obtenerLetraCodificada("j", ["hijo", "hija", "consejo", "julio", "joven", "abeja", "acoja", "acojo"], listaPalabras, diccionarioSol, diccionarioSolInverso)

        if("ñ" not in diccionarioSolInverso.keys()):
            # INTENTO Ñ
            obtenerLetraCodificada("ñ", ["año", "años", "niño", "niños", "niña", "niñas", "españa", "español", "española", "mañana", "señor", "señora", "añade", "añado", "añadir"], listaPalabras, diccionarioSol, diccionarioSolInverso)

        if("z" not in diccionarioSolInverso.keys()):
            # INTENTO Z
            obtenerLetraCodificada("z", ["vez", "hizo", "cabeza", "voz", "luz", "fuerza", "zona", "razon", "paz", "organizacion", "abraza", "abrazo", "actriz"], listaPalabras, diccionarioSol, diccionarioSolInverso)

        if("x" not in diccionarioSolInverso.keys()):
            # INTENTO X
            obtenerLetraCodificada("x", ["mexico", "texto", "textos", "ex", "existe", "existen", "existo", "existio", "exclusivo", "exclusiva"], listaPalabras, diccionarioSol, diccionarioSolInverso)

        if("k" not in diccionarioSolInverso.keys()):
            # INTENTO K
            obtenerLetraCodificada("k", ["kilo", "kilogramo", "kg", "kb", "hack", "ok", "okey", "rock", "york", "kanji", "kebab", "koala", "vodka"], listaPalabras, diccionarioSol, diccionarioSolInverso)

        if("w" not in diccionarioSolInverso.keys()):
            # INTENTO W
            obtenerLetraCodificada("w", ["kiwi", "word", "show", "flow", "hawai", "darwin", "newton", "taiwan", "whisky", "kw"], listaPalabras, diccionarioSol, diccionarioSolInverso)







        textoRes = ""
        for i in texto:
            if i in diccionarioSol.keys():
                textoRes = textoRes + diccionarioSol[i]
            else:
                textoRes = textoRes + i.upper()
        

        print()
        print("Traduccion hasta el momento : ")
        print(textoRes)
        
        print()
        print("¿Quieres arreglar o añadir mas letras a mano para acabar de descodificarlo?")
        print()
        print("[0] Salir")
        print("[1] Arreglar")
        print("[2] Añadir")
        respuesta = input()
        if respuesta == "2" or respuesta == "anadir":

            print()
            print("AVISO : Introduzca 'salir' cuando haya acabado")
            continuar = True

            while continuar:
                print("Introduzca letra supuesta. Primero la que ves, y luego la que crees que representa")

                print()
                letra1 = input("Letra Codificada : ")
                if(letra1.lower != "salir"):

                    letra2 = input("Letra Descodificada : ")
                    print()

                    diccionarioSol[letra1] = letra2
                    diccionarioSolInverso[letra2] = letra1

                    textoRes = ""
                    for i in texto:
                        if i in diccionarioSol.keys():
                            textoRes = textoRes + diccionarioSol[i]
                        else:
                            textoRes = textoRes + i.upper()
        
                    print(textoRes)
                else:
                    descodificando = False
                    continuar = False

        elif respuesta == "1" or respuesta == "arreglar":

            
            print("Introduzca letra erronea. Primero la que ves, y luego la que crees que deberia ser")

            print()
            letra1 = input("Letra Erronea : ")
            if(letra1.lower != "salir"):

                letra2 = input("Letra Correcta : ")
                print()

                letraCodificada = diccionarioSolInverso[letra1]

                diccionarioSol = {}
                diccionarioSolInverso = {}

                diccionarioSol[letraCodificada] = letra2
                diccionarioSolInverso[letra2] = letraCodificada
                print(letraCodificada + " --> " + letra2)



        else:
            descodificando = False

                

            
    return(textoRes)


resultado = solucionPoe(diccionarioPorcentajeFrecuencia, textoSInDescifrar)

print()
print("Texto descifrado : ")
print()
print(resultado)
        
          