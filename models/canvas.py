from PIL import Image
import numpy as np


class Canvas:
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

        #
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        #
        self.data[:] = self.color

    def make(self, filename):
        img = Image.fromarray(self.data, mode='RGB')
        img.save(f'output/{filename}.png')
