class დედისდედა(object):
    def ბურთი(self):
        print("მე მაქვს წითელი ბურთი!")

class დედისმამა(object):
    def ბურთი(self):
        print("მე მაქვს სტაფილოსფერი ბურთი!")

class მამისდედა(object):
    def ბურთი(self):
        print("მე მაქვს ყვითელი ბურთი!")

class მამისმამა(object):
    def ბურთი(self):
        print("მე მაქვს მწვანე ბურთი!")

class დედა(დედისდედა, დედისმამა):
    def ბურთი(self):
        print("მე მაქვს ცისფერი ბურთი!")

class მამა(მამისდედა, მამისმამა):
    def ბურთი(self):
        print("მე მაქვს ლურჯი ბურთი!")
        
class შვილი(დედა, მამა):
    def MRO(self):
      return self.__class__.__mro__

    def ბურთი(self,cls):
        super(cls, self).ბურთი()

ელისაბედი=შვილი()
mro=list(ელისაბედი.MRO())
# print(type(mro))
# print(mro)
for i in mro[:-2]:
  ელისაბედი.ბურთი(i)
