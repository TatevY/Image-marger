from PIL import Image

#helper finction, which is getting image name, cut an object from white background and save .
def Delete_Background(img_name):
    img = Image.open(img_name).convert('RGBA')
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            if item[0] > 150:
                newData.append((0, 0, 0, 255))
            else:
                newData.append(item)
    img.putdata(newData)
    img.save("cutted_obj.png", "PNG")

#paste object into the background using helper function
def Paste_Obj(background_img, object_img, x, y):
    background = Image.open(background_img).convert('RGBA')
    Delete_Background(object_img)
    object = Image.open("cutted_obj.png").convert('RGBA')
    background.paste(object, (x, y), object)
    background.save("pasted_picture.png")
    background.show()

#merging two images with same size
def Merge_images(img1, img2, trancparency):
    img1 = Image.open(img1).convert('RGBA')
    img2 = Image.open(img2).convert('RGBA')
    img3 = Image.blend(img1, img2, trancparency)
    img3.save("merged_picture.png")
    img3.show()

def main():
    print("Hi, please choose option.\n\nPRESS\n1 - for pasting object into the background\n2 - for merging images\n")
    option = input('Option = ')

    if option == '1':
        print ("You choosing to paste the object into the background. Please enter a background and an object name to be inserted into it. The object must be on a white background.\n")
        background_img = input ('Background image name in .png format - ')
        object_img = input ('Object image name in .png format - ')
        print ("Enter location of the object on the background using X and Y coordinates.")
        x = int(input ('X coordinate - '))
        y = int(input ('Y coordinate - '))
        Paste_Obj(background_img, object_img, x,y)

    if option == '2':
        print ("You choosing image merge option. Please enter names of two images. Images must be the same size.\n")
        img1 = input ('First image name in .png format - ')
        img2 = input ('Second image name in .png format - ')
        print ("Enter trancparency coefficient from 0.0 to 1.0 ")
        trancparency = float(input('Trancparency coefficient - '))
        Merge_images(img1, img2, trancparency)

    else:
        print("Please enter correct option")


if __name__ == "__main__":
    main()