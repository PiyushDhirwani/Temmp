import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder = '1QPO3G8J09nEZDZvnMmX7T-OnWNh31vf3'

# Upload files
directory = "/Users/apple/Desktop/Java_Begin"
for f in os.listdir(directory):
	filename = os.path.join(directory, f)
	gfile = drive.CreateFile({'parents' : [{'id' : folder}], 'title' : f})
	gfile.SetContentFile(filename)
	gfile.Upload()