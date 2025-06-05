from constants import *

pygame.init()


# dibujar el tablero principal del juego
def dibujar_tablero():
    for i in range(32):
        columna = i % 4
        fila = i // 4
        if fila % 2 == 0:
            pygame.draw.rect(pantalla, 'light gray', [600 - (columna * 200), fila * 100, 100, 100])
        else:
            pygame.draw.rect(pantalla, 'light gray', [700 - (columna * 200), fila * 100, 100, 100])
        pygame.draw.rect(pantalla, 'gray', [0, 800, ANCHO, 100])
        pygame.draw.rect(pantalla, 'gold', [0, 800, ANCHO, 100], 5)
        pygame.draw.rect(pantalla, 'gold', [800, 0, 200, ALTO], 5)
        texto_estado = ['Blancas: ¡Selecciona una pieza para mover!', 'Blancas: ¡Selecciona un destino!',
                        'Negras: ¡Selecciona una pieza para mover!', 'Negras: ¡Selecciona un destino!']
        pantalla.blit(fuente_grande.render(texto_estado[paso_turno], True, 'black'), (20, 820))
        for i in range(9):
            pygame.draw.line(pantalla, 'black', (0, 100 * i), (800, 100 * i), 2)
            pygame.draw.line(pantalla, 'black', (100 * i, 0), (100 * i, 800), 2)
        pantalla.blit(fuente_mediana.render('RENDIRSE', True, 'black'), (810, 830))
        if promocion_blanca or promocion_negra:
            pygame.draw.rect(pantalla, 'gray', [0, 800, ANCHO - 200, 100])
            pygame.draw.rect(pantalla, 'gold', [0, 800, ANCHO - 200, 100], 5)
            pantalla.blit(fuente_grande.render('Selecciona pieza para promocionar el peón', True, 'black'), (20, 820))


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
    global movimientos_enroque
    lista_movimientos = []
    lista_todos_movimientos = []
    movimientos_enroque = []
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
            lista_movimientos, movimientos_enroque = verificar_rey(posicion, turno)
        lista_todos_movimientos.append(lista_movimientos)
    return lista_todos_movimientos


# verificar movimientos válidos del rey
def verificar_rey(posicion, color):
    lista_movimientos = []
    movimientos_castillo = verificar_enroque()
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
    return lista_movimientos, movimientos_castillo


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
            # indentar la verificación para dos espacios adelante, solo se verifica si un espacio adelante también está abierto
            if (posicion[0], posicion[1] + 2) not in posiciones_blancas and \
                    (posicion[0], posicion[1] + 2) not in posiciones_negras and posicion[1] == 1:
                lista_movimientos.append((posicion[0], posicion[1] + 2))
        if (posicion[0] + 1, posicion[1] + 1) in posiciones_negras:
            lista_movimientos.append((posicion[0] + 1, posicion[1] + 1))
        if (posicion[0] - 1, posicion[1] + 1) in posiciones_negras:
            lista_movimientos.append((posicion[0] - 1, posicion[1] + 1))
        # agregar verificador de movimiento al paso
        if (posicion[0] + 1, posicion[1] + 1) == negras_ep:
            lista_movimientos.append((posicion[0] + 1, posicion[1] + 1))
        if (posicion[0] - 1, posicion[1] + 1) == negras_ep:
            lista_movimientos.append((posicion[0] - 1, posicion[1] + 1))
    else:
        if (posicion[0], posicion[1] - 1) not in posiciones_blancas and \
                (posicion[0], posicion[1] - 1) not in posiciones_negras and posicion[1] > 0:
            lista_movimientos.append((posicion[0], posicion[1] - 1))
            # indentar la verificación para dos espacios adelante, solo se verifica si un espacio adelante también está abierto
            if (posicion[0], posicion[1] - 2) not in posiciones_blancas and \
                    (posicion[0], posicion[1] - 2) not in posiciones_negras and posicion[1] == 6:
                lista_movimientos.append((posicion[0], posicion[1] - 2))
        if (posicion[0] + 1, posicion[1] - 1) in posiciones_blancas:
            lista_movimientos.append((posicion[0] + 1, posicion[1] - 1))
        if (posicion[0] - 1, posicion[1] - 1) in posiciones_blancas:
            lista_movimientos.append((posicion[0] - 1, posicion[1] - 1))
        # agregar verificador de movimiento al paso
        if (posicion[0] + 1, posicion[1] - 1) == blancas_ep:
            lista_movimientos.append((posicion[0] + 1, posicion[1] - 1))
        if (posicion[0] - 1, posicion[1] - 1) == blancas_ep:
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
    global jaque
    jaque = False
    if paso_turno < 2:
        if 'rey' in piezas_blancas:
            indice_rey = piezas_blancas.index('rey')
            posicion_rey = posiciones_blancas[indice_rey]
            for i in range(len(opciones_negras)):
                if posicion_rey in opciones_negras[i]:
                    jaque = True
                    if contador < 15:
                        pygame.draw.rect(pantalla, 'dark red', [posiciones_blancas[indice_rey][0] * 100 + 1,
                                                              posiciones_blancas[indice_rey][1] * 100 + 1, 100, 100], 5)
    else:
        if 'rey' in piezas_negras:
            indice_rey = piezas_negras.index('rey')
            posicion_rey = posiciones_negras[indice_rey]
            for i in range(len(opciones_blancas)):
                if posicion_rey in opciones_blancas[i]:
                    jaque = True
                    if contador < 15:
                        pygame.draw.rect(pantalla, 'dark blue', [posiciones_negras[indice_rey][0] * 100 + 1,
                                                               posiciones_negras[indice_rey][1] * 100 + 1, 100, 100], 5)


