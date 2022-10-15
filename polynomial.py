class Polinomial:
    def poly(self,coff,expo,x):
        result = 0
        for i in range(len(expo)):
            result = result + coff[i]*(x**expo[i])
        return result


n = int(input("Number of expression: "))

coff = []
expo = []
for i in range(n):
    co,ex = map(int, input().split())
    # print(co,ex)
    coff.append(co)
    expo.append(ex)
x = int(input("please enter the value of x :"))
ob = Polinomial()
print(ob.poly(coff, expo,x))