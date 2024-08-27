import math 
class Procesos:
    diccionario = " abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789!#$%&=?¿!¡@._-,;:+"
    #diccionario = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    MX = 10



    def Fibinazi(self,txt):
        resultado = ""
        resultado = txt[0]
        for i in range(1,len(txt)):
            n = self.numerar(txt[i]) + self.numerar(resultado[-1])
            while n >= len(self.diccionario):
                n = n - len(self.diccionario)
            resultado = resultado + self.n2l(n)
        return resultado
    
    def baraja(self,text):
        r = ""
        for i in range(1,len(text),2):
            print(text[i])
            r = r + text[i]
            r = r + text[i-1]
        if len(text) % 2 != 0:
            r = r + text[-1:]    
        print("resultado = "+ r)
        return r





    def numerar(self,L):
        for i,letra in enumerate(self.diccionario):
            if L == letra:
                return i
                break

    def n2l(self,n):
        if n == 0:
            n = n+ 1
        # print(n)
        return self.diccionario[n]
    
    def invertir(self,text):
        resultado = ""
        dic = self.diccionario[1:]
        dicr = dic[::-1]
        for i in range(len(text)):
            for j in range(len(dic)):
                if text[i] == dic[j]:
                    resultado = resultado + dicr[j]
        print("resultado invertido: " + resultado)
        return resultado




    def Viegener(self,data1,data2):
        resultado = ""
        if len(data1) < self.MX:
            data1 = data1 * math.ceil((self.MX/len(data1)))
        
        if len(data2) < self.MX:
            data2 = data2 * math.ceil((self.MX/len(data2)))

        data1 = data1[:self.MX]
        data2 = data2[:self.MX]
        for i in range(self.MX):
            n = self.numerar(data1[i]) + self.numerar(data2[i])
            if n >= len(self.diccionario):
                n = n - len(self.diccionario) 
            resultado = resultado + self.n2l(n)
        return resultado


p = Procesos()
print("Metodo:" + p.baraja("cesar"))

