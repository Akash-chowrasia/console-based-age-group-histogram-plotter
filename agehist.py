import sys
sys.path.append('/age_histo_lib/')
import age_histo_lib
from age_histo_lib.reading import *
from age_histo_lib.writing import *
from age_histo_lib.ploting import *
from sys import argv
try:
    if len(argv) < 2 and len(argv) >3:
        raise ValueError()
    if argv[1].upper() =='PLOT':
        ploting()
        exit()
    elif argv[1].upper() =='READ':
        reading(argv[2].upper())
        exit()
    elif argv[1].upper() =='WRITE':
        writing(argv[2].upper())
        exit()
    else:
        pass
except:
    pass
    #print("Error: 'arguments are not passed properly....?'")
