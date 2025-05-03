# created by Risegarro Klamactus for the aoe2 wiki
from pathlib import Path
from PIL import Image

p = Path(r"/path/to/your/unit/png/directory")
bounds = (50, 50, 350, 250)  # left, top, right, bottom
images = []
for file in p.glob("*.png"):
    with Image.open(file) as img:
        images.append(img.crop(bounds))

if images:
    images[0].save(p.parent / f"{p.name}.gif", "GIF", save_all=True, append_images=images[1:], duration=20, loop=0, disposal=2, transparency=0)
else:
    print("No PNGs found")
