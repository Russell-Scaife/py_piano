#Piano Project
import pygame
import sys
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode([1000,800])
pygame.display.set_caption('Pygame Test')

white = (255,255,255)
black = (0,0,0)
grey = (170,170,170)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
white_key_width = 50
white_key_height = 150
black_key_width = 36
black_key_height = 100
bottom_white_x = 275
bottom_white_y = 600
bottom_black_x = 307
bottom_black_y = 600
top_white_x = 125
top_white_y = 50
top_black_x=157
top_black_y = 50
black_key_spacing = [50,100,50,50,50]
top_black_spacing = [50,50,100,50,100,50,50,100,50,0]

bottom_white_letters = ['A','S','D','F','G','H','J','K']
bottom_black_letters = ['W','E','T','Y',"U"]
keyboard_letters = ['A','W','S','E','D','F','T','G','Y','H','U','J','K']
top_white_notes = ['F','G','A','B','C','D','E','F','G','A','B','C','D','E','F']
top_sharp_notes = ['F#','G#','A#','C#','D#','F#','G#','A#','C#','D#']
top_flat_notes = ['Gb','Ab','Bb','Db','Eb','Gb','Ab','Bb','Db','Eb']
font = pygame.font.SysFont('couriernew', 25,True)
key_presses = [K_a,K_w,K_s,K_e,K_d,K_f,K_t,K_g,K_y,K_h,K_u,K_j,K_k]


keyboard_letters_pressed = []
for i in keyboard_letters:
    keyboard_letters_pressed.append(i+'_pressed')

#Bottom Key Locations

bottom_white_keys =[]
bottom_black_keys = []

for i in range(8):
    bottom_white_keys.append(pygame.Rect(bottom_white_x,bottom_white_y,white_key_width,white_key_height))
    bottom_white_x +=50
for i in range(5):
    bottom_black_keys.append(pygame.Rect(bottom_black_x,bottom_black_y,black_key_width,black_key_height))
    bottom_black_x += black_key_spacing[i]

bottom_keys = [bottom_white_keys[0],bottom_black_keys[0],bottom_white_keys[1],bottom_black_keys[1],bottom_white_keys[2],bottom_white_keys[3],bottom_black_keys[2],bottom_white_keys[4],bottom_black_keys[3],bottom_white_keys[5],bottom_black_keys[4],bottom_white_keys[6],bottom_white_keys[7]]

bottom_keyboard_dictionary = {}
for i in range(len(keyboard_letters)):
    bottom_keyboard_dictionary[keyboard_letters[i]] = bottom_keys[i] 


#Top Key Locations

top_white_keys = []
top_black_keys = []

for i in range(15):
    top_white_keys.append(pygame.Rect(top_white_x,top_white_y,white_key_width,white_key_height))
    top_white_x += 50
for i in range(10):
    top_black_keys.append(pygame.Rect(top_black_x,top_black_y,black_key_width,black_key_height))
    top_black_x += top_black_spacing[i]

top_keys = [top_white_keys[0],top_black_keys[0],top_white_keys[1],top_black_keys[1],top_white_keys[2],top_black_keys[2],top_white_keys[3],top_white_keys[4],top_black_keys[3],top_white_keys[5],top_black_keys[4],top_white_keys[6],top_white_keys[7],top_black_keys[5],top_white_keys[8],top_black_keys[6],top_white_keys[9],top_black_keys[7],top_white_keys[10],top_white_keys[11],top_black_keys[8],top_white_keys[12],top_black_keys[9],top_white_keys[13],top_white_keys[14]]
pressed = pygame.key.get_pressed()

def major_chord_white():
    for i in range(13):
        if pressed[key_presses[i]]:
            if i <11:
                pygame.draw.rect(window,green,top_keys[i+7])
                pygame.draw.rect(window,green,top_keys[i+11])
                pygame.draw.rect(window,green,top_keys[i+14])
            else:
                pygame.draw.rect(window,green,top_keys[i-5])
                pygame.draw.rect(window,green,top_keys[i-1])
                pygame.draw.rect(window,green,top_keys[i+2])
