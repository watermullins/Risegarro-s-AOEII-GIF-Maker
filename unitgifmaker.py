# created by Risegarro Klamactus for the aoe2 wiki
from pathlib import Path
from PIL import Image

p = Path(__file__).resolve()
frames_dir = p.parent / "frames"

png_files = sorted(frames_dir.glob("*.png"))
anim_length = (len(png_files) - 1) // 16
total_valid_frames = anim_length * 16
png_files = png_files[:total_valid_frames] 

for chunk_index in range(0, len(png_files), anim_length):
    chunk_files = png_files[chunk_index:chunk_index + anim_length]
    if not chunk_files:
        break

    images = []
    minx = miny = float('inf')
    maxx = maxy = float('-inf')

    for file in chunk_files:
        with Image.open(file).convert("RGBA") as img:
            images.append(img)
            bbox = img.getbbox()  
            if bbox:
                x0, y0, x1, y1 = bbox
                minx = min(minx, x0 - 1)
                miny = min(miny, y0 - 1)
                maxx = max(maxx, x1 + 1)
                maxy = max(maxy, y1 + 1)

    print(minx, miny, maxx, maxy)
    cropped_images = [img.crop((minx, miny, maxx, maxy)) for img in images]
    output_path = Path(f"./{p.name}_{chunk_index // anim_length}.gif")
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
