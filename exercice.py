#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def average(a: float, b: float, c: float) -> float:
    z= (a+b+c)/3
    return z


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    v= math.radians(angle_degs + angle_mins/60 + angle_secs/3600)
    return v


def to_degrees(angle_rads: float) -> tuple:
    piw= math.pi
    d= (angle_rads * 360)/(2 * piw)
    m= d * 60
    s= m * 60
    return d, m, s


def to_celsius(temperature: float) -> float:
    Celsius= (temperature * (5/9)) - 32
    return Celsius


def to_farenheit(temperature: float) -> float:
    Farenheit= (temperature * (9/5)) + 32
    return Farenheit


def main() -> None:
    print(f"Moyenne des nombres 2, 4, 6: {average(2.1, 4.3, 6.5)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")

if __name__ == '__main__':
    main()
