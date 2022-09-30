#!/usr/bin/python
import modules
from os import getcwd

def main():	
	video_url = input("Please input the URL of the desired YT video: ")
	filename = modules.Download(video_url)

	try:
		file = open(str(filename))
		file.close()

		print("\nThe file " + filename + " is in folder " + getcwd() + " and is ready for use!")
	except FileNotFoundError:
		print("Something went wrong, the file does not appear to be in a valid form")
		print("\nTry again later...")
		exit()

if __name__ == "__main__":
	main()
