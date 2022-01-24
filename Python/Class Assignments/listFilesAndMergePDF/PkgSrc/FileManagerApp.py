import os
from PyPDF2 import PdfFileMerger
from tkinter import messagebox
import logging
logging.basicConfig(filename="App.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')


def get_files_dir(path):
    """
    This function will list all the directories and files in the Listbox for the given path.
    :param path: location/path to be searched for files & folders
    :return: List of all file names and folder names
    """

    result = []
    logging.info("FileManagerApp module started")
    try:
        file_list = os.listdir(path)
        result = sorted(file_list, key=lambda x: os.stat(os.path.join(path, x)).st_mode)

        # If the specified location doesn't have any files/folders, report warning.
        if len(result) == 0:
            messagebox.showinfo(title="Oops!!", message="No files or folders found in the specified location")
            logging.warning(f"Search event completed with warning. "
                            f"No files or folder found in the specified location\n {path}")
    except FileNotFoundError as fil_err:
        messagebox.showinfo(title="Oops!! Error..",
                            message="The specified location is either invalid or incorrectly spelled.\n"
                                    "Try again...")
        logging.error(f"The specified location is either invalid or incorrectly spelled. {path}")
    except Exception as err:
        logging.exception(f"Exception occurred. \n{err}")
    return result


def locate_pdf(file_list):
    """
    This function will find any pdf files available in the specified location.
    :param file_list: Listbox entries which has files and folder names in it.
    :return: List of pdf files available in the Listbox.
    """

    logging.info("FileManagerApp module started")
    pdf_list_data = []
    try:
        for i in range(file_list.size()):
            if file_list.get(i).endswith(".pdf"):
                pdf_list_data.append(file_list.get(i))
    except Exception as err:
        logging.exception(f"Exception occurred. Unable to locate PDF files. \n{err}")
    return pdf_list_data


def merge_pdf_files(pdf_list, path):
    """
    This function will merge all the pdf files available in the search location.
    It creates a folder called "output" and place the merged file.
    :param pdf_list: List of pdf file names to be merged.
    :param path: Location of the pdf files.
    :return: None.
    """

    logging.info("FileManagerApp module started")
    pdf_files = []
    try:
        new_dir = os.path.join(path, "output")
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
            logging.info(f"The output folder was created in the search location. \n {path}")
        outfile = os.path.join(new_dir, "new_file.pdf")
        if not os.path.exists(outfile):
            pdf_files = [os.path.join(path, pdf_list.get(x)) for x in range(pdf_list.size())]
            merger = PdfFileMerger()
            for pdf in pdf_files:
                merger.append(open(pdf, 'rb'))
            with open(outfile, "wb") as fileout:
                merger.write(fileout)
                messagebox.showinfo(title="Success", message="Merged PDf file was created")
                logging.info("Merged PDf file was created.")
        else:
            logging.warning(f"The merged pdf file name new_pdf is already available in the location.\n{outfile}")
            messagebox.showinfo(title="Warning",
                                message=f"The default file name new_pdf is already available in the directory.\n"
                                        f"Please have it removed from the below path? \n{outfile}")
    except Exception as err:
        logging.exception(f"Exception occurred. {err}")
