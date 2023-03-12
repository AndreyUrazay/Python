import Modul 

print(Modul.max1(5, 9))


from Modul import max1
print(max1(12, 9))


from Modul import * #из Modul импортируем все функции
print(max1(12, 21))

import Modul as M #переименование функции Modul в текущей программе как M
print(M.max1(11,8))