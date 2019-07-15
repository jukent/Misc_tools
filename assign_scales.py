# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 19:47:57 2019

@author: julia
"""
import numpy as np
import random

def assign_scales(number_of_scales, modality):
    """
    number_of_scales: defines how many scales will be listed
    
    modality: must enter key from list [0: 'Major', 1: 'Natural Minor', 
    2: 'Harmonic Minor', 3: 'Melodic Minor', 4: 'All Modalities']
    """
    tonic = ['C#', 'F#', 'B', 'E', 'A', 'G', 'C', 'F', 'B♭', 'E♭', 'A♭', \
             'D♭', 'G♭', 'C♭']
    modes = [' Major', ' Natural Minor', ' Harmonic Minor', ' Melodic Minor']

    assert any(np.arange(0,len(modes)+1) == modality), \
           'Input modality must be a number from 0 to ' + str(len(modes)) + \
           '. See documentation for key assignment'
        
    possible_scales = np.ravel([[t + modes[m] for t in tonic] for m in \
                                  np.arange(0,len(modes))]) if modality == 4 \
                                  else [t + modes[modality] for t in tonic]
    
    try:
       scale_indices  = random.sample(range(0,len(possible_scales)),number_of_scales)
       [print(possible_scales[i]) for i in scale_indices]
    except ValueError:
        print('Requested number of scales exceeded number of potential scales.')
    return;
    
    
        
    