import pygame, time
from pygame.constants import *
import random
import sys 
from pygame.locals import * 
import numpy as np
from dict_test import *
import saveslot1, saveslot2, saveslot3, saveslot4, saveslot5
from importlib import reload

# Inisiasi pygame
pygame.init()

# Tambahan
dt = time.time()
last_time = time.time()
mainClock = pygame.time.Clock()

# Membuat layarnya, (panjang,tinggi)
infoObject = pygame.display.Info() 
screen_width, screen_height = infoObject.current_w, infoObject.current_h
screen = pygame.display.set_mode((screen_width, screen_height))

height_ratio = screen_height/1080
width_ratio = screen_width/1920

# Variabel
player_VMAX_Y = 12
player_VMIN_Y = -16
player_V_Y = 0
gravity = 0.3
player_jump_V_Y = -15
player_jump = False

pillar1X = -1000
pillar1X2 = -1000
pillarV = 12

# Title and Icon
pygame.display.set_caption("./gambar/Game Tubes 8")
icon = pygame.image.load("./gambar/keqing logo.png")
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load("./gambar/paimon fly 128px.png")
playerImg = pygame.transform.scale(playerImg, (128 * width_ratio, 149 * height_ratio))
playerX = 1920*width_ratio/4
playerY = 0

# Image assets
backgroundImg = pygame.image.load("./gambar/background baru.jpg")
backgroundImg = pygame.transform.scale(backgroundImg, (1920 * width_ratio, 1080 * height_ratio))
pillarImg = pygame.image.load("./gambar/zhongli pillar.png")
pillarImg = pygame.transform.scale(pillarImg, (196 * width_ratio, 740 * height_ratio))
pillarImg2 = pygame.image.load("./gambar/zhongli pillar flipped.png")
pillarImg2 = pygame.transform.scale(pillarImg2, (196 * width_ratio, 740 * height_ratio))
bannerImg = pygame.image.load("./gambar/banner.png")
bannerImg = pygame.transform.scale(bannerImg, (1920 * width_ratio, 1080 * height_ratio))
banner160Img = pygame.image.load("./gambar/banner160x.png")
banner160Img = pygame.transform.scale(banner160Img, (1920 * width_ratio, 1080 * height_ratio))
banner1600Img = pygame.image.load("./gambar/banner1600x.png")
banner1600Img = pygame.transform.scale(banner1600Img, (1920 * width_ratio, 1080 * height_ratio))
gachabgImg = pygame.image.load('./gambar/gacha_bg.jpg')
gachabgImg = pygame.transform.scale(gachabgImg, (1920 * width_ratio, 1080 * height_ratio))
gachabgImg_rect = gachabgImg.get_rect()
primogemDisplayGameImg = pygame.image.load('./gambar/display primo game.png')
primogemDisplayGameImg = pygame.transform.scale(primogemDisplayGameImg, (402 * width_ratio, 91 * height_ratio))
primogemDisplayGameWhiteImg = pygame.image.load('./gambar/display primo game white.png')
primogemDisplayGameWhiteImg = pygame.transform.scale(primogemDisplayGameWhiteImg, (270 * width_ratio, 79 * height_ratio))

# Tambahan background menu
MenuTopImg = pygame.image.load("./gambar/menu/MenuTop.png") # Tombol2
MenuTopImg = pygame.transform.scale(MenuTopImg, (707 * width_ratio, 892 * height_ratio)) 
Menu1Img = pygame.image.load("./gambar/menu/Menu1.png") # Langit 
Menu1Img = pygame.transform.scale(Menu1Img, (3840 * width_ratio, 1080 * height_ratio)) 
Menu2Img = pygame.image.load("./gambar/menu/Menu2.png") # pegunungan
Menu2Img = pygame.transform.scale(Menu2Img, (1920 * width_ratio, 1043 * height_ratio)) 
Menu4Img = pygame.image.load("./gambar/menu/Menu4.png") # gelap
Menu4Img = pygame.transform.scale(Menu4Img, (1920 * width_ratio, 1080 * height_ratio)) 
loginImg = pygame.image.load("./gambar/menu/login.png")
loginImg = pygame.transform.scale(loginImg, (1920 * width_ratio, 1080 * height_ratio))

Ads0Img = pygame.image.load("./gambar/menu/Ads0.png")
Ads0Img = pygame.transform.scale(Ads0Img, (907 * width_ratio, 468 * height_ratio)) 
Ads1Img = pygame.image.load("./gambar/menu/Ads1.png")
Ads1Img = pygame.transform.scale(Ads1Img, (907 * width_ratio, 468 * height_ratio)) 
Ads2Img = pygame.image.load("./gambar/menu/Ads2.png")
Ads2Img = pygame.transform.scale(Ads2Img, (907 * width_ratio, 468 * height_ratio)) 
Ads3Img = pygame.image.load("./gambar/menu/Ads3.png")
Ads3Img = pygame.transform.scale(Ads3Img, (907 * width_ratio, 468 * height_ratio)) 
Ads4Img = pygame.image.load("./gambar/menu/Ads4.png")
Ads4Img = pygame.transform.scale(Ads4Img, (907 * width_ratio, 468 * height_ratio)) 

menuButton1Img = pygame.image.load('./gambar/menu/MenuButton1.png')
menuButton1Img = pygame.transform.scale(menuButton1Img, (707 * width_ratio, 892 * height_ratio)) 
menuButton2Img = pygame.image.load('./gambar/menu/MenuButton2.png')
menuButton2Img = pygame.transform.scale(menuButton2Img, (707 * width_ratio, 892 * height_ratio)) 
menuButton3Img = pygame.image.load('./gambar/menu/MenuButton3.png')
menuButton3Img = pygame.transform.scale(menuButton3Img, (707 * width_ratio, 892 * height_ratio)) 

MenuPaimonImg = pygame.image.load("./gambar/menu/MenuPaimon.png")
MenuPaimonImg = pygame.transform.scale(MenuPaimonImg, (398 * width_ratio, 690 * height_ratio)) 

