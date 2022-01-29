# **Project Overview:**
  Python based project was developed to list down all the files and folders in the specified location. This includes all the files including temporary files such as .ipynb_checkpoints. In addition to this, if the specified location has any PDF files in it, then it will be displayed in the separate List Box using a button click and those PDF files can be merged into a single file.
### **Functionalities:**
 - **Search:** List down all the files and folders in the first list box (sorted by its type)
 - **Locate PDF:** Locates all the PDF files available in the input location and displays them in second list box
 - **Merge PDF:** Merges all the PDF files and enables a download link for the user to download.
 - **Clear:** Clears all the fields
 - **Download PDF:** Link to download the merged PDF. This will be enabled only after pressing the Merge PDF button

# **Modules Used:**
![image](https://user-images.githubusercontent.com/90926526/151657751-84b5fef2-6145-42e9-a691-36c34263754d.png)

#### Additional libraries:
  - logging
  - PyPDF2
  - OS

# **Folder Structure:**
![image](https://user-images.githubusercontent.com/90926526/151658100-67e45a2c-4a29-46d3-b95d-d3bd15577893.png)


# **Screenshots**
Initial screen:

![image](https://user-images.githubusercontent.com/90926526/151657110-4f83489a-ea3f-4d6a-92e9-65c8a32e6a10.png)

Final screen:

![image](https://user-images.githubusercontent.com/90926526/151657545-993c2867-15bb-4331-9ab0-b8e97b0cc862.png)

# **References:**
- Python Tkinter - https://docs.python.org/3/library/tkinter.html
- Tkinter scrollbars - https://www.youtube.com/watch?v=8ijKnxkaoHE
- Tkinter scrollbars issue - https://stackoverflow.com/questions/24656138/python-tkinter-attach-scrollbar-to-listbox-as-opposed-to-window/24656407
