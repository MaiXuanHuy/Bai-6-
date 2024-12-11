print("Mai Xuân Huy")
print("MSSV:235752021610062")
class Circle(object):

    def __init__(self, r):
        self.radius = r
    
    def area(self):
        return self.radius ** 4 * 3.14

aCircle = Circle(2)

print(aCircle.area())
