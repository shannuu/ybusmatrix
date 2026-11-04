import pandas as pd
info=pd.read_csv("4bus.csv")
data = info.iloc[:, 1:6].values.tolist()


def admittance(k):
    rimp = k[2]
    iimp = k[3]
    susep = k[4]/2
    den = rimp**2 + iimp**2
    return round(rimp/den,1), round((-iimp/den)+susep,3)

maxv=0
for i in range(len(data)):
    if (data[i][0] > maxv or data[i][1] > maxv):
        maxv=max(data[i][0], data[i][1])

ybusmatrix=[]

maxv=int(maxv)

for i in range(maxv):
    for j in range(maxv):
        if i == j:
            summ=(0,0)
            for k in data:
                if k[0] == i+1 or k[1] == i+1:
                    summ=tuple(x+y for x,y in zip(summ, admittance(k)))
            ybusmatrix.append(f"{summ[0]}+{summ[1]}j")
        else:
            val=False
            for k in data:
                if (k[0] == i+1 and k[1] == j+1) or (k[0] == j+1 and k[1] == i+1):
                    val=tuple(-x for x in admittance(k))
            if val:
                ybusmatrix.append(f"{val[0]}+{val[1]}j")
            else:
                ybusmatrix.append(f"     0     ")

for i in range(len(ybusmatrix)):
    if (i+1)%maxv==0:
        print(ybusmatrix[i], end="\n")
    else:
        print(ybusmatrix[i], end=" ")