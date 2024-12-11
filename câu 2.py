print("Mai Xuân Huy")
print("MSSV:235752021610062")
class HinhChunhat(object):
    
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong
    
    def area(self):
        return self.dai * self.rong

hinhChunhat = HinhChunhat(7, 4)

print(hinhChunhat.area())
