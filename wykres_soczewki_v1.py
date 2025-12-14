import numpy as np
import matplotlib.pyplot as plt
size = 3
"""
Dodanie aparture tam gdzie brakuje

musimy dodac jeszcze zakresy parametrów, tak żeby soczewki miały sens

dodatkowo wartości pod pierwiastkiem dla nie których parametrów są ujemne.
np.clip obcina to, ale rysuje od razu prostą y=0 (nie dosłownie, bo to tablica samych 0, która wygląda jak y=0)
a tej prostej nie chcemy

wypełnienie soczewek jeszcze nie działa. myślę czy nie użyć fill_between() zamiast fill_betweenx()
"""


## soczewki dwuwypukłe
def dwuwypukle(x_1, x_2, R1, R2):

    prosta = (x_1 ** 2 - x_2 ** 2 - R1 ** 2 + R2 ** 2) / (2 * (x_1 - x_2))  # prosta w punktach przecięcia dwóch okręgów
    # print('prosta', prosta)

# równania soczewki nr 1 (okrag prawy)
    x1 = np.linspace(x_1 - R1, prosta, 500)
    z1_upper = np.sqrt(R1 ** 2 -(x1-x_1)**2 )   # górna półkula
    z1_lower = -z1_upper                        # dolna półkula

# równania soczewki nr 2 (okrag lewy)
    x2 = np.linspace(prosta, x_2 + R2, 500)
    z2_upper = np.sqrt(R2 ** 2 - (x2 - x_2)**2) # górna półkula
    z2_lower = -z2_upper                        # dolna półkula

    # plt.figure(figsize=(6, 6))
    #plt.fill_betweenx(z+z_c, x_lower, x_upper, color='skyblue')
    plt.plot(x1, z1_upper, 'b')
    plt.plot(x1, z1_lower, 'b')
    plt.plot(x2, z2_upper, 'b')
    plt.plot(x2, z2_lower, 'b')

    plt.xlim(-size, size)
    plt.ylim(-size, size)

#dwuwypukle(1,-1.2,1.16,2)


## soczewki dwuwklęsłe
def dwuwklesle(x_1, x_2, R1, R2, a): # a - aperture
    ograniczenie_1 = (
                x_1 - np.sqrt(R1 ** 2 - a ** 2))                            # proste pionowa, w punktach przecięcia y=a i y=-a (aperture) z okręgami
    ograniczenie_2 = (
                x_2 + np.sqrt(R2 ** 2 - a ** 2))                            # proste pionowa, w punktach przecięcia y=a i y=-a (aperture) z okręgami
    prosta = (x_1 ** 2 - x_2 ** 2 - R1 ** 2 + R2 ** 2) / (2 * (x_1 - x_2))  # prosta przechodząca przez środek soczewki

# okrąg prawy
    x1 = np.linspace(ograniczenie_2, ograniczenie_1, 500)
    z1_upper = np.sqrt(np.clip(R1 ** 2 - (x1 - x_1)**2))
    z1_lower = -z1_upper
#okrąg lewy
    x2 = np.linspace(ograniczenie_2, ograniczenie_1, 500)
    z2_upper = np.sqrt(np.clip(R2 ** 2 - (x2 - x_2)**2))
    z2_lower = -z2_upper

    # plt.figure(figsize=(6, 6))
    # plt.fill_betweenx(z1_upper, x1, x1, where=z1_upper>=z1_lower, color='lightblue', alpha=0.5) ## jeszcze nie działa
    plt.plot(x1, z1_upper, 'b')
    plt.plot(x1, z1_lower, 'b')
    plt.plot(x2, z2_upper, 'b')
    plt.plot(x2, z2_lower, 'b')
    plt.plot(x1, np.full_like(x1, a), 'b')
    plt.plot(x2, np.full_like(x2, -a), 'b')
    plt.xlim(-size, size)
    plt.ylim(-size, size)

# dwuwklesle(0.7,-1.2,0.8, 0.7,0.6)

def plasko_wypukle(x_1, R1, ograniczenie):
    """
    Docstring for plasko_wypukle

    :param x_1: Description
    :param R1: Description
    :param ograniczenie: ograniczenie soczewki   prosta < x_1   potem w innym pliku oznaczałem jako x_plane
    """
    x1 = np.linspace(x_1 - R1, ograniczenie, 500)
    z1_upper = np.sqrt(np.clip(R1 ** 2 - (x1 - x_1)**2, 0, None))
    z1_lower = -z1_upper

    # plt.figure(figsize=(6, 6))
    # plt.fill_betweenx(z+z_c, x_lower, x_upper, color='skyblue')
# rysowanie pionowej prostej x=prosta w zakresie soczewki:
    z_max = np.max(z1_upper)  # zakresy prostej ograniczającej soczewkę - płaska cześć soczewki
    z_min = np.min(z1_lower)
    plt.plot([ograniczenie, ograniczenie], [z_min, z_max], 'b')

    plt.plot(x1, z1_upper, 'b')
    plt.plot(x1, z1_lower, 'b')
    plt.xlim(-size, size)
    plt.ylim(-size, size)

#plasko_wypukle(0.64,1.0,0.2)

def plasko_wklesle(x_2, R2, a):
    """
    Docstring for plasko_wklesle

    :param x_2: Description
    :param R2: Description
    :param a:     a <= |x_2|

    x = x_2 + R2 + a/2

    """
    ograniczenie = (
                x_2 + np.sqrt(R2 ** 2 - a ** 2))  # proste pionowe, w punktach przecięcia y=a i y=-a (aperture) z okręgami

    x2 = np.linspace(ograniczenie, x_2 + R2 + (a / 2), 500)
    # z2_upper=np.sqrt(R2**2+2*x2*x_2-x2**2-x_2**2)
    z2_upper = np.sqrt(np.clip(R2 ** 2 + 2 * x2 * x_2 - x2 ** 2 - x_2 ** 2, 0, None))
    z2_lower = -z2_upper

    # plt.figure(figsize=(6, 6))
    # plt.fill_betweenx(z+z_c, x_lower, x_upper, color='skyblue')
    # rysowanie pionowej prostej x=ograniczenie w zakresie soczewki:
    z_max = np.max(z2_upper)  # zakresy prostej ograniczającej soczewkę - płaska cześć soczewki
    z_min = np.min(z2_lower)
    plt.plot([x_2 + R2 + (a / 2), x_2 + R2 + (a / 2)], [z_min, z_max], 'b')

    plt.plot(x2, z2_upper, 'b')
    plt.plot(x2, z2_lower, 'b')
    plt.plot(x2, np.full_like(x2, a), 'b')
    plt.plot(x2, np.full_like(x2, -a), 'b')
    plt.xlim(-size, size)
    plt.ylim(-size, size)

# plasko_wklesle(-1.4,1.1,0.85)