inventBoardImg = pygame.image.load("./gambar/menu/InventBoard.png")
inventBoardImg = pygame.transform.scale(inventBoardImg, (1920 * width_ratio, 1080 * height_ratio)) 
inventTopImg = pygame.image.load("./gambar/menu/InventoryTop.png")
inventTopImg = pygame.transform.scale(inventTopImg, (1920 * width_ratio, 1080 * height_ratio)) 
inventPaimonImg = pygame.image.load("./gambar/menu/InventPaimon.png")
inventPaimonImg = pygame.transform.scale(inventPaimonImg, (1920 * width_ratio, 1080 * height_ratio)) 


# Color
black = (0,0,0)
white = (255,255,255)
gray = (25,25,25)

# Fonts
font = pygame.font.Font('genshinfont.ttf', 20)
fontgacha = pygame.font.Font('genshinfont.ttf', 35)
fontprimogem = pygame.font.Font('genshinfont.ttf', 20)
fontInventory = pygame.font.Font('genshinfont.ttf', 13)
fontInventoryTitle = pygame.font.Font('genshinfont.ttf', 40)


# Function untuk mereset data akun (tidak termasuk id dan password)
def reset(acc,id,pw):
    reset = open('saveslot'+ str(acc) +'.py', 'w')
    reset.write('id = \'' + id + '\'')
    reset.write('\npw = \'' + pw + '\'')
    reset.write('\nitems_code = []')
    reset.write('\npity_4 = 0')
    reset.write('\npity_5 = 0')
    reset.write('\nprimogem = 14400')
    reset.close()

