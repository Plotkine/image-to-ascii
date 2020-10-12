from sys import argv
from math import floor
from PIL import Image

#returns min and max average value of the pixels of image
def stats(image): #image = Image.open('image.jpg','r')
    pixels = image.load()
    minimum = 255
    maximum = 0
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            average_pixel_value = floor((pixels[i,j][0]+pixels[i,j][1]+pixels[i,j][2])/3)
            if average_pixel_value < minimum:
                minimum = average_pixel_value
            if average_pixel_value > maximum:
                maximum = average_pixel_value
    return (minimum,maximum)

#converts pixel to ascii char
#considering min and max average pixel values of the whole image
def value_to_ascii_char(value, ascii_chars, minimum, maximum): #ascii_chars goes from darker to lighter
    values_range = maximum - minimum #average values range
    i = len(ascii_chars) #avoiding division by 0
    value_to_compare = (value - minimum)/values_range
    while (value_to_compare > 1/i):
        i -= 1
    return ascii_chars[i - 1]

def main(image, ascii_chars, size):
    im = Image.open(image)

    im2 = im.copy()
    im2 = im2.resize((size,size))
    minimum, maximum = stats(im2)
    pixels = im2.load()

    for i in range(size):
        for j in range(size-1):
            print(value_to_ascii_char(floor((pixels[j,i][0]+pixels[j,i][1]+pixels[j,i][2])/3), ascii_chars, minimum, maximum),end='')
        print(value_to_ascii_char(floor((pixels[size-1,i][0]+pixels[size-1,i][1]+pixels[size-1,i][2])/3), ascii_chars, minimum, maximum),end='\n')

if __name__ == '__main__':
    main(argv[1], '@$#*!=;:~-,. ', 150) #from darker to lighter
