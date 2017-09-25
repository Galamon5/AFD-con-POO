AFD con POO en python
Clase AFD - Automata Finito Determinista, se le envía información de cualquier automata y una cadena a  analizar, mostrando al final si la cadena es aceptada o no

Como usar:
- Importa la clase a tu programa
- Señala el o los estados iniciales de tu automata finito determinista a manera de Lista
- Señala el o los estados finales de tu automata finito determinista a manera de Lista
- Señala las transiciones con la tabla de transiciones a manera de lista de listas 
  Ej. transicion 1: [estado actual, caracter, estado al que pasa]
- A la funcion analizar se le manda 1 cadena.

Ej antes del front end.
automata = AFD() #Clase
automata.estadosIniciales = [1,2]
automata.estadosFinales = [2,4]
automata.transiciones = [[1,'1',2],[2,'0',3],[3,'1',4],[4,'0',1]]
cadena = '01'
automata.analizar(cadena)

Código front end en proceso.
