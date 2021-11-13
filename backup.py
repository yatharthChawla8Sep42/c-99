import os
import shutil

source = input("Enter the source folder:-")
destination = input("Enter the destination folder:-")

source = source + '/'
destination = destination + '/'

List_of_files = os.listdir(source)

for file in List_of_files:
    shutil.move((source+file), destination)