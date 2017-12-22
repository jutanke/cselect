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