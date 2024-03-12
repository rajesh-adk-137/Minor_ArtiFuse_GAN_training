import cv2
import numpy as np
import random
import time
import os

def select_random_points(image_path, central_region):
    # Seed the random number generator with the current time
    random.seed(int(time.time()) + hash(image_path))

    # Read the input image
    img = cv2.imread(image_path)

    # Ensure the image is not None
    if img is None:
        raise ValueError("Error reading the image")

    # Generate a random number of point pairs between 3 and 6
    num_points = random.randint(3, 8)

    # Generate random coordinates for point pairs within the central region
    points = []
    for _ in range(num_points):
        x1 = random.randint(central_region[0], central_region[0] + central_region[2] - 1)
        y1 = random.randint(central_region[1], central_region[1] + central_region[3] - 1)
        x2 = random.randint(x1 - 25, x1 + 25)  # Reduce range for nearby points
        y2 = random.randint(y1 - 25, y1 + 25)  # Reduce range for nearby points
        points.append(((x1, y1), (x2, y2)))  # Append pair of nearby points

    return points


def add_random_circles(img):
    # Generate random circles on the image
    for _ in range(random.randint(1, 3)):  # Reduced maximum number of circles
        center = (random.randint(0, int(img.shape[1]*0.75)), random.randint(0, int(img.shape[0]*0.75)))
        radius = random.randint(4, 6)  # Further reduced maximum radius
        cv2.circle(img, center, radius, (255, 255, 255), -1)

def add_random_squares(img):
    # Generate random squares on the image
    for _ in range(random.randint(1, 3)):  # Adjust number of squares as needed
        x = random.randint(0, int(img.shape[1]*0.75))
        y = random.randint(0, int(img.shape[0]*0.75))
        size = random.randint(3, 6)  # Further reduced maximum size
        cv2.rectangle(img, (x, y), (x + size, y + size), (255, 255, 255), -1)


def create_masked_images(original_folder_path, save_folder_path, num_images_to_process):
    # List all image files in the original folder
    image_files = [f for f in os.listdir(original_folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]

    # Limit the number of images to the specified value
    num_images_to_process = min(num_images_to_process, len(image_files))

    # Create the save folder if it doesn't exist
    os.makedirs(save_folder_path, exist_ok=True)
    print("started masking process")

    # Loop through each image in the original folder
    count = 1
    for image_file in image_files:
        # Construct the full path to the image
        image_path = os.path.join(original_folder_path, image_file)

        # Read the original image
        img = cv2.imread(image_path)

        # Define a central region within the image
        height, width, _ = img.shape
        central_region_width = max(1, int(width * 0.5))  # Ensure width is at least 1
        central_region_height = max(1, int(height * 0.5))  # Ensure height is at least 1
        central_region_x = int((width - central_region_width) / 2)
        central_region_y = int((height - central_region_height) / 2)
        central_region = (central_region_x, central_region_y, central_region_width, central_region_height)

        # Generate random points for the current image within the central region
        point_pairs = select_random_points(image_path, central_region)

        # Choose a random masking function and apply it to the image
        masking_functions = [ add_random_circles, add_random_squares] 
        random_masking_function = random.choice(masking_functions)
        random_masking_function(img)

        # Draw lines between nearby points directly on the original image
        for (p1, p2) in point_pairs:
            cv2.line(img, p1, p2, (255, 255, 255), random.randint(1, 5))  # Draw line between nearby points

        # Save the modified image to the new folder
        original_name = os.path.splitext(image_file)[0]
        masked_image_path = os.path.join(save_folder_path, f"{original_name}.jpg")
        cv2.imwrite(masked_image_path, img)
        print(f"masking file = {count}")
        count += 1

# Example usage:
original_folder_path = r'C:\Users\ACER\Downloads\new_custom_masking_\olds\train_2_new_dataset\train_2\train_original'
save_folder_path = r'C:\Users\ACER\Downloads\new_custom_masking_\olds\train_2_new_dataset\train_2\train_masked_'
num_images_to_process = 10000  # Specify the number of images to process
create_masked_images(original_folder_path, save_folder_path, num_images_to_process)
