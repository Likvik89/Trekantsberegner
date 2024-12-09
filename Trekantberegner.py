import math




def main():
     class side:
          def __init__(self, name, length):
               self.name = name
               self.length = length
     
     class vinkel:
          def __init__(self, name, angle):
               self.name = name
               self.angle = angle
     
     a = side("a", 0)
     b = side("b", 0)
     c = side("c", 0)
     A = side("A", 0)
     B = side("B", 0)
     C = side("C", 0)

     variablenames = ["a", "b", "c", "A", "B", "C"]
     variables = [a, b, c, A, B, C] 
     
     identifier_1 = input("indtast navnet på den første kendte variabel:")
     value_1 = float(input("indtast værdien på variablen:"))
     #identifier_2 = input("indtast navnet på den anden kendte variabel:")
     #value_2 = float(input("indtast værdien på variablen:"))
     #identifier_3 = input("indtast navnet på den tredje kendte variabel:")
     #value_3 = float(input("indtast værdien på variablen:"))

     if identifier_1 in variablenames:
          index = variablenames.index(identifier_1)
          if variables[index].__class__ == side:
               variables[index].length = value_1
          
          elif variables[index].__class__ == vinkel:
               variables[index].angle = value_1

          print(variables[index].length)


     #beregn_trekant(a, c, C)

def beregn_trekant(a, c, C):
     
     pass

if __name__ == "__main__":
    main()

