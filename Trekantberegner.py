import math

def main():

     class variable:
          def __init__(self, name, length):
               self.name = name
               self.value = length
     
     class calculate:
          def __init__(self, identifier_1, identifier_2, identifier_3, function):
               self.identifier_1 = identifier_1
               self.identifier_2 = identifier_2
               self.identifier_3 = identifier_3

               self.function = function

     a = variable("a", 0.0)
     b = variable("b", 0.0)
     c = variable("c", 0.0)
     A = variable("A", 0.0)
     B = variable("B", 0.0)
     C = variable("C", 0.0)

     abc = calculate(a, b, c, calculate_a_b_c)
     abA = calculate(a, b, A, calculate_a_b_A)
     abB = calculate(a, b, B, calculate_a_b_B)
     abC = calculate(a, b, C, calculate_a_b_C)
     acA = calculate(a, c, A, calculate_a_c_A)
     acB = calculate(a, c, B, calculate_a_c_B)
     acC = calculate(a, c, C, calculate_a_c_C)
     bcA = calculate(b, c, A, calculate_b_c_A)
     bcB = calculate(b, c, B, calculate_b_c_B)
     bcC = calculate(b, c, C, calculate_b_c_C)
     aAB = calculate(a, A, B, calculate_a_A_B)
     aAC = calculate(a, A, C, calculate_a_A_C)
     aBC = calculate(a, B, C, calculate_a_B_C)
     aAB = calculate(a, A, B, calculate_a_A_B)
     aAC = calculate(a, A, C, calculate_a_A_C)
     aBC = calculate(a, B, C, calculate_a_B_C)
     bAB = calculate(b, A, B, calculate_b_A_B)
     bAC = calculate(b, A, C, calculate_b_A_C)
     bBC = calculate(b, B, C, calculate_b_B_C)
     cAB = calculate(c, A, B, calculate_c_A_B)
     cAC = calculate(c, A, C, calculate_c_A_C)
     cBC = calculate(c, B, C, calculate_c_B_C)
     ABC = calculate(A, B, C, calculate_A_B_C)

     variablenames = ["a", "b", "c", "A", "B", "C"]
     variables = [a, b, c, A, B, C] 
     
     funktioner = [
     abc,
     abA,
     abB,
     abC,
     acA,
     acB,
     acC,
     bcA,
     bcB,
     bcC,
     aAB,
     aAC,
     aBC,
     aAB,
     aAC,
     aBC,
     bAB,
     bAC,
     bBC,
     cAB,
     cAC,
     cBC
     ]

     identifier_1 = input("indtast navnet på den første kendte variabel:")
     value_1 = float(input("indtast værdien på variablen:"))
     identifier_2 = input("indtast navnet på den anden kendte variabel:")
     value_2 = float(input("indtast værdien på variablen:"))
     identifier_3 = input("indtast navnet på den tredje kendte variabel:")
     value_3 = float(input("indtast værdien på variablen:"))

     if identifier_1 in variablenames:
          index = variablenames.index(identifier_1)
          variables[index].value = value_1


     if identifier_2 in variablenames:
          index = variablenames.index(identifier_2)
          variables[index].value = value_2

 
     if identifier_3 in variablenames:
          index = variablenames.index(identifier_3)
          variables[index].value = value_3

     
     for f in funktioner:
          v1 = variables[variablenames.index(identifier_1)]
          v2 = variables[variablenames.index(identifier_2)]
          v3 = variables[variablenames.index(identifier_3)]
          if v1 == f.identifier_1 or v1 == f.identifier_2 or v1 == f.identifier_3:
               if v2 == f.identifier_1 or v2 == f.identifier_2 or v2 == f.identifier_3:
                    if v3 == f.identifier_1 or v3 == f.identifier_2 or v3 == f.identifier_3:
                         f.function(f.identifier_1.value, f.identifier_2.value, f.identifier_3.value)
                         break

                         

def calculate_a_b_c(a, b, c):
     A = math.degrees(math.acos(max(-1, min(1, (b**2 + c**2 - a**2) / (2 * b * c)))))
     B = math.degrees(math.acos(max(-1, min(1, (a**2 + c**2 - b**2) / (2 * a * c)))))
     C = math.degrees(math.acos(max(-1, min(1, (a**2 + b**2 - c**2) / (2 * a * b))))) 
     print("a: ", a)
     print("b: ", b)
     print("c: ", c)
     print("A: " , A)
     print("B: " , B)
     print("C: " , C)
     main()

def calculate_a_b_A(a, b, A):
     B = math.degrees(math.asin(max(-1, min(1, (math.sin(math.radians(A)) * b)/a))))
     C = 180 - A - B
     c = math.sqrt(a**2 + b**2 - (2*a*b*(math.cos(math.radians(C)))))
     print("a: ", a)
     print("b: ", b)
     print("c: ", c)
     print("A: ", A)
     print("B: ", B)
     print("C: ", C)
     main()

