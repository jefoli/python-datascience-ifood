import math

lista = ["maça", "apple", "Lemon"]

for indice, list in enumerate(lista):
    print(f"{indice} : {list}")


def sub_rotina1 (x, y):
    valor = x + y
    return valor

var1 = 6
var2 = 3

receive = int(sub_rotina1(var1, var2))

print(f"Recebi os valores da sub_rotina 1: {receive}")


def sub_rotina2(valor_sub1):
    elevar_ao_quadrado = math.sqrt(valor_sub1)
    print(f"passagem de param da sub1 + elevado ao quadrado na sub_2 {elevar_ao_quadrado}")
    return(elevar_ao_quadrado)



v_sub2 = sub_rotina2(receive)

def sub_rotina3 (sub_1, sub_2):
    calc_valores = sub_1 - sub_2
    print(f"pegue v_sub1: {type(receive)} [{receive}] e va_sub2: {type(v_sub2)}[{v_sub2}] e subtrai:  {str(calc_valores)} {type(calc_valores)}")


recebi1 = sub_rotina3(receive, v_sub2)
