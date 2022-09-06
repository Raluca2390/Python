print("HellowWorld!")
print(1, 2, 1.2, 5+3j)

#type() -care este tipul de data al unei valorile
print(type(1), type(3+5j))

#id() - zona de memorie alocata
print(id(1), id(3+5j))


# int(), float(), complex() -alte functii predefinite
print(int(2), int(4.5), complex(4.7))

print((5 == 5) is True)

print((5 == 5) is False)

print((5 == 5) is None)

#escape la caractere \
print('That\'s my dog ')

print(r'\t is a special character')

my_age = 20
my_name = "John"
my_string = 'My age is 20.'
my_string1 = 'My age is' + str(my_age) + '.'
print('my_string', my_string)
#formatare se tine cont de ordinea lor intre ()
# Mod 1: my_string2 = 'My name is %s age is %d.' % (my_name, my_age)
# Mod2: my_string2 = 'My name is {0} age is {1}.'.format(name=my_name, age=my_age)   se indexeaza {}sau placeholderele pot purta nume {name} si {age}

my_string2 = f'My Name is {my_name} and i am {my_age} years old'
print(my_string2)

########

price = 23.50
print(f'Total price = {price:.2f} RON')
#nr zecimale ke putem formata cu :.2f adica 2 zecimale, daca avem :.5f are 5 zecimale

#scriere de stringuri pe mai multe linii
print('Row 1\nRow2 \n Row3') #se muta cursorul pe uramt linie
print("""Row1
Row4
Row2""")

#orice string este o secventa de caractere si fiecare are o pozitie cu indexare de la 0
my_secv = 'jhfgsdjhfgdsjhfgdsjhfgdj'
print(len(my_secv))
print('gdj' in my_secv)   #sau not int
#



