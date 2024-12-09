import math

def main():

     #definerer klasserne sider og vinkler
     class side:
          def __init__(self, name, length):
               self.name = name
               self.length = length
     
     class vinkel:
          def __init__(self, name, angle):
               self.name = name
               self.angle = angle
     
     #alle (relevante) variablerne i en trekant
     a = side("a", 0.0)
     b = side("b", 0.0)
     c = side("c", 0.0)
     A = vinkel("A", 0.0)
     B = vinkel("B", 0.0)
     C = vinkel("C", 0.0)

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

          #checker variablens klasse
          if variables[index].__class__ == side:

               #ændrer variablens længde og tilføjer den til listen over kendte sider
               variables[index].length = value_3
               known_sides.append(variables[index])

               #ændrer variablens vinkel og tilføjer den til listen over kendte vinkler
          elif variables[index].__class__ == vinkel:
               variables[index].angle = value_3
               known_angles.append(variables[index])
     
     match len(known_sides):
          case 0:
               print("Kan ikke udregne siderne")
          case 1:
               calculate_1_side()
          case 2:
               calculate_2_sides()
          case 3:
               calculate_3_sides(a.length, b.length, c.length)
          case _:
               print("noget gik galt, prøv igen")

     if False:
          print(a.length)
          print(b.length)
          print(c.length)
          print(A.angle)
          print(B.angle)
          print(C.angle)


def calculate_1_side():
     print("calculating 1")

def calculate_2_sides():
     print("calculate 2")

def calculate_3_sides(a, b, c):
     A = math.degrees(math.acos((b**2+c**2-a**2)/(2*b*c)))
     B = math.degrees(math.acos((a**2+c**2-b**2)/(2*a*c)))
     C = math.degrees(math.acos((a**2+b**2-c**2)/(2*a*b)))
     print(A, B, C)

     

if __name__ == "__main__":
    main()

