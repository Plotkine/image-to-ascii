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
    if ((size % 2) == 1): #even size
        size += 1
    im = Image.open(image)
    im2 = im.copy()
    im2 = im2.resize((size,size))
    #im2.show()
    minimum, maximum = stats(im2)
    pixels = im2.load()

    for i in range(0, size, 2): #looping on pixels lines
        for j in range(size): #on pixels colons
            #debug
            '''print("i: "+str(i))
            print("j: "+str(j))
            print("size: "+str(size))'''
            average_1 = (pixels[j,i][0]+pixels[j,i][1]+pixels[j,i][2])/3
            average_2 = (pixels[j,i+1][0]+pixels[j,i+1][1]+pixels[j,i+1][2])/3
            average = floor((average_1 + average_2)/2)
            print(value_to_ascii_char(average, ascii_chars, minimum, maximum),end='')
        print('\n', end='')

if __name__ == '__main__':
    if len(argv) < 4:
        print("Usage: python3 image_to_ascii.py image output_resolution dark/light")
        print("Example: python3 image_to_ascii.py rickRoll.jpg 150 dark")
        exit()
    print(argv)
    if argv[3] == "dark":
        main(argv[1], '#&B9XSxs~;:-,. ', int(argv[2]))
    else:
        main(argv[1], ' .,-:;~sxSX9B&#', int(argv[2]))
