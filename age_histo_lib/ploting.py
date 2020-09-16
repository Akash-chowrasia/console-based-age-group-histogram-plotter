import matplotlib.pyplot as plt
import csv
def ploting():
    with open('mycsv.csv') as fi:
        csv_reader=csv.reader(fi,delimiter=',')
        l=0
        m=[]
        for row in csv_reader:
            if l==0:
                l+=1
            else:
                m.append(f'{row[1]}')
    with open('mycsv1.csv') as fl:
        csv_reader1=csv.reader(fl,delimiter=',')
        k=0
        p=[]
        for i in csv_reader1:
            if k==0:
                k+=1
            else:
                p.append(f'{i[1]}')
    m.sort()
    p.sort()
    plt.xlabel('AGE')
    plt.ylabel('NUMBER OF PEOPLE')
    plt.title('AGE ANALYSIS')
    plt.hist([m,p],bins=12,rwidth=0.95,color=['red','black'],label=['men','women'])
    plt.legend()
    plt.show()

