from util import *
import numpy as np
import os
import os.path
import skimage.io
from vlg.util.parfun import *

from compute_statistics_exp import *
from configuration import *
import exp21

if __name__ == "__main__":
    # load configurations and parameters  
    conf = Configuration()
    params = exp21.Params()
    # experiment name
    params.exp_name = 'exp21_03'
    # take results from here
    params.exp_name_input = ['exp06_19', 'exp06_20']
    # default Configuration, image and label files
    params.conf = conf
    # max size of the HTML images
    params.html_max_img_size = 300
    # input/output directory
    params.output_dir = conf.experiments_output_directory \
                        + '/' + params.exp_name
    params.input_dirs = []
    for name in params.exp_name_input:
        params.input_dirs.append(conf.experiments_output_directory \
                                 + '/' + name)
    # Set jobname in case the process stop or crush
    params.run_on_anthill = True
    params.task = []
    logging.info('Started')
    # RUN THE EXPERIMENT
    if 1:
        exp21.run_exp(params)
    # RUN THE STATISTICS PIPELINE
    if 1:
        compute_statistics_exp(input_exp=params.exp_name)

