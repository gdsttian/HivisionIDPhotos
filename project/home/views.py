from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import os
from pathlib import Path

from project.home.forms import IDPhotoForm, PhotoMattingForm, PhotoCropForm, PhotoResizeForm
from project.home.utils import idphoto_inference, human_matting_inference, photo_add_background, \
    generate_layout_photos, watermark, set_kb, idphoto_crop_inference

from hivision.creator.choose_handler import HUMAN_MATTING_MODELS
from hivision import IDCreator
from hivision.error import FaceError
from hivision.creator.layout_calculator import (
    generate_layout_array,
    generate_layout_image,
)
from hivision.creator.choose_handler import choose_handler
from hivision.utils import (
    add_background,
    resize_image_to_kb,
    bytes_2_base64,
    base64_2_numpy,
    hex_to_rgb,
    add_watermark,
    save_image_dpi_to_bytes,
)

import base64
import numpy as np
import cv2

root_dir = Path(__file__).resolve().parent.parent.parent

# 获取存在的人像分割模型列表
# 通过检查 hivision/creator/weights 目录下的 .onnx 和 .mnn 文件
# 只保留文件名（不包括扩展名）
HUMAN_MATTING_MODELS_EXIST = [
    os.path.splitext(file)[0]
    for file in os.listdir(os.path.join(root_dir, "hivision/creator/weights"))
    if file.endswith(".onnx") or file.endswith(".mnn")
]

# 在HUMAN_MATTING_MODELS中的模型才会被加载到Gradio中显示
HUMAN_MATTING_MODELS_CHOICE = [
    model for model in HUMAN_MATTING_MODELS if model in HUMAN_MATTING_MODELS_EXIST
]

if len(HUMAN_MATTING_MODELS_CHOICE) == 0:
    raise ValueError(
        "未找到任何存在的人像分割模型，请检查 hivision/creator/weights 目录下的文件"
        + "\n"
        + "No existing portrait segmentation model was found, please check the files in the hivision/creator/weights directory."
    )

# 面部检测模型
FACE_DETECT_MODELS = ["face++ (联网Online API)", "mtcnn"]
FACE_DETECT_MODELS_EXPAND = (
    ["retinaface-resnet50"]
    if os.path.exists(
        os.path.join(
            root_dir, "hivision/creator/retinaface/weights/retinaface-resnet50.onnx"
        )
    )
    else []
)
FACE_DETECT_MODELS_CHOICE = FACE_DETECT_MODELS + FACE_DETECT_MODELS_EXPAND

# 语言选项
LANGUAGE = ["zh", "en", "ko", "ja"]

creator = IDCreator()


# Create your views here.
def index(request):
    return render(request, 'home/index.html', {})


def idphoto_form(request):
    form = IDPhotoForm()
    return render(request, 'home/idphoto.html', {'form': form})


class IDPhotoAPI(APIView):
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')

        return Response({'message': 'Success'}, status=status.HTTP_200_OK)


def human_matting(request):
    if request.method == "POST":
        form = IDPhotoForm(request.POST)
        if form.is_valid():

            return render(request, 'home/index.html', {})
    else:
        form = IDPhotoForm()

    return render(request, 'home/index.html', {})


def layout_photos(request):
    if request.method == "POST":
        form = IDPhotoForm(request.POST)
        if form.is_valid():

            return render(request, 'home/index.html', {})
    else:
        form = IDPhotoForm()

    return render(request, 'home/index.html', {})


def resize_photo(request):
    if request.method == "POST":
        form = IDPhotoForm(request.POST)
        if form.is_valid():

            return render(request, 'home/index.html', {})
    else:
        form = IDPhotoForm()

    return render(request, 'home/index.html', {})


def crop_photo(request):
    if request.method == "POST":
        form = IDPhotoForm(request.POST)
        if form.is_valid():

            return render(request, 'home/index.html', {})
    else:
        form = IDPhotoForm()

    return render(request, 'home/index.html', {})
