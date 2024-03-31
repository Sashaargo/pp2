import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    mode = 'eraser'
                elif event.key == pygame.K_c:
                    mode = 'circle'
                elif event.key == pygame.K_t:
                    mode = 'rectangle'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    if mode != 'rectangle' and mode != 'circle':
                        radius = min(200, radius + 1)
                    else:
                        x, y = event.pos
                elif event.button == 3: # right click shrinks radius
                    if mode != 'rectangle' and mode != 'circle':
                        radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        # draw all points
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, mode):
    if mode == 'eraser':
        color = (0, 0, 0)  # Eraser color (black)
    elif mode == 'circle':
        pygame.draw.circle(screen, (255, 255, 255), start, width)
    elif mode == 'rectangle':
        pygame.draw.rect(screen, (255, 255, 255), (start[0], start[1], end[0] - start[0], end[1] - start[1]), width)
    else:
        c1 = max(0, min(255, 2 * index - 256))
        c2 = max(0, min(255, 2 * index))
        
        if mode == 'blue':
            color = (c1, c1, c2)
        elif mode == 'red':
            color = (c2, c1, c1)
        elif mode == 'green':
            color = (c1, c2, c1)
    
        dx = start[0] - end[0]
        dy = start[1] - end[1]
        iterations = max(abs(dx), abs(dy))
        
        for i in range(iterations):
            progress = 1.0 * i / iterations
            aprogress = 1 - progress
            x = int(aprogress * start[0] + progress * end[0])
            y = int(aprogress * start[1] + progress * end[1])
            pygame.draw.circle(screen, color, (x, y), width)

main() 