# Function untuk menuliskan teks di layar
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Function untuk login/register
def login():
    # deklarasi variabel 
    click = False  
    id_text = ''
    pass_text = ''
    id_active = False
    pass_active = False
    a1_active = False
    a2_active = False
    a3_active = False
    a4_active = False
    a5_active = False
    btn_register_active = False
    btn_login_active = False
    aN = 0
    while True:
        
        # untuk screen
        screen.blit(loginImg, (0, 0))
        # untuk warna box
        rect_color_passive = pygame.Color(58,58,65)
        rect_color_active = pygame.Color(0,0,0)
        box_color_passive = pygame.Color(150,150,150)
        rect_color_id = box_color_passive
        rect_color_pass = box_color_passive
        rect_color_a1 = rect_color_passive
        rect_color_a2 = rect_color_passive
        rect_color_a3 = rect_color_passive
        rect_color_a4 = rect_color_passive
        rect_color_a5 = rect_color_passive

        # menentukan warna box sesuai aktif tidaknya
        if id_active == True:
            rect_color_id = rect_color_active
        else:
            rect_color_id = box_color_passive
        if pass_active == True:
            rect_color_pass = rect_color_active
        else:
            rect_color_pass = box_color_passive
        if a1_active == True:
            rect_color_a1 = rect_color_active
        else:
            rect_color_a1 = rect_color_passive
        if a2_active == True:
            rect_color_a2 = rect_color_active
        else:
            rect_color_a2 = rect_color_passive
        if a3_active == True:
            rect_color_a3 = rect_color_active
        else:
            rect_color_a3 = rect_color_passive
        if a4_active == True:
            rect_color_a4 = rect_color_active
        else:
            rect_color_a4 = rect_color_passive
        if a5_active == True:
            rect_color_a5 = rect_color_active
        else:
            rect_color_a5 = rect_color_passive

        # Box
        id_rect = pygame.Rect(661*width_ratio, 356*height_ratio, 599*width_ratio, 77*height_ratio)
        pygame.draw.rect(screen, rect_color_id, id_rect, width=2)
        pass_rect = pygame.Rect(661*width_ratio, 464*height_ratio, 599*width_ratio, 77*height_ratio)
        pygame.draw.rect(screen, rect_color_pass, pass_rect, width=2)

        # Text
        draw_text(id_text, pygame.font.SysFont(None, 35), (0,0,0), screen, 665*width_ratio, 380*height_ratio)
        draw_text(pass_text, pygame.font.SysFont(None, 35), (0,0,0), screen, 665*width_ratio, 488*height_ratio)

        # Button
        btn_register = pygame.Rect(661*width_ratio,572*height_ratio,162*width_ratio,32*height_ratio)
        btn_login = pygame.Rect(661*width_ratio,647*height_ratio,600*width_ratio,80*height_ratio)
        a1_rect = pygame.Rect(661*width_ratio,780*height_ratio,85*width_ratio,70*height_ratio)
        a2_rect = pygame.Rect(788*width_ratio,780*height_ratio,85*width_ratio,70*height_ratio)
        a3_rect = pygame.Rect(918*width_ratio,780*height_ratio,85*width_ratio,70*height_ratio)
        a4_rect = pygame.Rect(1045*width_ratio,780*height_ratio,85*width_ratio,70*height_ratio)
        a5_rect = pygame.Rect(1175*width_ratio,780*height_ratio,85*width_ratio,70*height_ratio)
        pygame.draw.rect(screen, rect_color_a1, a1_rect)
        pygame.draw.rect(screen, rect_color_a2, a2_rect)
        pygame.draw.rect(screen, rect_color_a3, a3_rect)
        pygame.draw.rect(screen, rect_color_a4, a4_rect)
        pygame.draw.rect(screen, rect_color_a5, a5_rect)
        draw_text("1", font, (237,214,172), screen, 692*width_ratio, 800*height_ratio)
        draw_text("2", font, (237,214,172), screen, 824*width_ratio, 800*height_ratio)
        draw_text("3", font, (237,214,172), screen, 954*width_ratio, 800*height_ratio)
        draw_text("4", font, (237,214,172), screen, 1081*width_ratio, 800*height_ratio)
        draw_text("5", font, (237,214,172), screen, 1211*width_ratio, 800*height_ratio)
        draw_text("Save Slot", pygame.font.SysFont(None, 25), (214,193,109), screen, 904*width_ratio, 745*height_ratio)
        
        for event in pygame.event.get():
            # Exit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # menerima input keyboard
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if id_active == True:
                    if event.key == pygame.K_BACKSPACE:
                        id_text = id_text[:-1]
                    else:
                        id_text += event.unicode
                if pass_active == True:
                    if event.key == pygame.K_BACKSPACE:
                        pass_text = pass_text[:-1]
                    else:
                        pass_text += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                # mendetect jika textbox sudah diklik
                if id_rect.collidepoint(event.pos):
                    id_active = True
                else:
                    id_active = False
                if pass_rect.collidepoint(event.pos):
                    pass_active = True
                else:
                    pass_active = False
                # ganti warna slot aktif (menggunakan for untuk memastikan hanya satu tombol yang aktif)
                for i in range(2):
                    if a1_rect.collidepoint(event.pos):
                        a1_active = True
                    elif a2_active or a3_active or a4_active or a5_active:
                        a1_active = False
                    if a2_rect.collidepoint(event.pos):
                        a2_active = True
                    elif a1_active or a3_active or a4_active or a5_active:
                        a2_active = False
                    if a3_rect.collidepoint(event.pos):
                        a3_active = True
                    elif a1_active or a2_active or a4_active or a5_active:
                        a3_active = False
                    if a4_rect.collidepoint(event.pos):
                        a4_active = True
                    elif a1_active or a2_active or a3_active or a5_active:
                        a4_active = False
                    if a5_rect.collidepoint(event.pos):
                        a5_active = True
                    elif a1_active or a2_active or a3_active or a4_active:
                        a5_active = False
                # mendetect klik tombol
                if btn_login.collidepoint(event.pos):
                    btn_login_active = True
                else:
                    btn_login_active = False
                if btn_register.collidepoint(event.pos):
                    btn_register_active = True
                else:
                    btn_register_active = False

        # detect klik di button
        reload(saveslot1) ; reload(saveslot2) ; reload(saveslot3) ; reload(saveslot4) ; reload(saveslot5)
        mx, my = pygame.mouse.get_pos()
        if btn_register.collidepoint(mx, my):
            if btn_register_active:
                if 1<=aN<=5:
                    items_code = []
                    pity_4 = 0
                    pity_5 = 0
                    primogem = 14400
                    overwrite = open('saveslot'+ str(aN) +'.py', 'w')
                    overwrite.write('id = \'' + id_text + '\'')
                    overwrite.write('\npw = \'' + pass_text + '\'')
                    overwrite.write('\nitems_code = ' + str(items_code))
                    overwrite.write('\npity_4 = ' + str(pity_4))
                    overwrite.write('\npity_5 = ' + str(pity_5))
                    overwrite.write('\nprimogem = ' + str(primogem))
                    overwrite.close()
                    draw_text("account registered",font,(0,0,0), screen, 1000*width_ratio,572*height_ratio)
                else:
                    draw_text("select saveslot",font,(0,0,0), screen, 1050*width_ratio,572*height_ratio)
        if btn_login.collidepoint(mx, my):
            if btn_login_active:
                if aN == 1:
                    if saveslot1.id == id_text and saveslot1.pw == pass_text:
                        main_menu(aN)
                    else:
                        draw_text("invalid id or pass",font,(0,0,0), screen, 1000*width_ratio,572*height_ratio)
                elif aN == 2:
                    if saveslot2.id == id_text and saveslot2.pw == pass_text:
                        main_menu(aN)
                    else:
                        draw_text("invalid id or pass",font,(0,0,0), screen, 1000*width_ratio,572*height_ratio)
                elif aN == 3:
                    if saveslot3.id == id_text and saveslot3.pw == pass_text:
                        main_menu(aN)
                    else:
                        draw_text("invalid id or pass",font,(0,0,0), screen, 1000*width_ratio,572*height_ratio)
                elif aN == 4:
                    if saveslot4.id == id_text and saveslot4.pw == pass_text:
                        main_menu(aN)
                    else:
                        draw_text("invalid id or pass",font,(0,0,0), screen, 1000*width_ratio,572*height_ratio)
                elif aN == 5:
                    if saveslot5.id == id_text and saveslot5.pw == pass_text:
                        main_menu(aN)
                    else:
                        draw_text("invalid id or pass",font,(0,0,0), screen, 1000*width_ratio,572*height_ratio)
                else:
                    draw_text("select saveslot",font,(0,0,0), screen, 1050*width_ratio,572*height_ratio)
        if a1_rect.collidepoint(mx,my):
            if a1_active:
                aN = 1
        if a2_rect.collidepoint(mx,my):
            if a2_active:
                aN = 2
        if a3_rect.collidepoint(mx,my):
            if a3_active:
                aN = 3
        if a4_rect.collidepoint(mx,my):
            if a4_active:
                aN = 4
        if a5_rect.collidepoint(mx,my):
            if a5_active:
                aN = 5
        # update
        pygame.display.update()

