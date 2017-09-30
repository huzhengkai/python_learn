class Athlete:
    def __init__(self,value=0):
        print(value)
        self.thing = value
    def how_big(self):
        return (len(self.thing))

d = Athlete("Holy Grail")
print(d.how_big())
print(type(d))

class NamedList(list):
    def __init__(self,a_name):
        list.__init__([])
        self.name=a_name
johnny = NamedList("John Paul Jones")
print(type(johnny))
print(dir(johnny))
print(johnny)
johnny.append("Bass Player")
johnny.extend(['Composer','Arranger','Musician'])
print(johnny)
