# This function is here while I learn how to fix it
class Function:
    def __init__(self,f):
        self.f = f
    def __call__(self,x):
        return eval(self.f)

def fixedpoint(f,x0,nit,error):
    #f(x)=x, iteration
    xk=f(x0)
    while(nit!=0 and  abs( f(xk)-xk ) > error):
        xk = f(xk)
        nit-=1
    return f(xk)

def newtonsMethod(f,x0,nit,error):
    xk = x0 - f(x0)/f.derivate(x0)
    while(nit!=0 and abs(f(xk)) > error ):
        xk = xk - f(xk)/f.derivate(xk)
        nit-=1
    return f(xk)


def secantMethod(f,x0,x1,nit,error):

    pass



f = Function("x**4")
print( f(2) )

print ( fixedpoint(f,-0.99,30, 0) )
