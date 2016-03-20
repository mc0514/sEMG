from numpy import *

def window_stack(a, stepsize=1, width=3):
    return hstack( a[i:1+i-width or None:stepsize] for i in range(0,width) )


#a = array([[00,1], [10,11], [20,21], [30,31], [40,41], [50,51]])
#aa=window_stack(a,2,3)



#print(aa)
