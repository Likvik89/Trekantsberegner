import math

def main():

     #definerer klasserne sider og vinkler
     class side:
          def __init__(self, name, length, pairing_angle):
               self.name = name
               self.length = length
               flag = False
               self.pairing_angle = pairing_angle
     
     class vinkel:
          def __init__(self, name, angle, pairing_side):
               self.name = name
               self.angle = angle
               flag = False
               self.pairing_side = pairing_side
     
     class calculate:
          def __init__(self, identifier_1, value_1, identifier_2, value_2, identifier_3, value_3):
               identifier_1 = identifier_1
               value_1 = value_1
               identifier_2 = identifier_2
               value_2 = value_2
               identifier_3 = value_3

     #alle (relevante) variabler i en trekant
     a = side("a", 0.0, A)
     b = side("b", 0.0, B)
     c = side("c", 0.0, C)
     A = vinkel("A", 0.0, a)
     B = vinkel("B", 0.0, b)
     C = vinkel("C", 0.0, c)

     #lister med variablernes navne
     #til sammenligning om de returnerede navne er gyldige
     variablenames = ["a", "b", "c", "A", "B", "C"]
     variables = [a, b, c, A, B, C] 
     
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
               variables[index].length = value_2
               known_sides.append(variables[index])

               #ændrer variablens vinkel og tilføjer den til listen over kendte vinkler
          elif variables[index].__class__ == vinkel:
               variables[index].angle = value_2
               known_angles.append(variables[index])
 
     #finder brugerens angivne variabel
     if identifier_3 in variablenames:
          index = variablenames.index(identifier_3)
          variables[index].flag = True

          #checker variablens klasse
          if variables[index].__class__ == side:

               #ændrer variablens længde og tilføjer den til listen over kendte sider
               variables[index].length = value_3
               known_sides.append(variables[index])

               #ændrer variablens vinkel og tilføjer den til listen over kendte vinkler
          elif variables[index].__class__ == vinkel:
               variables[index].angle = value_3
               known_angles.append(variables[index])
     
     calculate_triangle(a, b, c, A, B, C)


def calculate_triangle(a, b, c, A, B, C):
     pass

def calculate_3_sides(a, b, c):
     A = math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c)))
     B = math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
     C = math.degrees(math.acos((a**2+b**2-c**2)/(2*a*b)))
     print("A: " , A)
     print("B: " , B)
     print("C: " , C)

     

if __name__ == "__main__":
    main()