# Function untuk gacha
def gacha(acc, anemo=anemo, cryo=cryo, electro=electro, geo=geo, hydro=hydro, pyro=pyro, sword=sword, claymore=claymore, polearm=polearm, bow=bow, catalyst=catalyst):
    ABC = True
    running = True
    click = False
    while running == True:
        if acc == 1:
            reload(saveslot1)
            id = saveslot1.id
            pw = saveslot1.pw
            items_code = saveslot1.items_code
            pity_4 = saveslot1.pity_4
            pity_5 = saveslot1.pity_5
            primogem = saveslot1.primogem
        elif acc == 2:
            reload(saveslot2)
            id = saveslot2.id
            pw = saveslot2.pw
            items_code = saveslot2.items_code
            pity_4 = saveslot2.pity_4
            pity_5 = saveslot2.pity_5
            primogem = saveslot2.primogem
        elif acc == 3:
            reload(saveslot3)
            id = saveslot3.id
            pw = saveslot3.pw
            items_code = saveslot3.items_code
            pity_4 = saveslot3.pity_4
            pity_5 = saveslot3.pity_5
            primogem = saveslot3.primogem
        elif acc == 4:
            reload(saveslot4)
            id = saveslot4.id
            pw = saveslot4.pw
            items_code = saveslot4.items_code
            pity_4 = saveslot4.pity_4
            pity_5 = saveslot4.pity_5
            primogem = saveslot4.primogem
        elif acc == 5:
            reload(saveslot5)
            id = saveslot5.id
            pw = saveslot5.pw
            items_code = saveslot5.items_code
            pity_4 = saveslot5.pity_4
            pity_5 = saveslot5.pity_5
            primogem = saveslot5.primogem

        # Inisiasi variabel dan tampilan menu gacha
        a = [3, 4, 5]
        prob_3 = 0.943
        prob_4 = 0.051
        prob_5 = 0.006
        choices = []
        flag = False
        freq = -1
        mx, my = pygame.mouse.get_pos()
        button_1xWish = pygame.Rect((1148*width_ratio,  970*height_ratio), (340*width_ratio, 75*height_ratio))
        button_10xWish = pygame.Rect((1522*width_ratio, 970*height_ratio), (340*width_ratio, 75*height_ratio))
        pygame.draw.rect(screen, (75,53,34), button_1xWish)
        pygame.draw.rect(screen, (75,53,34), button_10xWish)
        screen.blit(bannerImg, (0, 0))
        screen.blit(primogemDisplayGameImg, (1920-402, 0))
        draw_text(str(primogem), pygame.font.Font('genshinfont.ttf', int(30*height_ratio)), ((255,255,255)), screen, 1600*width_ratio, 32*height_ratio)
        draw_text('Esc', pygame.font.Font('genshinfont.ttf', int(30*height_ratio)), ((255,255,255)), screen, 1820*width_ratio, 80*height_ratio)

        # Exit dari menu gacha
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        # Interaksi tombol untuk gacha
        if button_1xWish.collidepoint((mx, my)):
            screen.blit(banner160Img, (0, 0))
            if click:
                if primogem < 160:
                    pass
                else:
                    flag = True
                    freq = 1
                    primogem -= 160
        if button_10xWish.collidepoint((mx, my)):
            screen.blit(banner1600Img, (0, 0))
            if click:
                if primogem < 1600:
                    pass
                else:
                    flag = True
                    freq = 10
                    primogem -= 1600

        click = False

        if flag:
            # Pengaturan probabilitas item gacha dan pemilihan id item berdasarkan probabilitasnya
            for x in range(freq):
                if pity_5 == 9 and pity_4 == 89:
                    prob_3, prob_4, prob_5 = 0, 0, 1
                if pity_4 == 9:
                    prob_3, prob_4, prob_5 = 0, 1, 0
                if pity_5 == 89:
                    prob_3, prob_4, prob_5 = 0, 0, 1
                
                choice = np.random.choice(a, 1, replace=True, p=[prob_3, prob_4, prob_5])
                choices.append(choice)
                
                if choice == 4:
                    pity_4 = 0
                    prob_3, prob_4, prob_5 = 0.943, 0.051, 0.006
                else:
                    pity_4 += 1
                if choice == 5:
                    pity_5 = 0
                    if pity_4 == 9:
                        pity_4 = 0
                    prob_3, prob_4, prob_5 = 0.943, 0.051, 0.006
                else:
                    pity_5 += 1
            
            for choice in choices:
                
                if choice == 5:
                    x = random.randint(1, 40)
                elif choice == 4:
                    x = random.randint(41, 82)
                elif choice == 3:
                    x = random.randint(83, 96)
            
                items_code.append(x)

            overwrite = open('saveslot'+ str(acc) +'.py', 'w')
            overwrite.write('id = \'' + id + '\'')
            overwrite.write('\npw = \'' + pw + '\'')
            overwrite.write('\nitems_code = ' + str(items_code))
            overwrite.write('\npity_4 = ' + str(pity_4))
            overwrite.write('\npity_5 = ' + str(pity_5))
            overwrite.write('\nprimogem = ' + str(primogem))
            overwrite.close()

            # Display item gacha di layar
            for i in range(len(items_code) - freq, len(items_code)):
                click = False
                while not click:
                    screen.blit(gachabgImg, (0, 0))
                    gachaImg = pygame.image.load('./gambar/' + str(items_code[i]) + '_' + items_dictionary[items_code[i]] + '.png')
                    gachaImg_rect = gachaImg.get_rect()
                    if items_code[i] in polearm:
                        gachaImg = pygame.transform.scale(gachaImg, (gachaImg_rect.width * 0.8, gachaImg_rect.height * 0.8))
                    gachaImg_rect = gachaImg.get_rect()
                    screen.blit(gachaImg, (gachabgImg_rect.center[0] - gachaImg_rect.center[0], gachabgImg_rect.center[1] - gachaImg_rect.center[1]))
                    
                    if items_code[i] in anemo:
                        elementImg = pygame.image.load('./gambar/anemo.png')
                    elif items_code[i] in cryo:
                        elementImg = pygame.image.load('./gambar/cryo.png')
                    elif items_code[i] in electro:
                        elementImg = pygame.image.load('./gambar/electro.png')
                    elif items_code[i] in geo:
                        elementImg = pygame.image.load('./gambar/geo.png')
                    elif items_code[i] in hydro:
                        elementImg = pygame.image.load('./gambar/hydro.png')
                    elif items_code[i] in pyro:
                        elementImg = pygame.image.load('./gambar/pyro.png')
                    elif items_code[i] in sword:
                        elementImg = pygame.image.load('./gambar/sword.png')
                    elif items_code[i] in claymore:
                        elementImg = pygame.image.load('./gambar/claymore.png')
                    elif items_code[i] in polearm:
                        elementImg = pygame.image.load('./gambar/polearm.png')
                    elif items_code[i] in bow:
                        elementImg = pygame.image.load('./gambar/bow.png')
                    elif items_code[i] in catalyst:
                        elementImg = pygame.image.load('./gambar/catalyst.png')
                    elementImg_rect = elementImg.get_rect()
                    if items_code[i] in (sword + claymore + polearm + bow + catalyst):
                        elementImg = pygame.transform.scale(elementImg, (64, 64))
                        elementImg_rect = elementImg.get_rect()
                    screen.blit(elementImg, (0, 0))

                    if 1 <= items_code[i] <= 40:
                        starImg = pygame.image.load('./gambar/star5.png')
                    elif 41 <= items_code[i] <= 82:
                        starImg = pygame.image.load('./gambar/star4.png')
                    else:
                        starImg = pygame.image.load('./gambar/star3.png')
                    starImg_rect = starImg.get_rect()
                    starImg = pygame.transform.scale(starImg, (starImg_rect.width*2,starImg_rect.height*2))
                    screen.blit(starImg, (elementImg_rect.width, elementImg_rect.height * 0.75))
                    
                    draw_text(str(items_dictionary[items_code[i]]), fontgacha, (gray), screen, elementImg_rect.width - 1, 6)
                    draw_text(str(items_dictionary[items_code[i]]), fontgacha, ((gray)), screen, elementImg_rect.width - 1, 8)
                    draw_text(str(items_dictionary[items_code[i]]), fontgacha, ((gray)), screen, elementImg_rect.width + 1, 6)
                    draw_text(str(items_dictionary[items_code[i]]), fontgacha, ((gray)), screen, elementImg_rect.width + 1, 8)
                    draw_text(str(items_dictionary[items_code[i]]), fontgacha, ((white)), screen, elementImg_rect.width, 7)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        if event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                running = False
                        if event.type == MOUSEBUTTONDOWN:
                            if event.button == 1:
                                click = True
                    pygame.display.update()
            
            click = False
            flag = False
            freq = -1

        pygame.display.update()
        

