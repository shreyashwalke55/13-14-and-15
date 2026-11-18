
import gc

class Demo:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(self.name, "object destroyed")

obj1 = Demo("Object 1")
obj2 = Demo("Object 2")

print("Garbage collection enabled:", gc.isenabled())

del obj1
del obj2

print("Collecting garbage...")
collected = gc.collect()

print("Garbage collected:", collected)
