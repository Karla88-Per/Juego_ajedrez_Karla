import pygame
pygame.init()

ANCHO = 1000
ALTO = 900
pantalla = pygame.display.set_mode([ANCHO, ALTO])
pygame.display.set_caption('¡Ajedrez Pygame para Dos Jugadores!')
fuente = pygame.font.Font('freesansbold.ttf', 20)
fuente_mediana = pygame.font.Font('freesansbold.ttf', 40)
fuente_grande = pygame.font.Font('freesansbold.ttf', 50)
temporizador = pygame.time.Clock()
fps = 60



# variables del juego e imágenes
piezas_blancas = ['torre', 'caballo', 'alfil', 'rey', 'reina', 'alfil', 'caballo', 'torre',
                'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon']
posiciones_blancas = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]
piezas_negras = ['torre', 'caballo', 'alfil', 'rey', 'reina', 'alfil', 'caballo', 'torre',
                'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon']
posiciones_negras = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
piezas_capturadas_blancas = []
piezas_capturadas_negras = []

# 0 - turno blancas sin selección: 1-turno blancas con pieza seleccionada: 2- turno negras sin selección, 3 - turno negras con pieza seleccionada
paso_turno = 0
seleccion = 100
movimientos_validos = []


# cargar imágenes de piezas (reina, rey, torre, alfil, caballo, peón) x 2



reina_negra = pygame.image.load('assets/images/black queen.png')
reina_negra = pygame.transform.scale(reina_negra, (80, 80))
reina_negra_pequena = pygame.transform.scale(reina_negra, (45, 45))
rey_negro = pygame.image.load('assets/images/black king.png')
rey_negro = pygame.transform.scale(rey_negro, (80, 80))
rey_negro_pequeno = pygame.transform.scale(rey_negro, (45, 45))
torre_negra = pygame.image.load('assets/images/black rook.png')
torre_negra = pygame.transform.scale(torre_negra, (80, 80))
torre_negra_pequena = pygame.transform.scale(torre_negra, (45, 45))
alfil_negro = pygame.image.load('assets/images/black bishop.png')
alfil_negro = pygame.transform.scale(alfil_negro, (80, 80))
alfil_negro_pequeno = pygame.transform.scale(alfil_negro, (45, 45))
caballo_negro = pygame.image.load('assets/images/black knight.png')
caballo_negro = pygame.transform.scale(caballo_negro, (80, 80))
caballo_negro_pequeno = pygame.transform.scale(caballo_negro, (45, 45))
peon_negro = pygame.image.load('assets/images/black pawn.png')
peon_negro = pygame.transform.scale(peon_negro, (65, 65))
peon_negro_pequeno = pygame.transform.scale(peon_negro, (45, 45))
reina_blanca = pygame.image.load('assets/images/white queen.png')
reina_blanca = pygame.transform.scale(reina_blanca, (80, 80))
reina_blanca_pequena = pygame.transform.scale(reina_blanca, (45, 45))
rey_blanco = pygame.image.load('assets/images/white king.png')
rey_blanco = pygame.transform.scale(rey_blanco, (80, 80))
rey_blanco_pequeno = pygame.transform.scale(rey_blanco, (45, 45))
torre_blanca = pygame.image.load('assets/images/white rook.png')
torre_blanca = pygame.transform.scale(torre_blanca, (80, 80))
torre_blanca_pequena = pygame.transform.scale(torre_blanca, (45, 45))
alfil_blanco = pygame.image.load('assets/images/white bishop.png')
alfil_blanco = pygame.transform.scale(alfil_blanco, (80, 80))
alfil_blanco_pequeno = pygame.transform.scale(alfil_blanco, (45, 45))
caballo_blanco = pygame.image.load('assets/images/white knight.png')
caballo_blanco = pygame.transform.scale(caballo_blanco, (80, 80))
caballo_blanco_pequeno = pygame.transform.scale(caballo_blanco, (45, 45))
peon_blanco = pygame.image.load('assets/images/white pawn.png')
peon_blanco = pygame.transform.scale(peon_blanco, (65, 65))
peon_blanco_pequeno = pygame.transform.scale(peon_blanco, (45, 45))
imagenes_blancas = [peon_blanco, reina_blanca, rey_blanco, caballo_blanco, torre_blanca, alfil_blanco]
promociones_blancas = ['alfil', 'caballo', 'torre', 'reina']
blancas_movidas = [False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False]
imagenes_blancas_pequenas = [peon_blanco_pequeno, reina_blanca_pequena, rey_blanco_pequeno, caballo_blanco_pequeno,
                        torre_blanca_pequena, alfil_blanco_pequeno]
imagenes_negras = [peon_negro, reina_negra, rey_negro, caballo_negro, torre_negra, alfil_negro]
imagenes_negras_pequenas = [peon_negro_pequeno, reina_negra_pequena, rey_negro_pequeno, caballo_negro_pequeno,
                        torre_negra_pequena, alfil_negro_pequeno]
promociones_negras = ['alfil', 'caballo', 'torre', 'reina']
negras_movidas = [False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False]
lista_piezas = ['peon', 'reina', 'rey', 'caballo', 'torre', 'alfil']
# variables de jaque/contador de parpadeo


contador = 0
ganador = ''
juego_terminado = False
blancas_ep = (100, 100)
negras_ep = (100, 100)
promocion_blanca = False
promocion_negra = False
indice_promocion = 100
jaque = False
movimientos_enroque = []