# Function untuk membuat sistem inventory
def inventory(acc):
    if acc == 1:
        reload(saveslot1)
        items_code = saveslot1.items_code
        primogem = saveslot1.primogem
    elif acc == 2:
        reload(saveslot2)
        items_code = saveslot2.items_code
        primogem = saveslot2.primogem
    elif acc == 3:
        reload(saveslot3)
        items_code = saveslot3.items_code
        primogem = saveslot3.primogem
    elif acc == 4:
        reload(saveslot4)
        items_code = saveslot4.items_code
        primogem = saveslot4.primogem
    elif acc == 5:
        reload(saveslot5)
        items_code = saveslot5.items_code
        primogem = saveslot5.primogem
    
    # Inisiasi variabel
    Z = 0
    Menu1x = -10
    Menu3x = -1800
    last_time = time.time()
    char_5 = []
    char_4 = []
    weapon_5 = []
    weapon_4 = []
    weapon_3 = []
    running = True
    click = False
    while running == True:
        screen.fill(((232,220,191)))
        dt = time.time() - last_time
        last_time = time.time()
        dt *= 144
        
        # Display primogem
        screen.blit(primogemDisplayGameImg, (0,0))
        display_primogem = fontprimogem.render(str(primogem), True, white)
        screen.blit(display_primogem, (1620 * width_ratio, 35 * height_ratio))

        if Menu1x <= -1930:
            Menu1x = -10
        else:
            Menu1x -= 0.1*dt
        
        # tambahan
        screen.blit(Menu1Img, (Menu1x, 0))
        screen.blit(Menu2Img, (0, 37))
        screen.blit(Menu4Img, (0, 0))
        screen.blit(inventBoardImg, (0, 0))
        screen.blit(inventTopImg, (0, 0))
        screen.blit(inventPaimonImg, (0, 0))
        draw_text(str(primogem), pygame.font.Font('genshinfont.ttf', int(30*height_ratio)), ((75*2,53*2,34*2)), screen, 1600*width_ratio, 32*height_ratio)

        # Penggolongan item gacha berdasarkan jenis dan kelangkaannya dan perhitungan jumlah tiap item gacha
        item_amount = [0 for n in range(96)]
        for item_id in items_code:
            if 1 <= item_id <= 19 or 41 <= item_id <= 60:
                type = 'c'
            else:
                type = 'w'

            if 1 <= item_id <= 40:
                star = 5
            elif 41 <= item_id <= 82:
                star = 4
            else:
                star = 3
            
            item_amount[item_id - 1] += 1 
            
            if type == 'c':
                if star == 5:
                    char_5.append(item_id)
                else:
                    char_4.append(item_id)
            else:
                if star == 5:
                    weapon_5.append(item_id)
                elif star == 4:
                    weapon_4.append(item_id)
                else:
                    weapon_3.append(item_id)

        # Menghilangkan duplikat item gacha untuk ditampilkan
        setchar_5 = set(char_5)
        setchar_4 = set(char_4)
        setweapon_5 = set(weapon_5)
        setweapon_4 = set(weapon_4)
        setweapon_3 = set(weapon_3)

        # Tampilan inventory
        Z = 0       
        draw_text('5* Character', pygame.font.Font('genshinfont.ttf', int(25*height_ratio)), ((75,53,34)), screen, 650 * width_ratio, 190 * height_ratio)
        for item in setchar_5:
            draw_text(items_dictionary[item] + ' (x' + str(item_amount[item - 1]) + ')', fontInventory, ((75,53,34)), screen, 650 * width_ratio, (225 + Z) * height_ratio)
            Z += 20
        Z = 0
        draw_text('4* Character', pygame.font.Font('genshinfont.ttf', int(30*height_ratio)), ((75,53,34)), screen, 1100 * width_ratio, 190 * height_ratio)
        for item in setchar_4:
            draw_text(items_dictionary[item] + ' (x' + str(item_amount[item - 1]) + ')', fontInventory, ((75,53,34)), screen, 1100 * width_ratio, (225 + Z) * height_ratio)
            Z += 20
        Z = 0
        draw_text('5* Weapon', pygame.font.Font('genshinfont.ttf', int(30*height_ratio)), ((75,53,34)), screen, 1550 * width_ratio, 190 * height_ratio)
        for item in setweapon_5:
            draw_text(items_dictionary[item] + ' (x' + str(item_amount[item - 1]) + ')', fontInventory, ((75,53,34)), screen, 1550 * width_ratio, (225 + Z) * height_ratio)
            Z += 20
        Z = 0
        draw_text('4* Weapon', pygame.font.Font('genshinfont.ttf', int(30*height_ratio)), ((75,53,34)), screen, 650 * width_ratio, (1080/2 + 90) * height_ratio)
        for item in setweapon_4:
            draw_text(items_dictionary[item] + ' (x' + str(item_amount[item - 1]) + ')', fontInventory, ((75,53,34)), screen, 650 * width_ratio, (1080/2 + 125+ Z) * height_ratio)
            Z += 20
        Z = 0
        draw_text('3* Weapon', pygame.font.Font('genshinfont.ttf', int(30*height_ratio)), ((75,53,34)), screen, 1100 * width_ratio, (1080/2 + 90) * height_ratio)
        for item in setweapon_3:
            draw_text(items_dictionary[item] + ' (x' + str(item_amount[item - 1]) + ')', fontInventory, ((75,53,34)), screen, 1100 * width_ratio, (1080/2 + 125 + Z) * height_ratio)
            Z += 20

        # Keluar dari inventory
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()

