class AFD:
    def __init__(self):
        self.estadosIniciales = []
        self.estadosFinales = []
        self.transiciones = []
        self.flagInicial = 0
        self.flagFinal = 0

    def analizar(self,cadena):
        self.flagInicial = 0
        self.flagFinal = 0
        aux = 0
        estadoActual = 0
        for caracter in cadena:
            self.flagFinal = 0
            #Saber donde empezar
            if(self.flagInicial == 0 and aux == 0):
                aux = aux + 1
                for estadoInicial in self.estadosIniciales:
                    if self.flagInicial:
                        break
                    else:
                        for transicion in self.transiciones:
                            if(estadoInicial == transicion[0] and caracter in transicion):
                                aux = 0
                                self.flagInicial = 1
                                estadoActual = transicion[2]
                                if(estadoActual in self.estadosFinales):
                                    self.flagFinal = 1
                                break
            #Saber donde esta
            else:
                if(aux == 0):
                    for transicion in self.transiciones:
                        aux = aux + 1
                        if(estadoActual == transicion[0] and caracter in transicion):
                            aux = 0
                            estadoActual = transicion[2]
                            if(estadoActual in self.estadosFinales):
                                self.flagFinal = 1
                            break
                else: break

        #Saber donde terminar
        if(self.flagInicial == 1 and self.flagFinal == 1):
            print ("La cadena " + cadena + " es una cadena aceptada")
        else:
            print ("La cadena " + cadena + " es una cadena invalida")

automata = AFD()
automata.estadosIniciales = [1,2]
automata.estadosFinales = [2,4]
automata.transiciones = [[1,'1',2],[2,'0',3],[3,'1',4],[4,'0',1]]
cadena = '01'
automata.analizar(cadena)

