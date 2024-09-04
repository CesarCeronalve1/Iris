import math 
class Procesos:
    #diccionario = " abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789!#$%&=?¿!¡@._-,;:+"
    diccionario = " abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=[]|:;<>,.?ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    #diccionario = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    MX = 10

    def calidad(self,text):
        resultado = ""
        # Inicializar las variables
        A = False  # Indica si hay vocales
        B = False  # Indica si hay consonantes
        N = False  # Indica si hay números
        S = False  # Indica si hay símbolos
        M = False
        MI = False
        # Definir conjuntos de caracteres
        vocales = set("aeiouAEIOU") & set(self.diccionario)
        consonantes = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ") & set(self.diccionario)
        numeros = set("0123456789") & set(self.diccionario)
        simbolos = set("!@#$%^&*()_+-=[]|;:',.<>?/`~") & set(self.diccionario)

        # Iterar sobre cada carácter en la frase
        while not A or not B or not N or not S or not M or not MI:
            A = False  # Indica si hay vocales
            B = False  # Indica si hay consonantes
            N = False  # Indica si hay números
            S = False  # Indica si hay símbolos
            M = False
            MI = False
            text = self.Viegener(text,self.Fibonazi(text))
            # print(text)
            for char in text:
                if char in vocales:
                    A = True
                    # print("A" + char)
                if char in consonantes:
                    B = True
                    # print("B" + char)
                if char in numeros:
                    N = True
                    # print("n" + char)
                if char in simbolos:
                    S = True
                    # print("s" + char)
                if char.isupper():
                    M = True
                    # print("M" + char)
                if char.islower():
                    MI = True
                    # print("mi" + char)
        resultado = text
        # print(resultado)
        return resultado
    
    def moduloR(self,text):
        resultado = ""
        suma = 0
        for i in range(len(text)):
            suma  = suma + self.numerar(text[i])
        l = self.n2l(int(suma/(len(text))))
        m = suma % len(text)
        # print("suma: " + str(suma) + " promedio: " + str(m))
        ###sin acabar
        resultado = text[:m] + l + text[m + 1:]
        return resultado
    
    
    def moduloC(self,text):
        resultado = ""
        suma = 0
        for i in range(len(text)):
            suma  = suma + self.numerar(text[i])
        l = self.n2l(int(suma/(len(text))))
        m = suma % len(text)
        # print("suma: " + str(suma) + " promedio: " + str(m))
        ###sin acabar
        resultado = self.CCesar(text,m)
        return resultado


    def CCesar(self,text,n):
        resultado = ""
        dic = self.diccionario[1:]
        for i in range(len(text)):
            m = self.numerar(text[i])
            r = n+m
            while r > len(dic):
                r = r - len(dic)
            resultado = resultado + self.n2l(r)

        return resultado

    def Fibonazi(self,txt):
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
            r = r + text[i]
            r = r + text[i-1]
        if len(text) % 2 != 0:
            r = r + text[-1:]    
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
    
    def hop(self,text):
        resultado = ""
        for i in range(int(len(text)/2)):
            resultado = resultado + text[-(i+1)] 
            # print("text-i: " + text[-(i+1)])
            # print("texti: " + text[i])
            resultado = resultado + text[i]
        if len(text) % 2 != 0:
            # print(math.ceil(len(text)/2))
            resultado = resultado + text[math.ceil(len(text)/2)-1]
        # print("resu "+resultado)
        return resultado

    def piramide(self,text):
        resultado = ""
        return resultado

if __name__ == "__main__":
    p = Procesos()
    print("Metodo piramide:" + p.piramide("abc"))

