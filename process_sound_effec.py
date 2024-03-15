from constant import sound_path
from pydub import AudioSegment

def process_sound_effect(output_path, sounds=[{"name":"手枪", "begin": 0}]):
    audio = AudioSegment.from_file(output_path)
    for object in sounds:
        sound_effect = AudioSegment.from_file(sound_path + object["name"]+ ".mp3")
        #设置音效声音
        desired_volume = -10
        sound_effect_volume = sound_effect.set_channels(2)
        sound_effect_volume = sound_effect_volume + desired_volume
        if object["begin"] == 0:
            audio = sound_effect_volume + audio
        elif object["begin"] == 100:
            audio = audio + sound_effect_volume
        else:
            audio = audio.overlay(sound_effect_volume, position=object["begin"] * 1000)
    audio.export(output_path, format="mp3")
    return output_path