# created by Risegarro Klamactus for the aoe2 wiki
from pathlib import Path
from PIL import Image

p = Path(r"/path/to/your/unit/png/directory")



png_files = sorted(p.glob("*.png"))
anim_length = (len(png_files) - 1) // 16
total_valid_frames = anim_length * 16
png_files = png_files[:total_valid_frames] 

for chunk_index in range(0, len(png_files), anim_length):
    chunk_files = png_files[chunk_index:chunk_index + anim_length]
    if not chunk_files:
        break

    images = []
    minx = miny = maxx = maxy = None

    for file in chunk_files:
        with Image.open(file).convert("RGBA") as img:
            images.append(img)
            pixels = img.load()
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

    cropped_images = [img.crop((minx, miny, maxx, maxy)) for img in images]
    output_path = p.parent / f"{p.name}_{chunk_index // anim_length}.gif"
    cropped_images[0].save(
        output_path,
        "GIF",
        save_all=True,
        append_images=cropped_images[1:],
        duration=20,
        loop=0,
        disposal=2,
        transparency=0,
    )

print("GIF generation complete.")

# urumi attack = 45
# mango attack = 60
# idle camel = 60
