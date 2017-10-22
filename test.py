import AFD.py
import AFN.py

automata = AFD()
automata.estadosIniciales = [1,2]
automata.estadosFinales = [2,4]
automata.transiciones = [[1,'1',2],[2,'0',3],[3,'1',4],[4,'0',1]]
cadena = '01'
automata.analizar(cadena)
