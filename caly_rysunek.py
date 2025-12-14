import numpy as np
import matplotlib.pyplot as plt
import wykres_soczewki_v1 as lens
import liczenie_promienia as ray


# ### D W U W Y P U K Ł E :
# x0, z0 = -2.0, 0.5         # punkt startow
# k = np.array([1.0, 0.0])   # kierunek początkowy
# x_1, R1 = 1, 1.16
# x_2, R2 = -1.2, 2
# n_air, n_lens = 1.0, 1.5   # współczynniki załamania

# # punkt startowy i punkt przecięcia
# p_start = np.array([x0, z0])
# # pierwszy odcinek: lewa powierzchnia soczewki
# p_hit1, k_out1 = ray.ray_on_circ(x0, z0, k, x_1, R1, n_air, n_lens)

# # drugi odcinek: prawa powierzchnia soczewki
# p_hit2, k_out2 = ray.ray_on_circ(p_hit1[0], p_hit1[1], k_out1, x_2, R2, n_lens, n_air)

# # rysowanie
# plt.figure(figsize=(6,6))
# lens.dwuwypukle(x_1, x_2, R1, R2)
# # pierwszy odcinek: od startu do lewej powierzchni
# ray.draw_ray(p_start, p_hit1)

# # drugi odcinek: od lewej powierzchni do prawej
# ray.draw_ray(p_hit1, p_hit2)

# # trzeci odcinek: od prawej powierzchni do powietrza
# x_final = 6
# z_final = p_hit2[1] + k_out2[1]/k_out2[0] * (x_final - p_hit2[0])
# ray.draw_ray(p_hit2, np.array([x_final, z_final]))




# ### P Ł A S K O - W Y P U K Ł E:
# x0, z0 = -2.0, 0.3
# k = np.array([1.0, 0.0])
# x_1, R1 = 0.64, 1.0
# x_plane = 0.2
# n_air, n_lens = 1.0, 1.5

# p_start = np.array([x0, z0])
# p_hit1, k_out1 = ray.ray_on_circ(x0, z0, k, x_1, R1, n_air, n_lens)
# p_hit2, k_out2 = ray.ray_on_plane(p_hit1[0], p_hit1[1], k_out1, x_plane, n_air, n_lens)

# plt.figure(figsize=(6,6))
# lens.plasko_wypukle(x_1, R1, x_plane)
# ray.draw_ray(p_start, p_hit1)
# ray.draw_ray(p_hit1, p_hit2)
# x_final = 6
# z_final = p_hit2[1] + k_out2[1]/k_out2[0] * (x_final - p_hit2[0])
# ray.draw_ray(p_hit2, np.array([x_final, z_final]))



# ### P Ł A S K O - W K L Ę S Ł E:
# x0, z0 = -1.6, 0.3
# k = np.array([1.0, 0.0])
# x_2, R2 = -1.4, 1.1
# a = 2.0
# x_plane = x_2 + R2 + a/2
# n_air, n_lens = 1.0, 1.5

# p_start = np.array([x0, z0])
# p_hit1, k_out1 = ray.ray_on_circ(x0, z0, k, x_2, R2, n_air, n_lens)
# p_hit2, k_out2 = ray.ray_on_plane(p_hit1[0], p_hit1[1], k_out1, x_plane, n_air, n_lens)

# plt.figure(figsize=(6,6))
# lens.plasko_wklesle(x_2, R2, x_plane)
# ray.draw_ray(p_start, p_hit1)
# ray.draw_ray(p_hit1, p_hit2)
# x_final = 6
# z_final = p_hit2[1] + k_out2[1]/k_out2[0] * (x_final - p_hit2[0])
# ray.draw_ray(p_hit2, np.array([x_final, z_final]))



### D W U W K L Ę S Ł E:
x0, z0 = -1.6, -0.23
k = np.array([1.0, 0.0])
x_1, R1 = 0.7, 0.8
x_2, R2 = -1.2, 0.7
a = 0.6
n_air, n_lens = 1.0, 1.5

p_start = np.array([x0, z0])
p_hit1, k_out1 = ray.ray_on_circ(x0, z0, k, x_2, R2, n_air, n_lens)
p_hit2, k_out2 = ray.ray_on_circ(p_hit1[0], p_hit1[1], k_out1, x_1, R1, n_lens, n_air)

plt.figure(figsize=(6,6))
lens.dwuwklesle(x_1, x_2, R1, R2, a)
ray.draw_ray(p_start, p_hit1)
ray.draw_ray(p_hit1, p_hit2)
x_final = 6
z_final = p_hit2[1] + k_out2[1]/k_out2[0] * (x_final - p_hit2[0])
ray.draw_ray(p_hit2, np.array([x_final, z_final]))




plt.xlim(-3,3)
plt.ylim(-3,3)
plt.grid(False)
plt.show()