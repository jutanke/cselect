import numpy as np
from skimage import color
import numpy as np
from random import uniform

def lincolor(n, random_sat=False, random_val=False):
    """ returns linearly sampled colors from HSV space
        with randomised Saturation and Value
    """
    HSV = []
    for h in np.linspace(0, 1, n):
        HSV.append((h, 
                    uniform(0.6, 1) if random_sat else 1, 
                    uniform(0.5, 1) if random_val else 1))
    HSV = np.array([HSV], 'float64')
    RGB = color.hsv2rgb(HSV) * 255
    return np.squeeze(RGB).astype('uint8')