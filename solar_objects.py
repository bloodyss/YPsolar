# coding: utf-8
# license: GPLv3


class CosmicBody:
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """
    
    type : str
    """Признак объекта звезды"""
    R : int
    """Радиус звезды"""
    color : str
    """Цвет звезды"""
    m : float
    """Масса звезды"""
    x : float
    """Координата по оси **x**"""
    y : float
    """Координата по оси **y**"""

    Fx : float
    """Сила по оси **x**"""
    Fy : float
    """Сила по оси **y**"""
    image = None
    """Изображение звезды"""


    def parse_cosmic_body_parameters(self, line):
        """Считывает данные о звезде из строки.
        
        Входная строка должна иметь следующий формат:
        Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
        
        Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
        Пример строки:
        Star 50 yellow 1.0 100.0 200.0 0.0 0.0
        
        Параметры:
        **line** — строка с описанием звезды.
        **star** — объект звезды.
        """

        line = line.strip()
        if line and not line.startswith('#'):
            parts = line.split()
            
            self.R = int(parts[1])
            self.color = parts[2]
            self.m = float(parts[3])
            self.x = float(parts[4])
            self.y = float(parts[5])
        
    def calculate_cosmic_body_force(self, space_objects, G):
        import math
        """Вычисляет силу, действующую на тело.

        Параметры:

        **body** — тело, для которого нужно вычислить дейстующую силу.
        **space_objects** — список объектов, которые воздействуют на тело.
        """

        self.Fx = self.Fy = 0
        for obj in space_objects:
            if self == obj:
                continue  # тело не действует гравитационной силой на само себя!
            r = ((self.x - obj.x)**2 + (self.y - obj.y)**2)**0.5
            F = G*((self.m*obj.m)/r**2)  # FIXME: нужно вывести формулу...
            alpha = math.atan2(obj.y - self.y, obj.x - self.x)
            self.Fx += F * math.cos(alpha)
            self.Fy += F * math.sin(alpha)


class Star(CosmicBody):
    type = 'star'

    def parse_star_parameters(self, line):
        super().parse_cosmic_body_parameters(line)
    
class Satelite(CosmicBody):
    type = 'planet'

    Vx : float
    """Скорость по оси **x**"""
    Vy : float
    """Скорость по оси **y**"""


    def parse_planet_parameters(self, line):
        super().parse_cosmic_body_parameters(line)

        line = line.strip()
        if line and not line.startswith('#'):
            parts = line.split()
            
            self.Vx = float(parts[6])
            self.Vy = float(parts[7])

    
    def move_planet(self, dt):
        """Перемещает тело в соответствии с действующей на него силой.

        Параметры:

        **body** — тело, которое нужно переместить.
        """

        ax = self.Fx/self.m
        self.Vx += ax*dt # учтена v0 при +=
        self.x += self.Vx*dt + (ax*dt**2)/2 # учтено x0 при +=
        # FIXME: not done recalculation of y coordinate!
        ay = self.Fy/self.m
        self.Vy += ay*dt
        self.y += self.Vy*dt + (ay*dt**2)/2 