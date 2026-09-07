import matplotlib.pyplot as plt
from PIL import Image

# Step 1: Load the input image
image_path = "question.png"
img = Image.open(image_path)
img.show()  # Optional: to preview the image

# Step 2: LaTeX code (normally you'd extract using OCR like MathPix or LaTeX-OCR)
latex_code = r"\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}"

# Step 3: Render LaTeX to image
plt.rcParams.update({"text.usetex": False})  # Set to True if LaTeX is installed
plt.figure(figsize=(6, 1))
plt.text(0.5, 0.5, f"${latex_code}$", fontsize=20, ha='center', va='center')
plt.axis("off")
plt.savefig("output.png", bbox_inches="tight")

print("✅ Output image saved as output.png")
# Step 4: Display the output image
#output_img = Image.open("output.png")
#output_img.show()  # Optional: to preview the output image
