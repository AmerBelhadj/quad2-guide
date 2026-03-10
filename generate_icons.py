from PIL import Image, ImageDraw, ImageFont
import os

os.makedirs('/home/claude/pwa-quad2/icons', exist_ok=True)

sizes = [72, 96, 128, 144, 152, 192, 384, 512]

for size in sizes:
    img = Image.new('RGBA', (size, size), (2, 13, 26, 255))
    draw = ImageDraw.Draw(img)
    
    # Background circle gradient effect
    for i in range(size//2, 0, -1):
        alpha = int(30 * (1 - i/(size//2)))
        draw.ellipse([size//2-i, size//2-i, size//2+i, size//2+i],
                    fill=(0, 212, 255, alpha))
    
    # Outer ring
    lw = max(2, size//30)
    draw.ellipse([lw, lw, size-lw, size-lw], outline=(0, 212, 255, 200), width=lw)
    
    # Inner design - dive computer shape
    margin = size // 5
    r = size // 10
    draw.rounded_rectangle([margin, margin, size-margin, size-margin],
                           radius=r, fill=(10, 31, 53, 255), outline=(0, 212, 255, 150), width=max(1,lw//2))
    
    # Screen inside
    sm = size // 4
    draw.rounded_rectangle([sm, sm, size-sm, size-sm],
                           radius=r//2, fill=(0, 0, 0, 255))
    
    # "Q2" text on screen
    fs = max(8, size // 6)
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', fs)
    except:
        font = ImageFont.load_default()
    
    text = 'Q2'
    bbox = draw.textbbox((0,0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    draw.text((size//2 - tw//2, size//2 - th//2 - size//20), text,
             fill=(0, 212, 255, 255), font=font)
    
    # Small dots for buttons
    dot_r = max(1, size//25)
    dot_color = (0, 255, 136, 200)
    positions = [
        (margin - dot_r*2, size//3),
        (margin - dot_r*2, 2*size//3),
        (size - margin + dot_r*2, size//3),
        (size - margin + dot_r*2, 2*size//3),
    ]
    for px, py in positions:
        draw.ellipse([px-dot_r, py-dot_r, px+dot_r, py+dot_r], fill=dot_color)
    
    img.save(f'/home/claude/pwa-quad2/icons/icon-{size}.png')
    print(f'Generated icon-{size}.png')

print('All icons generated!')
