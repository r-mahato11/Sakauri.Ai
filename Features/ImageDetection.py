# package - pip install bardapi
# pip install datetime
# importing
from bardapi import BardCookies
import datetime

cookie_dict = {
    "__Secure-1PSID": "awjMIL2yEUQXpI-2eE0INx9hqhdcZrShBE0MN12Jrk92XNFROb2YXuOkCWWlCxjHtJHcBg.",
    "__Secure-1PSIDTS": "sidts-CjIBSAxbGfGPoP7w9vNIp_dgb-EwVLChKoSHm_IATuoUQyUMYIk1iPg5mvcVE_gAj7NROxAA",
    "__Secure-1PSIDCC": "APoG2W-CF9lYafqlUG7M959SGSJVQNK50A5BIjkMRmlaHr5Pgy44xhqbbVgWl_x3mt6Op_dvSvQR"
}

bard = BardCookies(cookie_dict=cookie_dict)

# Text Modification Function -


def split_and_save_paragraphs(data, filename):
    paragraphs = data.split('\n\n')
    with open(filename, 'w') as file:
        file.write(data)
    data = paragraphs[:2]
    separator = ', '
    joined_string = separator.join(data)
    return joined_string

# Main Execution

# Image Detection


while True:
    imagename = str(input("Enter The Image Name : "))
    image = open(imagename, 'rb').read()
    bard = BardCookies(cookie_dict=cookie_dict)
    results = bard.ask_about_image(
        'what is in the image?', image=image)['content']
    current_datetime = datetime.datetime.now()
    formatted_time = current_datetime.strftime("%H%M%S")
    filenamedate = str(formatted_time) + str(".txt")
    filenamedate = "Brain\\DataBase\\" + filenamedate
    print(split_and_save_paragraphs(results, filename=filenamedate))
