from PIL import Image, ImageDraw, ImageFont
import os

img = Image.open(os.path.join(os.path.dirname(__file__), "powerhedging-raw.png"))
draw = ImageDraw.Draw(img)

# Try to load a clean font, fallback to default
try:
    font_small = ImageFont.truetype("arial.ttf", 12)
    font_med = ImageFont.truetype("arial.ttf", 14)
    font_name = ImageFont.truetype("arial.ttf", 13)
except:
    font_small = ImageFont.load_default()
    font_med = ImageFont.load_default()
    font_name = ImageFont.load_default()

# Colors sampled from the dark UI
bg_navbar = (30, 24, 40)       # navbar background
bg_card = (22, 20, 32)         # card background
bg_dark = (16, 14, 26)         # darker background
text_white = (220, 220, 220)
text_gray = (160, 160, 170)
text_red = (230, 60, 60)

# 1. Cover "MATTIA BEZZI" in navbar (top right area)
draw.rectangle([970, 8, 1080, 28], fill=bg_navbar)
draw.text((972, 10), "DEMO USER", fill=text_white, font=font_med)

# 2. Cover email "mattia.bezzi97.work" + "ADMIN"
draw.rectangle([1105, 8, 1210, 30], fill=bg_navbar)
draw.text((1107, 8), "demo@matrix.pro", fill=text_gray, font=font_small)
draw.text((1107, 20), "DEMO", fill=text_red, font=font_small)

# 3. Cover FUNDED NEXT entries with names
# Line 1: "FUNDED NEXT #13798290  gianluca angelelli"
draw.rectangle([46, 515, 340, 530], fill=bg_card)
draw.text((48, 516), "FUNDED NEXT #10042851  marco rossi", fill=text_gray, font=font_small)

# Line 2: "FUNDED NEXT #13958308  gianluca angelelli"
draw.rectangle([46, 537, 340, 552], fill=bg_card)
draw.text((48, 538), "FUNDED NEXT #10038764  luca bianchi", fill=text_gray, font=font_small)

# Line 3: "FUNDED NEXT #13936784  stefano angelelli"
draw.rectangle([46, 558, 340, 574], fill=bg_card)
draw.text((48, 560), "FUNDED NEXT #10051293  andrea verdi", fill=text_gray, font=font_small)

out_path = os.path.join(os.path.dirname(__file__), "powerhedging.png")
img.save(out_path, quality=95)
print(f"Saved to {out_path}")
print(f"Size: {img.size}")
