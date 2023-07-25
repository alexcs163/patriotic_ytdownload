from pytube import YouTube
from tkinter import Tk, filedialog, Button, Entry, StringVar, Label, PhotoImage
from PIL import Image, ImageTk

def browse_files():
    foldername = filedialog.askdirectory()
    return foldername

def download_file():
    link = link_text.get()
    yt = YouTube(link)
    dl = yt.streams.get_highest_resolution()
    dl.download(browse_files())

root = Tk()

root.resizable(False, False)
root.geometry('400x200')
root.title('My Youtube Downloader')

background_image = Image.open("USA.jpg")
background_image = ImageTk.PhotoImage(background_image)
background_label = Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

Label(root, text="Enter YouTube link:").pack()
link_text = StringVar()
link_entry = Entry(root, textvariable=link_text)
link_entry.pack()

Button(root, text="Download", command=download_file, padx=10, pady=15, bg="blue", fg="white", font=("Helvetica", 16)).pack()

root.mainloop()
