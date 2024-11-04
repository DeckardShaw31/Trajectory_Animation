import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from IPython.display import HTML

def animate_trajectory(v0, a):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 1.2 * 0.5 * a * v0 * 5**2) 
    ax.set_ylim(0, 1.2 * v0 * 5) 
    ax.set_xlabel('x(t) (m)')
    ax.set_ylabel('y(t) (m)')
    ax.set_title('Real-Time Animation of Trajectory')
    ax.grid(True)
    
    # Create a line object that will be updated during the animation
    line, = ax.plot([], [], 'b', linewidth=2)

    # Time array
    t = np.linspace(0, 5, 100)

    # Animation function
    def update(frame):
        x = 0.5 * a * v0 * t[:frame]**2  
        y = v0 * t[:frame]  
        line.set_data(x, y)
        return line,

    # Create the animation
    ani = FuncAnimation(fig, update, frames=len(t), interval=50, blit=True)

    # Save the animation as a video and display it
    plt.close(fig)  # Close the figure to prevent double display
    return HTML(ani.to_jshtml())

v0 = float(input("Nhập vận tốc ban đầu của khí cầu (m/s): "))
a = float(input("Nhập gia tốc a (m/s^2): "))

animate_html = animate_trajectory(v0, a)
display(animate_html)