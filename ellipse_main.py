## Tzu-Yang (Josh) Yueh
import ellipse as elps
import random as rd

def intro():
    '''
    About:
        Print the intro of this program 
    '''
    print('This is a program using Monte Carlo simulation')
    print('to approach the overlapping area of two ellipses')
    print('-'*50 +'\n')

def simulate_many(n,e1,e2):
    '''
    About:
        repeat simulation and record the results
    Args:
        n (int): how many times for simulation
        e1 (ellipse): an ellipse obejct
        e2 (ellipse): an ellipse obejct
    return:
        float: overlapping area based on two given ellipses
    '''
    ## get horizontal_range, vertical_range, frame_area
    h ,v, area = frame(e1,e2)

    ## init the success count and total count
    success = 0
    total = 0

    ## n times simulation
    for i in range(n):
        ## recording the success and total count
        success += simulate_once(e1,e2,h,v)
        total += 1
        
    ## get probability
    p = success/total
    return p*area

def simulate_once(e1,e2,h,v):
    '''
    About:
        To test whether a random point (within the range) fall on the overlap area
    Args:
        e1 (ellipse): an ellipse obejct
        e2 (ellipse): an ellipse obejct
        h (tuple): the horizontal range
        v (tuple): the vertical range
    return:
        boolean: whether a random point fall on the overlap area
    '''
    ## get random point
    p = elps.point(rd.uniform(*h), rd.uniform(*v))
    
    ## get boolean of whether p in each ellipses
    return True if e1.is_inellipse(p) and e2.is_inellipse(p) else False

def frame(e1,e2):
    '''
    About:
        To construct a frame based on two given ellipses
    Args:
        e1 (ellipse): an ellipse obejct
        e2 (ellipse): an ellipse obejct
    return:
        tuple: the horizontal range
        tuple: the vertical range
        float: the frame area
    '''
    ## get centers
    c1, c2= e1.cpoint, e2.cpoint
    ## get boundaries
    left = min(c1.x-e1.a,c2.x-e2.a)
    right = min(c1.x+e1.a,c2.x+e2.a)
    lower = min(c1.y-e1.a,c2.y-e2.a)
    upper = min(c1.y+e1.a,c2.y+e2.a)
    
    return (left, right), (lower, upper), (right-left)*(upper-lower)

def summary(area, e1, e2):
    '''
    About:
        Print the summary of simulation result
    '''
    print('Ellipses:')
    print('\t{}\t{}\t{}'.format('F1', 'F2', 'Semi-Major'))
    print('e1:   ',e1)
    print('e2:   ',e2)
    print('-'*40)
    print('Overlap area: {}'.format(area))
    

def main():
    '''
    About:
        This is the main function.
    '''
    ## get intro
    intro()
    
    ## get the first ellipses
    params1 = {'f1':elps.point(1,0),
               'f2':elps.point(2,0),
               'a':2}
    e1 = elps.ellipse(**params1)
    ## get the second ellipses
    params2 = {'f1':elps.point(0,0),
               'f2':elps.point(4,0),
               'a':5}
    e2 = elps.ellipse(**params2)

    ## call simulate_many
    overlap = simulate_many(1000000, e1, e2)
    
    ## print the simulation result
    summary(overlap, e1, e2)

    
if __name__ == '__main__':
    main()
