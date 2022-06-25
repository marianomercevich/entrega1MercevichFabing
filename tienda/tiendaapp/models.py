from django.db import models

class casco(models.Model):

    marca = models.CharField("Marca", max_length=30)
    tipo = models.CharField("Tipo", max_length=30)
    TALLES= (
    (1, "XS 55 CM"),
    (2, "S 58 CM"),
    (3, "M 60 CM"),
    (4, "L 62 CM" ),
    (5, "XL 63 CM"),
    (6, "XXL 65 CM"),
    )
    talle = models.PositiveSmallIntegerField("Talle", choices=TALLES)
    precio = models.FloatField ("Precio $")

class campera(models.Model):

    marca = models.CharField("Marca", max_length=30)
    tipo = models.CharField("Tipo", max_length=30)
    TALLES= (
    (1, "XS"),
    (2, "S"),
    (3, "M"),
    (4, "L" ),
    (5, "XL"),
    (6, "XXL"),
    )
    talle = models.PositiveSmallIntegerField("Talle", choices=TALLES)
    precio = models.FloatField ("Precio $")
class bolso(models.Model):

    marca = models.CharField("Marca", max_length=30)
    tipo = models.CharField("Tipo", max_length=30)
    TALLES= (
    (1, "15 L"),
    (2, "20 L"),
    (3, "30 L"),
    (4, "45 L" ),
    )
    talle = models.PositiveSmallIntegerField("Talle", choices=TALLES)
    precio = models.FloatField ("Precio $")
class guante(models.Model):

    marca = models.CharField("Marca", max_length=30)
    TIPO= (
    (1, "invierno"),
    (2, "verano"),
    (3, "4 estaciones"),
    )
    tipo = models.PositiveSmallIntegerField("Tipo", choices=TIPO)
    TALLES= (
    (1, "XS"),
    (2, "S"),
    (3, "M"),
    (4, "L" ),
    (5, "XL"),
    (6, "XXL"),
    )
    talle = models.PositiveSmallIntegerField("Talle", choices=TALLES)
    precio = models.FloatField ("Precio $")
class pantalon(models.Model):

    marca = models.CharField("Marca", max_length=30)
    TIPO= (
    (1, "invierno"),
    (2, "verano"),
    (3, "4 estaciones"),
    )
    tipo = models.PositiveSmallIntegerField("Tipo", choices=TIPO)
    TALLES= (
    (1, "38"),
    (2, "40"),
    (3, "42"),
    (4, "44"),
    (5, "46"),
    (6, "48"),
    (7, "50"),
    (8, "52"),
    (9, "54"),
    (10, "56"),
    )
    talle = models.PositiveSmallIntegerField("Talle", choices=TALLES)
    precio = models.FloatField ("Precio $")
