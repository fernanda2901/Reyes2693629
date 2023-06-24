from Book import *
from User import *
from Account import *


obj2 = Book ("La llorona" , "luisa" , 102866 , "10/25/2014" , "diego")
obj1 = User ("luisa" , 102866,obj2._obj_titulo)
obj3 = Account ("luisa" , 102866,)


print(obj3.LibroReservado("luisa","La llorona"))
print(obj3.LibroReservado("luisa","La guerra de los cielos" ))
print(obj3.LibroDevuelto("luisa","La llorona"))
print(obj3.LibroDevuelto("luisa","La guerra de los cielos"))
print(obj3.LibroPerdido("luisa"," La llorona"))
print(obj3.LibroPerdido("luisa", "La Guerra de los cielos"))
print(obj3.LibroPerdido("luisa", "La guerra de los cielos"))
print(obj3.LibroPerdido("luisa", "La guerra de los cielos"))
print(obj3.calculate_fine())

obj1.CheckAccount("luisa" , obj3._obj_titulo["luisa"])

obj2.AgregarBook()

# print(obj1.get_book_info ("La guerra de los cielos", obj2._informacion))
obj1.get_book_info ("La guerra de los cielos", obj2._informacion)