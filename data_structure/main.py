print([1, 3.5, 3+1j, True, None, 'randomString', [1, 2, 3]])
print(type([1, 3.5, 3+1j, True, None, 'randomString', [1, 2, 3]]))
# -6        -5      -4  etc

my_list = [1, 3.5, 3+1j, True, None, 'randomString', [1, 2, 3]]
print(my_list)

print(my_list[5])

print(len(my_list))

empty_lis = []


#adaugare elemente in listm

empty_lis.append(24)

print(my_list)

empty_lis.append(45)

print(my_list)

#adaugam noua val a primului element din lista
my_list[0] = 100

list_1 = [1, 2, 3]
list_2 = list_1

#afisam true si True
print(list_1 is list_2, list_1==list_2 )

#se afiseaza list 2 tot 1,2,3,4 pentru ca list_2 = list_1
list_1.append(4)
print(list_1, list_2)

#concatenare [1,2,32,3,4]
list_1 = [1, 2, 3]
list_2 = [2, 3, 4]
print(list_1 + list_2)

#slice list_name[start:stop:step]
#liste pe baza altor liste
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_1[5:])
print(list_1[5:7]) #doa list[5] si 6 ; [-3:] ultimele 3 elemente
#daca punem asa [::] vom obtine fix lista noastra [0:-1:1]
print(list_1[1:8:2]) #se incepe cu poz 1, pana la 8 cu steps de 2
#[-1::-1] lista de la cap la coada ==[::-1]


#TUPLURI - immutable- nu se pot modifica - nu se pot adauga sau sterge
my_tuple = (1, 2, 3, 3+5j, True)
print(my_tuple, type(my_tuple), my_tuple[1:3])

#my_tuple = 100 nu se poate, ca nu se poate modifica lista

#lista din tuplu si tuplu din lista
my_list = []
my_list = list()
print(my_list, type(my_list))


my_tuple1 = (1,2,3,4)
my_list = list(my_tuple1)
print(my_list, type(my_list))

my_list.append(60)

#fac tuplu dintr-o lista
my_tuple = tuple(my_list)
print('my tuple is', my_tuple, type(my_tuple))









