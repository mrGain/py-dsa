class Tax:

    tax = {
        'food':20,
        'clothes': 40,
        'makeup' : 5,
        'grocery' : 12
    }

    def add_tax(self,key,value):
        for i in self.tax:
            if key == i :
                return "Iteam already exist", self.tax
        self.tax[key] = value
        return self.tax
        

    def clac_tax(self,item_type):
        try:
            return self.tax[item_type]
        except Exception as e:
            return -1    


if __name__ == "__main__":
    ob = Tax()
    # print(ob.clac_tax('food'))
    print(ob.add_tax('food',12))            