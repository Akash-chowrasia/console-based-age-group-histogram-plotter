import csv
def male():
    with open('mycsv.csv','a',newline='') as f:
        thewriter=csv.writer(f)
        #thewriter.writerow(['name','age','roll'])
        x=int(input('please enter number of data you want to insert'))
        print("FORMATE: NAME AGE ROLL")
        for i in range(x):
            print('enter NAME AGE ROLL for ',i+1,'th men:')
            y=[j for j in input().split()]
            l=[y[0],int(y[1]),int(y[2])]
            thewriter.writerow([l[0],l[1],l[2]])
    print('writing done')
def female():
    with open('mycsv1.csv','a',newline='') as fi:
        thewriter=csv.writer(fi)
        #thewriter.writerow(['name','age','roll'])
        y=int(input('please enter number of data you want to insert'))
        print("FORMATE: NAME AGE ROLL")
        for j in range(y):
            print('enter NAME AGE ROLL for ',j+1,'th women:')
            z=[k for k in input().split()]
            n=[z[0],int(z[1]),int(z[2])]
            thewriter.writerow([n[0],n[1],n[2]])
    print('writing done')
def writing(a):
    if a=='M':
        male()
    elif a=='F':
        female()
