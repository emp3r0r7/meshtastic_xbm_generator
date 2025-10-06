# Meshtastic XBM Generator

This tool generates a **50x28 pixel black and white XBM bitmap** from an input image for LED or small display visualization.

---

## Requirements

- Python 3.x
- An image editor such as **Photopea**, **Photoshop**, or **GIMP**

---

## Creating the Image

1. Create a **50x28 pixel** image in **pure black and white** mode.  
   - **White pixels** = LED **off**  
   - **Black pixels** = LED **on**

2. Save the image (for example `image.png`) in the **same directory** as the Python scripts.

---

## Generating the Bitmap

Run the following command:

```bash
python3 generate_image.py
