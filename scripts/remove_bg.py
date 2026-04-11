import cv2
import numpy as np

input_path = "logo-vieglin.png"
output_path = "logo.png"

# Read image
img = cv2.imread(input_path)

# The background is dark navy blue (approx RGB: 20-35, 25-40, 50-70)
# We'll make pixels transparent if they're close to this dark blue

# Calculate distance from dark navy background color
# Background appears to be around BGR (50, 35, 25) based on the image
bg_color = np.array([50, 35, 25])  # BGR

# Calculate color distance for each pixel
diff = img.astype(np.float32) - bg_color
distance = np.sqrt(np.sum(diff ** 2, axis=2))

# Pixels far from background color are kept (high alpha)
# Threshold: if distance > 40, it's not background
threshold = 40
alpha = np.clip((distance - threshold) * 5, 0, 255).astype(np.uint8)

# Create RGBA image
img_rgba = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
img_rgba[:, :, 3] = alpha

cv2.imwrite(output_path, img_rgba)
print(f"Background removed. Saved to {output_path}")
