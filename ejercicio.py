#!/usr/bin/python
# -*- coding: utf-8 -*-

fichero = open("/etc/passwd", "r")

while 1:
    lineas = fichero.readline()
    user = lineas.split(":")
    print user[0], user[-1][:-1]
    if not lineas:
         break

fichero.close()
fichero = open("/etc/passwd", "r")
num_lineas = fichero.readlines()
print "Hay", len(num_lineas), "usuarios"


fichero.close()
