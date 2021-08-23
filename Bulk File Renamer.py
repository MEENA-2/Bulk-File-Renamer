import os

def renamer():
    i = 0   #(i - initiate/Iterate over files/lists) -choosing i for this reason always
    path = "C:\\Users\\GOD\\Downloads\\VS code Files\\Bulk\img1\\"
    for filename in os.listdir(path):
        names = f"Image {i}.jpeg"
        src = path + filename
        dest = path + names

        os.rename(src, dest)
        i = i + 1

if __name__ == "__main__":
    renamer()