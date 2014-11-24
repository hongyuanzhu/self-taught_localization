from util import *
import numpy as np
import os
import os.path
import skimage.io
from vlg.util.parfun import *

from configuration import *
from compute_statistics_exp import *
import exp32

if __name__ == "__main__":
    # load configurations and parameters
    conf = Configuration()
    params = exp32.Params()
    # experiment name
    params.exp_name = 'exp32_01'
    # input (GT AnnotatatedImages)
    params.exp_name_input = 'exp03_05'
    # Num elements in batch (for decaf/caffe eval)
    params.batch_sz = 1
    # default Configuration, image and label files
    params.conf = conf
    # select network: 'CAFFE' or 'DECAF'
    params.classifier = 'CAFFE'
    params.center_only = True
    # select top C classes used to generate the predicted bboxes
    params.topC = 5     # if 0, take the max across classes
    # method for calculating the confidence
    params.heatextractor_confidence_tech = 'full_obf_positive'
    # obfuscation search params
    params.min_sz_segm = 5 # keep this low (because we resize!!)
    params.alpha = 1/4.0*np.ones((4,))
    params.function_stl = 'similarity+cnnfeature'
    params.obfuscate_bbox = True
    params.use_fullimg_GT_label = True      # not actually using the GT_label...
    params.use_fullimg_top5_estimate = True # use convnet estimate instead of GT
    params.nms_iou_threshold = 0.5
    # input/output directory
    params.output_dir = conf.experiments_output_directory \
                        + '/' + params.exp_name
    params.input_dir = conf.experiments_output_directory \
                        + '/' + params.exp_name_input
    # parallelize the script on Anthill?
    params.run_on_anthill = True
    # list of tasks to execute
    params.task = []
    logging.info('Started')
    # RUN THE EXPERIMENT
    if 1:
        exp32.run_exp(params)
