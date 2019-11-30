import urllib.request

def download_web_image(image_url):
	name = input("Enter the name you want to save the image as: ")
	fullname = str(name) + ".jpg"
	print("Downloading " + fullname + " ...")
	urllib.request.urlretrieve(image_url, fullname)
	print(fullname + " downloaded.")

url = str(input("Hi there! This is a program that lets you download an image from the web.\nEnter the url of the image: "))

download_web_image(url)
input("Press any key to exit...")