class Bus:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super (Bus, cls).__new__(cls)
        return cls.instance
s = Bus()
print("Объект создан" , s)
s1 = Bus()
print("Объект создан" , s1)

