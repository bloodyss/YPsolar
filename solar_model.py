# coding: utf-8
# license: GPLv3

from solar_objects import *
G = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        Star.calculate_cosmic_body_force(body, space_objects, G)
        Satelite.calculate_cosmic_body_force(body, space_objects, G)
    for body in space_objects:
        if isinstance(body, Satelite):
            Satelite.move_planet(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
