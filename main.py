
# parte uno, configurar variables, imágenes y bucle del juego

import pygame

pygame.init()
ancho = 1000
alto = 900
pantalla = pygame.display.set_mode([ancho, alto])
pygame.display.set_caption('Ajedrez')
fuente = pygame.font.Font('freesansbold.ttf', 20)
fuente_intermedia = pygame.font.Font('freesansbold.ttf', 30)
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


# cargar imágenes de piezas (reina, rey, torre, alfil, caballo, peón)


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
imagenes_blancas_pequenas = [peon_blanco_pequeno, reina_blanca_pequena, rey_blanco_pequeno, caballo_blanco_pequeno,
                        torre_blanca_pequena, alfil_blanco_pequeno]
imagenes_negras = [peon_negro, reina_negra, rey_negro, caballo_negro, torre_negra, alfil_negro]
imagenes_negras_pequenas = [peon_negro_pequeno, reina_negra_pequena, rey_negro_pequeno, caballo_negro_pequeno,
                        torre_negra_pequena, alfil_negro_pequeno]
lista_piezas = ['peon', 'reina', 'rey', 'caballo', 'torre', 'alfil']


# variables de jaque/contador de parpadeo
contador = 0
ganador = ''
juego_terminado = False


# dibujar el tablero principal del juego
def dibujar_tablero():
    for i in range(32):
        columna = i % 4
        fila = i // 4
        if fila % 2 == 0:
            pygame.draw.rect(pantalla, 'light gray', [600 - (columna * 200), fila * 100, 100, 100])
        else:
            pygame.draw.rect(pantalla, 'light gray', [700 - (columna * 200), fila * 100, 100, 100])
        pygame.draw.rect(pantalla, 'gray', [0, 800, ancho, 100])
        pygame.draw.rect(pantalla, 'gold', [0, 800, ancho, 100], 5)
        pygame.draw.rect(pantalla, 'gold', [800, 0, 200, alto], 5)
        texto_estado = ['Blancas: ¡Selecciona una ficha!', 'Blancas: ¡Selecciona un destino!',
                        'Negras: ¡Selecciona una ficha!', 'Negras: ¡Selecciona un destino!']
        pantalla.blit(fuente_mediana.render(texto_estado[paso_turno], True, 'black'), (20, 820))
        for i in range(9):
            pygame.draw.line(pantalla, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(pantalla, 'black', (100 * i, 0), (100 * i, 800), 2)
        pantalla.blit(fuente_intermedia.render('RENDIRSE', True, 'black'), (810, 830))


# dibujar piezas en el tablero
def dibujar_piezas():
    for i in range(len(piezas_blancas)):
        indice = lista_piezas.index(piezas_blancas[i])
        if piezas_blancas[i] == 'peon':
            pantalla.blit(peon_blanco, (posiciones_blancas[i][0] * 100 + 22, posiciones_blancas[i][1] * 100 + 30))
        else:
            pantalla.blit(imagenes_blancas[indice], (posiciones_blancas[i][0] * 100 + 10, posiciones_blancas[i][1] * 100 + 10))
        if paso_turno < 2:
            if seleccion == i:
                pygame.draw.rect(pantalla, 'red', [posiciones_blancas[i][0] * 100 + 1, posiciones_blancas[i][1] * 100 + 1,
                                                100, 100], 2)

    for i in range(len(piezas_negras)):
        indice = lista_piezas.index(piezas_negras[i])
        if piezas_negras[i] == 'peon':
            pantalla.blit(peon_negro, (posiciones_negras[i][0] * 100 + 22, posiciones_negras[i][1] * 100 + 30))
        else:
            pantalla.blit(imagenes_negras[indice], (posiciones_negras[i][0] * 100 + 10, posiciones_negras[i][1] * 100 + 10))
        if paso_turno >= 2:
            if seleccion == i:
                pygame.draw.rect(pantalla, 'blue', [posiciones_negras[i][0] * 100 + 1, posiciones_negras[i][1] * 100 + 1,
                                                    100, 100], 2)


# función para verificar todas las opciones válidas de las piezas en el tablero
def verificar_opciones(piezas, posiciones, turno):
    lista_movimientos = []
    lista_todos_movimientos = []
    for i in range((len(piezas))):
        posicion = posiciones[i]
        pieza = piezas[i]
        if pieza == 'peon':
            lista_movimientos = verificar_peon(posicion, turno)
        elif pieza == 'torre':
            lista_movimientos = verificar_torre(posicion, turno)
        elif pieza == 'caballo':
            lista_movimientos = verificar_caballo(posicion, turno)
        elif pieza == 'alfil':
            lista_movimientos = verificar_alfil(posicion, turno)
        elif pieza == 'reina':
            lista_movimientos = verificar_reina(posicion, turno)
        elif pieza == 'rey':
            lista_movimientos = verificar_rey(posicion, turno)
        lista_todos_movimientos.append(lista_movimientos)
    return lista_todos_movimientos


# verificar movimientos válidos del rey
def verificar_rey(posicion, color):
    lista_movimientos = []
    if color == 'white':
        lista_enemigos = posiciones_negras
        lista_amigos = posiciones_blancas
    else:
        lista_amigos = posiciones_negras
        lista_enemigos = posiciones_blancas
    # 8 casillas para verificar para los reyes, pueden ir una casilla en cualquier dirección
    objetivos = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        objetivo = (posicion[0] + objetivos[i][0], posicion[1] + objetivos[i][1])
        if objetivo not in lista_amigos and 0 <= objetivo[0] <= 7 and 0 <= objetivo[1] <= 7:
            lista_movimientos.append(objetivo)
    return lista_movimientos


# verificar movimientos válidos de reina
def verificar_reina(posicion, color):
    lista_movimientos = verificar_alfil(posicion, color)
    segunda_lista = verificar_torre(posicion, color)
    for i in range(len(segunda_lista)):
        lista_movimientos.append(segunda_lista[i])
    return lista_movimientos


# verificar movimientos de alfil
def verificar_alfil(posicion, color):
    lista_movimientos = []
    if color == 'white':
        lista_enemigos = posiciones_negras
        lista_amigos = posiciones_blancas
    else:
        lista_amigos = posiciones_negras
        lista_enemigos = posiciones_blancas
    for i in range(4):  # arriba-derecha, arriba-izquierda, abajo-derecha, abajo-izquierda
        camino = True
        cadena = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while camino:
            if (posicion[0] + (cadena * x), posicion[1] + (cadena * y)) not in lista_amigos and \
                    0 <= posicion[0] + (cadena * x) <= 7 and 0 <= posicion[1] + (cadena * y) <= 7:
                lista_movimientos.append((posicion[0] + (cadena * x), posicion[1] + (cadena * y)))
                if (posicion[0] + (cadena * x), posicion[1] + (cadena * y)) in lista_enemigos:
                    camino = False
                cadena += 1
            else:
                camino = False
    return lista_movimientos


# verificar movimientos de torre
def verificar_torre(posicion, color):
    lista_movimientos = []
    if color == 'white':
        lista_enemigos = posiciones_negras
        lista_amigos = posiciones_blancas
    else:
        lista_amigos = posiciones_negras
        lista_enemigos = posiciones_blancas
    for i in range(4):  # abajo, arriba, derecha, izquierda
        camino = True
        cadena = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while camino:
            if (posicion[0] + (cadena * x), posicion[1] + (cadena * y)) not in lista_amigos and \
                    0 <= posicion[0] + (cadena * x) <= 7 and 0 <= posicion[1] + (cadena * y) <= 7:
                lista_movimientos.append((posicion[0] + (cadena * x), posicion[1] + (cadena * y)))
                if (posicion[0] + (cadena * x), posicion[1] + (cadena * y)) in lista_enemigos:
                    camino = False
                cadena += 1
            else:
                camino = False
    return lista_movimientos


# verificar movimientos válidos de peón
def verificar_peon(posicion, color):
    lista_movimientos = []
    if color == 'white':
        if (posicion[0], posicion[1] + 1) not in posiciones_blancas and \
                (posicion[0], posicion[1] + 1) not in posiciones_negras and posicion[1] < 7:
            lista_movimientos.append((posicion[0], posicion[1] + 1))
        if (posicion[0], posicion[1] + 2) not in posiciones_blancas and \
                (posicion[0], posicion[1] + 2) not in posiciones_negras and posicion[1] == 1:
            lista_movimientos.append((posicion[0], posicion[1] + 2))
        if (posicion[0] + 1, posicion[1] + 1) in posiciones_negras:
            lista_movimientos.append((posicion[0] + 1, posicion[1] + 1))
        if (posicion[0] - 1, posicion[1] + 1) in posiciones_negras:
            lista_movimientos.append((posicion[0] - 1, posicion[1] + 1))
    else:
        if (posicion[0], posicion[1] - 1) not in posiciones_blancas and \
                (posicion[0], posicion[1] - 1) not in posiciones_negras and posicion[1] > 0:
            lista_movimientos.append((posicion[0], posicion[1] - 1))
        if (posicion[0], posicion[1] - 2) not in posiciones_blancas and \
                (posicion[0], posicion[1] - 2) not in posiciones_negras and posicion[1] == 6:
            lista_movimientos.append((posicion[0], posicion[1] - 2))
        if (posicion[0] + 1, posicion[1] - 1) in posiciones_blancas:
            lista_movimientos.append((posicion[0] + 1, posicion[1] - 1))
        if (posicion[0] - 1, posicion[1] - 1) in posiciones_blancas:
            lista_movimientos.append((posicion[0] - 1, posicion[1] - 1))
    return lista_movimientos


# verificar movimientos válidos de caballo
def verificar_caballo(posicion, color):
    lista_movimientos = []
    if color == 'white':
        lista_enemigos = posiciones_negras
        lista_amigos = posiciones_blancas
    else:
        lista_amigos = posiciones_negras
        lista_enemigos = posiciones_blancas
    # 8 casillas para verificar para caballos, pueden ir dos casillas en una dirección y una en otra
    objetivos = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        objetivo = (posicion[0] + objetivos[i][0], posicion[1] + objetivos[i][1])
        if objetivo not in lista_amigos and 0 <= objetivo[0] <= 7 and 0 <= objetivo[1] <= 7:
            lista_movimientos.append(objetivo)
    return lista_movimientos


# verificar movimientos válidos para la pieza seleccionada
def verificar_movimientos_validos():
    if paso_turno < 2:
        lista_opciones = opciones_blancas
    else:
        lista_opciones = opciones_negras
    opciones_validas = lista_opciones[seleccion]
    return opciones_validas


# dibujar movimientos válidos en pantalla
def dibujar_validos(movimientos):
    if paso_turno < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(movimientos)):
        pygame.draw.circle(pantalla, color, (movimientos[i][0] * 100 + 50, movimientos[i][1] * 100 + 50), 5)


