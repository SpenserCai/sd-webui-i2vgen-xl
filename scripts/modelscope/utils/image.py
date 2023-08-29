'''
Author: SpenserCai
Date: 2023-08-29 15:03:57
version: 
LastEditors: SpenserCai
LastEditTime: 2023-08-29 15:05:19
Description: file content
'''
import io
from typing import Any, Dict, Union

import cv2
import numpy as np
import PIL
from numpy import ndarray
from PIL import Image, ImageOps

class LoadImage:
    @staticmethod
    def convert_to_img(input) -> ndarray:
        if isinstance(input, str):
            img = load_image(input)
        elif isinstance(input, PIL.Image.Image):
            img = input.convert('RGB')
        elif isinstance(input, np.ndarray):
            if len(input.shape) == 2:
                img = cv2.cvtColor(input, cv2.COLOR_GRAY2BGR)
            img = input[:, :, ::-1]
            img = Image.fromarray(img.astype('uint8')).convert('RGB')
        else:
            raise TypeError(f'input should be either str, PIL.Image,'
                            f' np.array, but got {type(input)}')
        return img
    
def load_image(image_path_or_url: str) -> Image.Image:
    """ simple interface to load an image from file or url

    Args:
        image_path_or_url (str): image file path or http url
    """
    loader = LoadImage()
    return loader(image_path_or_url)['img']