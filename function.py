class Function:
    def __init__(self,f):
        self.f = f
    def __call__(self,x):
        return eval(self.f)
