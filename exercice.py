#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
pi= 3.14

def average(a: float, b: float, c: float) -> float:
    z= (a+b+c)/3
    return z


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    x=(angle_degs*pi)/180 t= (angle_mins*pi)/360 v= (angle_secs*pi)/
())    return x, c, v


def to_degrees(angle_rads: float) -> tuple:
    return 0.0, 0.0, 0.0


def to_celsius(temperature: float) -> float:
    return 0.0


def to_farenheit(temperature: float) -> float:
    return 0.0


def main() -> None:
    print(f"Moyenne des nombres 2, 4, 6: {average(2.1, 4.3, 6.5)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")
print(x,c,v)

if __name__ == '__main__':
    main()
