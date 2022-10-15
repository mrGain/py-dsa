
class Item:
    discount = 20
    def __init__(self):
        self.dis = {}
    
    def set(self, key:str, value:int):
        self.dis[key]=value
        

    def get(self):
        return self.dis 
      

if __name__ == "__main__":
    item1 = Item()
    item1.set("name",2345)
    item1.set("price",100)
    print(item1.get())

    item2 = Item()
    item2.set("name",23)
    print(item2.get())

    print("-----------")
    print(Item.__dict__) # All the attribute for class level
    print()
    print(item1.__dict__) # All the attribute for instance level

