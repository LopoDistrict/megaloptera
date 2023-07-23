
hashed = str(hash("megaloptera"))


with open("information.txt", "w+") as f:
    f.write(hashed)