def major_chord_black():
    for i in range(13):
        if pressed[key_presses[i]]:
            if i<11:
                if top_keys[i+7] in top_black_keys:
                    pygame.draw.rect(window,green,top_keys[i+7])
                if top_keys[i+11] in top_black_keys:    
                    pygame.draw.rect(window,green,top_keys[i+11])
                if top_keys[i+14] in top_black_keys:
                    pygame.draw.rect(window,green,top_keys[i+14])
            else:
                if top_keys[i-5] in top_black_keys:
                    pygame.draw.rect(window,green,top_keys[i-5])
                if top_keys[i-1] in top_black_keys:    
                    pygame.draw.rect(window,green,top_keys[i-1])
                if top_keys[i+2] in top_black_keys:
                    pygame.draw.rect(window,green,top_keys[i+2])
def minor_chord_white():
    for i in range(13):
        if pressed[key_presses[i]]:
            if i <11:
                pygame.draw.rect(window,green,top_keys[i+7])
                pygame.draw.rect(window,green,top_keys[i+10])
                pygame.draw.rect(window,green,top_keys[i+14])
            else:
                pygame.draw.rect(window,green,top_keys[i-5])
                pygame.draw.rect(window,green,top_keys[i-2])
                pygame.draw.rect(window,green,top_keys[i+2])
def minor_chord_black():
    for i in range(13):
        if pressed[key_presses[i]]:
            if i<11:
                if top_keys[i+7] in top_black_keys:
                    pygame.draw.rect(window,green,top_keys[i+7])
                if top_keys[i+10] in top_black_keys:    
                    pygame.draw.rect(window,green,top_keys[i+10])
                if top_keys[i+14] in top_black_keys:
                    pygame.draw.rect(window,green,top_keys[i+14])
            else:
                if top_keys[i-5] in top_black_keys:
                    pygame.draw.rect(window,green,top_keys[i-5])
                if top_keys[i-2] in top_black_keys:    
                    pygame.draw.rect(window,green,top_keys[i-2])
                if top_keys[i+2] in top_black_keys:
                    pygame.draw.rect(window,green,top_keys[i+2])
def augmented_chord_white():
    for i in range(13):
        if pressed[key_presses[i]]:
            if i <10:
                pygame.draw.rect(window,green,top_keys[i+7])
                pygame.draw.rect(window,green,top_keys[i+11])
                pygame.draw.rect(window,green,top_keys[i+15])
            else:
                pygame.draw.rect(window,green,top_keys[i-5])
                pygame.draw.rect(window,green,top_keys[i-1])
                pygame.draw.rect(window,green,top_keys[i+3])
def augmented_chord_black():
    for i in range(13):
        if pressed[key_presses[i]]:
            if i<10:
                if top_keys[i+7] in top_black_keys:
                    pygame.draw.rect(window,green,top_keys[i+7])
                if top_keys[i+11] in top_black_keys:    
                    pygame.draw.rect(window,green,top_keys[i+11])
                if top_keys[i+15] in top_black_keys:
                    pygame.draw.rect(window,green,top_keys[i+15])
            else:
                if top_keys[i-5] in top_black_keys:
                    pygame.draw.rect(window,green,top_keys[i-5])
                if top_keys[i-1] in top_black_keys:    
                    pygame.draw.rect(window,green,top_keys[i-1])
                if top_keys[i+3] in top_black_keys:
                    pygame.draw.rect(window,green,top_keys[i+3])

white_chord_functions = [major_chord_white,minor_chord_white,augmented_chord_white]
black_chord_functions = [major_chord_black,minor_chord_black,augmented_chord_black]

chord_names = ['major_chord', 'minor_chord', 'augmented_chord']
chords_pressed = [False for i in range(len(chord_names))]

chord_dict = {}
for i in range(len(chord_names)):
    chord_dict[chord_names[i]] = chords_pressed[i]

chord_boxes = []

for i in range(3):
    box = pygame.Rect((275 + i*150), 375, 100, 50)
    chord_boxes.append(box)

while True:
    window.fill(grey)
    mouse_position = pygame.mouse.get_pos( )
    pressed = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        for i in range(len(chord_names)):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if chord_boxes[i].collidepoint(mouse_position):
                    for j in range(len(chord_names)):
                        if j != i:
                            chord_dict[chord_names[j]] = False
                    chord_dict[chord_names[i]] = not chord_dict[chord_names[i]]
            


    
    for i in range(len(chord_names)):
        if chord_dict[chord_names[i]]:
            pygame.draw.rect(window,green,chord_boxes[i])
        else:
           pygame.draw.rect(window,white,chord_boxes[i])
        pygame.draw.rect(window,black,chord_boxes[i],2)

