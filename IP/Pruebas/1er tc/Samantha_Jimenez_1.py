def mezcla(lista1, lista2):
    
    if valido(lista1) and valido(lista2):
        i=j=0
        result = []
        while i<len(lista1) and j<len(lista2):
            if lista1[i]<lista2[j]:
                if lista1[i] not in result:
                    result.append(lista1[i])
                i+=1
            else:
                if lista2[j] not in result: 
                    result.append(lista2[j])
                j+=1
        
        while i<len(lista1):
            if lista1[i] not in result:
                result.append(lista1[i])
            i+=1

        while j<len(lista2):
            if lista2[j] not in result:
                result.append(lista2[j])
            j+=1

        return (True, result)
    else: 
        return (False, [])


def valido(lst):
    for i in range(len(lst)-1):
        if lst[i+1]<lst[i]: return False
    return True
print(mezcla([1,2,3], [2,3,4]))