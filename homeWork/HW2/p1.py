# ● Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor
# care reprezintă numere întregi sau reale.
# ○ your_function(1, 5, -3, ‘abc’, [12, 56, ‘cad’]) va returna 3 (1 + 5 - 3).  []- lista, tuplu () immutable, dictionar {}, set () immutable
# ○ your_function() va returna 0.
# ○ your_function(2, 4, ‘abc’, param_1=2) va returna 6 (2 + 4).
#
# #TUPLU - immutable
# my_tuple = (1, 2, 3, 3+5j, True)
# #index       0   1   2    3    4
# #index desc -5  -4  -3   -2    -1
#
# print(my_tuple)
# print(my_tuple[3])
# print(my_tuple[-2])
#
# print(my_tuple[2])
# print(my_tuple[-3])
# print('hello world')
#
# #inlocuire valoare in tuplu - immutable
# my_tuple[3] = 'Raluca'
# print(my_tuple)
#
# #LISTA
# my_list = [1, 2, 3, 3+5j, True]
# print(my_list)
#
# #inlocuire valoare in lista - mutable
# my_list[3] = 'Raluca'
# print(my_list)

#Slice
my_list = [1, 2, 3, 3+5j, True, 8, 9, 7]
# my_slice_list = my_list[1:4]
#  #                       n: n-1
# print(my_slice_list)
# print(my_list[1:-1])
# print(my_list[-4:-1])
#print(my_list[100]) - index out of range
#print(my_list[1:100]) - merge!!!printeaza toti idexii dintre primul si al doilea parametruu

# print(my_list[0:10:3])
# print(my_list[1:4:2])

#Dictionare
my_dict = {
  # key  :  Value
    "key_1": 1,
    "key_2": "Raluca",
    "key_3": True

}

#print(my_dict.get("key_2"))
#print(my_dict["key_2"])
#Printeaza cheila
# for i in my_dict:
#     print(i)

#printeaza key/value
# for i in my_dict:
#     print(i,my_dict[i])

# for k,v in my_dict.items():
#     print(k,v)
#
# print(my_dict.items())


# def my_function(#parametrii - la definire):
#     print("inside my f")
#
#     my_function(#argument - la chemare)

# def my_function(param1):
#     param1 = 'Raluca'
#     return param1
#
#
# print(my_function("catalin"))

# def my_function(*param1, param_1):
#     suma = 0
#     for i in param1:
#         if (type(i) is int) or (type(i) is float):
#             suma = suma + i
#     return suma
#
# print(my_function(2, 4, "abc", param_1=22))
#

def my_function(*param1):
    suma = 0
    for i in param1:
        if isinstance(i, (int,float)):
            suma = suma + i
    return suma

print(my_function(2.1, 4, "abc"))


