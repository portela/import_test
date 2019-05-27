# from src.a.a import *
# from src.b.b import *

from src.c import *
from src.a.a import *
from src.b.b import *
from outros.e import *
from scripts.d import *

#Uma forma é:
# from a.a import faz_a
# from b.b import faz_b

#Outra forma é:
# from a.a import *
# from b.b import *



def main():
    faz_a()
    faz_b()
    faz_c()

if __name__ == '__main__':
    main()
    faz_d()
    faz_e()