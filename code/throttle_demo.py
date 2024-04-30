elif keys[pygame.K_UP]:
            val = 150
            val = min(val, 220)
            data = str.encode(chr(val))
            ser_throttle.write(data)
            print((ser_throttle.read()).decode())
            print("pressed up")
        elif keys[pygame.K_DOWN]:
            ser_throttle.write(b'0') #throttle 0 
            print("pressed down")