def formarLista(num):
    if num == 0:
        return[]
    elif ((num % 10) % 2) == 0:
        return [num%10] + formarLista(num//10)
    else: return formarLista(num//10)
