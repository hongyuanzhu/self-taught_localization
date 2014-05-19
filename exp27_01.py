from util import *
import numpy as np
import os
import os.path
import skimage.io
from vlg.util.parfun import *

from heatmap import *
from network import *
from configuration import *
from imgsegmentation import *
from heatextractor import *
from htmlreport import *
import exp27

if __name__ == "__main__":
    conf = Configuration()
    params = exp27.Params()
    # experiment name
    params.exp_name = 'exp27_01'
    # which subset? train or val
    params.subset = 'train'
    # Only classes that overlap with ILSVRC2012? (i.e. 150, instead of 200)
    params.overlap_ilsvrc2012 = True
    # default Configuration, image and label files
    params.conf = conf
    # we first resize each image to this size, if bigger
    params.fix_sz = 600
    # image transformation. it could be 'centered_crop', or 'original'
    params.image_transformation = 'original'
    # output directory
    params.output_dir = conf.experiments_output_directory \
                        + '/' + params.exp_name
    # number of output chunks (the number of databases to create)
    params.num_chunks = 1000
    # parallelize the script on Anthill?
    params.run_on_anthill = True
    # visualize images (for DEBUGGING)
    params.visualize_annotated_images = False
    # specify task to debug ([] process everything)
    params.task = []
    # RUN THE EXPERIMENT
    exp27.run_exp(params)