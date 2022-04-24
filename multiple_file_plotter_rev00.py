import pandas as pd
import matplotlib.pyplot as plt
import glob
from tkinter import filedialog
from tkinter import *
import os
import shutil


# Taking the directory address of the multiple .csv files from the user
target_directory = filedialog.askdirectory()

# Name of the folder used to store the output images
output_images ="Plots"

# Directory address of the folder used to store the output images
child_directory_address = os.path.join(target_directory, output_images)

# Making the directory according to the address of the folder used to store the output images
os.mkdir(child_directory_address)

# Making a list of all .csv file addresses 
all_files = glob.glob(target_directory + "/*.csv")

# Making a loop to read the csv files one by one, 
# plot the graphs of each csv file, and 
# save the image of the graph same as its origin csv file name
for file in all_files:
    df = pd.read_csv(file)

    #plt.rcParams["savefig.directory"] = os.path.join(target_directory, output_images)
    df.plot(subplots = True, layout = (6,2), figsize = (15, 20))

    # Making a new file same as the existing one differing in their last four characters (i.e., the file extension)
    plot_image_address = file.replace(".csv", ".png")

    # Saving the image with .png extension in the target directory
    plt.savefig(plot_image_address)

    # Moving the generated images to Plots folder created in the previous lines
    # The first argument in the below line is the source address and
    # the second one is the destination address
    shutil.move(plot_image_address, child_directory_address + plot_image_address.replace(target_directory, ""))











# Plot by selecting specific columns
# https://stackoverflow.com/questions/41825939/plot-pandas-dataframe-two-columns

# Read specific columns of a csv file
# https://www.geeksforgeeks.org/reading-specific-columns-of-a-csv-file-using-pandas/