# dibujar piezas capturadas al lado de la pantalla
def dibujar_capturadas():
    for i in range(len(piezas_capturadas_blancas)):
        pieza_capturada = piezas_capturadas_blancas[i]
        indice = lista_piezas.index(pieza_capturada)
        pantalla.blit(imagenes_negras_pequenas[indice], (825, 5 + 50 * i))
    for i in range(len(piezas_capturadas_negras)):
        pieza_capturada = piezas_capturadas_negras[i]
        indice = lista_piezas.index(pieza_capturada)
        pantalla.blit(imagenes_blancas_pequenas[indice], (925, 5 + 50 * i))


# dibujar un cuadrado parpadeante alrededor del rey si está en jaque
def dibujar_jaque():
    if paso_turno < 2:
        if 'rey' in piezas_blancas:
            indice_rey = piezas_blancas.index('rey')
            posicion_rey = posiciones_blancas[indice_rey]
            for i in range(len(opciones_negras)):
                if posicion_rey in opciones_negras[i]:
                    if contador < 15:
                        pygame.draw.rect(pantalla, 'dark red', [posiciones_blancas[indice_rey][0] * 100 + 1,
                                                              posiciones_blancas[indice_rey][1] * 100 + 1, 100, 100], 5)
    else:
        if 'rey' in piezas_negras:
            indice_rey = piezas_negras.index('rey')
            posicion_rey = posiciones_negras[indice_rey]
            for i in range(len(opciones_blancas)):
                if posicion_rey in opciones_blancas[i]:
                    if contador < 15:
                        pygame.draw.rect(pantalla, 'dark blue', [posiciones_negras[indice_rey][0] * 100 + 1,
                                                               posiciones_negras[indice_rey][1] * 100 + 1, 100, 100], 5)


