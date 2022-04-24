import pandas as pd
import matplotlib.pyplot as plt
import glob
from tkinter import filedialog
from tkinter import *
import os
import shutil
from tkinter import ttk


# ========== Function section ==========

def browse():

    # Taking the directory address of the multiple .csv files from the user
    target_directory = filedialog.askdirectory()

    # Making sure that there is no content in the entry box
    entAddress.delete(0, "end")

    # Displaying the input Excel file address in the entry box
    entAddress.insert(END, target_directory)

def plot():

    # Taking the address available in the entry box
    target_directory = entAddress.get()

    # Name of the folder used to store the output images
    output_images ="Plots"

    # Directory address of the folder used to store the output images
    child_directory_address = os.path.join(target_directory, output_images)

    # Making the directory according to the address of the folder used to store the output images
    os.mkdir(child_directory_address)

    # Making a list of all .csv file addresses 
    all_files = glob.glob(target_directory + "/*.csv")

    # Finding the number of available .csv files
    number_of_files = len(all_files)

    # Number of progress bar divisions
    num_progress_div = 100 / number_of_files
    

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

        progress['value'] += num_progress_div
        main_window.update_idletasks()

        

# ========== GUI section ==========

# START of the mail loop
main_window = Tk()
main_window.title("Multiple CSV Plotter")

# ====>> Creating the required widgets
lblBrowse = Label(main_window, text="Address of the folder containing the .csv files: ")
entAddress = Entry(main_window, width=60)
btnBrowse = Button(main_window, text="Browse", bg="gray", borderwidth=3, command=browse)
btnPlot = Button(main_window, text="Plot", bg="yellow", borderwidth=3, command=plot)
lblContact = Label(main_window, text="More info.: amir.mousavian@northvolt.com", font=("Helvetica", 8))
progress = ttk.Progressbar(main_window, orient=HORIZONTAL, length=50, mode="determinate")

# <<==== Shoving the widgets into the window
lblBrowse.grid(row=0, column=0, padx=2.5, sticky="w")
entAddress.grid(row=0, column=1, pady=2.5, sticky="w")
btnBrowse.grid(row=0, column=2, padx=2.5, ipadx=40)
btnPlot.grid(row=1, column=1, columnspan=1, pady=2.5, ipadx=40)
lblContact.grid(row=2, column=0, pady=2.5, sticky="w")
progress.grid(row=2, column=2, ipadx=35)

# Preventing the size of the main window to be changed by the user
main_window.resizable(False, False)

main_window.geometry("760x100")

#main_window.call("tk", "scaling", 2.0)

# END of the main loop
main_window.mainloop()






# Plot by selecting specific columns
# https://stackoverflow.com/questions/41825939/plot-pandas-dataframe-two-columns

# Read specific columns of a csv file
# https://www.geeksforgeeks.org/reading-specific-columns-of-a-csv-file-using-pandas/

# How to change a label's text dymanically
# https://stackhowto.com/how-to-change-label-text-on-button-click-in-tkinter/

# ===================== FINAL NOTE =====================
# Converting the .py file to .exe file considering pyinstaller is installed
# Being in the .py directory
# pyinstaller --onefile --noconsole multiple_file_plotter_rev01.py



