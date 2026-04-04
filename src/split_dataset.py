import os
import shutil
import random

# Paths
BASE_DIR = "data"
TRAIN_IMAGES = os.path.join(BASE_DIR, "train/images")
TRAIN_LABELS = os.path.join(BASE_DIR, "train/labels")

VALID_IMAGES = os.path.join(BASE_DIR, "valid/images")
VALID_LABELS = os.path.join(BASE_DIR, "valid/labels")

TEST_IMAGES = os.path.join(BASE_DIR, "test/images")
TEST_LABELS = os.path.join(BASE_DIR, "test/labels")

# Create folders if not exist
for path in [VALID_IMAGES, VALID_LABELS, TEST_IMAGES, TEST_LABELS]:
    os.makedirs(path, exist_ok=True)

# Get all images
images = [f for f in os.listdir(TRAIN_IMAGES) if f.endswith(('.jpg', '.png'))]

random.shuffle(images)

total = len(images)
valid_split = int(0.1 * total)
test_split = int(0.1 * total)

valid_images = images[:valid_split]
test_images = images[valid_split:valid_split + test_split]

def move_files(image_list, dest_img, dest_lbl):
    for img in image_list:
        label = img.rsplit('.', 1)[0] + ".txt"

        src_img = os.path.join(TRAIN_IMAGES, img)
        src_lbl = os.path.join(TRAIN_LABELS, label)

        dst_img = os.path.join(dest_img, img)
        dst_lbl = os.path.join(dest_lbl, label)

        if os.path.exists(src_img) and os.path.exists(src_lbl):
            shutil.move(src_img, dst_img)
            shutil.move(src_lbl, dst_lbl)

# Move files
move_files(valid_images, VALID_IMAGES, VALID_LABELS)
move_files(test_images, TEST_IMAGES, TEST_LABELS)

print("✅ Dataset split completed!")
print(f"Total images: {total}")
print(f"Validation: {len(valid_images)}")
print(f"Test: {len(test_images)}")
print(f"Remaining Train: {total - len(valid_images) - len(test_images)}")