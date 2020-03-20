# -*- coding: <encoding name> -*-
import cv2
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def cut():
    name = f'./data/first_frame.jpg'
    save_path = f'./data/'
    r1 = (0, 0, 720, 720)  # 1280 * 720
    r2 = (640 - 720/2, 0, 640 + 720/2, 720)
    r3 = (1280 - 720, 0, 1280, 720)

    img1 = Image.open(name)
    cropped_img1 = Image.Image.crop(img1, r1)
    cropped_img1.save(save_path + "1.jpg")

    img2 = Image.open(name)
    cropped_img2 = Image.Image.crop(img2, r2)
    cropped_img2.save(save_path + "2.jpg")

    img3 = Image.open(name)
    cropped_img3 = Image.Image.crop(img3, r3)
    cropped_img3.save(save_path + "3.jpg")


def cut_png():
    name = 'first_frame.png'
    r1 = (0, 0, 720, 720)  # 1280 * 720
    r2 = (640 - 720/2, 0, 640 + 720/2, 720)
    r3 = (1280 - 720, 0, 1280, 720)

    img1 = Image.open(name)
    cropped_img1 = Image.Image.crop(img1, r1)
    cropped_img1.save("first.png")

    img2 = Image.open(name)
    cropped_img2 = Image.Image.crop(img2, r2)
    cropped_img2.save("second.png")

    img3 = Image.open(name)
    cropped_img3 = Image.Image.crop(img3, r3)
    cropped_img3.save("third.png")

def do_image(input_str):

    filename = "Blogger Sans.otf"
    kegl = 65
    font = ImageFont.truetype(filename, kegl)

    up_string = (70, 845)
    down_string = (70, 915)
    middle_string = (70, 870)

    input_str = input_str.upper()
    words = input_str.split(" ")
    for i in range(1, 4):
        img_name = f".\\data\\{i}.jpg"
        save_path = f".\\output\\{i}.png"
        print(i)
        if len(input_str) < 51:
            img1 = Image.open("source.png").convert('RGBA')
            draw1 = ImageDraw.Draw(img1)

            if len(words) == 1:
                font = ImageFont.truetype(filename, 90)
                draw1.text(middle_string, words[0], (255, 255, 255, 255), font=font)
                img2 = Image.open(img_name).convert('RGBA')
                img2 = img2.resize((1024, 1024))
                result2 = Image.alpha_composite(img2, img1)
                result2.save(save_path)

            elif len(words) == 2:

                draw1.text(up_string, words[0], (255, 255, 255, 255), font=font)
                draw1.text(down_string, words[1], (255, 255, 255, 255), font=font)
                img2 = Image.open(img_name).convert('RGBA')
                img2 = img2.resize((1024, 1024))
                result2 = Image.alpha_composite(img2, img1)
                result2.save(save_path)

            elif len(words) == 3 and len(words[0] + " " + words[1]) < 25:

                draw1.text(up_string, words[0] + " " + words[1], (255, 255, 255, 255), font=font)
                draw1.text(down_string, words[2], (255, 255, 255, 255), font=font)
                img2 = Image.open(img_name).convert('RGBA')
                img2 = img2.resize((1024, 1024))
                result2 = Image.alpha_composite(img2, img1)
                result2.save(save_path)

            elif len(words) == 4 and len(words[0] + " " + words[1]) < 25 and len(words[2] + " " + words[3]) < 25:

                draw1.text(up_string, words[0] + " " + words[1], (255, 255, 255, 255), font=font)
                draw1.text(down_string, words[2] + " " + words[3], (255, 255, 255, 255), font=font)
                img2 = Image.open(img_name).convert('RGBA')
                img2 = img2.resize((1024, 1024))
                result2 = Image.alpha_composite(img2, img1)
                result2.save(save_path)

            elif len(words) == 5 and len(words[0] + " " + words[1] + " " + words[2]) < 25 and len(
                    words[3] + " " + words[4]) < 25:

                draw1.text(up_string, words[0] + " " + words[1] + " " + words[2], (255, 255, 255, 255), font=font)
                draw1.text(down_string, words[3] + " " + words[4], (255, 255, 255, 255), font=font)
                img2 = Image.open(img_name).convert('RGBA')
                img2 = img2.resize((1024, 1024))
                result2 = Image.alpha_composite(img2, img1)
                result2.save(save_path)

            elif len(words) == 6 and len(words[0] + " " + words[1] + " " + words[2]) < 25 and len(
                    words[3] + " " + words[4] + " " + words[5]) < 25:

                draw1.text(up_string, words[0] + " " + words[1] + " " + words[2], (255, 255, 255, 255), font=font)
                draw1.text(down_string, words[3] + " " + words[4] + " " + words[5], (255, 255, 255, 255), font=font)
                img2 = Image.open(img_name).convert('RGBA')
                img2 = img2.resize((1024, 1024))
                result2 = Image.alpha_composite(img2, img1)
                result2.save(save_path)

            elif len(words) == 7 and len(words[0] + " " + words[1] + " " + words[2] + " " + words[3]) < 25 and len(
                    words[4] + " " + words[5] + " " + words[6]) < 25:

                draw1.text(up_string, words[0] + " " + words[1] + " " + words[2] + " " + words[3], (255, 255, 255, 255),
                           font=font)
                draw1.text(down_string, words[4] + " " + words[5] + " " + words[6], (255, 255, 255, 255), font=font)
                img2 = Image.open(img_name).convert('RGBA')
                img2 = img2.resize((1024, 1024))
                result2 = Image.alpha_composite(img2, img1)
                result2.save(save_path)

            elif len(words) == 8 and len(words[0] + " " + words[1] + " " + words[2] + " " + words[3]) < 25 and len(
                    words[4] + " " + words[5] + " " + words[6] + " " + words[7]) < 25:

                draw1.text(up_string, words[0] + " " + words[1] + " " + words[2] + " " + words[3], (255, 255, 255, 255),
                           font=font)
                draw1.text(down_string, words[4] + " " + words[5] + " " + words[6] + words[7], (255, 255, 255, 255),
                           font=font)
                img2 = Image.open(img_name).convert('RGBA')
                img2 = img2.resize((1024, 1024))
                result2 = Image.alpha_composite(img2, img1)
                result2.save(save_path)


