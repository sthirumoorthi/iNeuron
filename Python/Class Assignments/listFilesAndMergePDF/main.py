import os.path
import subprocess
from tkinter import *
from tkinter import ttk
from PkgSrc import FileManagerApp
from tkinter import messagebox
import logging
logging.basicConfig(filename="App.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


# ---------------------------- Command Functions ------------------------------- #
def list_files_dir():
    """
    This function will list all the directories and files in the Listbox for the given path.
    :return: None. It populates only the Listbox.
    """

    path = entry_path.get()
    if not path:    # check if the path is empty
        messagebox.showinfo(title="Try Again!!", message="Please enter the path.")
    else:
        logging.info(f"The search button was clicked and the event started to find files in location: \n{path}")
        file_list_data = FileManagerApp.get_files_dir(path)
        if len(file_list_data) > 0:
            for value in file_list_data:
                fileListBox.insert(END, value)
            button_loc_pdf["state"] = ACTIVE
            logging.info("The search event completed successfully and the listbox was updated")


def search_pdf():
    """
    This function will find any pdf files available in the specified location.
    :return: None. It populates only Listbox.
    """

    logging.info(f"The locate PDF button was clicked and the event started to find PDF files in location: "
                 f"\n{entry_path.get()}")
    pdf_list_data = FileManagerApp.locate_pdf(fileListBox)
    if len(pdf_list_data) == 0:
        logging.info(f"No PDF files found from the specified location. \n {entry_path.get()}")
    else:
        button_merge_pdf["state"] = ACTIVE
        for value in pdf_list_data:
            pdfListBox.insert(END, value)
        logging.info("The PDF locate event completed successfully and the pdf listbox was updated")


def merge_pdf():
    """
    This function will merge pdf files available in the search location.
    :return: None. The merged file will be stored in the specified location.
    """

    logging.info(f"The Merge PDF button was clicked and the event started to merge the PDF files in location: "
                 f"\n{entry_path.get()}")
    FileManagerApp.merge_pdf_files(pdfListBox, entry_path.get())
    button_download.pack()
    logging.info("The PDF merge event completed successfully and the listbox was updated")


def open_pdf_file():
    """
    This function will open the merged pdf file from the standard location.
    :return: None
    """

    path = os.path.join(entry_path.get(), "output", "new_file.pdf")
    subprocess.Popen([path], shell=True)


def clear_data():
    """
    This function clears all the data from the Text and list boxes
    :return: None
    """

    entry_path.delete(0, END)
    fileListBox.delete(0, END)
    pdfListBox.delete(0, END)
    button_loc_pdf["state"] = DISABLED
    button_merge_pdf["state"] = DISABLED
    button_download.pack_forget()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("List Files and Directories")
window.config(padx=25, pady=25)

logging.info("#######-------- File Manager application has been started --------#######")
logging.info("UI is being popped up")
# Make pane-window0 child of window - to hold banner
pane_window0 = ttk.Panedwindow(window, orient=HORIZONTAL)
pane_window0.grid(row=1, column=1)
# Make pane-window1 child of window - to hold the input path & buttons
pane_window1 = ttk.Panedwindow(window, orient=HORIZONTAL)
pane_window1.grid(row=2, column=1)
# Make pane_window2 child of window - to hold images and display text
pane_window2 = ttk.Panedwindow(window, orient=HORIZONTAL)
pane_window2.grid(row=3, column=1)
# Make pane_window3 child of window - to hold the result
pane_window3 = ttk.Panedwindow(window, orient=HORIZONTAL)
pane_window3.grid(row=4, column=1)
# Make pane_window3 child of window - to hold the result
pane_window4 = ttk.Panedwindow(window, orient=HORIZONTAL)
pane_window4.grid(row=5, column=1)

# header frame with banner
head_frame = ttk.Frame(pane_window0, width=580, height=100, relief=GROOVE)
head_frame.config(padding=1)
#
canvas_head = Canvas(head_frame, width=580, height=100)
ban_img = PhotoImage(file="PkgImages/banner.png")
canvas_head.create_image(290, 40, image=ban_img)
canvas_head.grid(row=1, column=1)

# Input frame with entry & buttons in it
inp_frame = ttk.Frame(pane_window1, width=580, height=400, relief=RIDGE)
inp_frame.config(padding=10)
#
label_path = Label(inp_frame, text="Path", width=6)
label_path.grid(row=1, column=1)
#
entry_path = Entry(inp_frame, width=85)
entry_path.grid(row=1, column=2, columnspan=3)
entry_path.focus()
#
img_reset = PhotoImage(file="PkgImages/reset.PNG")
button_reset = Button(inp_frame, image=img_reset, borderwidth=0, command=clear_data)
button_reset.grid(row=2, column=1, pady=10)
button_search = Button(inp_frame, text="Search", width=18, command=list_files_dir)
button_search.grid(row=2, column=2, pady=10)
button_loc_pdf = Button(inp_frame, text="Locate PDFs", width=18, command=search_pdf)
button_loc_pdf.grid(row=2, column=3, pady=10)
button_merge_pdf = Button(inp_frame, text="Merge PDF", width=18, command=merge_pdf)
button_merge_pdf.grid(row=2, column=4, pady=10)
button_loc_pdf["state"] = DISABLED
button_merge_pdf["state"] = DISABLED

# result frame with entry & buttons in it
result_frame = ttk.Frame(pane_window2, width=580, height=100)
result_frame.config(padding=5)
#
label_fill = Label(result_frame, width=30)
label_fill.grid(row=1, column=1, columnspan=3)
# - display the folder icon and text
canvas1 = Canvas(result_frame, height=40, width=30)
file_img1 = PhotoImage(file="PkgImages/folder.png")
canvas1.create_image(25, 25, image=file_img1)
canvas1.grid(row=2, column=1, ipadx=15)
label_file1 = Label(result_frame, text="Files and Folders", width=40, anchor="w")
label_file1.grid(row=2, column=2, ipadx=20)
# - display the pdf icon and text
canvas2 = Canvas(result_frame, height=40, width=20)
file_img2 = PhotoImage(file="PkgImages/pdf.png")
canvas2.create_image(25, 25, image=file_img2)
canvas2.grid(row=2, column=3, ipadx=15)
label_file2 = Label(result_frame, text="Available PDF files", width=15, anchor="w")
label_file2.grid(row=2, column=4, ipadx=20)

# file frame to hold the results
file_frame = ttk.Frame(pane_window3, width=580, height=200, relief=GROOVE)
#
fileListBox = Listbox(file_frame)
fileListBox.config(height=15, width=60)
fileListBox.pack(side=LEFT)
file_scroll = Scrollbar(file_frame, orient="vertical")
file_scroll.pack(side=RIGHT, fill=Y)
fileListBox.config(yscrollcommand=file_scroll.set)
file_scroll.config(command=fileListBox.yview)

# pdf frame to hold the results
pdf_frame = ttk.Frame(pane_window3, width=580, height=200, relief=GROOVE)
pdfListBox = Listbox(pdf_frame)
pdfListBox.config(height=15, width=30)
pdfListBox.pack(side=LEFT)
pdf_scroll = Scrollbar(pdf_frame, orient="vertical")
pdf_scroll.pack(side=RIGHT, fill=Y)
pdfListBox.config(yscrollcommand=pdf_scroll.set)
pdf_scroll.config(command=pdfListBox.yview)

# pdf frame to hold the PDF download button
download_frame = ttk.Frame(pane_window4, width=580, height=100)
download_frame.config(padding=10)
img = PhotoImage(file="PkgImages/downloadPDF.png")
button_download = Button(download_frame, text="", image=img, borderwidth=0, command=open_pdf_file)
button_download.pack_forget()

# Display the panel windows in the order
pane_window0.add(head_frame, weight=1)
pane_window1.add(inp_frame, weight=1)
pane_window2.add(result_frame, weight=1)
pane_window3.add(file_frame, weight=1)
pane_window3.add(pdf_frame, weight=1)
pane_window4.add(download_frame, weight=1)
window.mainloop()
