import os
import time

import edge_tts
import asyncio
import constant


def audio_process(_text, voice, output_path=None, rate=15, volume=15,  language=None):
    if _text is None and voice is None and rate is None and volume is None:
        return None

    if language == "en":
        voiceMap =  constant.voice_map_en
    else:
        #language == "zh":
        voiceMap = constant.voiceMap

    voice_name = voiceMap[voice]

    if rate is not None and rate > 0.0:
        rate_float = "+" + str(rate) + "%"
    else:
        rate_float = "-" + str(rate) + "%"
    if volume is not None and volume > 0.0:
        volume_float = "+" + str(volume) + "%"
    else:
        volume_float = "-" + str(volume) + "%"

    timestamp = int(time.time())
    file_name = f"{timestamp}.mp3"
    file_path= os.path.join(output_path, file_name)

    tts_processor = TTSProcessor(_text, voice_name, file_path, rate_float, volume_float)
    asyncio.run(tts_processor.text_to_speech())
    return file_path


class TTSProcessor:
    def __init__(self, text, voice, output, rate, volume):
        self.text = text
        self.voice = voice
        self.output = output
        self.rate = rate
        self.volume = volume

    async def text_to_speech(self):
        tts = edge_tts.Communicate(text=self.text, voice=self.voice, rate=self.rate, volume=self.volume)
        await tts.save(self.output)
