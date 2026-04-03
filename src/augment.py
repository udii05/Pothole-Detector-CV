import cv2
import matplotlib.pyplot as plt

def show_sample(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    plt.imshow(img)
    plt.title("Sample Image")
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    show_sample("data/train/images/sample.jpg")  # update path