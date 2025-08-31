lista = [1,2,3,4,5,6,7,8]
k=14
def suma_encontrada(lista,k):
    A=lista [:]
    B=lista[:]
    for i in range(len(A)):
        for j in range(len(B)):
          if i !=j:
            if A[i]+B[j]==k:
              print(f"{A[i]}+{B[j]}={k}")
              return True
    return False

if suma_encontrada(lista,k):
  print("Si")
else:
  print("Ño")