def do_image_png(input_str, switcher='economy'):
    fonts = {'economy': 'Blogger Sans.otf',
             'minitrip': 'HelveticaNeueCyr.otf'}

    font_sizes = {'economy': 65,
             'minitrip': 80}

    filename = fonts[switcher]
    kegl = font_sizes[switcher]
    font = ImageFont.truetype(filename, kegl)

    up_string = (70, 845)
    down_string = (70, 915)
    middle_string = (70, 870)

    input_str = input_str.upper()
    words = input_str.split(" ")
    for i in ['first', 'second', 'third']:
        img_name = f"{i}.png"
        save_path = f"{i}_done.png"
        print(i)
        if len(input_str) < 51:
            img1 = Image.open("source.png").convert('RGBA')
            draw1 = ImageDraw.Draw(img1)

            if len(words) == 1:
                font = ImageFont.truetype(filename, 90)
                draw1.text(middle_string, words[0], (255, 255, 255, 255), font=font)
                img2 = Image.open(img_name).convert('RGBA')
                img2 = img2.resize((1024, 1024))
                result2 = Image.alpha_composite(img2, img1)
                result2.save(save_path)

            elif len(words) == 2:

                draw1.text(up_string, words[0], (255, 255, 255, 255), font=font)
                draw1.text(down_string, words[1], (255, 255, 255, 255), font=font)
                img2 = Image.open(img_name).convert('RGBA')
                img2 = img2.resize((1024, 1024))
                result2 = Image.alpha_composite(img2, img1)
                result2.save(save_path)

            elif len(words) == 3 and len(words[0] + " " + words[1]) < 25:

                draw1.text(up_string, words[0] + " " + words[1], (255, 255, 255, 255), font=font)
                draw1.text(down_string, words[2], (255, 255, 255, 255), font=font)
                img2 = Image.open(img_name).convert('RGBA')
                img2 = img2.resize((1024, 1024))
                result2 = Image.alpha_composite(img2, img1)
                result2.save(save_path)

            elif len(words) == 4 and len(words[0] + " " + words[1]) < 25 and len(words[2] + " " + words[3]) < 25:

                draw1.text(up_string, words[0] + " " + words[1], (255, 255, 255, 255), font=font)
                draw1.text(down_string, words[2] + " " + words[3], (255, 255, 255, 255), font=font)
                img2 = Image.open(img_name).convert('RGBA')
                img2 = img2.resize((1024, 1024))
                result2 = Image.alpha_composite(img2, img1)
                result2.save(save_path)

            elif len(words) == 5 and len(words[0] + " " + words[1] + " " + words[2]) < 25 and len(
                    words[3] + " " + words[4]) < 25:

                draw1.text(up_string, words[0] + " " + words[1] + " " + words[2], (255, 255, 255, 255), font=font)
                draw1.text(down_string, words[3] + " " + words[4], (255, 255, 255, 255), font=font)
                img2 = Image.open(img_name).convert('RGBA')
                img2 = img2.resize((1024, 1024))
                result2 = Image.alpha_composite(img2, img1)
                result2.save(save_path)

            elif len(words) == 6 and len(words[0] + " " + words[1] + " " + words[2]) < 25 and len(
                    words[3] + " " + words[4] + " " + words[5]) < 25:

                draw1.text(up_string, words[0] + " " + words[1] + " " + words[2], (255, 255, 255, 255), font=font)
                draw1.text(down_string, words[3] + " " + words[4] + " " + words[5], (255, 255, 255, 255), font=font)
                img2 = Image.open(img_name).convert('RGBA')
                img2 = img2.resize((1024, 1024))
                result2 = Image.alpha_composite(img2, img1)
                result2.save(save_path)

            elif len(words) == 7 and len(words[0] + " " + words[1] + " " + words[2] + " " + words[3]) < 25 and len(
                    words[4] + " " + words[5] + " " + words[6]) < 25:

                draw1.text(up_string, words[0] + " " + words[1] + " " + words[2] + " " + words[3], (255, 255, 255, 255),
                           font=font)
                draw1.text(down_string, words[4] + " " + words[5] + " " + words[6], (255, 255, 255, 255), font=font)
                img2 = Image.open(img_name).convert('RGBA')
                img2 = img2.resize((1024, 1024))
                result2 = Image.alpha_composite(img2, img1)
                result2.save(save_path)

            elif len(words) == 8 and len(words[0] + " " + words[1] + " " + words[2] + " " + words[3]) < 25 and len(
                    words[4] + " " + words[5] + " " + words[6] + " " + words[7]) < 25:

                draw1.text(up_string, words[0] + " " + words[1] + " " + words[2] + " " + words[3], (255, 255, 255, 255),
                           font=font)
                draw1.text(down_string, words[4] + " " + words[5] + " " + words[6] + words[7], (255, 255, 255, 255),
                           font=font)
                img2 = Image.open(img_name).convert('RGBA')
                img2 = img2.resize((1024, 1024))
                result2 = Image.alpha_composite(img2, img1)
                result2.save(save_path)


