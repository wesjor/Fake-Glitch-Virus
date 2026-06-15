import pygame, random, math, array, sys, time

pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2)

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Roblox")
clock = pygame.time.Clock()

# Fake Roblox loading screen
font_logo = pygame.font.SysFont(None, 110)
font_small = pygame.font.SysFont(None, 42)

screen.fill((35, 35, 35))
title = font_logo.render("Roblox", True, (255, 255, 255))
loading = font_small.render("Starting Roblox...", True, (210, 210, 210))
screen.blit(title, (WIDTH//2 - title.get_width()//2, HEIGHT//2 - 100))
screen.blit(loading, (WIDTH//2 - loading.get_width()//2, HEIGHT//2 + 25))
pygame.display.flip()
pygame.time.wait(2500)

STAGE_SECONDS = 5
stage = 0
stage_start = time.time()
frame = 0

font_big = pygame.font.SysFont(None, 74)
font_mid = pygame.font.SysFont(None, 46)

fake_tasks = [
    "DELETING IMPORTANT FILES",
    "DELETING ALL GAMES",
    "CHANGING HOMEWORK TO 67",
    "REMOVING ROBLOX",
    "DELETING MINECRAFT WORLDS",
    "SCANNING HOMEWORK FOLDER",
    "INSTALLING 999 PING",
    "DOWNLOADING CHAOS",
    "REMOVING FPS",
    "HACKING ROBLOX ACCOUNT",
    "STEALING ROBUX",
    "SETTING CPU TEMPERATURE TO 1000 DEGREES",
    "TEXTING EVERYONE 67",
]

def make_noise(freq, duration=0.05, volume=0.15):
    sr = 44100
    samples = int(sr * duration)
    audio = array.array("h")

    for i in range(samples):
        t = i / sr
        wave = math.sin(2 * math.pi * freq * t)
        wave += 0.7 * math.sin(2 * math.pi * freq * 1.41 * t)
        wave += 0.5 * math.sin(2 * math.pi * freq * 2.73 * t)
        wave += random.uniform(-0.6, 0.6)

        value = int(max(-1, min(1, wave * volume)) * 32767)
        audio.append(value)
        audio.append(int(value * random.uniform(0.4, 1.0)))

    return pygame.mixer.Sound(buffer=audio)

sounds = [
    make_noise(f, random.uniform(0.02, 0.08), random.uniform(0.07, 0.16))
    for f in [60, 77, 93, 120, 155, 201, 260, 333, 420, 555, 666, 777, 999, 1333]
]

def invert():
    img = screen.copy()
    img.fill((255, 255, 255), special_flags=pygame.BLEND_RGB_SUB)
    screen.blit(img, (0, 0))

def flash():
    s = pygame.Surface((WIDTH, HEIGHT))
    s.set_alpha(random.randint(40, 130))
    s.fill((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
    screen.blit(s, (0, 0))

def readable_fake_warning():
    box = pygame.Surface((980, 210))
    box.set_alpha(220)
    box.fill((0, 0, 0))

    x = (WIDTH - 980) // 2
    y = (HEIGHT - 210) // 2
    screen.blit(box, (x, y))

    pygame.draw.rect(screen, (255, 0, 0), (x, y, 980, 210), 5)

    task = fake_tasks[(frame // 45) % len(fake_tasks)]
    percent = (frame * 3) % 101

    title = font_big.render(f"{task}...", True, (255, 80, 80))
    screen.blit(title, (x + 35, y + 30))

    bar_x, bar_y = x + 35, y + 115
    bar_w, bar_h = 900, 35

    pygame.draw.rect(screen, (255, 255, 255), (bar_x, bar_y, bar_w, bar_h), 3)
    pygame.draw.rect(screen, (255, 0, 0), (bar_x + 5, bar_y + 5, int((bar_w - 10) * percent / 100), bar_h - 10))

    status = font_mid.render(f"{percent}% COMPLETE   |   YOUR COOKED >:)", True, (255, 255, 255))
    screen.blit(status, (x + 35, y + 160))

running = True

while running:
    frame += 1

    if time.time() - stage_start > STAGE_SECONDS:
        stage = (stage + 1) % 20
        stage_start = time.time()
        screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    if stage == 0:
        screen.fill((0, 0, 0))
        for i in range(90):
            pygame.draw.circle(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (WIDTH//2, HEIGHT//2), i * 9 + frame % 50, 2)

    elif stage == 1:
        for _ in range(80):
            pygame.draw.rect(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)),
                             (random.randint(0,WIDTH), random.randint(0,HEIGHT), random.randint(20,300), random.randint(20,200)))

    elif stage == 2:
        screen.fill((0, 0, 0))
        for y in range(0, HEIGHT, 10):
            x = int(math.sin(y * 0.04 + frame * 0.15) * 250 + WIDTH/2)
            pygame.draw.line(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (x, y), (WIDTH-x, y), 5)

    elif stage == 3:
        tiny = pygame.transform.scale(screen, (WIDTH//20, HEIGHT//20))
        screen.blit(pygame.transform.scale(tiny, (WIDTH, HEIGHT)), (0, 0))

    elif stage == 4:
        screen.fill((0, 0, 0))
        for _ in range(2500):
            c = random.randint(0,255)
            screen.set_at((random.randint(0,WIDTH-1), random.randint(0,HEIGHT-1)), (c,c,c))

    elif stage == 5:
        screen.fill((0,0,0))
        for i in range(70):
            angle = frame*0.05 + i
            x = WIDTH//2 + math.cos(angle) * i * 9
            y = HEIGHT//2 + math.sin(angle) * i * 9
            pygame.draw.circle(screen, (255-i*3%255, i*5%255, i*9%255), (int(x), int(y)), 40, 3)

    elif stage == 6:
        if random.random() < 0.5:
            invert()
        flash()

    elif stage == 7:
        for _ in range(40):
            h = random.randint(5,60)
            y = random.randint(0, HEIGHT-h)
            strip = screen.subsurface((0,y,WIDTH,h)).copy()
            screen.blit(strip, (random.randint(-250,250), y))

    elif stage == 8:
        screen.fill((0,0,0))
        for _ in range(120):
            pygame.draw.line(screen, (random.randint(0,255),0,random.randint(0,255)),
                             (WIDTH//2, HEIGHT//2), (random.randint(0,WIDTH), random.randint(0,HEIGHT)), random.randint(1,8))

    elif stage == 9:
        for _ in range(30):
            w,h = random.randint(30,200), random.randint(30,200)
            x,y = random.randint(0,WIDTH-w), random.randint(0,HEIGHT-h)
            chunk = screen.subsurface((x,y,w,h)).copy()
            screen.blit(pygame.transform.rotate(chunk, random.randint(-90,90)), (x+random.randint(-100,100), y+random.randint(-100,100)))

    elif stage == 10:
        screen.fill((0,0,0))
        for i in range(30):
            rect = pygame.Rect(0,0, i*60 + frame%60, i*30 + frame%30)
            rect.center = (WIDTH//2, HEIGHT//2)
            pygame.draw.rect(screen, (i*8%255, i*13%255, i*21%255), rect, 4)

    elif stage == 11:
        for _ in range(200):
            pygame.draw.circle(screen, (255,255,255), (random.randint(0,WIDTH), random.randint(0,HEIGHT)), random.randint(1,4))

    elif stage == 12:
        screen.fill((255,255,255))
        for _ in range(100):
            pygame.draw.circle(screen, (0,0,0), (random.randint(0,WIDTH), random.randint(0,HEIGHT)), random.randint(10,80))

    elif stage == 13:
        for x in range(0, WIDTH, 20):
            pygame.draw.line(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), (x,0), (WIDTH-x,HEIGHT), 3)

    elif stage == 14:
        screen.fill((0,0,0))
        for i in range(300):
            x = int(WIDTH/2 + math.sin(i+frame*0.1)*i*3)
            y = int(HEIGHT/2 + math.cos(i+frame*0.1)*i*2)
            pygame.draw.rect(screen, (i%255, (i*2)%255, (i*3)%255), (x,y,8,8))

    elif stage == 15:
        flash()
        for _ in range(12):
            invert()

    elif stage == 16:
        screen.scroll(random.randint(-40,40), random.randint(-40,40))

    elif stage == 17:
        screen.fill((0,0,0))
        for _ in range(50):
            points = [(random.randint(0,WIDTH), random.randint(0,HEIGHT)) for _ in range(5)]
            pygame.draw.polygon(screen, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), points, 2)

    elif stage == 18:
        small = pygame.transform.smoothscale(screen, (WIDTH//5, HEIGHT//5))
        screen.blit(pygame.transform.smoothscale(small, (WIDTH, HEIGHT)), (0,0))
        if random.random() < 0.3:
            invert()

    elif stage == 19:
        screen.fill((random.randint(0,255), random.randint(0,255), random.randint(0,255)))
        for _ in range(20):
            flash()

    if frame % 20 < 14:
        readable_fake_warning()

    if random.random() < 0.32:
        random.choice(sounds).play()

    if random.random() < 0.05:
        for _ in range(random.randint(2, 5)):
            random.choice(sounds).play()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
