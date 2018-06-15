import numpy as np
from skimage import color
import numpy as np
from scipy.spatial import KDTree
from random import random, uniform, randint

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


def rangecolor(n, start_rgb, end_rgb, max_value=255):
    assert len(start_rgb) == 3
    start_rgb = np.expand_dims(
        np.expand_dims(start_rgb, axis=0), axis=0)/max_value
    start_hsv = np.squeeze(color.rgb2hsv(start_rgb))
    
    end_rgb = np.expand_dims(
        np.expand_dims(end_rgb, axis=0), axis=0)/max_value
    end_hsv = np.squeeze(color.rgb2hsv(end_rgb))
    
    h_start, s_start, v_start = start_hsv
    h_end, s_end, v_end = end_hsv
    
    H = np.expand_dims(np.linspace(h_start, h_end, n), axis=0)
    S = np.expand_dims(np.linspace(s_start, s_end, n), axis=0)
    V = np.expand_dims(np.linspace(v_start, v_end, n), axis=0)
    
    HSV = np.transpose(np.concatenate([H,S,V], axis=0))
    
    RGB = []
    for hsv in HSV:
        hsv = np.expand_dims(
            np.expand_dims(hsv, axis=0), axis=0)
        rgb  = np.squeeze(color.hsv2rgb(hsv)) * max_value
        RGB.append(rgb)
    
    return np.array(RGB)


def poisson_disc_sampling(n, gen_candidate=None, n_candidates=150):
    """ generate random-evenly spaced points
    """
    if gen_candidate is None:
        gen_candidate = lambda: (random(), random())  # between 0..1

    data = [gen_candidate()]

    for _ in range(1, n):
        lookup = KDTree(data)

        best_cand = None
        best_dist = 0

        for _ in range(n_candidates):  # find best candidate
            cand = gen_candidate()
            dist, _ = lookup.query(cand)
            if best_dist < dist:
                best_dist = dist
                best_cand = cand
        assert best_cand is not None  # make sure best candidate exists
        data.append(best_cand)

    return data

def poisson_disc_sampling_Lab(n):
    """ randomly sample colors from Lab space
    """
    gen_ab_candidate = lambda: \
        (uniform(30, 100), uniform(-127, 128), uniform(-127, 128))
    Samples = poisson_disc_sampling(n, gen_candidate=gen_ab_candidate)
    Lab = np.array([(L, a, b) for L,a,b in Samples])
    Lab = np.array([Lab], 'float64')  # elevate dims to fit conversion
                                      # libraries API
    RGB = color.lab2rgb(Lab) * 255
    return np.squeeze(RGB.astype('uint8'))
