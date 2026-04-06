from PIL import Image
import os

print("Building...")

os.makedirs("temp", exist_ok=True)

_RESAMPLE = getattr(Image, "Resampling", Image).LANCZOS

#flavour icon
def flavour(type):

    flavours = {
        "Apple" : "HardDrive.png",
        "ExtApple" : "ExtHardDrive.png",
        "AppleRecv" : "AppleRecv.png",
        "ExtAppleRecv" : "ExtAppleRecv.png"
    }

    overlay_png = flavours[type]

    for f in os.listdir("flavour"):
        if not f.lower().endswith(".png"):
            continue

        flavour_icon = Image.open(os.path.join("flavour", f)).convert("RGBA")

        # hdd img
        overlay = Image.open(os.path.join("source", overlay_png)).convert("RGBA")

        # scale hdd img
        if type == "Apple" or type == "ExtApple":
            overlay = overlay.resize((150, 150))
            position = (122, 110)

        else:
            overlay = overlay.resize((135, 135))
            position = (125, 115)

        flavour_icon.paste(overlay, position, overlay)

        flavour_icon.save(os.path.join("source", type+f))

flavour("Apple")
flavour("ExtApple")
flavour("AppleRecv")
flavour("ExtAppleRecv")

shutil.rmtree("temp")

shutil.rmtree("source/ExtAppleRecv10_4.png")
shutil.rmtree("source/ExtAppleRecv10_5.png")
shutil.rmtree("source/ExtAppleRecv10_6.png")
shutil.rmtree("source/AppleRecv10_4.png")
shutil.rmtree("source/AppleRecv10_5.png")
shutil.rmtree("source/AppleRecv10_6.png")