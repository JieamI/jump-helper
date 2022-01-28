from os import path, system

dir = path.dirname(__file__)
adb = f"{dir}/../tools/adb.exe"

# capture screen and save image to directory assets
def screenCap(): 
    if system(f"{adb} root") != 0:
        raise Exception("adb root fail, please confirm adb has connected")
    isFail = \
    system(f"{adb} shell screencap -p /sdcard/demo.png") or \
    system(f"{adb} pull /sdcard/demo.png {dir}/../assets/demo.png")
    if(isFail):
        raise Exception("capture screen fail")

def press(position, duration):
    format_pos = " ".join(list(map(str, position)))
    print(f"{adb} shell input swipe {format_pos} {format_pos} {duration}")
    isFail = system(f"{adb} shell input swipe {format_pos} {format_pos} {duration}")
    if isFail:
        raise Exception("press fail")

    
