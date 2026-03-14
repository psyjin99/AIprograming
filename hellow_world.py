import numpy as np
import matplotlib.pyplot as plt

def generate_heart_image():
    # Create an array of values for t from 0 to 2*pi
    t = np.linspace(0, 2 * np.pi, 1000)

    # Parametric equations for a beautiful heart shape
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

    # Create the plot figure
    plt.figure(figsize=(8, 8), facecolor='white')
    
    # Plot and fill the heart with red color
    plt.plot(x, y, color='crimson', linewidth=2)
    plt.fill(x, y, color='crimson')

    # Add the text "hi_hello" in the center of the heart
    plt.text(0, 0, 'hi_hello', fontsize=36, color='white', 
             fontweight='bold', ha='center', va='center')

    # Remove axes and borders for a clean image
    plt.axis('off')
    
    # Ensure equal aspect ratio so the heart isn't distorted
    plt.gca().set_aspect('equal')

    # Save the generated image as a PNG file
    output_filename = 'heart_hi_hello.png'
    plt.savefig(output_filename, bbox_inches='tight', dpi=300, facecolor='white')
    print(f"Success! The heart image has been saved as '{output_filename}'")

    # Display the image window
    plt.show()

if __name__ == "__main__":
    generate_heart_image()
