import numpy as np
import matplotlib.pyplot as plt

def ray_on_circ(x0, z0, k, x_c, R, n1, n2):
    """
    Oblicza punkt przecięcia promienia o kierunku k z okręgiem
    i zwraca nowy kierunek po załamaniu.

    :param x0, z0: punkt startowy promienia
    :param k: kierunek promienia (wektor 2D, np. np.array([kx, kz]))
    :param x_c: środek okręgu (x, 0)
    :param R: promień okręgu
    :param n1: współczynnik załamania w ośrodku wejściowym
    :param n2: współczynnik załamania w ośrodku wyjściowym
    :return: p_hit (punkt przecięcia), k_out (wektor kierunku po załamaniu)
    """

    # równanie parametryczne promienia: r(t) = (x0, z0) + t*k ,  równanie okręgu: (x - x_c)**2 + z**2 = R**2 ,  podstawiamy: (x0 + t*k[0] - x_c)**2 + (z0 + t*k[1])**2 = R**2
    # t to nie czas, to liczba mowiąca jak daleko wzdłuż promienia jesteś, czyli w punkcie startowym mamy t=0. jak promień leci w prawo to t>0 a jak w lewo to t< 0
    dx = x0 - x_c   #ile punkt startowy jest przesunięty w osi x od środka okręgu
    dz = z0     #   ile jest w osi z (bo środek ma z = 0)
    # z równania kwadratowego z komentarza wyżej mamy współczynniki:
    a = k[0]**2 + k[1]**2
    b = 2*(dx*k[0] + dz*k[1])
    c = dx**2 + dz**2 - R**2

    delta = b**2 - 4*a*c
    if delta < 0:
        raise ValueError("Brak przecięcia promienia z okręgiem")

    # wybieramy najmniejszy dodatni t (najbliższe przecięcie w kierunku k)
    t1 = (-b + np.sqrt(delta)) / (2*a)
    t2 = (-b - np.sqrt(delta)) / (2*a)
    # t_all = np.array([t1, t2])
    # t = t_all[np.argmin(np.abs(t_all))]
    t_candidates = np.array([t1, t2])
    t_candidates = t_candidates[t_candidates > 1e-9]

    if len(t_candidates) == 0:
        raise ValueError("Przecięcie tylko za promieniem")

    t = np.min(t_candidates)


    # punkt przecięcia
    p_hit = np.array([x0 + t*k[0], z0 + t*k[1]])

    # normalna w punkcie przecięcia
    n = np.array([p_hit[0] - x_c, p_hit[1]])
    n = n / np.linalg.norm(n)

    if np.dot(k, n) > 0:
        n = -n


    # kąt padania i załamania
    cos_theta_i = -np.dot(k, n)
    sin2_theta_t = (n1/n2)**2 * (1 - cos_theta_i**2)    # sin kwadrat theta

    if sin2_theta_t > 1.0:
        raise ValueError("Całkowite wewnętrzne odbicie")
    
    cos_theta_t = np.sqrt(1 - sin2_theta_t)
    k_out = (n1/n2)*k + ((n1/n2)*cos_theta_i - cos_theta_t)*n
    k_out = k_out / np.linalg.norm(k_out)

    return p_hit, k_out


def draw_ray(p_start, p_hit):
    plt.plot([p_start[0], p_hit[0]], [p_start[1], p_hit[1]], 'r', linewidth=1.5)


def ray_on_plane(x0, z0, k, x_plane, n1, n2):
    """
    Docstring for ray_on_plane
    
    :param x0: pkt startowy
    :param z0: -||-
    :param k: kiernek
    :param x_plane: równanie płaszczyzny - położenie płaszczyzny
    :param n1: współczynnik załamania w ośrodku wejściowym
    :param n2: współczynnik załamania w ośrodku wyjściowym
    """

    # parametr t przecięcia z prostą x=x_plane
    if k[0] == 0:
        raise ValueError("Promień równoległy do płaszczyzny")

    t = (x_plane - x0) / k[0]

    if t < 0:
        raise ValueError("Płaszczyzna za promieniem")

    # punkt przecięcia
    p_hit = np.array([x_plane, z0 + t*k[1]])

    # normalna do płaszczyzny
    n = np.array([1.0, 0.0])
    if k[0] > 0:
        n = -n

    # kąty
    cos_theta_i = -np.dot(k, n)

    sin2_theta_t = (n1/n2)**2 * (1 - cos_theta_i**2)
    if sin2_theta_t > 1.0:
        raise ValueError("Całkowite wewnętrzne odbicie")

    cos_theta_t = np.sqrt(1 - sin2_theta_t)

    k_out = (n1/n2)*k + ((n1/n2)*cos_theta_i - cos_theta_t)*n
    k_out = k_out / np.linalg.norm(k_out)

    return p_hit, k_out
