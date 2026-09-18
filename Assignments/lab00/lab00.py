# -*- coding: utf-8 -*-
"""Lab 00 — Introduction: Simple Image Processing.

Welcome to your first lab!  The goal is to get comfortable with the lab
workflow: implement a class in this file, run an evaluation script to see your
results.

Task
----
Implement the two methods inside the SimpleImageProcessing class:

  add_blur(image, **kwargs)
      Apply Gaussian blur to image.  Use the 'ksize' keyword argument
      (default 15) to control the kernel size (must be a positive odd integer).

  add_sharpen(image, **kwargs)
      Sharpen image using an unsharp-mask approach (subtract a blurred version
      from the original, scaled by a 'strength' keyword argument (default 1.5)).

Both methods should return the processed image as a uint8 numpy array with the
same shape as the input.
"""
import cv2
import numpy as np
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from helpers.dataloader import get_data_path, load_image  # noqa: F401


class SimpleImageProcessing:
   
    

    def add_blur(self, image, **kwargs):
        ksize = kwargs.get("ksize", 15)

        if ksize <= 0 or ksize % 2 == 0:
            raise ValueError("ksize must be a positive odd interger")

        return cv2.GaussianBlur(image, (ksize,ksize), 0)

    def add_sharpen(self, image, **kwargs):
        ksize = kwargs.get("ksize", 15)
        strength = kwargs.get("strength", 1.5)

        if ksize <= 0 or ksize % 2 == 0:
            raise ValueError("ksize must be a positive odd integer")

        blurred = cv2.GaussianBlur(image, (ksize, ksize), 0)

        image_float = image.astype(np.float32)
        blurred_float = blurred.astype(np.float32)

        sharpened = image_float + strength * (image_float - blurred_float)

        sharpened = np.clip(sharpened, 0, 255)

        return sharpened.astype(np.uint8)

image = cv2.imread("/workspaces/27076624lab00/Data/960px-Le_sacre_Coeur_bordercropped.jpg")

proc = SimpleImageProcessing()
blurred   = proc.add_blur(image, ksize=21)
sharpened = proc.add_sharpen(image, strength=2.0)
