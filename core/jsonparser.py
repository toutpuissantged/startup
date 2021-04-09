from json import loads

class JsonParser():
    ''' for import  config variable for json to python objects  '''
    def __init__(self,dir):
        super().__init__()
        self.dir=dir

    def parse(self): return loads(open(self.dir,'r').read())