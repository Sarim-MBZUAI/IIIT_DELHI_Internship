from re import I
import pygame
import serial
import time

flag = 1


def pygameSetup():
    pygame.init()
    screen = pygame.display.set_mode((1400, 70))

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render(
            "SPACE/b=FRONT BREAK || 5/.=REAR BREAK || 0=reverse REAR break || Leftkey->left!", 1, (10, 10, 10))
        textpos = text.get_rect(centerx=background.get_width()/2)
        background.blit(text, textpos)

    screen.blit(background, (0, 0))
    pygame.display.flip()


def main():
    pygameSetup()
    initialized = False

    while not initialized:
        try:
            # open('COM8')
            ser = serial.Serial('COM4', 9600)  # steer and break arduino port
            # ser_throttle = serial.Serial("COM6", 9600)  # throttle arduino port
            initialized = True
            print("serial up")
            # print(ser.read())
        except:
            # time.sleep(500)
            print("waiting for serial")

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE] or (keys[pygame.K_LCTRL] and keys[pygame.K_c]):
            ser.write(b's')
            time.sleep(1)
            return
        elif (keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_KP4]):
            ser.write(b'r')
            print("pressed left")

        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[pygame.K_KP6]):
            ser.write(b'l')
            print("pressed right")

        elif (keys[pygame.K_SPACE] or keys[pygame.K_b]):  # front break
            ser.write(b'b')
            print("pressed space")

        elif(keys[pygame.K_n]):
            ser.write(b'B')
            print("n -> reverse front break")

        elif(keys[pygame.K_KP_PERIOD] or keys[pygame.K_KP5]):  # rear break
            ser.write(b'z')
            print("pressed period/5")

        elif(keys[pygame.K_KP0] or keys[pygame.K_KP_PLUS]):
            ser.write(b'Z')
            print("pressed keypad 0")

        # elif keys[pygame.K_UP]:
        #     flag = 1
        #     val = "140"
        #     # val = 140
        #     # val = min(val, 220)
        #     # data = str.encode(chr(val))
        #     data = val.encode('utf-8')
        #     print("sending data", data)
        #     print("data", (data.decode()))
        #     ser_throttle.write(data)
        #     rec = ser_throttle.read()
        #     print(rec)
        #     print("Rec", ord(rec.decode()))
        #     print("pressed up")
        # elif keys[pygame.K_DOWN]:
        #     ser_throttle.write(b'0')  # throttle 0
        #     print("pressed down")
        elif(keys[pygame.K_KP_ENTER]):
            ser.write(b's')
            
        elif((event.type == pygame.KEYUP) and flag):

            # time.sleep(3)
            ser.write(b's')
            time.sleep(1)
            flag = 0
            continue

        else:
            ser.write(b's')  
            flag = 1


if __name__ == '__main__':
    main()
