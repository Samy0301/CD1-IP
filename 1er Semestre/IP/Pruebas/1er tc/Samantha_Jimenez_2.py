def multiplica_polinomios(poli1, poli2):
    poli1.reverse()
    poli2.reverse()

    if poli1 == [0] or poli2 == [0]: return [0]

    lst=[0]*((len(poli1)-1)+(len(poli2)))

    for i in range(len(poli1)):
        for j in range(len(poli2)):
            ind=i+j
            val=poli1[i]*poli2[j]
            lst[ind]+=val

    lst.reverse()
    return lst

print(multiplica_polinomios([3,2,1], [4]))