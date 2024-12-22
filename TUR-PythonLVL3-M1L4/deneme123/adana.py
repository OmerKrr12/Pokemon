from attr import has


class Hayvan: 
    def __init__(self, isim, yas): 
        self.isim = isim
        self.yas = yas 
    
    def ses(self): 
        print(f"{self.isim} diyor ki: Ben bir hayvanım!")  




class  Kopek ( Hayvan ) : 
    def __init__(self, isim, cins , yas):
        super().__init__(isim, yas)
        self.cins = cins


    def  havla ( self ) : 
        print ( f" {self.isim} havlıyor: hav-hav!" )



at = Hayvan(isim="At", yas=5)
at.ses()
esek = Hayvan("Eşek" , 2)
esek.ses()


tarçın = Kopek("Tarçın",  "Golden", 3)
tarçın.ses()
tarçın.havla()


