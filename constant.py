

voiceMap = {
    "芊芊": "zh-CN-XiaoxiaoNeural",
    "马长老": "zh-CN-YunjianNeural",
    "云溪": "zh-CN-YunxiNeural",
    "系统": "zh-CN-YunxiaNeural",
    "李青阳": "zh-TW-YunJheNeural",
    "李家主": "zh-CN-YunyangNeural",
    "吃瓜群众": "zh-CN-liaoning-XiaobeiNeural",
    "群众": "zh-CN-shaanxi-XiaoniNeural",
    "娇声公主二号": "zh-CN-XiaoyiNeural",
    "温柔女主三号": "zh-TW-HsiaoChenNeural",
    "温柔女主四号": "zh-TW-HsiaoYuNeural",
    "虎啸宗执事": "zh-CN-YunjianNeural",
    "大刀帮长老": "zh-CN-YunyangNeural",
    "管家": "zh-CN-YunjianNeural",
    "苏锦": "zh-CN-XiaoyiNeural",
    "女子": "zh-TW-HsiaoChenNeural",
    "子吟": "zh-CN-YunxiaNeural",
    "赵熙悦": "zh-CN-XiaoxiaoNeural",
    "姚月": "zh-TW-HsiaoChenNeural",
    "韦一怒": "zh-CN-YunyangNeural",
    "旁白": "zh-CN-YunjianNeural",
    "路人甲": "zh-CN-YunjianNeural",
}

voiceArray = ["芊芊",
              "君常笑",
              "云溪",
              "马长老",
              "李家主",
              "系统",
              "老刀疤",
              "虎啸宗执事",
              "大刀帮长老",
              "群众",
              "吃瓜群众",
              "娇声公主二号",
              "温柔女主三号",
              "温柔女主四号",
              "管家",
              "苏锦",
              "女子",
              "子吟",
              "赵熙悦",
              "姚月",
              "韦一怒",
              "旁白",
              "路人甲"]


voice_map_en = {
    "JennyNeural": "en-US-JennyNeural",
    "GuyNeural": "en-US-GuyNeural",
    "AriaNeural": "en-US-AriaNeural",
    "DavisNeural": "en-US-DavisNeural",
    "ChristopherNeural": "en-US-ChristopherNeural",
    "EricNeural": "en-US-EricNeural",
    "MichelleNeural": "en-US-MichelleNeural",
    "RogerNeural": "en-US-RogerNeural",
    "SteffanNeural": "en-US-SteffanNeural",
}

voice_array_en = [
              "JennyNeural",
              "GuyNeural",
              "AriaNeural",
              "DavisNeural",
              "ChristopherNeural",
              "EricNeural",
              "MichelleNeural",
              "RogerNeural",
              "SteffanNeural",
            ]


size_mapping = {
    "16:9": (1920, 1080),
    "9:16": (720, 1280),
}

merge_array = ["今天星期天",
               "捡了200块钱",
               "准备去偷鸡",
               "被发现了",
               "壮烈激战",
               "挨了不少打",
               "跑了",
               "200块丢了明天星期一",
               ]

sizeArray = ["16:9", "9:16", ]

transform_list = ["默认", "随机", "左移动", "上移动", "放大"]

transform_random_list = ["left", "up", "zoom"]

transform_dict = {"默认": "non", "随机": None, "左移动": "left", "上移动": "up", "放大": "zoom"}

image_extensions = (".jpg", ".jpeg", ".png", ".PNG")

title_sequence_list = ["None", "word", "video"]

audio_path = "./source/audio/"
video_path = "./source/video/"
effcet_path = "./source/effcet/"
sound_path = "./source/asset/sound/"