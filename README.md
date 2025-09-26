Proyecto: Comparación de Gramáticas ANTLR en Python
Este proyecto implementa y compara dos gramáticas en ANTLR:

- ExprIzq.g4: con asociatividad izquierda.
- ExprDer.g4: con asociatividad derecha y operador de exponenciación.

Ambas se evalúan en Python utilizando el patrón Visitor.
Archivos del Proyecto
- ExprIzq.g4: Gramática original con asociatividad izquierda
- ExprDer.g4: Gramática rediseñada con asociatividad derecha y exponenciación
- EvalVisitor.py: Visitadores para evaluar las expresiones
- main.py: Programa principal
- cadena.txt: Archivo con las cadenas de prueba
- README.md: Documentación del proyecto
 Instrucciones de Ejecución
1. Generar los parsers con ANTLR
antlr4 -Dlanguage=Python3 -visitor ExprIzq.g4
antlr4 -Dlanguage=Python3 -visitor ExprDer.g4
2. Ejecutar el programa principal
python main.py
El programa leerá automáticamente las expresiones desde cadena.txt y mostrará los resultados usando ambas gramáticas.

