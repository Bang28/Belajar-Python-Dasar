import pygame

# init (inisialiasi)
pygame.init() #untuk menjalankan game enggine nya
# variable running game
isRun = True

# membuat display surface object
window_lebar = 500
window_panjang = 500
window = pygame.display.set_mode((window_lebar,window_panjang))

# object game
# koordinat/posisi
x = 250
y = 250

# ukuran
panjang = 20
lebar = 20

# kecepatan gerak
speed = 5

while isRun: #agar si aplikasi tetap berjalan menggunakan while true
    pygame.time.delay(5) #biar ga wuz wuz banget
    '''user input, database input'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRun = False

    '''ambil smua keyboard press'''
    keys = pygame.key.get_pressed()
    
    '''ambil ke kiri'''
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    
    '''ambil kanan'''
    if keys[pygame.K_RIGHT] and x < window_lebar - lebar:
        x += speed

    '''ambil atas'''
    if keys[pygame.K_UP] and y > 0:
        y -= speed
    
    '''ambil bawah'''
    if keys[pygame.K_DOWN] and y < window_panjang - panjang:
        y += speed
    
    '''update asset'''
    window.fill((255,255,255))
    pygame.draw.rect(window,(255,0,0),(x,y,lebar,panjang))

    '''render display'''
    pygame.display.update()


pygame.quit()