click = False
 
# Function untuk menampilkan main menu
def main_menu(acc, anemo=anemo, cryo=cryo, electro=electro, geo=geo, hydro=hydro, pyro=pyro, sword=sword, claymore=claymore, polearm=polearm, bow=bow, catalyst=catalyst):
    click = False
    Menu1x = -10
    Menu3x = -1800
    last_time = time.time()
    ads = 1
    MenuPaimonY = 0
    MenuPaimonVY = 12
    AdsTime = 100
    while True:
        if acc == 1:
            reload(saveslot1)
            id = saveslot1.id
            pw = saveslot1.pw
            items_code = saveslot1.items_code
            pity_4 = saveslot1.pity_4
            pity_5 = saveslot1.pity_5
            primogem = saveslot1.primogem
        elif acc == 2:
            reload(saveslot2)
            id = saveslot2.id
            pw = saveslot2.pw
            items_code = saveslot2.items_code
            pity_4 = saveslot2.pity_4
            pity_5 = saveslot2.pity_5
            primogem = saveslot2.primogem
        elif acc == 3:
            reload(saveslot3)
            id = saveslot3.id
            pw = saveslot3.pw
            items_code = saveslot3.items_code
            pity_4 = saveslot3.pity_4
            pity_5 = saveslot3.pity_5
            primogem = saveslot3.primogem
        elif acc == 4:
            reload(saveslot4)
            id = saveslot4.id
            pw = saveslot4.pw
            items_code = saveslot4.items_code
            pity_4 = saveslot4.pity_4
            pity_5 = saveslot4.pity_5
            primogem = saveslot4.primogem
        elif acc == 5:
            reload(saveslot5)
            id = saveslot5.id
            pw = saveslot5.pw
            items_code = saveslot5.items_code
            pity_4 = saveslot5.pity_4
            pity_5 = saveslot5.pity_5
            primogem = saveslot5.primogem

        dt = time.time() - last_time
        last_time = time.time()
        dt *= 144 * height_ratio
        
        # Tampilan main menu
        button_1 = pygame.Rect((198) * width_ratio, (502) * height_ratio, 491 * width_ratio, 69 * height_ratio)
        button_2 = pygame.Rect((198) * width_ratio, (594) * height_ratio, 491 * width_ratio, 69 * height_ratio)
        button_3 = pygame.Rect((198) * width_ratio, (686) * height_ratio, 491 * width_ratio, 69 * height_ratio)
        button_4 = pygame.Rect((790) * width_ratio, (281) * height_ratio, 906 * width_ratio, 467 * height_ratio)
        button_5 = pygame.Rect((35) * width_ratio, (1020) * height_ratio, 145 * width_ratio, 43 * height_ratio)
        button_6 = pygame.Rect((200) * width_ratio, (1020) * height_ratio, 100 * width_ratio, 43 * height_ratio)
        pygame.draw.rect(screen, (75,53,34), button_1)
        pygame.draw.rect(screen, (75,53,34), button_2)
        pygame.draw.rect(screen, (75,53,34), button_3)
        pygame.draw.rect(screen, (75,53,34), button_4)
        pygame.draw.rect(screen, (0,0,0), button_5, width=2)
        pygame.draw.rect(screen, (0,0,0), button_6, width=2)
        
        if Menu1x <= -1930 * width_ratio:
            Menu1x = -10 * width_ratio
        else:
            Menu1x -= 0.1*dt

        screen.blit(primogemDisplayGameImg, (0,0))
        screen.blit(Menu1Img, (Menu1x, 0))
        screen.blit(Menu2Img, (0, 37 * height_ratio))
        screen.blit(Menu4Img, (0, 0))
        screen.blit(MenuTopImg, (0, 188 * height_ratio))

        # Tampilan banner gacha di main menu
        if ads == 1:
            screen.blit(Ads1Img, (790 * width_ratio, 281 * height_ratio))
        elif ads == 2:
            screen.blit(Ads2Img, (790 * width_ratio, 281 * height_ratio))
        elif ads == 3:
            screen.blit(Ads3Img, (790 * width_ratio, 281 * height_ratio))
        elif ads == 4:
            screen.blit(Ads4Img, (790 * width_ratio, 281 * height_ratio))
        else:
            ads = 1

        if AdsTime <= 0:
            screen.blit(Ads0Img, (790 * width_ratio, 281 * height_ratio))
            ads += 1
            if ads > 4:
                ads = 1
            AdsTime = 100

        AdsTime -= 4
        
        # Animasi/gerakan karakter Paimon di main menu
        screen.blit(MenuPaimonImg, (1430*width_ratio, (MenuPaimonY + 195)*height_ratio))
        MenuPaimonY += MenuPaimonVY

        if MenuPaimonY >= 60*height_ratio:
            MenuPaimonVY = -0.23*dt
        elif MenuPaimonY <= -60*height_ratio:
            MenuPaimonVY = 0.23*dt

        if MenuPaimonY > 60*height_ratio:
            MenuPaimonY = 60*height_ratio
        elif MenuPaimonY < -60*height_ratio:
            MenuPaimonY = -60*height_ratio

        if MenuPaimonY >= 0 and MenuPaimonVY >= 0:
            MenuPaimonVY *= 0.97
        if MenuPaimonY >= 0 and MenuPaimonVY < 0:
            MenuPaimonVY *= 1.25

        if MenuPaimonY < 0 and MenuPaimonVY >= 0:
            MenuPaimonVY *= 1.25
        if MenuPaimonY < 0 and MenuPaimonVY < 0:
            MenuPaimonVY *= 0.97

        # Display primogem
        screen.blit(primogemDisplayGameWhiteImg, ((1920-401) * width_ratio, 0))
        draw_text('Account '+ str(acc), pygame.font.Font('genshinfont.ttf', int(30*height_ratio)), ((255,255,255)), screen, 45*width_ratio, 976*height_ratio)
        draw_text(str(primogem), pygame.font.Font('genshinfont.ttf', int(30*height_ratio)), ((75*2,53*2,34*2)), screen, 1600*width_ratio, 32*height_ratio)
        draw_text('Reset', pygame.font.Font('genshinfont.ttf', int(30*height_ratio)), ((255,255,255)), screen, (210) * width_ratio, (1020) * height_ratio)

        # Interaksi tombol di main menu
        mx, my = pygame.mouse.get_pos()
        if button_1.collidepoint((mx, my)):
            screen.blit(menuButton1Img, (0, 188*height_ratio))
            if click:
                game(acc)

        if button_2.collidepoint((mx, my)):
            screen.blit(menuButton2Img, (0, 188*height_ratio))
            if click:
                gacha(acc)

        if button_3.collidepoint((mx, my)):
            screen.blit(menuButton3Img, (0, 188*height_ratio))
            if click:
                inventory(acc)
        if button_4.collidepoint((mx, my)):
            if click:
                ads += 1
                if ads > 4:
                    ads = 1
                AdsTime = 100

        if button_5.collidepoint((mx, my)):
            if click:
                login()

        if button_6.collidepoint((mx, my)):
            if click:
                reset(acc,id,pw)

        # Keluar dari main menu
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()

