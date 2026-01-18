import numpy as np
import matplotlib.pyplot as plt
size = 3
"""

musimy dodac jeszcze zakresy parametrów, tak żeby soczewki miały sens

dodatkowo wartości pod pierwiastkiem dla niektórych parametrów są ujemne.
np.clip obcina to, ale rysuje od razu prostą y=0 (nie dosłownie, bo to tablica samych 0, która wygląda jak y=0)
a tej prostej nie chcemy

"""


## soczewki dwuwypukłe
def dwuwypukle(x_1, x_2, R1, R2, ax):
    """

    :param x_1: środek okręgu prawego
    :param x_2: środek okręgu lewego
    :param R1: promień okręgu prawego
    :param R2: promień okręgu drugiego
    :param ax: parametr do rysowania odpowiedniego wykresu (to samo dla pozostałych funkcji)
    :return:
    """

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

    # Rysowanie na przekazanej osi
    ax.plot(x1, z1_upper, 'b')
    ax.plot(x1, z1_lower, 'b')
    ax.plot(x2, z2_upper, 'b')
    ax.plot(x2, z2_lower, 'b')

    #ax.set_xlim(-size, size)
    #ax.set_ylim(-size, size)

#dwuwypukle(1,-1.2,1.16,2, ax)


## soczewki dwuwklęsłe
def dwuwklesle(x_1, x_2, R1, R2, a, ax):
    """

    :param x_1: środek okręgu prawego
    :param x_2: środek okręgu lewego
    :param R1: promień okręgu prawego
    :param R2: promień okręgu lewego
    :param a: apartura
    :return:
    """
    ograniczenie_1 = x_1 - np.sqrt(R1 ** 2 - a ** 2)  # proste pozioma, w punktach przecięcia y=a i y=-a (aperture) z okręgami
    ograniczenie_2 = x_2 + np.sqrt(R2 ** 2 - a ** 2)  # proste pozioma
    prosta = (x_1 ** 2 - x_2 ** 2 - R1 ** 2 + R2 ** 2) / (2 * (x_1 - x_2))  # prosta przechodząca przez środek soczewki

    # okrąg prawy
    x1 = np.linspace(ograniczenie_2, ograniczenie_1, 500)
    z1_upper = np.sqrt(np.clip(R1 ** 2 - (x1 - x_1)**2, 0, None))
    z1_lower = -z1_upper
    # okrąg lewy
    x2 = np.linspace(ograniczenie_2, ograniczenie_1, 500)
    z2_upper = np.sqrt(np.clip(R2 ** 2 - (x2 - x_2)**2, 0, None))
    z2_lower = -z2_upper

    # Rysowanie na osi
    ax.plot(x1, z1_upper, 'b')
    ax.plot(x1, z1_lower, 'b')
    ax.plot(x2, z2_upper, 'b')
    ax.plot(x2, z2_lower, 'b')
    ax.plot(x1, np.full_like(x1, a), 'b')
    ax.plot(x2, np.full_like(x2, -a), 'b')
    #ax.set_xlim(-size, size)
    #ax.set_ylim(-size, size)

# dwuwklesle(0.7,-1.2,0.8, 0.7,0.6, ax)


def plasko_wypukle(x_1, R1, ograniczenie, ax):
    """
    Docstring for plasko_wypukle

    :param x_1: środek okręgu
    :param R1: promień okręgu
    :param ograniczenie: ograniczenie soczewki   prosta < x_1   potem w innym pliku oznaczałem jako x_plane
    """
    x1 = np.linspace(x_1 - R1, ograniczenie, 500)
    z1_upper = np.sqrt(np.clip(R1 ** 2 - (x1 - x_1)**2, 0, None))
    z1_lower = -z1_upper

    # rysowanie pionowej prostej x=prosta w zakresie soczewki:
    z_max = np.max(z1_upper)
    z_min = np.min(z1_lower)
    ax.plot([ograniczenie, ograniczenie], [z_min, z_max], 'b')

    ax.plot(x1, z1_upper, 'b')
    ax.plot(x1, z1_lower, 'b')
    #ax.set_xlim(-size, size)
    #ax.set_ylim(-size, size)

#plasko_wypukle(0.64,1.0,0.2, ax)


def plasko_wklesle(x_2, R2, a, ax):
    """
    Docstring for plasko_wklesle

    :param x_2: środek okręgu
    :param R2: promień okręgu
    :param a:  apartura   a <= |x_2|
    """
    ograniczenie = x_2 + np.sqrt(R2 ** 2 - a ** 2)  # proste pionowe

    x2 = np.linspace(ograniczenie, x_2 + R2 + (a / 2), 500)
    z2_upper = np.sqrt(np.clip(R2 ** 2 + 2 * x2 * x_2 - x2 ** 2 - x_2 ** 2, 0, None))
    z2_lower = -z2_upper

    z_max = np.max(z2_upper)
    z_min = np.min(z2_lower)
    ax.plot([x_2 + R2 + (a / 2), x_2 + R2 + (a / 2)], [z_min, z_max], 'b')

    ax.plot(x2, z2_upper, 'b')
    ax.plot(x2, z2_lower, 'b')
    ax.plot(x2, np.full_like(x2, a), 'b')
    ax.plot(x2, np.full_like(x2, -a), 'b')
    #ax.set_xlim(-size, size)
    #ax.set_ylim(-size, size)

# plasko_wklesle(-1.4,1.1,0.85, ax)
