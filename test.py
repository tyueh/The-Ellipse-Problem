## Tzu-Yang (Josh) Yueh
from ellipse import *
from ellipse_main import *
import sys

## A4_P3 simulate_many function
#################################
print('Function: {}'.format(simulate_many.__name__))
print('-'*30)
print('Docstring:')
print(simulate_many.__doc__)
#################################
print('-'*30)
print('Testing the overlap area of two identical circle (r=1)')
print('Input:')
e1 = ellipse(f1=point(0,0), f2=point(0,0), a=1)
e2 = ellipse(f1=point(0,0), f2=point(0,0), a=1)
print('    e1:  F1{}  F2{}  A:{}'.format(e1.f1,e1.f2,e1.a))
print('    e2:  F1{}  F2{}  A:{}'.format(e2.f1,e2.f2,e2.a))
print('Output:')
print('    Overlap area: {}'.format(simulate_many(1000000,e1,e2)))
print('Check (calling area method):')
print('    e1 area: {}'.format(e1.area()))
#################################
print('-'*30)
print('Testing the overlap area of two separate ellipses')
print('input:')
e1 = ellipse(f1=point(0,0), f2=point(1,1), a=1)
e2 = ellipse(f1=point(15,15), f2=point(16,16), a=1.5)
print('    e1:  F1{}  F2{}  A:{}'.format(e1.f1,e1.f2,e1.a))
print('    e2:  F1{}  F2{}  A:{}'.format(e2.f1,e2.f2,e2.a))
print('output:')
print('    overlap area: {}'.format(simulate_many(1000000,e1,e2)))
#################################
print('-'*30)
print('Testing the overlap area of one ellipse in another one')
print('input:')
e1 = ellipse(f1=point(0,0), f2=point(10,0), a=10)
e2 = ellipse(f1=point(0,0), f2=point(100,0), a=100)
print('    e1:  F1{}  F2{}  A:{}'.format(e1.f1,e1.f2,e1.a))
print('    e2:  F1{}  F2{}  A:{}'.format(e2.f1,e2.f2,e2.a))
print('output:')
print('    overlap area: {}'.format(simulate_many(1000000,e1,e2)))
print('Check (calling area method):')
print('    e1 area: {}'.format(e1.area()))
#################################
print('-'*30)
print('Testing the overlap area of two overlap ellipses')
print('input:')
e1 = ellipse(f1=point(1,0), f2=point(2,0), a=2)
e2 = ellipse(f1=point(0,0), f2=point(4,0), a=5)
print('    e1:  F1{}  F2{}  A:{}'.format(e1.f1,e1.f2,e1.a))
print('    e2:  F1{}  F2{}  A:{}'.format(e2.f1,e2.f2,e2.a))
print('output:')
print('    overlap area: {}'.format(simulate_many(1000000,e1,e2)))
print('-'*30)
print('#'*80+'\n\n\n')
