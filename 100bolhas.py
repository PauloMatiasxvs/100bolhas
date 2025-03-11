import pygame
import random
import math

# Inicializar Pygame
pygame.init()

# Configurações da tela
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("100 Bolas Quicando em Círculo")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), 
          (255, 0, 255), (0, 255, 255), (128, 0, 128)]

# Parâmetros do círculo principal
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2
RADIUS = 350

# Classe para representar cada bola
class Ball:
    def __init__(self):
        self.radius = random.randint(5, 15)
        # Posição inicial dentro do círculo
        angle = random.uniform(0, 2 * math.pi)
        distance = random.uniform(0, RADIUS - self.radius)
        self.x = CENTER_X + distance * math.cos(angle)
        self.y = CENTER_Y + distance * math.sin(angle)
        # Velocidade inicial
        self.dx = random.uniform(-3, 3)
        self.dy = random.uniform(-3, 3)
        self.color = random.choice(COLORS)

    def move(self):
        # Atualizar posição
        self.x += self.dx
        self.y += self.dy
        
        # Calcular distância do centro
        distance_from_center = math.sqrt((self.x - CENTER_X)**2 + (self.y - CENTER_Y)**2)
        
        # Verificar colisão com a borda do círculo
        if distance_from_center + self.radius > RADIUS:
            # Normalizar o vetor da posição
            nx = (self.x - CENTER_X) / distance_from_center
            ny = (self.y - CENTER_Y) / distance_from_center
            
            # Calcular componente normal da velocidade
            normal_speed = self.dx * nx + self.dy * ny
            
            # Refletir a velocidade
            self.dx = self.dx - 2 * normal_speed * nx
            self.dy = self.dy - 2 * normal_speed * ny
            
            # Ajustar posição para ficar dentro do círculo
            self.x = CENTER_X + nx * (RADIUS - self.radius)
            self.y = CENTER_Y + ny * (RADIUS - self.radius)

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

# Criar lista de 100 bolas
balls = [Ball() for _ in range(100)]

# Loop principal
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Preencher tela com branco
    screen.fill(WHITE)
    
    # Desenhar círculo limite
    pygame.draw.circle(screen, BLACK, (CENTER_X, CENTER_Y), RADIUS, 2)
    
    # Atualizar e desenhar todas as bolas
    for ball in balls:
        ball.move()
        ball.draw()
    
    # Atualizar display
    pygame.display.flip()
    
    # Controlar FPS
    clock.tick(60)

pygame.quit()