def dibujar_fin_juego():
    pygame.draw.rect(pantalla, 'black', [200, 200, 400, 70])
    pantalla.blit(fuente.render(f'¡{ganador} Ganó el juego!', True, 'white'), (210, 210))
    pantalla.blit(fuente.render(f'¡Presiona ENTER para reiniciar!', True, 'white'), (210, 240))


# verificar al paso
def verificar_ep(coords_antiguas, coords_nuevas):
    if paso_turno <= 1:
        indice = posiciones_blancas.index(coords_antiguas)
        coords_ep = (coords_nuevas[0], coords_nuevas[1] - 1)
        pieza = piezas_blancas[indice]
    else:
        indice = posiciones_negras.index(coords_antiguas)
        coords_ep = (coords_nuevas[0], coords_nuevas[1] + 1)
        pieza = piezas_negras[indice]
    if pieza == 'peon' and abs(coords_antiguas[1] - coords_nuevas[1]) > 1:
        # si la pieza era un peón y se movió dos espacios, devuelve coordenadas EP como se definió arriba
        pass
    else:
        coords_ep = (100, 100)
    return coords_ep


# agregar enroque
def verificar_enroque():
    # el rey no debe estar actualmente en jaque, ni la torre ni el rey se han movido previamente, nada entre
    # y el rey no pasa a través o termina en una casilla atacada
    movimientos_castillo = []  # almacenar cada movimiento de castillo válido como [((coords_rey), (coords_castillo))]
    indices_torre = []
    posiciones_torre = []
    indice_rey = 0
    pos_rey = (0, 0)
    if paso_turno > 1:
        for i in range(len(piezas_blancas)):
            if piezas_blancas[i] == 'torre':
                indices_torre.append(blancas_movidas[i])
                posiciones_torre.append(posiciones_blancas[i])
            if piezas_blancas[i] == 'rey':
                indice_rey = i
                pos_rey = posiciones_blancas[i]
        if not blancas_movidas[indice_rey] and False in indices_torre and not jaque:
            for i in range(len(indices_torre)):
                castillo = True
                if posiciones_torre[i][0] > pos_rey[0]:
                    casillas_vacias = [(pos_rey[0] + 1, pos_rey[1]), (pos_rey[0] + 2, pos_rey[1]),
                                        (pos_rey[0] + 3, pos_rey[1])]
                else:
                    casillas_vacias = [(pos_rey[0] - 1, pos_rey[1]), (pos_rey[0] - 2, pos_rey[1])]
                for j in range(len(casillas_vacias)):
                    if casillas_vacias[j] in posiciones_blancas or casillas_vacias[j] in posiciones_negras or \
                            casillas_vacias[j] in opciones_negras or indices_torre[i]:
                        castillo = False
                if castillo:
                    movimientos_castillo.append((casillas_vacias[1], casillas_vacias[0]))
    else:
        for i in range(len(piezas_negras)):
            if piezas_negras[i] == 'torre':
                indices_torre.append(negras_movidas[i])
                posiciones_torre.append(posiciones_negras[i])
            if piezas_negras[i] == 'rey':
                indice_rey = i
                pos_rey = posiciones_negras[i]
        if not negras_movidas[indice_rey] and False in indices_torre and not jaque:
            for i in range(len(indices_torre)):
                castillo = True
                if posiciones_torre[i][0] > pos_rey[0]:
                    casillas_vacias = [(pos_rey[0] + 1, pos_rey[1]), (pos_rey[0] + 2, pos_rey[1]),
                                        (pos_rey[0] + 3, pos_rey[1])]
                else:
                    casillas_vacias = [(pos_rey[0] - 1, pos_rey[1]), (pos_rey[0] - 2, pos_rey[1])]
                for j in range(len(casillas_vacias)):
                    if casillas_vacias[j] in posiciones_blancas or casillas_vacias[j] in posiciones_negras or \
                            casillas_vacias[j] in opciones_blancas or indices_torre[i]:
                        castillo = False
                if castillo:
                    movimientos_castillo.append((casillas_vacias[1], casillas_vacias[0]))
    return movimientos_castillo


