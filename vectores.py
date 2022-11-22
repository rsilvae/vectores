class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def vector_addition(self,b):
        cx=int(self.x)+int(b.x) 
        cy=int(self.y)+int(b.y)
        cz=int(self.z)+int(b.z)
        answer=Vector(cx,cy,cz)
        return answer
 

    def vector_subtraction(self,b):
        cx=int(self.x)-int(b.x)
        cy=int(self.y)-int(b.y)
        cz=int(self.z)-int(b.z)
        answer=Vector(cx,cy,cz)
        return answer
    def producto_punto(self,b):
        cx=int(self.x)*int(b)
        cy=int(self.y)*int(b)
        cz=int(self.z)*int(b)
        answer = cx+cy+cz
        print(answer)


    def print_vector(self):
        print(self.x,self.y,self.z)
    
    def print_menu(self):
        print("Elija una opcion")
        print("1.Suma.")
        print("2.Resta.")
        print("3.Producto punto.")
            
        
        
    
    
print("Elija una opcion")
print("1.Suma.")
print("2.Resta.")
print("3.Producto punto.")
opcion = input()


if (opcion == "1"):
    x1=input("Ingrese la x del primer vector: ")
    y1=input("Ingrese la y del primer vector: ")
    z1=input("Ingrese la z del primer vector: ")
    x2=input("Ingrese la x del segundo vector: ")
    y2=input("Ingrese la y del segundo vector: ")
    z2=input("Ingrese la z del segundo vector: ")
    vector1= Vector(x1,y1,z1)
    vector2= Vector(x2,y2,z2)
    vectorf=vector1.vector_addition(vector2)
    print("La suma es: ")
    #vectorf.print_vector
    vector1.vector_addition(vector2).print_vector()

elif opcion =="2":
    x1=input("Ingrese la x del primer vector: ")
    y1=input("Ingrese la y del primer vector: ")
    z1=input("Ingrese la z del primer vector: ")
    x2=input("Ingrese la x del segundo vector: ")
    y2=input("Ingrese la y del segundo vector: ")
    z2=input("Ingrese la z del segundo vector: ")
    vector1= Vector(x1,y1,z1)
    vector2= Vector(x2,y2,z2)
    vectorf=vector1.vector_subtraction(vector2)
    print("La resta es: ")
    vectorf.print_vector
    vector1.vector_subtraction(vector2).print_vector()

elif opcion =="3":
    x1=input("Ingrese la x del vector: ")
    y1=input("Ingrese la y del vector: ")
    z1=input("Ingrese la z del vector: ")
    vector1= Vector(x1,y1,z1)
    pro = input("Ingrese el numero con para multiplicar: ")
    print("La resta es: ",vector1.producto_punto(pro))
    
