import pygame

# Initialisation de Pygame
pygame.init()

# Définition de quelques couleurs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Paramètres de la fenêtre
screen_width = 600
screen_height = 400

# Initialisation de la fenêtre
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Créer un curseur en Pygame")

# Position initiale du curseur
cursor_x = 300
cursor_y = 200
cursor_radius = 10

# Position de la ligne sur laquelle le curseur peut être déplacé
line_y = 200

# Le curseur est en mode "non déplacé" par défaut
is_cursor_dragging = False

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if cursor_x - cursor_radius <= mouse_x <= cursor_x + cursor_radius and line_y - cursor_radius <= mouse_y <= line_y + cursor_radius:
                    is_cursor_dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                is_cursor_dragging = False

    if is_cursor_dragging:
        mouse_x, _ = pygame.mouse.get_pos()
        cursor_x = max(cursor_radius, min(screen_width - cursor_radius, mouse_x))

    # Remplissage de l'écran avec une couleur de fond
    screen.fill(WHITE)

    # Dessin de la ligne
    pygame.draw.line(screen, BLACK, (0, line_y), (screen_width, line_y), 2)

    # Dessin du curseur
    pygame.draw.circle(screen, BLACK, (cursor_x, line_y), cursor_radius)

    # Mise à jour de l'écran
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
