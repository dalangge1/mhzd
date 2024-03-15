from moviepy.video.VideoClip import TextClip
from moviepy.video.compositing.concatenate import concatenate_videoclips

import constant
import novel_tools
import re

def process_subtitle(text= None, duration = 0 , size = None):
    text_clips = []
    if text != None and text != "":
        fade_duration = 0.5
        sentences = re.split(r'(?<=[.?!。？！，,])', text)
        sentences = [s.strip() for s in sentences if s.strip()]
        # 字幕处理
        for c_text in sentences:
            rendering_text = remove_trailing_punctuation(c_text)
            text_clip = TextClip(rendering_text, font='./source/asset/Songti_1.ttc', fontsize=novel_tools.font_size(size),
                                 color='white', stroke_color="lightblue", bg_color="black", stroke_width=0.8)
            text_clip = text_clip.set_duration(test_time(text, c_text, duration)).crossfadein(
                fade_duration).crossfadeout(fade_duration)
            text_clip = text_clip.set_position(("center", 0.84), relative=True)
            text_clips.append(text_clip)
            pass

    # 合成文本剪辑
    offset = 0.84 if size == "9:16" else 0.9
    text_video = concatenate_videoclips(text_clips).set_position(("center", offset), relative=True)
    return text_video



def test_time(text, c_text, duration):
    num_sentences = len(text)
    time_per_sentence = duration / num_sentences
    return time_per_sentence * len(c_text)

def remove_trailing_punctuation(text):
    pattern = r'[.?!。？！，,]+$'
    match = re.search(pattern, text)
    if match:
        text = text[:match.start()]
    return text