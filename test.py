class Glas:
    def __init__(self,diameter,hoogte,oor,inhoud,vol):
        self.diameter = diameter
        self.hoogte = hoogte
        self.oor = oor
        self.inhoud = inhoud
        self.vol = vol
        
    def vullen(self):
        print('dit glas wordt gevuld')
    
    def ruimte(self):
        #bereken de inhoud van het glas in vierkante centimeter
        return round(((((self.diameter)/2)**2)*3.14159)*(self.hoogte),3)

MijnGlas= Glas(10,15,True,None,0)


print(MijnGlas.ruimte(),"cm^3")