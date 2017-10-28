from math import pi
import random
import pygame
import PyParticles

(width, height) = (400, 400)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Springs')

universe = PyParticles.Environment((width, height))
universe.colour = (255,255,255)
universe.addFunctions(['move', 'bounce', 'collide', 'drag', 'accelerate'])
universe.acceleration = (pi, 0.01)
universe.mass_of_air = 0.02

universe.addParticles(mass=100, size=16, speed=2, elasticity=1, colour=(20,40,200), fixed=True, x=175, y=100)
universe.addParticles(mass=100, size=16, speed=2, elasticity=1, colour=(20,40,200), fixed=False)
universe.addParticles(mass=100, size=16, speed=2, elasticity=1, colour=(20,40,200), fixed=False)
universe.addParticles(mass=100, size=16, speed=2, elasticity=1, colour=(20,40,200), fixed=True, x=225, y=100)
universe.addParticles(mass=100, size=16, speed=2, elasticity=1, colour=(20,40,200), fixed=False)
universe.addParticles(mass=100, size=16, speed=2, elasticity=1, colour=(20,40,200), fixed=False)

universe.addSpring(0,1, length=50, strength=1)
universe.addSpring(1,2, length=50, strength=1)
universe.addSpring(3,4, length=50, strength=1)
universe.addSpring(4,5, length=50, strength=1)

selected_particle = None
paused = False
running = True
while running:
    #print pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = (True, False)[paused]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            selected_particle = universe.findParticle(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_particle = None

    if selected_particle:
        selected_particle.mouseMove(pygame.mouse.get_pos())
    if not paused:
        universe.update()
        
    screen.fill(universe.colour)
    
    for p in universe.particles:
        pygame.draw.circle(screen, p.colour, (int(p.x), int(p.y)), p.size, 0)
        
    for s in universe.springs:
        pygame.draw.aaline(screen, (0,0,0), (int(s.p1.x), int(s.p1.y)), (int(s.p2.x), int(s.p2.y)))

    pygame.display.flip()