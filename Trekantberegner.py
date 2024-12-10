import math

def main():

     #definerer klasserne sider og vinkler
     class side:
          def __init__(self, name, length):
               self.name = name
               self.value = length
               flag = False
     
     class vinkel:
          def __init__(self, name, angle):
               self.name = name
               self.value = angle
               flag = False
     
     class calculate:
          def __init__(self, identifier_1, identifier_2, identifier_3, function):
               self.identifier_1 = identifier_1
               self.identifier_2 = identifier_2
               self.identifier_3 = identifier_3

               self.function = function


     #alle (relevante) variabler i en trekant
     a = side("a", 0.0)
     b = side("b", 0.0)
     c = side("c", 0.0)
     A = vinkel("A", 0.0)
     B = vinkel("B", 0.0)
     C = vinkel("C", 0.0)

     abc = calculate(a, b, c, calculate_a_b_C)
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

     #lister med variablernes navne
     #til sammenligning om de returnerede navne er gyldige
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

     #liste over de kendte sider
     known_sides = []
     #liste over de kendte vinkler
     known_angles = []

     #tager input fra brugeren
     #identifier er variablens navn, og value er dens værdi
     identifier_1 = input("indtast navnet på den første kendte variabel:")
     value_1 = float(input("indtast værdien på variablen:"))
     identifier_2 = input("indtast navnet på den anden kendte variabel:")
     value_2 = float(input("indtast værdien på variablen:"))
     identifier_3 = input("indtast navnet på den tredje kendte variabel:")
     value_3 = float(input("indtast værdien på variablen:"))

     #finder brugerens angivne variabel
     if identifier_1 in variablenames:
          index = variablenames.index(identifier_1)
          variables[index].flag = True

          #checker variablens klasse
          if variables[index].__class__ == side:

               #ændrer variablens længde og tilføjer den til listen over kendte sider
               variables[index].length = value_1
               known_sides.append(variables[index])

               #ændrer variablens vinkel og tilføjer den til listen over kendte vinkler
          elif variables[index].__class__ == vinkel:
               variables[index].angle = value_1
               known_angles.append(variables[index])

     #finder brugerens angivne variabel
     if identifier_2 in variablenames:
          index = variablenames.index(identifier_2)
          variables[index].flag = True

          #checker variablens klasse
          if variables[index].__class__ == side:

               #ændrer variablens længde og tilføjer den til listen over kendte sider
               variables[index].value = value_2
               known_sides.append(variables[index])

               #ændrer variablens vinkel og tilføjer den til listen over kendte vinkler
          elif variables[index].__class__ == vinkel:
               variables[index].value = value_2
               known_angles.append(variables[index])
 
     #finder brugerens angivne variabel
     if identifier_3 in variablenames:
          index = variablenames.index(identifier_3)
          variables[index].flag = True

          #checker variablens klasse
          if variables[index].__class__ == side:

               #ændrer variablens længde og tilføjer den til listen over kendte sider
               variables[index].value = value_3
               known_sides.append(variables[index])

               #ændrer variablens vinkel og tilføjer den til listen over kendte vinkler
          elif variables[index].__class__ == vinkel:
               variables[index].value = value_3
               known_angles.append(variables[index])
     
     #matcher de angivne variabler med 
     for f in funktioner:
          print("søger")
          v1 = variables[variablenames.index(identifier_1)]
          v2 = variables[variablenames.index(identifier_2)]
          v3 = variables[variablenames.index(identifier_3)]

          if v1 == (f.identifier_1 or f.identifier_2 or f.identifier_3):
               print("Fandt første variabel")
               if v2 == (f.identifier_1 or f.identifier_2 and f.identifier_3):
                    print("fandt anden variabel")
                    if v3 == (f.identifier_1 or f.identifier_2 or f.identifier_3):
                         print("fandt funktionen")
                         f.function(f.identifier_1.value, f.identifier_2.value, f.identifier_3.value)


          




def calculate_a_b_c(a, b, c):
     A = math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c)))
     B = math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
     C = math.degrees(math.acos((a**2+b**2-c**2)/(2*a*b)))
     print("A: " , A)
     print("B: " , B)
     print("C: " , C)

def calculate_a_b_A(a, b, A):
     pass

def calculate_a_b_B(a, b, B):
     pass

def calculate_a_b_C(a, b, C):
     pass

def calculate_a_c_A(a, c, A):
     pass

def calculate_a_c_B(a, c, B):
     pass

def calculate_a_c_C(a, c, C):
     pass

def calculate_b_c_A(b, c, A):
     pass

def calculate_b_c_B(b, c, B):
     pass

def calculate_b_c_C(b, c, C):
     pass

def calculate_a_A_B(a, A, B):
     pass

def calculate_a_A_C(a, A, C):
     pass

def calculate_a_B_C(a, B, C):
     pass

def calculate_b_A_B(b, A, B):
     pass

def calculate_b_A_C(b, A, C):
     pass

def calculate_b_B_C(b, B, C):
     pass

def calculate_c_A_B(c, A, B):
     pass

def calculate_c_A_C(c, A, C):
     pass

def calculate_c_B_C(c, B, C):
     pass

def calculate_A_B_C(A, B, C):
     pass

if __name__ == "__main__":
    main()

