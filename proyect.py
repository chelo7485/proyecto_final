import pygame
import numpy as np
import noise

class Organismo:
    def __init__(self, posicion, vida, comida, velocidad):
        self.posicion = posicion
        self.vida = vida
        self.comida = comida
        self.velocidad = velocidad

class Animal(Organismo):
    def __init__(self, posicion, vida, comida, velocidad, especie, dieta):
        super().__init__(posicion, vida, comida, velocidad)
        self.especie = especie
        self.dieta = dieta

    def hunt(self):
        pass  # Método para cazar

class Planta(Organismo):
    def __init__(self, posicion, vida, comida):
        super().__init__(posicion, vida, comida)

    def photosynthesis(self):
        pass  # Método para realizar la fotosíntesis

    def reproduce_by_seeds(self):
        pass  # Método para reproducción por semillas


# Función para asignar colores según el terreno
def get_color(color):
    if color < 85:              #Agua poco profunda
        return 0, 170, 255
    elif color < 95:           # Barro
        return 115, 65, 35
    elif color < 120:           # Lugar con más vegetación
        return 0, 150, 0
    elif color < 170:           # Lugar con menos vegetación
        return 0, 200, 0
    else:                       # Zona alta y rocosa
        return 140, 140, 120

# Generación del terreno
ancho = 1000
alto = 750
escala = 200

terreno = np.zeros((ancho, alto))

for i in range(ancho):
    for j in range(alto):
        terreno[i][j] = noise.pnoise2(i / escala,
                                      j / escala,
                                      octaves=6,
                                      persistence=0.5,
                                      lacunarity=2.0,
                                      repeatx=1024,
                                      repeaty=1024,
                                      base=0)
        terreno[i][j] = int((terreno[i][j] + 1) * 127.5)

terreno = np.array(terreno, dtype=np.uint8)

# Inicializar Pygame
pygame.init()

# Configurar la pantalla de Pygame
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Generación Procedural de Bioma con ruido de Perlin')

# Crear una superficie para el terreno y renderizarlo
terreno_surface = pygame.Surface((ancho, alto))
for x in range(ancho):
    for y in range(alto):
        color = get_color(terreno[x][y])
        terreno_surface.set_at((x, y), color)
xd = 0
a =  pygame.image.load('img\pasto.jpg')
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pantalla.blit(terreno_surface, (0, 0))

    pantalla.blit(a,(xd,0))
    pygame.display.flip()

pygame.quit()
