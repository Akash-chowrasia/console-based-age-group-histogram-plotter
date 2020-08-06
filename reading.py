import csv
import pandas as pd
def male():
    with open('mycsv.csv') as fi:
        csv_reader=csv.reader(fi,delimiter=',')
        l=0
        m=[]
        for row in csv_reader:
            if l==0:
                l+=1
            else:
                t=[f'{row[0]}',f'{row[1]}',f'{row[2]}']
                m.append(t)
        temp=pd.DataFrame(m,columns=['NAME','AGE','ROLL'])
        print(temp)
def female():
    with open('mycsv1.csv') as fl:
        csv_reader1=csv.reader(fl,delimiter=',')
        k=0
        p=[]
        for i in csv_reader1:
            if k==0:
                k+=1
            else:
                t=[f'{i[0]}',f'{i[1]}',f'{i[2]}']
                p.append(t)
        temp=pd.DataFrame(p,columns=['NAME','AGE','ROLL'])
        print(temp)
def reading(a):
    if a=='M':
        male()
    elif a=='F':
        female()
