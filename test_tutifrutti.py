# JUEGO TUTIFRUTTI
# Hay 3 niveles: Fácil, intermedio , difícil
#Categorías en el nivel fácil: Nombre, Color, Animal,País,
# Frutas o verduras, Partes de la casa.
#Categorías en el nivel intermedio: Indumemtaria, Electrodomésticos,
#Medios de transportes, Profesión, Sustantivo y Verbo.
#Categorías en el nivel difícil: Partes del cuerpo, Adjetivos,
# Deportes, Nombre de famosos, Plantas y Series o películas.
#Condiciones del juego:
#1-Si la palabra es correcta y no se repite con ninguno de los
# participantes, la palabra vale 10 puntos.
#2- Si la palabra es correcta y se repite con algunos de los
# participantes, la palabra vale 5.
#3- Si la palabra es incorrecta, vale 0 puntos.
#4- Las categorías que están vacías cuando se termina el tutifrutti,
#valen 0.
#5- Cuando un participante hace tutifrutti, no se permite escribir más.
#6- Se pueden tipear las palabras en mayúscula y minúscula, pero no
#se admite la palabra mal escrita o que le falte alguna letra.
from practica.tutifrutti import Tutifrutti


def test_retornar_10_puntos_si_la_palabra_es_un_nombre():

    tutifrutti = Tutifrutti()

    assert tutifrutti.validar_palabra("melina") == 10
    assert tutifrutti.validar_palabra("Melina") == 10


def test_retornar_0_si_la_palabra_no_es_un_nombre():
    tutifrutti = Tutifrutti()

    assert tutifrutti.validar_palabra("Vaca") == 0
    assert tutifrutti.validar_palabra("melina9") == 0
    assert tutifrutti.validar_palabra("") == 0
    assert tutifrutti.validar_palabra("   ") == 0





