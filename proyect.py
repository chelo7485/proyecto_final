import pygame
import numpy as np
import noise

# Función para asignar colores según el terreno
def get_color(value):
    if value < 85:              # Agua profunda
        return 0, 170, 255
    elif value < 95:           # Agua poco profunda
        return 115, 65, 35
    elif value < 120:           # Agua poco profunda
        return 0, 150, 0
    elif value < 170:           # Lugar con más vegetación
        return 0, 200, 0
    else:                       # Otros detalles
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
screen = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Generación Procedural de Bioma con ruido de Perlin')

# Crear una superficie para el terreno y renderizarlo
terreno_surface = pygame.Surface((ancho, alto))
for x in range(ancho):
    for y in range(alto):
        color = get_color(terreno[x][y])
        terreno_surface.set_at((x, y), color)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(terreno_surface, (0, 0))
    pygame.display.flip()

pygame.quit()
