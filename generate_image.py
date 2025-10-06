from PIL import Image
import numpy as np

input_path = "pic.png"  # deve essere 50x28, 1-bit
output_path = "icon_bits.c"
array_name = "icon_bits"

img = Image.open(input_path).convert("1")  # forza 1-bit
w, h = img.size
pixels = np.array(img, dtype=np.uint8)

pixels = (pixels == 0).astype(np.uint8)

bytes_per_row = (w + 7) // 8
data = []

for y in range(h):
    for bx in range(bytes_per_row):
        byte = 0
        for b in range(8):
            x = bx * 8 + b
            if x < w:
                bit = pixels[y, x]
                byte |= (bit << b)
        data.append(byte)

lines = []
lines.append(f"#define icon_width {w}")
lines.append(f"#define icon_height {h}")
lines.append(f"static uint8_t {array_name}[] = {{")

for i in range(0, len(data), 12):
    chunk = data[i:i+12]
    hexes = ", ".join(f"0x{b:02X}" for b in chunk)
    lines.append("    " + hexes + ",")

lines.append("};\n")

with open(output_path, "w") as f:
    f.write("\n".join(lines))

print(f"File generated: {output_path}")
print(f"Dimensioni: {w}x{h}, bytes totali: {len(data)}")
