from PIL import Image


def resize_image(input_image_path,
                 output_image_path,
                 size):
    original_image = Image.open(input_image_path)
    #print('The original image size is {wide} wide x {height} high')

    resized_image = original_image.resize(size)
    #print('The resized image size is {wide} wide x {height} high'.format(wide=width, height=height))
    resized_image.save(output_image_path)
