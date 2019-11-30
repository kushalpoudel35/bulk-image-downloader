import urllib.request

def download_web_image(image_url):
	name = input("Enter the name you want to save the image as: ")
	fullname = str(name) + ".jpg"
	urllib.request.urlretrieve(image_url, fullname)

url = str(input("Hi there! This is a program that lets you download an image from the web.\nEnter the url of the image: "))

download_web_image(url)
input("Your image has been downloaded. Press any key to exit...")