def dibujar_enroque(movimientos):
    if paso_turno < 2:
        color = 'red'
    else:
        color = 'blue'
    for i in range(len(movimientos)):
        pygame.draw.circle(pantalla, color, (movimientos[i][0][0] * 100 + 50, movimientos[i][0][1] * 100 + 70), 8)
        pantalla.blit(fuente.render('rey', True, 'black'), (movimientos[i][0][0] * 100 + 30, movimientos[i][0][1] * 100 + 70))
        pygame.draw.circle(pantalla, color, (movimientos[i][1][0] * 100 + 50, movimientos[i][1][1] * 100 + 70), 8)
        pantalla.blit(fuente.render('torre', True, 'black'),
                    (movimientos[i][1][0] * 100 + 30, movimientos[i][1][1] * 100 + 70))
        pygame.draw.line(pantalla, color, (movimientos[i][0][0] * 100 + 50, movimientos[i][0][1] * 100 + 70),
                         (movimientos[i][1][0] * 100 + 50, movimientos[i][1][1] * 100 + 70), 2)


# agregar promoción de peón
def verificar_promocion():
    indices_peon = []
    promocion_blanca = False
    promocion_negra = False
    indice_promocion = 100
    for i in range(len(piezas_blancas)):
        if piezas_blancas[i] == 'peon':
            indices_peon.append(i)
    for i in range(len(indices_peon)):
        if posiciones_blancas[indices_peon[i]][1] == 7:
            promocion_blanca = True
            indice_promocion = indices_peon[i]
    indices_peon = []
    for i in range(len(piezas_negras)):
        if piezas_negras[i] == 'peon':
            indices_peon.append(i)
    for i in range(len(indices_peon)):
        if posiciones_negras[indices_peon[i]][1] == 0:
            promocion_negra = True
            indice_promocion = indices_peon[i]
    return promocion_blanca, promocion_negra, indice_promocion


def dibujar_promocion():
    pygame.draw.rect(pantalla, 'dark gray', [800, 0, 200, 420])
    if promocion_blanca:
        color = 'white'
        for i in range(len(promociones_blancas)):
            pieza = promociones_blancas[i]
            indice = lista_piezas.index(pieza)
            pantalla.blit(imagenes_blancas[indice], (860, 5 + 100 * i))
    elif promocion_negra:
        color = 'black'
        for i in range(len(promociones_negras)):
            pieza = promociones_negras[i]
            indice = lista_piezas.index(pieza)
            pantalla.blit(imagenes_negras[indice], (860, 5 + 100 * i))
    pygame.draw.rect(pantalla, color, [800, 0, 200, 420], 8)


