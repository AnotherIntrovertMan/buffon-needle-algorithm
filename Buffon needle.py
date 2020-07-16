#Naufal Zahid Yoga P
#1301170345

import math
import random

a = 3 #banyak percobaan
N = 10000000 #banyak jarum
l = 3 #panjang jarum
d = 5 #diameter garis
pi_eksak = math.pi


i = 0
while (i < a):
    hasil = 0
    Q = 0 #hit
    for j in range(N):
        #pembangkitan nilai acak
        xi= random.uniform(0,d)
        teta = random.uniform(0,math.pi/2)
        x = l*math.cos(teta)
        if (xi < x):
            Q+=1
    hasil = (2.0*l*N)/(d*Q)
    print("Percobaan",i+1,": Nilai Pi = ",hasil,"| Error = ",abs(hasil - pi_eksak))
    i+=1