# Function untuk membuat karakter di dalam mini game
def player(player_V_Y, playerImg, playerY):
    playerX = 1920*width_ratio/4
    playerImg = pygame.transform.rotate(playerImg, -80*player_V_Y//17)
    screen.blit(playerImg, (playerX, playerY))
    playerImg = pygame.transform.rotate(playerImg, 80*player_V_Y//17)

# Function untuk membuat dan mengoperasikan mini game
def game(acc):
    if acc == 1:
        reload(saveslot1)
        id = saveslot1.id
        pw = saveslot1.pw
        items_code = saveslot1.items_code
        pity_4 = saveslot1.pity_4
        pity_5 = saveslot1.pity_5
        primogem = saveslot1.primogem
    elif acc == 2:
        reload(saveslot2)
        id = saveslot2.id
        pw = saveslot2.pw
        items_code = saveslot2.items_code
        pity_4 = saveslot2.pity_4
        pity_5 = saveslot2.pity_5
        primogem = saveslot2.primogem
    elif acc == 3:
        reload(saveslot3)
        id = saveslot3.id
        pw = saveslot3.pw
        items_code = saveslot3.items_code
        pity_4 = saveslot3.pity_4
        pity_5 = saveslot3.pity_5
        primogem = saveslot3.primogem
    elif acc == 4:
        reload(saveslot4)
        id = saveslot4.id
        pw = saveslot4.pw
        items_code = saveslot4.items_code
        pity_4 = saveslot4.pity_4
        pity_5 = saveslot4.pity_5
        primogem = saveslot4.primogem
    elif acc == 5:
        reload(saveslot5)
        id = saveslot5.id
        pw = saveslot5.pw
        items_code = saveslot5.items_code
        pity_4 = saveslot5.pity_4
        pity_5 = saveslot5.pity_5
        primogem = saveslot5.primogem

    screen.fill((232,220,191))
    screen.blit(backgroundImg, (0, 0))
    player(0, playerImg, screen_height//2)
    screen.blit(primogemDisplayGameImg, (1920-402, 0))
    draw_text(str(primogem), pygame.font.Font('genshinfont.ttf', int(30*height_ratio)), ((255,255,255)), screen, 1600*width_ratio, 32*height_ratio)
        

    running0 = True
    running = True
    running3 = False
    primoCount = 0

    last_time = time.time()

    player_jump_V_Y = -15
    player_VMAX_Y = 12
    player_VMIN_Y = -15
    player_V_Y = -1
    gravity = 0.3
    player_jump_V_Y = -15
    player_jump = False
    
    playerY = screen_height/2 - (149/2)
    while running0:

        screen.fill((232,220,191))
        dt = time.time() - last_time
        last_time = time.time()
        dt *= 144

        screen.blit(backgroundImg, (0, 0))
        player(0, playerImg, playerY)
        screen.blit(primogemDisplayGameImg, ((1920-402) * width_ratio, 0))
        draw_text(str(primogem), pygame.font.Font('genshinfont.ttf', int(30*height_ratio)), ((255,255,255)), screen, 1600*width_ratio, 32*height_ratio)
        draw_text("Press Space to Jump", pygame.font.Font('genshinfont.ttf', int(30*height_ratio)), ((255,255,255)), screen, 400*width_ratio, playerY + 200*height_ratio)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running0 = False 
                running = False 
            if event.type == pygame.KEYDOWN and event.key == K_SPACE:
                player_V_Y = player_jump_V_Y * dt
                player_jump = True
                running0 = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running0 = False
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    player_V_Y = player_jump_V_Y * dt
                    player_jump = True
                    running0 = False
        pygame.display.update()
        dt = time.time() - last_time
    last_time = time.time()


    pillar1X = -1000
    pillar1X2 = -1000
    
    pillar2X = screen_width + screen_width/2 + (196/2) * width_ratio
    pillar2X2 = screen_width + screen_width/2 + (196/2) * width_ratio
    pillar2Y = random.randrange(int(screen_height/2 + 150*height_ratio), int(screen_height/2 + 400*height_ratio))
    pillar2Y2 = pillar2Y - random.randrange(400, 650)*height_ratio - pillarImg2.get_height()

    pillarV = 3

    dt = time.time()
    
    while running:


        dt = time.time() - last_time
        last_time = time.time()
        dt *= 144

        # Warna screen, dalem kurung R, G, B
        screen.fill((232,220,191))

        # Tombol semua event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == K_SPACE:
                player_V_Y = player_jump_V_Y * dt
                player_jump = True
                running3 = True
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    player_V_Y = player_jump_V_Y * dt
                    player_jump = True
                    running3 = True

        # Background
        screen.blit(backgroundImg, (0, 0))

        # Pergerakan player
        if player_V_Y < player_VMAX_Y and not player_jump:
            player_V_Y += gravity * dt * height_ratio

        if player_jump:
            player_jump = False

        if player_V_Y <= player_VMIN_Y:
            player_V_Y = player_VMIN_Y
        if playerY >= screen_height-128*height_ratio-100:
            playerY = screen_height-128*height_ratio-100
        if playerY <= 0:
            playerY = 0

        playerY += player_V_Y * height_ratio
        
        # Pillar 1
        if pillar1X < -200:
            pillar1Y = random.randrange((int(screen_height/2+225)), 880)*height_ratio
            pillar1X = screen_width
        if pillar1X2 < -200:
            pillar1Y2 = (pillar1Y - random.randrange(375, 600) - pillarImg2.get_height())*height_ratio
            pillar1X2 = pillar1X
        screen.blit(pillarImg, (pillar1X, pillar1Y))
        screen.blit(pillarImg2, (pillar1X, pillar1Y2))
        pillar1X2 = pillar1X
        if playerY + 28*height_ratio <= pillar1Y2 + 740*height_ratio and ((playerX <= pillar1X2 <= playerX + 128*width_ratio) or (playerX <= pillar1X2 + 196*width_ratio <= playerX + 128*width_ratio)):
            running = False
        
        if playerY + (149 - 14)*height_ratio >= pillar1Y and ((playerX <= pillar1X <= playerX + 128*width_ratio) or (playerX <= pillar1X + 196*width_ratio <= playerX + 128*width_ratio)):
            running = False

        # Pillar 2
        if pillar2X < -200:
            pillar2Y = random.randrange(int(1080/2+150), 880)*height_ratio
            pillar2X = screen_width
            pillar2Y2 = (pillar2Y - random.randrange(500, 750) - pillarImg2.get_height())*height_ratio
            pillar2X2 = pillar2X
        screen.blit(pillarImg, (pillar2X, pillar2Y))
        screen.blit(pillarImg2, (pillar2X2, pillar2Y2))
        pillar2X2 = pillar2X
        if playerY + 28*height_ratio <= pillar2Y2 + 740*height_ratio and ((playerX <= pillar2X2 <= playerX + 128*width_ratio) or (playerX <= pillar2X2 + 196*width_ratio <= playerX + 128*width_ratio)):
            running = False
        
        if playerY + (149 - 14)*height_ratio >= pillar2Y and ((playerX <= pillar2X <= playerX + 128*width_ratio) or (playerX <= pillar2X + 196*width_ratio <= playerX + 128*width_ratio)):
            running = False
        
        #Display primogem
        if pillar1X + (196/2 - 40)*width_ratio <= playerX + 64*width_ratio <= pillar1X + (196/2 + 40)*width_ratio:
            primogem += 50
            primoCount += 50
        if pillar2X + (196/2 - 40)*width_ratio <= playerX + 64*width_ratio <= pillar2X + (196/2 + 40)*width_ratio:
            primogem += 50
            primoCount += 50
        player(player_V_Y, playerImg, playerY)

        screen.blit(primogemDisplayGameImg, ((1920-402) * width_ratio, 0))
        draw_text(str(primogem), pygame.font.Font('genshinfont.ttf', int(30*height_ratio)), ((255,255,255)), screen, 1600*width_ratio, 32*height_ratio)
        
        # Untuk update layar
        pillar1X -= pillarV * dt
        pillar2X -= pillarV * dt
        overwrite = open('saveslot'+ str(acc) +'.py', 'w')
        overwrite.write('id = \'' + id + '\'')
        overwrite.write('\npw = \'' + pw + '\'')
        overwrite.write('\nitems_code = ' + str(items_code))
        overwrite.write('\npity_4 = ' + str(pity_4))
        overwrite.write('\npity_5 = ' + str(pity_5))
        overwrite.write('\nprimogem = ' + str(primogem))
        overwrite.close()

        pygame.display.update()

    while running3:
        screen.blit(Menu4Img, (0, 0))
        draw_text("GAME OVER", pygame.font.Font('genshinfont.ttf', int(200*height_ratio)), ((255,255,255)), screen, 100*width_ratio, 250*height_ratio)
        draw_text("You gained " + str(primoCount) + " primogems", pygame.font.Font('genshinfont.ttf', int(50*height_ratio)), ((255,255,255)), screen, 100*width_ratio, 600*height_ratio)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running3 = False
            
            if event.type == pygame.KEYDOWN and event.key == K_SPACE:
                running3 = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running3 = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    running3 = False
        pygame.display.update()

# Backsound               
file = 'Liyue.wav'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1) #0.0 < volume < 1.0
pygame.event.wait()
login()