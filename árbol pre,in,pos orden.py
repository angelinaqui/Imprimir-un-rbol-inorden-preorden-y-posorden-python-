#Programa para imprimir un árbol inorden, preorden y posorden 
class Nodo:
    def __init__(self, valor):
        self.hijoIzq = None
        self.hijoDer = None
        self.val = valor
class Arbol:
    def __init__(self,raiz):
        self.raiz = raiz
    def obtenerRaiz(self):
        return self.raiz
    def agregar(self, val):
        if(self.raiz == None):
            self.raiz == Nodo(val)
        else:
            self.agregarNodo(val, self.raiz)
    def agregarNodo(self, val, nodo):
        if(val < nodo.val):
            if(nodo.hijoIzq != None):
                self.agregarNodo(val, nodo.hijoIzq)
            else:
                nodo.hijoIzq = Nodo(val)
        else:
            if(nodo.hijoDer != None):
                self.agregarNodo(val, nodo.hijoDer)
            else:
                nodo.hijoDer = Nodo(val)
    def preorden(self, nodo):
        if(nodo != None):
            print (str(nodo.val))
            if nodo.hijoIzq != None:
                self.preorden(nodo.hijoIzq)
            if nodo.hijoDer != None:
                self.preorden(nodo.hijoDer)
    def inorden(self,nodo):
        if(nodo != None):
            if nodo.hijoIzq != None:
                self.preorden(nodo.hijoIzq)
            print (str(nodo.val))
            if nodo.hijoDer != None:
                self.preorden(nodo.hijoDer)
    def postorden(self,nodo):
        if(nodo != None):
            if nodo.hijoIzq != None:
                self.preorden(nodo.hijoIzq)
            if nodo.hijoDer != None:
                self.preorden(nodo.hijoDer)
            print (str(nodo.val))

class Controladora:
    def main(self):
        g=Arbol(Nodo(8))
        edges=[3,10,1,6,14,4,7,13]
        for i in edges:
            g.agregar(i)
        print("Imprimiendo árbol preorden: ")
        g.preorden(g.obtenerRaiz())
        print("Imprimiendo árbol in-orden: ")
        g.inorden(g.obtenerRaiz())
        print("Imprimiendo árbol postorden: ")
        g.postorden(g.obtenerRaiz())
        
obj=Controladora()
obj.main()