def verificar_seleccion_promocion():
    pos_raton = pygame.mouse.get_pos()
    click_izquierdo = pygame.mouse.get_pressed()[0]
    pos_x = pos_raton[0] // 100
    pos_y = pos_raton[1] // 100
    if promocion_blanca and click_izquierdo and pos_x > 7 and pos_y < 4:
        piezas_blancas[indice_promocion] = promociones_blancas[pos_y]
    elif promocion_negra and click_izquierdo and pos_x > 7 and pos_y < 4:
        piezas_negras[indice_promocion] = promociones_negras[pos_y]


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
    if not juego_terminado:
        promocion_blanca, promocion_negra, indice_promocion = verificar_promocion()
        if promocion_blanca or promocion_negra:
            dibujar_promocion()
            verificar_seleccion_promocion()
    if seleccion != 100:
        movimientos_validos = verificar_movimientos_validos()
        dibujar_validos(movimientos_validos)
        if pieza_seleccionada == 'rey':
            dibujar_enroque(movimientos_enroque)
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
                    # verificar qué pieza está seleccionada, para que solo puedas dibujar movimientos de enroque si se selecciona el rey
                    pieza_seleccionada = piezas_blancas[seleccion]
                    if paso_turno == 0:
                        paso_turno = 1
                if coords_click in movimientos_validos and seleccion != 100:
                    blancas_ep = verificar_ep(posiciones_blancas[seleccion], coords_click)
                    posiciones_blancas[seleccion] = coords_click
                    blancas_movidas[seleccion] = True
                    if coords_click in posiciones_negras:
                        pieza_negra = posiciones_negras.index(coords_click)
                        piezas_capturadas_blancas.append(piezas_negras[pieza_negra])
                        if piezas_negras[pieza_negra] == 'rey':
                            ganador = 'Blancas'
                        piezas_negras.pop(pieza_negra)
                        posiciones_negras.pop(pieza_negra)
                        negras_movidas.pop(pieza_negra)
                    # agregar verificación si un peón en passant fue capturado
                    if coords_click == negras_ep:
                        pieza_negra = posiciones_negras.index((negras_ep[0], negras_ep[1] - 1))
                        piezas_capturadas_blancas.append(piezas_negras[pieza_negra])
                        piezas_negras.pop(pieza_negra)
                        posiciones_negras.pop(pieza_negra)
                        negras_movidas.pop(pieza_negra)
                    opciones_negras = verificar_opciones(piezas_negras, posiciones_negras, 'black')
                    opciones_blancas = verificar_opciones(piezas_blancas, posiciones_blancas, 'white')
                    paso_turno = 2
                    seleccion = 100
                    movimientos_validos = []
                # agregar opción de enroque
                elif seleccion != 100 and pieza_seleccionada == 'rey':
                    for q in range(len(movimientos_enroque)):
                        if coords_click == movimientos_enroque[q][0]:
                            posiciones_blancas[seleccion] = coords_click
                            blancas_movidas[seleccion] = True
                            if coords_click == (1, 0):
                                coords_torre = (0, 0)
                            else:
                                coords_torre = (7, 0)
                            indice_torre = posiciones_blancas.index(coords_torre)
                            posiciones_blancas[indice_torre] = movimientos_enroque[q][1]
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
                    # verificar qué pieza está seleccionada, para que solo puedas dibujar movimientos de enroque si se selecciona el rey
                    pieza_seleccionada = piezas_negras[seleccion]
                    if paso_turno == 2:
                        paso_turno = 3
                if coords_click in movimientos_validos and seleccion != 100:
                    negras_ep = verificar_ep(posiciones_negras[seleccion], coords_click)
                    posiciones_negras[seleccion] = coords_click
                    negras_movidas[seleccion] = True
                    if coords_click in posiciones_blancas:
                        pieza_blanca = posiciones_blancas.index(coords_click)
                        piezas_capturadas_negras.append(piezas_blancas[pieza_blanca])
                        if piezas_blancas[pieza_blanca] == 'rey':
                            ganador = 'Negras'
                        piezas_blancas.pop(pieza_blanca)
                        posiciones_blancas.pop(pieza_blanca)
                        blancas_movidas.pop(pieza_blanca)
                    if coords_click == blancas_ep:
                        pieza_blanca = posiciones_blancas.index((blancas_ep[0], blancas_ep[1] + 1))
                        piezas_capturadas_negras.append(piezas_blancas[pieza_blanca])
                        piezas_blancas.pop(pieza_blanca)
                        posiciones_blancas.pop(pieza_blanca)
                        blancas_movidas.pop(pieza_blanca)
                    opciones_negras = verificar_opciones(piezas_negras, posiciones_negras, 'black')
                    opciones_blancas = verificar_opciones(piezas_blancas, posiciones_blancas, 'white')
                    paso_turno = 0
                    seleccion = 100
                    movimientos_validos = []
                # agregar opción de enroque
                elif seleccion != 100 and pieza_seleccionada == 'rey':
                    for q in range(len(movimientos_enroque)):
                        if coords_click == movimientos_enroque[q][0]:
                            posiciones_negras[seleccion] = coords_click
                            negras_movidas[seleccion] = True
                            if coords_click == (1, 7):
                                coords_torre = (0, 7)
                            else:
                                coords_torre = (7, 7)
                            indice_torre = posiciones_negras.index(coords_torre)
                            posiciones_negras[indice_torre] = movimientos_enroque[q][1]
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
                blancas_movidas = [False, False, False, False, False, False, False, False,
                                False, False, False, False, False, False, False, False]
                piezas_negras = ['torre', 'caballo', 'alfil', 'rey', 'reina', 'alfil', 'caballo', 'torre',
                                'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon', 'peon']
                posiciones_negras = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
                                    (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]
                negras_movidas = [False, False, False, False, False, False, False, False,
                                False, False, False, False, False, False, False, False]
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