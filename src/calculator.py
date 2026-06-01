# Ce fichier contient des violations PEP8 intentionnelles pour l'exercice
import os
import sys

def add(a,b):  # E231 : espace manquant après la virgule
    return a+b  # E225 : espaces manquants autour de l'opérateur

def subtract( a, b ):  # E201/E202 : espaces parasites
    result=a-b  # E225
    return result

class calculator:  # N801 : nom de classe doit être en PascalCase
    def multiply(self,x,y):  # E231
        return x*y  # E225