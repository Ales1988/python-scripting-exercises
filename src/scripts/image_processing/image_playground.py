# Trying some methods from PIL
if __name__ == "__main__":
    from PIL import Image, ImageFilter

    images_path = "./src/scripts/image_processing/image/"
    img_name = "bison"

    img = Image.open(images_path + img_name + ".jpeg")
    print(f"{img.format}, {img.size}, {img.mode}")

    # Blur an image
    filtered_img = img.filter(ImageFilter.BLUR)
    filtered_img.save(images_path + "blur_" + img_name + ".png", "png")

    # Grey out an image
    grey_scaled_img = img.convert("L")  # L stand for grey scaled format
    grey_scaled_img.save(images_path + "grey_" + img_name + ".png", "png")

    # Rotate an image
    rotated_img = img.rotate(45)
    rotated_img.save(images_path + "rotated_" + img_name + ".png", "png")

    # Resize an image
    resized_img = img.resize((600, 600))  # resize changes the aspect ratio
    resized_img.save(images_path + "resized_" + img_name + ".png", "png")

    # Resize an image preserving the aspect ratio
    thumbnail_img = img.copy()  # Need a copy: thumbnail modifies directly the object
    thumbnail_img.thumbnail((600, 600))
    thumbnail_img.save(images_path + "thumbnail_" + img_name + ".png", "png")

    # Crop an image
    box = (100, 100, 300, 300)
    cropped_img = img.crop(box)
    cropped_img.save(images_path + "cropped_" + img_name + ".png", "png")
