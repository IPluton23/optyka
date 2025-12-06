import numpy as np
import matplotlib.pyplot as plt


## soczewki dwuwypukłe
def dwuwypukle(x_1, x_2, R1, R2):
    z=0
    size=3

    prosta = (x_1**2-x_2**2-R1**2+R2**2)/(2*(x_1-x_2))  # prosta w punktach przecięcia dwóch okręgów
    # print('prosta', prosta)

    # równania soczewki nr 1 (prawej)

    x1=np.linspace(x_1-R1, prosta, 500)
    z1_upper=np.sqrt(R1**2+2*x1*x_1-x1**2-x_1**2)
    z1_lower=-np.sqrt(R1**2+2*x1*x_1-x1**2-x_1**2)

    # równania soczewki nr 2 (lewej)

    x2=np.linspace(prosta, x_2+R2, 500)
    z2_upper=np.sqrt(R2**2+2*x2*x_2-x2**2-x_2**2)
    z2_lower=-np.sqrt(R2**2+2*x2*x_2-x2**2-x_2**2)



    plt.figure(figsize=(6,6))
    # plt.fill_betweenx(z+z_c, x_lower, x_upper, color='skyblue')
    plt.plot(x1, z1_upper, 'b')
    plt.plot(x1, z1_lower, 'b')
    plt.plot(x2, z2_upper, 'b')
    plt.plot(x2, z2_lower, 'b')

    plt.xlim(-size, size)
    plt.ylim(-size, size)
    plt.gca().set_aspect('equal')
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('z')
    plt.show()


# dwuwypukle(1,-1.2,1.16,2)

## soczewki dwuwklęsłe

def dwuwklesle(x_1, x_2, R1, R2, a):
    z=0
    size=3
    y=a
    ograniczenie_1=(x_1-np.sqrt(R1**2-a**2))    # proste x, w punktach przecięcia y=a i y=-a (aperture) z okręgami
    ograniczenie_2=(x_2+np.sqrt(R2**2-a**2))    # proste x, w punktach przecięcia y=a i y=-a (aperture) z okręgami
    prosta = (x_1**2-x_2**2-R1**2+R2**2)/(2*(x_1-x_2))      # prosta przechodząca przez środek soczewki
    x1=np.linspace(ograniczenie_2, ograniczenie_1, 500)
    z1_upper=np.sqrt(R1**2+2*x1*x_1-x1**2-x_1**2)
    z1_lower=-np.sqrt(R1**2+2*x1*x_1-x1**2-x_1**2)

    x2=np.linspace(ograniczenie_2, ograniczenie_1, 500)
    z2_upper=np.sqrt(R2**2+2*x2*x_2-x2**2-x_2**2)
    z2_lower=-np.sqrt(R2**2+2*x2*x_2-x2**2-x_2**2)

    plt.figure(figsize=(6,6))
    # plt.fill_betweenx(z1_upper, x1, x1, where=z1_upper>=z1_lower, color='lightblue', alpha=0.5) ## jeszcze nie działa
    plt.plot(x1, z1_upper, 'b')
    plt.plot(x1, z1_lower, 'b')
    plt.plot(x2, z2_upper, 'b')
    plt.plot(x2, z2_lower, 'b')
    plt.plot(x1, np.full_like(x1, y), 'b')
    plt.plot(x2, np.full_like(x2, -y), 'b')
    plt.xlim(-size, size)
    plt.ylim(-size, size)
    plt.gca().set_aspect('equal')
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('z')
    plt.show()

# dwuwklesle(0.7,-1.2,0.8,-0.7,0.6)

def plasko_wypukle():
    return 0

def plasko_wklesle():
    return 0