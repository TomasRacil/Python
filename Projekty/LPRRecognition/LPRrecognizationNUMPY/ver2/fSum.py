import os

def fAmount(folder = "spz"):
    img_folder_path = folder
    dirListing = os.listdir(img_folder_path)
    
    return len(dirListing)