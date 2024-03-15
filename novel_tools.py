import os
import re
import time

import cv2
from PIL import Image
from moviepy.editor import ImageClip

import constant
import real_gan



def path(path_name, type):
    directory = os.path.dirname(os.path.abspath(__file__))
    timestamp = int(time.time())
    file_path = f"source/{path_name}/{timestamp}.{type}"
    file_name = os.path.join(directory, file_path)
    return file_name

def custom_video_path(path_name):
    timestamp = int(time.time())
    file_path = f"{path_name}/{timestamp}.mp4"
    return file_path

def custom_video_result_path(path_name):
    timestamp = int(time.time())
    result_folder = f"{path_name}/result"

    if not os.path.exists(result_folder):
        os.makedirs(result_folder)
    file_path = f"{result_folder}/{timestamp}.mp4"
    return file_path

def sound_rename():
    return path("sound", "mp3")


def video_rename():
    return path("video", "mp4")


def result_rename():
    return path("result", "mp4")


def effcet_rename():
    return path("effcet", "mp4")


def effcet_rename_mov():
    return path("effcet", "mov")


def audio_rename():
    return path("audio", "mp3")


def image_rename():
    return path("image", "jpg")


def resize_image(image_path, w, h, repair=False, crop_fit=False):
    if crop_fit == True:
        new_image_path = crop_to_fit_screen(image_path, w, h)
    else:
        new_image_path = crop_image(image_path, w, h)

    if repair == True:
        real_gan.inference_gan(new_image_path)
    image_clip = ImageClip(new_image_path)
    os.remove(new_image_path)
    return image_clip


def crop_image(image_path, w, h, repair=False):
    original_image = cv2.imread(image_path)
    w, h = int(w), int(h)
    resized_image = cv2.resize(original_image, (w, h))
    new_image_path = image_rename()
    cv2.imwrite(new_image_path, resized_image)
    return new_image_path


def crop_to_fit_screen(image_path, w, h, repair=False):
    # 打开图像
    img = Image.open(image_path)

    # 获取图像的原始尺寸
    img_width, img_height = img.size

    # 计算屏幕和图像的宽高比例
    screen_ratio = w / h
    image_ratio = img_width / img_height

    # 根据不同的宽高比例进行裁剪
    if screen_ratio > image_ratio:
        # 屏幕更宽，裁剪图像的高度以匹配屏幕高度
        new_height = int(img_width / screen_ratio)
        top_margin = (img_height - new_height) // 2
        bottom_margin = img_height - (top_margin + new_height)
        img = img.crop((0, top_margin, img_width, img_height - bottom_margin))
    else:
        # 屏幕更高，裁剪图像的宽度以匹配屏幕宽度
        new_width = int(img_height * screen_ratio)
        left_margin = (img_width - new_width) // 2
        right_margin = img_width - (left_margin + new_width)
        img = img.crop((left_margin, 0, img_width - right_margin, img_height))
    cropped_image = img.convert("RGB")
    new_image_path = image_rename()
    # 保存裁剪后的图像
    cropped_image.save(new_image_path)
    return new_image_path


def font_size(size = None):
    if size == "16:9":
        return 54
    if size == "4:3":
        return 36
    if size == "1:1":
        return 26
    if 9 / 16:
        return 30
    if 21 / 9:
        return 50
    if size == "32:9":
        return 56
    return 44


def background_audio(title):
    directory = os.path.dirname(os.path.abspath(__file__))
    file_path = f"source/asset/mp3/{title}.mp3"
    file_name = os.path.join(directory, file_path)
    return file_name


# 自定义排序函数，从文件名中提取数字并进行比较
def extract_number(filename):
    # 使用正则表达式从文件名中提取数字部分
    match = re.search(r'\d+', filename)
    if match:
        return int(match.group())
    else:
        return 0  # 如果文件名中没有数字，则返回0


def delete_file(file_path):
    for filename in os.listdir(file_path):
        full_path = os.path.join(file_path, filename)
        if os.path.isfile(full_path):
            os.remove(full_path)
            print(f"已删除文件: {full_path}")


def text_process(text="{暴力枪}累死爷了 不过已经招收了十名中品灵根{一拳}四十个凡品灵根。"):
    voice = ""
    for v in constant.voiceArray:
        if text.startswith(v + ":"):
            split_result = text.split(v + ":")
            if len(split_result) == 2:
                text = split_result[1]
                voice = v
                break

    matches = re.finditer(r'\{([^}]+)\}', text)

    sounds = []

    for match in matches:
        content = match.group(0)
        start = match.start()
        end = match.end()
        sounds.append((content, start, end))

    # 打印找到的花括号内容和位置
    for content, start, end in sounds:
        print(f"内容: {content}, 位置: ({start}, {end})")

    # 从文本中删除花括号内容
    top = 0
    for content, start, end in sounds:
        # text = text[:(start - top)] + text[(end - top):]
        # top = end - start
        text = text.replace(content, "")
    # 打印删除花括号内容后的文本
    print("删除花括号内容后的文本:", text)
    if voice == "":
        return (text, sounds)
    else:
        return (voice + ":" + text, sounds)

