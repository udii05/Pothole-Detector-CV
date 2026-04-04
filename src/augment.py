import cv2
import matplotlib.pyplot as plt
import os
import random

def show_sample(image_folder):
    images = os.listdir(image_folder)

    if not images:
        print("No images found!")
        return

    img_name = random.choice(images)
    img_path = os.path.join(image_folder, img_name)

    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.imshow(img)
    plt.title(f"Sample: {img_name}")
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    show_sample("../data/train/images")