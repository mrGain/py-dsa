class Mobile:
    fp = "Yes"              #Class variable

    def __init__(self) -> None:
        self.model = "Realme X"         # Instance variable

    def show_model(self):               # Instance method
        print("Model :",self.model)

    @classmethod
    def is_fp(cls):                     # Class method
        print("finger Print :",cls.fp)



realme = Mobile()
redme = Mobile()
realme.show_model()   
realme.model = "Realme 7s"
realme.show_model()  
redme.show_model() 

Mobile.is_fp()
Mobile.fp = "NO"
Mobile.is_fp()