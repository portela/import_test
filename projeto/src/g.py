from src.b.b import *

print('Inside g.py')

def faz_g():
    print('chamando b')
    faz_b()
    print('Fazendo G - faz_g()')
    return 'G'