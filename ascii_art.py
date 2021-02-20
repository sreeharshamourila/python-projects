#!/usr/bin/python
# -*- coding: utf-8 -*-
import PIL.Image

###ASCII_CHARS= ["@","#","S","%","?","*","+",";",":",",","."]
ASCII_CHARS= ["$","@","B","%","8","&","W","M","#","*","o","a","h","k","b","d","p","q","w","m","Z","O","0","Q","L","C","J","U","Y","X","z","c","v","u","n","x","r","j","f","t","/","|","(",")","1","{","}","[","]","?","-","_","+","~","<",">","i","!","l","I",";",":","^","`","'","."," "]

def resize_image(image,new_width=600):
    width, height = image.size
    ratio=height/width/1.65
    print(ratio)
    new_height=int(new_width*ratio)
    resized_image = image.resize((new_width,new_height))
    return(resized_image)

def grayify(image):
    grayscale_image=image.convert("L")
    return(grayscale_image)

def pixels_to_ascii(image):
    pixels=image.getdata()
    maxi=max(list(pixels))
    mini=min(list(pixels))
    new_ratio=(float(maxi)-float(mini))/67
    #print(mini)
    characters="".join([ASCII_CHARS[(int(pixel//4))] for pixel in pixels])
    return(characters)

    

def main(new_width=600):
    path=input("enter a valid image:\n")
    try:
        image=PIL.Image.open(path)
    except:
        print("path name is not valid\n")

    newimage_data=pixels_to_ascii(grayify(resize_image(image)))
    
    pixel_count=len(newimage_data)
    print(pixel_count)
    ascii_image="\n".join(newimage_data[i:(i+new_width)] for i in range(0,pixel_count,new_width))
    print(ascii_image)



main()