def get_first_frame():

    cap = cv2.VideoCapture(f'1.MOV')
    try:
        if not os.path.exists('data'):
            os.makedirs('data')
    except OSError:
        print('Error: Creating directory of data')
    ret, frame = cap.read()
    name = f'first_frame.png'
    cv2.imwrite(name, frame)
    cap.release()
    cv2.destroyAllWindows()
    return name



def economy(a):
    string = ""
    for i in a:
        if i == '':
            string = string + "👥\n"
        else:
            string = string + i + "\n"
    string = string + "👥\n"
    string = string + "#экономикарф #экономикароссии #economyrus "
    return string


def array_to_string(a):
    responde = ''
    for i in a:
        responde = responde + i
    return responde


def divide_to_words(s):
    symbols = [".", ",", ":", "!", "?", " ", '', '\n', "«", '»' '—', '-', '&']
    w = ''
    words = []
    for i in range(len(s)):

        if s[i] in symbols:
            if w != '':
                words.append(w)
                w = ''
            words.append(s[i])
        else:
            w = w + s[i]
    words.append(w)
    return words


def parse_string(s):
    s = s + "\n"
    k = ""
    a = []

    for i in s:
        if i != "":
            if i == "\n":
                a.append(k.strip())
                k = ""
            else:
                k = k + i
    return a


def find_hastags(s):
    hash_tags = ''
    keywords = {'коронавирус': '#covid-19 #коронавирус #коронавирус2020 #коронавирусмир #коронавируснаяинфекция',
                'кредит': '#кредит2020 #кредитрф',
                'covid-19': '#covid-19 #коронавирус #коронавирус2020 #коронавирусмир #коронавируснаяинфекция',
                'коронавирусная': '#covid-19 #коронавирус #коронавирус2020 #коронавирусмир #коронавируснаяинфекция',
                'зеленский': '#слуганарода #президентукраины #украина2020'}

    words = divide_to_words(s)
    print(words)
    words.append(" ")
    for i in range(len(words)):
        if words[i].istitle() and words[i + 2].istitle() and (words[i] not in hash_tags) and (words[i + 2]
                                                                                              not in hash_tags):
            if (len(words) - 1 < i + 3) and words[i + 3].istitle():
                hash_tags += f'#{words[i]}{words[i + 2]}{words[i + 3]} '
            else:
                hash_tags += f'#{words[i]}{words[i + 2]} '
        elif words[i].istitle() and (words[i - 3] != "." or words[i - 1] != '\n' or words[i - 2] != '.' and
                                                                                        (words[i] not in hash_tags)):
            hash_tags += f"#{words[i]} "
        elif words[i].lower() in keywords and keywords[words[i].lower()] not in hash_tags:
            hash_tags += f'{keywords[words[i].lower()]} '

    return hash_tags
