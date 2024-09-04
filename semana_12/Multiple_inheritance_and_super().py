# 3. Investigue qué usos se le pueden dar a la herencia multiple y cree un ejemplo.

# Ejercicio de herencia multiple utilizando super() y MRO.

class A:
    def metodo(self):
        print("Método de A")

class B(A):
    def metodo(self):
        print("Método de B")
        super().metodo() 

class C(A):
    def metodo(self):
        print("Método de C")
        super().metodo()

class D(B, C):
    def metodo(self):
        print("Método de D")
        super().metodo() 

obj = D()
obj.metodo()

# Print MRO para observar flujo de ejecución de super().
print(D.__mro__)
