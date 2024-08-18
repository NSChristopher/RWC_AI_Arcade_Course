import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
import cv2

def display_video(frames, interval=50, scale=0.5):
    # Downscale the frames
    scaled_frames = [cv2.resize(frame, (0, 0), fx=scale, fy=scale) for frame in frames]
    
    fig, ax = plt.subplots()
    ax.axis('off')
    img = ax.imshow(scaled_frames[0])
    
    def update(frame):
        img.set_array(frame)
        return [img]
    
    ani = FuncAnimation(fig, update, frames=scaled_frames, interval=interval, blit=True)
    plt.close(fig)  # Prevents the static image from displaying
    return ani


def plot_q_values_grid(q_table, map_size=8):
    q_table_max_values = np.max(q_table, axis=1).reshape(map_size, map_size)
    q_table_best_actions = np.argmax(q_table, axis=1).reshape(map_size, map_size)
    directions = {0: "←", 1: "↓", 2: "→", 3: "↑"}
    q_table_directions = np.empty(q_table_best_actions.flatten().shape, dtype=str)
    eps = np.finfo(float).eps
    for inx, val in enumerate(q_table_best_actions.flatten()):
        if q_table_max_values.flatten()[inx] > eps:
            q_table_directions[inx] = directions[val]
        else:
            q_table_directions[inx] = ""
    q_table_directions = q_table_directions.reshape(map_size, map_size)

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.heatmap(
        q_table_max_values,
        annot=q_table_directions,
        fmt="",
        ax=ax,
        cmap=sns.color_palette("Blues", as_cmap=True),
        linewidths=0.7,
        linecolor="black",
        xticklabels=[],
        yticklabels=[],
        annot_kws={"fontsize": "xx-large"},
    ).set(title="Learned Q-values\nArrows represent best action")
    
    for _, spine in ax.spines.items():
        spine.set_visible(True)
        spine.set_linewidth(0.7)
        spine.set_color("black")

    img_title = f"frozenlake_q_values_{map_size}x{map_size}.png"
    fig.savefig(img_title, bbox_inches="tight")
    plt.show()