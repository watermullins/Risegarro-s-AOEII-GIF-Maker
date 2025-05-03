# created by Risegarro Klamactus for the aoe2 wiki
from pathlib import Path
from PIL import Image

p = Path(r"/path/to/your/unit/png/directory") 


minx, miny, maxx, maxy = (20, 20, 250, 170)  # left, top, right, bottom, has to be set manually and will be used if has_bounds is True
has_bounds = False  # It will auto-detect and crop if this is False, set it to True to use above values
if not has_bounds:
    minx = miny = maxx = maxy = None


images = []
for file in p.glob("*.png"):
    csv = file.with_suffix(".csv").with_stem(file.stem + ".png")
    with Image.open(file).convert("RGBA") as img:
        images.append(img)
        pixels = img.load()
        if not has_bounds:
            for y in range(img.size[1]):
                for x in range(img.size[0]):
                    if pixels[x, y][3] != 0:
                        if minx is None:
                            minx = x - 1
                        if miny is None:
                            miny = y - 1
                        if maxx is None:
                            maxx = x + 1
                        if maxy is None:
                            maxy = y + 1
                        minx = min(minx, x - 1)
                        miny = min(miny, y - 1)
                        maxx = max(maxx, x + 1)
                        maxy = max(maxy, y + 1)

            
for i, img in enumerate(images):
    images[i] = img.crop((minx, miny, maxx, maxy))


images[0].save(p.parent / f"{p.name}.gif", "GIF", save_all=True, append_images = images[1:], duration=20, loop=0, disposal=2, transparency=0)
