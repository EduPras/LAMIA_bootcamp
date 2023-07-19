class Contador:
    contador = 0 #atributo de classe

    def inc_maluco(self):
        self.contador += 1 #atributo de instância
        return self.contador
        
    @classmethod
    def inc(cls):
        cls.contador += 1
        return cls.contador

    @classmethod
    def dec(cls):
        cls.contador -= 1
        return cls.contador 
    
    @staticmethod
    def mais_um(n):
        n + 1
    

print(Contador.inc())
print(Contador.inc())
print(Contador.inc())
print(Contador.inc())
print(Contador.dec())
print(Contador.dec())