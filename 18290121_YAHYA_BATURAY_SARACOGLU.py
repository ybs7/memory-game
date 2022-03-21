import random
import pygame

pygame.init()

c1 = (53,64,79)
c2 = (228,95,86)
c3 = (141,182,205)
c4 =(28,134,238)
c5 = (255, 105, 97)
c6 = (217, 239, 252)

dispw = 500
disph = 500

screen = pygame.display.set_mode((dispw,disph))
pygame.display.set_caption('Memory Game')

memory = pygame.image.load('memory.png')
pygame.display.set_icon(memory)

sound = pygame.mixer.Sound('blop.mp3')
winsound = pygame.mixer.Sound('win.mp3')
failsound = pygame.mixer.Sound('fail.mp3')

font = pygame.font.SysFont(str(None), 35)
clock = pygame.time.Clock()

def text_objects(text,color):
    textSurface = font.render(text,True,color)
    return textSurface, textSurface.get_rect()

def message(msg,color,x):
    textSurf,textrect = text_objects(msg,color)
    textrect.center = (dispw/2),(x)
    screen.blit(textSurf,textrect)

def intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == 113:
                    pygame.quit()
                    quit()
                if event.key == 99:
                    run()
                    pygame.quit()
                    quit()

        screen.fill(c1)
        message("MEMORY GAME",c6,70)
        message("Press c to play",c6,200)
        message("Press q to quit",c6,250)
        pygame.display.update()
        clock.tick(15)

def fail(sc):
    fail = True
    box = pygame.Rect(disph/2-95, dispw/2-30, 180, 40)

    while fail:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if box.collidepoint(event.pos):
                    fail = False
                    run()

        screen.fill(c1)
        message("FAILED !", c5,110)
        message(f"SCORE : {sc} ",c4,180)
        message(" Play Again  ",(242,242,242),241)
        pygame.draw.rect(screen,c3,box,4)
        pygame.display.update()
        clock.tick(15)

def run():
    randomx = random.randint(1, 450)
    randomy = random.randint(1, 450)
    def message_to_screen(msg, color):
        screen_text = font.render(msg, True, color)
        screen.blit(screen_text, [randomx, randomy])

    input_box = pygame.Rect(disph / 2 - 90, dispw / 2 - 20, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ''
    screen.fill(c1)
    count = 0
    count2 = 0
    maxx = 5
    ar1 = []
    FPS = 60
    score = 0

    running = True
    while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill(c1)
            while count != maxx:
                var = random.randint(1,9)
                ar1.append(var)
                message_to_screen(str(var),c6)
                sound.play()
                pygame.display.flip()
                pygame.time.delay(1000)
                screen.fill(c1)
                pygame.display.flip()
                randomx = random.randint(1, 450)
                randomy = random.randint(1, 450)
                count+=1
            if count == maxx:
                    done  = False
                    while not done:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                done = True
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if input_box.collidepoint(event.pos):
                                    active = not active
                                else:
                                    active = False
                                color = color_active if active else color_inactive
                            if event.type == pygame.QUIT:
                                running = False
                            if event.type == pygame.KEYDOWN:
                                if active:
                                    if event.key == pygame.K_RETURN:
                                        y = 0
                                        for x in range(maxx):
                                            if str(ar1[x]) == str(text[y]):
                                                count2+=1
                                                y+=1
                                        text = ''
                                        if count2 == maxx:
                                            winsound.play()
                                            count = 0
                                            count2 = 0
                                            ar1 = []
                                            score += maxx
                                            maxx+=1
                                            done = True
                                            continue
                                        else :
                                            failsound.play()
                                            count = 0
                                            count2 = 0
                                            ar1 = []
                                            done = True
                                            screen.fill(c2)
                                            running=False
                                            fail(score)

                                    elif event.key == pygame.K_BACKSPACE:
                                        text = text[:-1]
                                    else:
                                        text += event.unicode

                        screen.fill((53, 64, 79))
                        message("write the numbers seen without spaces !",c6,120)
                        txt_surface = font.render(text, True, color)
                        width = max(200, txt_surface.get_width() + 10)
                        input_box.w = width
                        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
                        pygame.draw.rect(screen, color, input_box, 2)
                        pygame.display.flip()
                        clock.tick(30)

            clock.tick(FPS)
        
intro()
