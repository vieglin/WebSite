import cv2
import numpy as np

input_path = "logo.jpeg"
output_path = "logo.png"

# Read image
img = cv2.imread(input_path)
mask = np.zeros(img.shape[:2], np.uint8)

# GrabCut parameters
bgd_model = np.zeros((1, 65), np.float64)
fgd_model = np.zeros((1, 65), np.float64)

# Define rectangle around the foreground (adjust margins as needed)
h, w = img.shape[:2]
margin = 10
rect = (margin, margin, w - 2 * margin, h - 2 * margin)

# Apply GrabCut
cv2.grabCut(img, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

# Create binary mask
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype("uint8")

# Apply mask and create RGBA image
img_rgba = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
img_rgba[:, :, 3] = mask2 * 255

cv2.imwrite(output_path, img_rgba)
print(f"Background removed. Saved to {output_path}")
