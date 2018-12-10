## Tzu-Yang (Josh) Yueh
import math
class point():
    '''
    About:
        This is a class represent a point. 
      
    Args: 
        x (float): The poistion on x-axis. 
        y (float): The poistion on y-axis. 
    '''

    def __init__(self, x, y):
        '''
        About:
            The constructor of point object.
        
        Args: 
            x (float): The poistion on x-axis. 
            y (float): The poistion on y-axis.
        '''
        ## Exception: if x is not valid
        if type(x) is int or type(x) is float: 
            self.x = x
        else:
            raise Exception("Warning: '{}' is not a number.".format(x))
        ## Exception: if y is not valid
        if type(y) is int or type(y) is float: 
            self.y = y
        else:
            raise Exception("Warning: '{}' is not a number.".format(y))

        
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

class ellipse():
    '''
    About:
        This is a class represent a ellipse. 
      
    Args: 
        f1 (object): An point object 
        f2 (object): An point object
        a (float): The length of semi-major axis
    '''
    def __init__(self, f1=None, f2=None, a=None):
        '''
        About:
            The constructor of ellipse object.
        
        Args: 
            f1 (object): An point object 
            f2 (object): An point object
            a (float): The length of semi-major axis
        '''
        ## init f1
        if f1==None:
            self.f1 = point(0,0)
        elif type(f1).__name__ != 'point':
            raise Exception('Warning: f1 type is not "point", Given {}'.format(type(f1).__name__))
        else:
            self.f1 = f1
        ## init f2 
        if f2==None:
            self.f2 = point(0,0)
        elif type(f2).__name__ != 'point':
            raise Exception('Warning: f2 type is not "point", Given {}'.format(type(f2).__name__))
        else:
            self.f2 = f2
            
        ## init major axis (a)  
        if a==None: # no input
            self.a = 1.0
        elif not(type(a) is float or type(a) is int): # wrong type
            raise Exception('Warning: The semi-major (a) param should be numeric,\
                                given {}'.format(type(a)))
        elif a<0: # negative value
            raise Exception('Warning: The semi-major (a) param should be greater\
                            than 0, given {}'.format(a))
        elif a*2<=distance(self.f1, self.f2):
            raise Exception('Warning: Two times semi-major (a) param should be greater\
                            than the distance bewteew F1 and F2, given {}'.format(a))
        else:
            self.a = float(a)
             
        ## init minor axis and center point
        self.b = math.sqrt(self.a**2-(distance(self.f1, self.f2)/2)**2)
        self.cpoint = point((self.f1.x+self.f2.x)/2,(self.f1.y+self.f2.y)/2)
        
    def set_params(self, f1=None, f2=None, a=None):
        '''
        About:
            set the ellipse parameters (e.g. F1/F2/Major_Axis)

        Args:
            f1 (object): An point object 
            f2 (object): An point object
            a (float): The length of semi-major axis
        ''' 
        if f1!=None:
            if type(f1).__name__ == 'point':
                self.f1 = f1
            else:
                raise Exception('Warning: f1 type is not "point", Given {}'.format(type(f1).__name__))

        if f2!=None:
            if type(f2).__name__ == 'point':
                self.f2 = f2
            else:
                raise Exception('Warning: f1 type is not "point", Given {}'.format(type(f2).__name__))
        if a!=None:
            if not(type(a) is float or type(a) is int):
                raise Exception('Warning: The semi-major (a) param should be numeric,\
                                given {}'.format(type(a)))
            elif a<0:
                raise Exception('Warning: The semi-major (a) param should be greater\
                            than 0, given {}'.format(a))
            elif a*2<=distance(self.f1, self.f2):
                raise Exception('Warning: Two times semi-major should be greater\
                            than the distance bewteew F1 and F2, given {}'.format(a))
            else:
                self.a = a

        ## adjust minor_axis and center point
        self.b = math.sqrt(self.a**2-(distance(self.f1, self.f2)/2)**2)
        self.cpoint = point((self.f1.x+self.f2.x)/2,(self.f1.y+self.f2.y)/2)

        
    def area(self):
        '''
        return:
            float: The area of this ellipse
        '''
        return math.pi*self.a*self.b
    
    def circumf(self):
        '''
        return:
            float: The circumference of this ellipse
        '''
        return 2*math.pi*self.b + 4*(self.a-self.b)
        
    def is_inellipse(self, p):
        '''
        About:
            test whether a point is in this ellipse
        args:
            p (point): a point object
        return:
            A Boolean value 
        '''
        return distance(p,self.f1) + distance(p,self.f2) < self.a*2

    def __str__(self):
        '''
        About:
            print(F1, F2, Major_Axis)
        '''
        return '{}\t{}\t{}'.format(self.f1, self.f2, self.a)

    
def distance(p1,p2):
    '''
    About:
        Euclidean distance
    Args:
        p1 (point): a point object
        p2 (point): a poont object
    return:
        float: Distance between two points
    '''
    x2 = (p1.x-p2.x)**2
    y2 = (p1.y-p2.y)**2
    return math.sqrt(x2+y2)

        

