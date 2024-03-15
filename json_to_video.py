import json
from moviepy.editor import *

import constant
import novel_tools
import gradio as gr

import tts
from process_image_effect import precess_image_clip
from process_sound_effec import process_sound_effect
from process_subtitle import process_subtitle
from process_video import merge_video


def batch_video_process(inp = None, inp7 =None , ouput_path = None):
    json_object = json.loads(inp)

    background_music = json_object["background_music"]
    lines = json_object["lines"]
    novel_tools.delete_file(ouput_path)
    for line in lines:
        json_line = json.dumps(line, indent=4, ensure_ascii=False)
        video_process(json_line, inp7, ouput_path)

    output_file = merge_video(ouput_path,background_music)
    return  output_file

def video_process(inp = None , inp7 =None, ouput_path = None, audioPath = None ,size =None):

    width, height = 1920, 1080
    if inp7 in constant.size_mapping:
        width, height = constant.size_mapping[inp7]

    json_object = json.loads(inp)

    # 音频文件路径
    #if json_object["audio_path"] != "" :
    if "audio_path" in json_object and json_object["audio_path"] not in ["", None]:
        audioPath = json_object["audio_path"]
    else:
        voice = "云溪"
        if "tts" in json_object and json_object["tts"] not in ["", None]:
            voice = json_object["tts"]
        audioPath = tts.audio_process(json_object["subtitle"], voice, ouput_path)

    # 音效处理
    if "sound_effects" in json_object and json_object["sound_effects"] not in ["", None]:
        process_sound_effect(audioPath, sounds=json_object["sound_effects"])

    audio = AudioFileClip(audioPath)
    duration = audio.duration

    # 合成文本剪辑
    text_clip = process_subtitle(json_object["subtitle"],duration ,inp7)

    background_color = (255, 255, 255)  # 背景颜色（RGB）
    video = ColorClip((width, height), background_color, duration=duration)

    if json_object["image_path"] != "":
        inp = json_object["image_path"]

    shaken_clip = precess_image_clip(inp,duration,json_object ,width, height)
    final_clip = CompositeVideoClip([video, shaken_clip , shaken_clip.set_audio(audio), text_clip])

    output_file = novel_tools.custom_video_path(ouput_path)
    final_clip.write_videofile(output_file, codec='libx264', audio_codec='aac', fps=40)
    return output_file



json_data = {
    "subtitle": "世界上哪有那么多的岁月静好 都是有人在为我们负重前行 , 世界上哪有那么多的岁月静好 都是有人在为我们负重前行。",
    "audio_path": "/Users/wangjian/Desktop/测试/audio/王10s.mp3",
    "image_path": "/Users/wangjian/Desktop/测试/image/t1.png",
    "sound_effects": [
        {
            "name": "手枪",
            "begin": 2
        },
        {
            "name": "凶狗",
            "begin": 4
        }
    ],
    "video_effects": "右放大",
    "video_filters": [
        {
            "name": "灵魂出窍",
            "begin": 2,
            "end": 4
        },
        {
            "name": "震动",
            "begin": 5,
            "end": 7
        },
        {
            "name": "膨胀",
            "begin": 7,
            "end": 9
        }
    ]
}


json_lines = {
    "background_music": "壮烈激战",
    "lines": [
        {
            "subtitle": "世界上哪有那么多的岁月静好 都是有人在为我们负重前行 ",
            "audio_path": "/Users/wangjian/Desktop/测试/audio/王10s.mp3",
            "image_path": "/Users/wangjian/Desktop/测试/image/t1.png",
            "sound_effects": [
                {"name": "手枪", "begin": 2},
                {"name": "凶狗", "begin": 4}
            ],
            "video_effects": "右放大",
            "video_filters": [
                {"name": "抖动", "begin": 2, "end": 4},
                {"name": "灵魂出窍", "begin": 6, "end": 7}
            ]
        },
        {
            "subtitle": "这是个悲惨的世界 世界上全是乌鸦没其他的。",
            "audio_path": "/Users/wangjian/Desktop/测试/audio/王10s.mp3",
            "image_path": "/Users/wangjian/Desktop/测试/image/t2.png",
            "sound_effects": [
                {"name": "乌鸦", "begin": 4},
            ],
            "video_effects": "左放大",
            "video_filters": [
                {"name": "模糊", "begin": 2, "end": 4},
                {"name": "腐蚀", "begin": 6, "end": 8}
            ]
        }
    ]
}

# 转换为字符串
json_string = json.dumps(json_data, indent=4, ensure_ascii=False)

json_string1 = json.dumps(json_lines, indent=4, ensure_ascii=False)

with gr.Blocks() as demo:

    with gr.Tab("单片生成"):
        ouput_path = gr.Textbox(label="输出路径", value="/Users/wangjian/Desktop/测试/video" , interactive= True)
        inp = gr.Textbox(label="输入json文件", value=json_string ,lines=16 ,max_lines=16 , interactive= True)
        inp7 = gr.Radio(constant.sizeArray, label="尺寸", value=constant.sizeArray[0])
        video_file_path = gr.Video(label="视频", type="filepath")
        video_btn = gr.Button("生成")
        video_btn.click(fn=video_process, inputs=[inp,inp7,ouput_path],
                        outputs=video_file_path)

    with gr.Tab("批量生成"):
        ouput_path = gr.Textbox(label="输出路径", value="/Users/wangjian/Desktop/测试/video" , interactive= True)
        inp1 = gr.Textbox(label="输入json文件", value=json_string1 ,lines=8,max_lines=8, interactive= True)
        inp7 = gr.Radio(constant.sizeArray, label="尺寸", value=constant.sizeArray[0])
        video_file_path = gr.Video(label="视频", type="filepath")
        video_btn = gr.Button("生成")
        video_btn.click(fn=batch_video_process, inputs=[inp1,inp7,ouput_path],
                        outputs=video_file_path)
demo.launch()