def calculate_a_b_B(a, b, B):
     A = math.degrees(math.asin(max(-1, min(1, (math.sin(math.radians(B)) * a)/b))))
     C = 180 - A - B
     c = math.sqrt(a**2 + b**2 - (2*a*b*(math.cos(math.radians(C)))))
     print("a: ", a)
     print("b: ", b)
     print("c: ", c)
     print("A: ", A)
     print("B: ", B)
     print("C: ", C)
     main()

def calculate_a_b_C(a, b, C):
     c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(C)))
     A = math.degrees(math.acos(max(-1, min(1, (b**2 + c**2 - a**2) / (2 * b * c)))))
     B = 180 - A - C
     print("a: ", a)
     print("b: ", b)
     print("c: ", c)
     print("A: ", A)
     print("B: ", B)
     print("C: ", C)
     main()

def calculate_a_c_A(a, c, A):
     C = math.degrees(math.asin(max (-1, min(1, (math.sin(math.radians(A)) * c)/a))))
     B = 180 - C - A
     b = math.sqrt(a**2 + c**2 - 2*a*c*math.cos(math.radians(A)))
     print("a: ", a)
     print("b: ", b)
     print("c: ", c)
     print("A: ", A)
     print("B: ", B)
     print("C: ", C)
     main()

def calculate_a_c_B(a, c, B):
     b = math.sqrt(a**2 + c**2 - 2*a*c*math.cos(math.radians(B)))
     A = math.degrees(math.asin(max (-1, min(1, (math.sin(math.radians(B)) * a)/b))))
     C = 180 - A - B
     print("a: ", a)
     print("b: ", b)
     print("c: ", c)
     print("A: ", A)
     print("B: ", B)
     print("C: ", C)
     main()

def calculate_a_c_C(a, c, C):
     A = math.degrees(math.asin(max (-1, min(1, (math.sin(math.radians(C)) * a)/c))))
     B = 180 - A - C
     b = math.sqrt(a**2 + c**2 - 2*a*c*math.cos(math.radians(B)))
     print("a: ", a)
     print("b: ", b)
     print("c: ", c)
     print("A: ", A)
     print("B: ", B)
     print("C: ", C)
     main()

def calculate_b_c_A(b, c, A):
     a = math.sqrt(b**2 + c**2 - 2*b*c*math.cos(math.radians(A)))
     B = math.degrees(math.asin(max (-1, min(1, (math.sin(math.radians(A)) * b)/a))))
     C = 180 - A - B
     print("a: ", a)
     print("b: ", b)
     print("c: ", c)
     print("A: ", A)
     print("B: ", B)
     print("C: ", C)
     main()

def calculate_b_c_B(b, c, B):
     C = math.degrees(math.asin(max (-1, min(1, (math.sin(math.radians(B)) * c)/b))))
     A = 180 - C - B
     a = math.sqrt(b**2 + c**2 - 2*b*c*math.cos(math.radians(A)))
     print("a: ", a)
     print("b: ", b)
     print("c: ", c)
     print("A: ", A)
     print("B: ", B)
     print("C: ", C)
     main()

def calculate_b_c_C(b, c, C):
     print("a: ", a)
     print("b: ", b)
     print("c: ", c)
     print("A: ", A)
     print("B: ", B)
     print("C: ", C)

def calculate_a_A_B(a, A, B):
     print("a: ", a)
     print("b: ", b)
     print("c: ", c)
     print("A: ", A)
     print("B: ", B)
     print("C: ", C)

def calculate_a_A_C(a, A, C):
     print("a: ", a)
     print("b: ", b)
     print("c: ", c)
     print("A: ", A)
     print("B: ", B)
     print("C: ", C)

def calculate_a_B_C(a, B, C):
     print("a: ", a)
     print("b: ", b)
     print("c: ", c)
     print("A: ", A)
     print("B: ", B)
     print("C: ", C)

def calculate_b_A_B(b, A, B):
     print("a: ", a)
     print("b: ", b)
     print("c: ", c)
     print("A: ", A)
     print("B: ", B)
     print("C: ", C)

def calculate_b_A_C(b, A, C):
     print("a: ", a)
     print("b: ", b)
     print("c: ", c)
     print("A: ", A)
     print("B: ", B)
     print("C: ", C)

def calculate_b_B_C(b, B, C):
     print("a: ", a)
     print("b: ", b)
     print("c: ", c)
     print("A: ", A)
     print("B: ", B)
     print("C: ", C)

def calculate_c_A_B(c, A, B):
     print("a: ", a)
     print("b: ", b)
     print("c: ", c)
     print("A: ", A)
     print("B: ", B)
     print("C: ", C)

def calculate_c_A_C(c, A, C):
     print("a: ", a)
     print("b: ", b)
     print("c: ", c)
     print("A: ", A)
     print("B: ", B)
     print("C: ", C)

def calculate_c_B_C(c, B, C):
     print("a: ", a)
     print("b: ", b)
     print("c: ", c)
     print("A: ", A)
     print("B: ", B)
     print("C: ", C)

def calculate_A_B_C(A, B, C):
     print("a: ", a)
     print("b: ", b)
     print("c: ", c)
     print("A: ", A)
     print("B: ", B)
     print("C: ", C)

if __name__ == "__main__":
    main()