def dibujar_fin_juego():
    pygame.draw.rect(pantalla, 'black', [200, 200, 400, 70])
    pantalla.blit(fuente.render(f'¡{ganador} Ganó el juego!', True, 'white'), (210, 210))
    pantalla.blit(fuente.render(f'¡Presiona ENTER para reiniciar!', True, 'white'), (210, 240))


# bucle principal del juego
opciones_negras = verificar_opciones(piezas_negras, posiciones_negras, 'black')
opciones_blancas = verificar_opciones(piezas_blancas, posiciones_blancas, 'white')
ejecutar = True
while ejecutar:
    temporizador.tick(fps)
    if contador < 30:
        contador += 1
    else:
        contador = 0
    pantalla.fill('dark gray')
    dibujar_tablero()
    dibujar_piezas()
    dibujar_capturadas()
    dibujar_jaque()
    if seleccion != 100:
        movimientos_validos = verificar_movimientos_validos()
        dibujar_validos(movimientos_validos)
    # manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutar = False
        if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1 and not juego_terminado:
            coord_x = evento.pos[0] // 100
            coord_y = evento.pos[1] // 100
            coords_click = (coord_x, coord_y)
            if paso_turno <= 1:
                if coords_click == (8, 8) or coords_click == (9, 8):
                    ganador = 'Negras'
                if coords_click in posiciones_blancas:
                    seleccion = posiciones_blancas.index(coords_click)
                    if paso_turno == 0:
                        paso_turno = 1
                if coords_click in movimientos_validos and seleccion != 100:
                    posiciones_blancas[seleccion] = coords_click
                    if coords_click in posiciones_negras:
                        pieza_negra = posiciones_negras.index(coords_click)
                        piezas_capturadas_blancas.append(piezas_negras[pieza_negra])
                        if piezas_negras[pieza_negra] == 'rey':
                            ganador = 'Blancas'
                        piezas_negras.pop(pieza_negra)
                        posiciones_negras.pop(pieza_negra)
                    opciones_negras = verificar_opciones(piezas_negras, posiciones_negras, 'black')
                    opciones_blancas = verificar_opciones(piezas_blancas, posiciones_blancas, 'white')
                    paso_turno = 2
                    seleccion = 100
                    movimientos_validos = []
            if paso_turno > 1:
                if coords_click == (8, 8) or coords_click == (9, 8):
                    ganador = 'Blancas'
                if coords_click in posiciones_negras:
                    seleccion = posiciones_negras.index(coords_click)
                    if paso_turno == 2:
                        paso_turno = 3
                if coords_click in movimientos_validos and seleccion != 100:
                    posiciones_negras[seleccion] = coords_click
                    if coords_click in posiciones_blancas:
                        pieza_blanca = posiciones_blancas.index(coords_click)
                        piezas_capturadas_negras.append(piezas_blancas[pieza_blanca])
                        if piezas_blancas[pieza_blanca] == 'rey':
                            ganador = 'Negras'
                        piezas_blancas.pop(pieza_blanca)
                        posiciones_blancas.pop(pieza_blanca)
                    opciones_negras = verificar_opciones(piezas_negras, posiciones_negras, 'black')
                    opciones_blancas = verificar_opciones(piezas_blancas, posiciones_blancas, 'white')
                    paso_turno = 0
                    seleccion = 100
                    movimientos_validos = []
        if evento.type == pygame.KEYDOWN and juego_terminado:
            if evento.key == pygame.K_RETURN:
                juego_terminado = False
                ganador = ''
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
                paso_turno = 0
                seleccion = 100
                movimientos_validos = []
                opciones_negras = verificar_opciones(piezas_negras, posiciones_negras, 'black')
                opciones_blancas = verificar_opciones(piezas_blancas, posiciones_blancas, 'white')

    if ganador != '':
        juego_terminado = True
        dibujar_fin_juego()

    pygame.display.flip()
pygame.quit()