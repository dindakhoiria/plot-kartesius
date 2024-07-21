import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

# Fungsi untuk konversi dari Kartesius ke Polar
def cartesian_to_polar(x, y):
    r = np.sqrt(x**2 + y**2)
    theta = np.arctan2(y, x)
    return r, np.degrees(theta)

# Fungsi untuk update plot
def update_plot(event):
    try:
        x = float(text_box_x.text)
        y = float(text_box_y.text)
        r, theta = cartesian_to_polar(x, y)
        text_box_r.set_val(f"{r:.2f}")
        text_box_theta.set_val(f"{theta:.2f}")
        
        ax_cartesian.cla()
        ax_polar.cla()

        # Plot Kartesius
        ax_cartesian.set_title("Cartesian Coordinates")
        ax_cartesian.set_xlim(-10, 10)
        ax_cartesian.set_ylim(-10, 15)
        ax_cartesian.plot([0, x], [0, y], 'b--')
        ax_cartesian.plot(x, y, 'bo')
        ax_cartesian.text(x, y, f"A ({x:.2f}, {y:.2f})")

        # Plot Polar
        ax_polar.set_title("Polar Coordinates")
        ax_polar.set_ylim(0, 10)
        ax_polar.set_yticks(np.arange(0, 11, 2))
        ax_polar.plot([0, np.radians(theta)], [0, r], 'b--')
        ax_polar.plot(np.radians(theta), r, 'bo')
        ax_polar.text(np.radians(theta), r, f"A")
        
        plt.draw()
    except ValueError:
        pass

# Inisialisasi plot
fig, (ax_cartesian, ax_polar) = plt.subplots(1, 2, figsize=(10, 5), subplot_kw={'polar': [False, True]})

# Inisialisasi textbox
ax_box_x = plt.axes([0.1, 0.02, 0.1, 0.05])
text_box_x = TextBox(ax_box_x, 'X:', initial="0")
ax_box_y = plt.axes([0.3, 0.02, 0.1, 0.05])
text_box_y = TextBox(ax_box_y, 'Y:', initial="0")
ax_box_r = plt.axes([0.5, 0.02, 0.1, 0.05])
text_box_r = TextBox(ax_box_r, 'r:', initial="0")
ax_box_theta = plt.axes([0.7, 0.02, 0.1, 0.05])
text_box_theta = TextBox(ax_box_theta, 'θ:', initial="0")

# Mengatur textbox 'r' dan 'θ' agar hanya readonly
text_box_r.set_active(False)
text_box_theta.set_active(False)

# Menghubungkan textbox dengan fungsi update_plot
text_box_x.on_submit(update_plot)
text_box_y.on_submit(update_plot)

# Plot awal
update_plot(None)

plt.show()