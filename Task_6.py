# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
import math


x1 = float(input("ВВедите координаты 1 точки x = "))
y1 = float(input("ВВедите координаты 1 точки y = "))
x2 = float(input("ВВедите координаты 2 точки x = "))
y2 = float(input("ВВедите координаты 2 точки y = "))
z = math.pow((math.pow((y2-y1),2) + math.pow((x2-x1),2) ),0.5 )
print(z)