#Bottom Keyboard Rectangles - Order of rectangle placement is: White-White Key, Green-White Key, White Key Outline, Black-Black Key, Green-Black Key, Black Key Outline

    #Bottom White-White and Green-White Rectangles
    for i in range(len(keyboard_letters)):
        if keyboard_letters[i] in bottom_white_letters:
            pygame.draw.rect(window,white,bottom_keys[i])
        if pressed[key_presses[i]] and keyboard_letters[i] in bottom_white_letters:
            pygame.draw.rect(window,green,bottom_keys[i])
    #Bottom White Outline        
    for i in range(len(keyboard_letters)):
        if keyboard_letters[i] in bottom_white_letters:
            pygame.draw.rect(window,black,bottom_keys[i],2)
    #Botttom Black-Black and Green-Black Rectangles        
    for i in range(len(keyboard_letters)):
        if keyboard_letters[i] in bottom_black_letters:
            pygame.draw.rect(window,black,bottom_keys[i])
        if pressed[key_presses[i]] and keyboard_letters[i] in bottom_black_letters:
            pygame.draw.rect(window,green,bottom_keys[i])
    #Bottom Black Outlines        
    for i in range(len(keyboard_letters)):   
        if keyboard_letters[i] in bottom_black_letters:
            pygame.draw.rect(window,black,bottom_keys[i],2)

#Bottom Keyboard Letters
    
    #Bottom White Key Letters
    bottom_white_letters_x = 292   
    for i in range (len(bottom_white_letters)):
        bottom_key_name = font.render(bottom_white_letters[i],True,black)
        window.blit(bottom_key_name,(bottom_white_letters_x,712))
        bottom_white_letters_x +=50
    
    #Bottom Black Key Letters
    bottom_black_letters_x = 315
    for i in range(len(bottom_black_letters)):
        bottom_black_key_name = font.render(bottom_black_letters[i],True,white)
        window.blit(bottom_black_key_name,(bottom_black_letters_x,655))
        bottom_black_letters_x += black_key_spacing[i]
    
#Top Keyboard Rectangles - Order of rectangle placement is: White-White Key, Green-White Key, White Key Outline, Black-Black Key, Green-Black Key, Black Key Outline

    #Top White-White Rectangles
    for i in range(25):
        if top_keys[i] in top_white_keys:
            pygame.draw.rect(window,white,top_keys[i])
    
    for i in range(len(chord_names)):
        if chord_dict[chord_names[i]]:
           white_chord_functions[i]()

         
            


    #Top White Outlines        
    for i in range(25):
        if top_keys[i] in top_white_keys:
            pygame.draw.rect(window,black,top_keys[i],2)
    
    #Top Black Rectangles
    for i in range(25):
        if top_keys[i] in top_black_keys:
            pygame.draw.rect(window, black, top_keys[i])

    for i in range(len(chord_names)):
        if chord_dict[chord_names[i]]:
           black_chord_functions[i]()

    
            
          
    

    #Top Black Outlines
    for i in range(25):
        if top_keys[i] in top_black_keys:
            pygame.draw.rect(window, black, top_keys[i],2)

#Top Keyboard Note Names
    top_white_notes_x = 140
    for i in range(len(top_white_notes)):
        top_key_name = font.render(top_white_notes[i],True,black)
        window.blit(top_key_name,(top_white_notes_x,160))
        top_white_notes_x +=50
    
    top_black_sharps_x = 160
    for i in range(len(top_sharp_notes)):
        top_sharp_name = font.render(top_sharp_notes[i],True,white)
        top_flat_name = font.render(top_flat_notes[i],True,white)
        window.blit(top_sharp_name,(top_black_sharps_x,70))
        window.blit(top_flat_name,(top_black_sharps_x,110))
        top_black_sharps_x += top_black_spacing[i]
        
    
    window.blit(font.render('Major',True,black),(288,385))
    window.blit(font.render('Minor',True,black),(438,385))
    window.blit(font.render('Aug',True,black),(595,385))


    pygame.display.flip()