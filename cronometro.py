import pygame
import time as tm
import threading

pygame.init()


SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cronómetro")

font = pygame.font.Font(None, 36)

class Cronometro:
    def __init__(self):
        self.HORA = 0
        self.MINUTO = 0
        self.SEGUNDO = 0
        self.running = False
        self.thread = None

    def start_cronometro(self):
        self.running = True
        self.thread = threading.Thread(target=self._cronometro_loop)
        self.thread.start()

    def stop_cronometro(self):
        self.running = False
        self.thread.join()

    def _cronometro_loop(self):
        while self.running:
            tm.sleep(1)
            self.SEGUNDO += 1
            if self.SEGUNDO == 60:
                self.MINUTO += 1
                self.SEGUNDO = 0
                if self.MINUTO == 60:
                    self.HORA += 1
                    self.MINUTO = 0

    def get_time(self):
        return f"Horas {self.HORA}, Minutos {self.MINUTO}, Segundos {self.SEGUNDO}"

cronometro = Cronometro()

def main():
    clock = pygame.time.Clock()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if cronometro.running:
                        cronometro.stop_cronometro()
                    else:
                        cronometro.start_cronometro()

        screen.fill(BLACK)
        
        text = font.render(cronometro.get_time(), True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
