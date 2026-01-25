import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, RadioButtons

import wykres_soczewki_v1 as lens
import liczenie_promienia as ray


def interaktywna_soczewka():
    """
    Ta funkcja rysuje soczewkę i promień
    x0 - położenie początkowe
    k - wektor kierunkowy (skierowany poziomo w stronę rosnącego x)
    x_final - punkt końca rysowania promienia
    n_air, n_lens - wartości współczynnika załamania dla powietrza i soczewki

    potem zakresy wykresu

    potem słownik z soczewkami gdzie
        'draw' rysuje soczewkę o parametrach z pliku wykres_soczewki.py
        'trace' liczy pkty przecięcia i nowy kierunek promienia

    """
    x0 = -1.6
    k = np.array([1.0, 0.0])
    x_final = 6
    n_air, n_lens = 1.0, 1.5

    fig, ax = plt.subplots(figsize=(12, 6))
    plt.subplots_adjust(left=0.3, bottom=0.25)
    ax.set_xlim(-1.2, 1.44)
    ax.set_ylim(-1.2, 1.2)
    ax.grid(False)

    # --- definicje soczewek ---
    soczewki = {
        "Dwuwklęsła": lambda ax: lens.dwuwklesle(0.7, -1.2, 0.8, 0.7, 0.6, ax), #0.7, -1.2, 0.8, 0.7, 0.6, ax #1.7, -1.2, 1.4, 0.6, 0.8, ax
        "Dwuwypukła": lambda ax: lens.dwuwypukle(1.0, -1.2, 1.16, 2.0, ax),
        "Płasko-wypukła": lambda ax: lens.plasko_wypukle(0.64, 1.0, 0.2, ax),
        "Płasko-wklęsła": lambda ax: lens.plasko_wklesle(-1.4, 1.1, 0.85, ax)
    }

    # --- funkcje promieni dla soczewek ---
    """
        p_start - punkt startowy promienia na płaszczyźnie XZ, gdzie z0 jest sterowany sliderem
        p1 - pierwszy pkt przecięcia promienia z soczewką liczony z funkcji z pliku liczenie_promieni.py
        k1 - kierunek promienia po pierwszym przecięciu promienia z soczewką liczone z pliku ^^^
        p2,k2 analogicznie, ale dla drugiego przecięcia
        zf - końcowe położenie promienia na osi Z dla x=x_final
    """
    def ray_dwuwklesla(z0):
        p_start = np.array([x0, z0])
        p1, k1 = ray.ray_on_circ(x0, z0, k, -1.2, 0.7, n_air, n_lens)
        p2, k2 = ray.ray_on_circ(p1[0], p1[1], k1, 0.7, 0.8, n_lens, n_air)
        zf = p2[1] + k2[1]/k2[0]*(x_final - p2[0])
        return p_start, p1, p2, np.array([x_final, zf])

    def ray_dwuwypukla(z0):
        p_start = np.array([x0, z0])
        p1, k1 = ray.ray_on_circ(x0, z0, k, 1.0, 1.16, n_air, n_lens)
        p2, k2 = ray.ray_on_circ(p1[0], p1[1], k1, -1.2, 2.0, n_lens, n_air)
        zf = p2[1] + k2[1]/k2[0]*(x_final - p2[0])
        return p_start, p1, p2, np.array([x_final, zf])

    def ray_plasko_wypukla(z0):
        p_start = np.array([x0, z0])
        p1, k1 = ray.ray_on_circ(x0, z0, k, 0.64, 1.0, n_air, n_lens)
        p2, k2 = ray.ray_on_plane(p1[0], p1[1], k1, 0.2, n_lens, n_air)
        zf = p2[1] + k2[1]/k2[0]*(x_final - p2[0])
        return p_start, p1, p2, np.array([x_final, zf])

    def ray_plasko_wklesla(z0):
        p_start = np.array([x0, z0])
        p1, k1 = ray.ray_on_circ(x0, z0, k, -1.4, 1.1, n_air, n_lens)
        p2, k2 = ray.ray_on_plane(p1[0], p1[1], k1, -1.4 + 1.1 + 0.85/2, n_air, n_lens)
        zf = p2[1] + k2[1]/k2[0]*(x_final - p2[0])
        return p_start, p1, p2, np.array([x_final, zf])

    # --- update wykresu ---
    def update(val=None):
        """
        z0 - aktualna wartość z slidera
        ax.cla() - czyszczenie osi, aby narysować nowy wykres
        nazwa - którą soczewkę wybrano z przycisków radio

        :return:
        """
        z0 = slider.val
        ax.cla()
        ax.set_xticks([])
        ax.set_yticks([])

        ax.set_xlim(-1.2, 1.44)
        ax.set_ylim(-1.2, 1.2)
        ax.grid(False)


        # oś optyczna
        ax.axhline(y=0, color='blue', linewidth=1.2, linestyle='-')

        nazwa = radio.value_selected
        # rysujemy soczewkę
        soczewki[nazwa](ax)

        # rysujemy promień
        try:
            if nazwa == "Dwuwklęsła":
                p0, p1, p2, pf = ray_dwuwklesla(z0)
            elif nazwa == "Dwuwypukła":
                p0, p1, p2, pf = ray_dwuwypukla(z0)
            elif nazwa == "Płasko-wypukła":
                p0, p1, p2, pf = ray_plasko_wypukla(z0)
            elif nazwa == "Płasko-wklęsła":
                p0, p1, p2, pf = ray_plasko_wklesla(z0)

            ax.plot([p0[0], p1[0]], [p0[1], p1[1]], 'r', linewidth=1.5)
            ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'r', linewidth=1.5)
            ax.plot([p2[0], pf[0]], [p2[1], pf[1]], 'r', linewidth=1.5)
        except Exception as e:
            print("Błąd w rysowaniu promienia:", e)

        fig.canvas.draw_idle()

    # --- slider ---
    # Zmienia położenie promienia na osi Z
    ax_slider = plt.axes([0.35, 0.1, 0.5, 0.03])
    slider = Slider(ax_slider, "z0", -0.32, 0.32, valinit=0.0)

    # --- radio buttons ---
    # do wyboru soczewki
    ax_radio = plt.axes([0.05, 0.4, 0.2, 0.25])
    radio = RadioButtons(ax_radio, list(soczewki.keys()))

    radio.on_clicked(lambda label: update())
    slider.on_changed(update)

    update()
    plt.show()

# uruchomienie wszystkiego
interaktywna_soczewka()
