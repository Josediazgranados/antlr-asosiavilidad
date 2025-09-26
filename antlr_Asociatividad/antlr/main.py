import sys
from antlr4 import *
from ExprLeftLexer import ExprLeftLexer
from ExprLeftParser import ExprLeftParser
from ExprRightLexer import ExprRightLexer
from ExprRightParser import ExprRightParser
from EvalVisitor import EvalLeftVisitor, EvalRightVisitor

def main():
    try:
        with open("cadena.txt", "r") as f:
            lines = f.readlines()
        test_expressions = []
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#'):
                test_expressions.append(line)
                
    except FileNotFoundError:
        print("Aviso: No se encontro el archivo cadena.txt")
        with open("cadena.txt", "w") as f:
            for expr in sample_expressions:
                f.write(expr + "\n")
        test_expressions = sample_expressions
        print("Se creo el archivo cadena.txt con ejemplos por defecto")
    
    print("=" * 70)
    print("EJECUCION DEL PROGRAMA ANTLR")
    print("=" * 70)
    
    print("\nGRAMATICA LEFT (original):")
    print("- Asociatividad: izquierda en todos los operadores")
    print("- Precedencia: multiplicacion/division sobre suma/resta")
    print("- Operadores soportados: +, -, *, /")
    
    print("\nGRAMATICA RIGHT (redisenada):")
    print("- Asociatividad: potencia a la derecha, resto a la izquierda")  
    print("- Precedencia: ^ mayor que */ y mayor que +-")
    print("- Operadores soportados: +, -, *, /, ^")
    
    print(f"\nSe cargaron {len(test_expressions)} expresiones desde cadena.txt")
    
    print("\n" + "=" * 70)
    print("EVALUACION DE RESULTADOS")
    print("=" * 70)
    
    for i, expr in enumerate(test_expressions, 1):
        print(f"\n{i}. Expresion: {expr}")
        print("-" * 50)
        try:
            input_stream = InputStream(expr)
            lexer = ExprLeftLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = ExprLeftParser(stream)
            tree = parser.prog()
            result_left = EvalLeftVisitor().visit(tree)
            print(f"Left -> {result_left}")
        except Exception:
            print("Left -> ERROR (operador no valido)")
        
        try:
            input_stream = InputStream(expr)
            lexer = ExprRightLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = ExprRightParser(stream)
            tree = parser.prog()
            result_right = EvalRightVisitor().visit(tree)
            print(f"Right -> {result_right}")
        except Exception as e:
            print(f"Right -> ERROR ({e})")

if __name__ == "__main__":
    main()

