import urllib.request
import requests
from bs4 import BeautifulSoup

def downThemAll(site_url):
	source_code = requests.get(site_url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text, 'html.parser')
	firstName = input("Enter the common first name for all the images: ")
	imageNumber = 1
	for link in soup.findAll('a', {'class': 'rel-link'}):		#This part can vary between websites. View page source for this.
		href = link.get('href')
		fullname = str(firstName) + str(imageNumber) + ".jpg"
		print("Downloading {} ...".format(fullname), end=' ')
		urllib.request.urlretrieve(href, fullname)
		print("Downloaded.")
		imageNumber = imageNumber + 1

print("Hi there! This is a program that lets you download multiple images on a website at once.")
url = str(input("Enter the site url: "))

downThemAll(url)
input("Task completed. Press any key to exit...")