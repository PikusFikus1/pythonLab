from math import pi,exp
import matplotlib.pyplot as plt

class Funzione:

    def eval(self,x):
        pass

    def integraleInc(self,a,b,M):
        h = (b-a)/M
        return [self.eval(a+(i*h)) for i in range(M)]
    
    def integrale(self,a,b,M):
        h = (b-a)/M
        #sum = 0
        #for i in range(M):
        #    sum += self.eval(a+(i*h))
        #return h*sum
        return h*sum([self.eval(a+(i*h)) for i in range(M)])

class Funzione1(Funzione):

    def eval(self,x):
        return x*x-2*x


class Funzione2(Funzione):

    def eval(self,x):
        return exp(2*x)

    def integrale(self,a,b,M):
        return super().integrale(a,b,M)

class Funzione3(Funzione):

    def eval(self,x):
        return x*x-2*x

    def integrale(self,a,b,M):
        return super().integrale(a,b,M)

f1 = Funzione1()
print(f1.integrale(0,1,100))
f2 = Funzione2()
print(f2.integrale(-pi/2,pi,500))
f3 = Funzione3()
print(f3.integrale(0,1,100))

data = f1.integraleInc(0,1,100)
plt.plot(data, color='tab:red')
plt.show()