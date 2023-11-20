import numpy as np
import matplotlib.pyplot as plt
import noise

width = 300
height = 300

scale = 100.0

terrain = np.zeros((width, height))

for i in range(width):
    for j in range(height):
        terrain[i][j] = noise.pnoise2(i / scale, 
                                      j / scale, 
                                      octaves=6, 
                                      persistence=0.5, 
                                      lacunarity=2.0, 
                                      repeatx=1024, 
                                      repeaty=1024, 
                                      base=0)

terrain = (terrain - np.min(terrain)) / (np.max(terrain) - np.min(terrain))

plt.imshow(terrain, cmap='terrain', interpolation='nearest')
plt.colorbar(label='Altura')
plt.title('Generación Procedural de Bioma con ruido de Perlin (Usando noise)')
plt.show()