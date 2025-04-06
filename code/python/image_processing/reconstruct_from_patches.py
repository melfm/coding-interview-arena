import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

"""
Q : Given a grayscale image, exract patches of a given size given the
stride, and reconstruct the image from the extracted patches.
"""
def extract_patches(image, patch_size, stride):


    h, w = image.shape
    ph, pw = patch_size

    # Because we start at position 0, stride tells how many steps to take
    nh = (h - ph) // stride + 1
    nw = (w - pw) // stride + 1

    patches = np.zeros((nh, nw, ph, pw))
    for i in range(nh):
        for j in range(nw):
            top = i * stride
            left = j * stride
            patch = image[top:top + ph, left:left + pw]
            patches[i, j] = patch
    return patches


def reconstruct_image(patches, image_shape, stride):
    """
    Args:
        patches: 4D numpy array of extracted patches.
        image_shape: the original shape of image.
        stride: the stride used during patch extraction.
    """

    # Calculating how many patches will be extracted from an image
    # and much overlap or gaps there will be.
    # num_patches_y = (image_height - patch_height) // stride + 1
    # last_covered_y = (num_patches_y - 1) * stride + patch_height

    h, w = image_shape
    ph, pw = patches.shape[2], patches.shape[3]
    nh, nw = patches.shape[0], patches.shape[1]

    recon_image = np.zeros((h, w))
    weight_map = np.zeros((h, w))

    for i in range(nh):
        for j in range(nw):
            top = i * stride
            left = j * stride
            recon_image[top:top + ph, left:left + pw] += patches[i, j]
            weight_map[top:top + ph, left:left + pw] += 1

    # To fix overlapping regions
    weight_map[weight_map == 0] = 1  # Avoid division by zero
    return recon_image / weight_map

# Generate sample grayscale image
lena = Image.open("Lenna.png").convert("L")  # Convert to grayscale
image = np.array(lena)

patch_size = (8, 8)
stride = 4

patches = extract_patches(image, patch_size, stride)
reconstructed = reconstruct_image(patches, image.shape, stride)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap='gray')

plt.subplot(1, 2, 2)
plt.title("Reconstructed Image")
plt.imshow(reconstructed, cmap='gray')

plt.show()

error = np.mean((image - reconstructed) ** 2)
print(f"Reconstruction MSE: {error:.4f}")


