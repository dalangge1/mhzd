# NovelT

## 描述

一个简单的推文视频制作工具，基于一些开源工具进行开发。

## 特征

- 图文视频生成

## 运行

安装conda环境

```python
git clone https://github.com/douhaohaode/NovelT.git
cd NovelT
conda create -n novelt python=3.10 -y  
conda activate novelt
pip install -r requirements.txt
python json_to_video.py
```

mac 为例:

1. 安装
```python
brew install tesseract
brew install tesseract-lang
```

## 字幕功能
使用了moviepy中的添加字幕功能需要安装[ImageMagick](https://www.imagemagick.org/script/index.php) 才能使用全部功能


## 三方库:
感谢下列开源工具排名不分先后
- [gradio](https://github.com/gradio-app/gradio)
- [moviepy](https://github.com/Zulko/moviepy)
- [gfpgan](https://github.com/TencentARC/GFPGAN)
- opencv-python
- edge_tts
