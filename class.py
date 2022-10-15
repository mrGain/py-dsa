class Mobile:
    def __init__(self,m):
        self.model = m

    def show_model(self,p):
        price = p
        print("Model :",self.model, "Price :",price)


realme = Mobile("Realme X")
 
# realme.model = "Realme Pro 2" 
realme.show_model(1000)
print(realme.model)      