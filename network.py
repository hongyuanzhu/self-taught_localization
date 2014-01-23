import numpy as np
from skimage import io
import os
try:
    from decaf.scripts.imagenet import DecafNet
except: 
    print "Warning: Decaf not loaded. \n"
try:
    import caffe.imagenet
except:
    print "Warning: Caffe not loaded. \n"


class Network:
    """Network class"""

    def __init__(self):
        raise NotImplementedError()

    def evaluate(self, img, layer_name = 'softmax'):
        """Evaluate the network given a an image, and export the layer
        named 'layer_name'.
        The 'layer_name' can be:
        - 'softmax'
        - 'fc7_relu' (Note: Decaf only)
        - 'fc7' (Note: Decaf only)
        - 'fc6_relu' (Note: Decaf only)
        - 'fc6' (Note: Decaf only)
        - 'pool5' (Note: Decaf only)

        image: ndarray.uint8
        layer_name: string
        """
        raise NotImplementedError()

    def get_mean_img(self):
        """
        Returns the unique label id \in {0, ..., num_labels-1}
        """
        raise NotImplementedError()
    
    def get_label_id(self, label):
        """
        Returns the unique label id \in {0, ..., num_labels-1}
        """
        raise NotImplementedError()

    def get_label_desc(self, label):
        """
        Returns a textual description of the label
        """
        raise NotImplementedError()

    def get_labels(self):
        """
        Returns the list of labels (in order of id) that the network can use
        """
        raise NotImplementedError()

#=============================================================================

class NetworkDecaf(Network):
    """
    Implementation for the Decaf library.
    """
    def __init__(self, model_spec_filename, model_filename,\
                 wnid_words_filename):
        # load Decaf model
        self.net_ = DecafNet(model_filename, model_spec_filename)
        # build a dictionary label --> description
        self.dict_label_desc_ = {}
        dict_desc_label = {}
        fd = open(wnid_words_filename)
        for line in fd:
            temp = line.strip().split('\t')
            wnid = temp[1].strip()
            self.dict_label_desc_[wnid] = temp[2].strip()
            dict_desc_label[temp[2].split(',')[0]] = wnid
        fd.close()
        # build a dictionary label --> label_id
        self.dict_label_id_ = {}
        self.labels_ = []
        for i, desc in enumerate(self.net_.label_names):
            self.dict_label_id_[dict_desc_label[desc]] = i
            self.labels_.append(dict_desc_label[desc])
        # Load the mean vector from file
        self.net_.mean_img = np.mean(np.mean(self.net_._data_mean,axis=1),axis=0) # mean of 3 channels
        self.net_.mean_img = self.net_.mean_img[::-1]   # it is in BGR convert in RGB
        
    def get_mean_img(self):
        return self.net_.mean_img

    def get_label_id(self, label):
        return self.dict_label_id_[label]

    def get_label_desc(self, label):
        return self.dict_label_desc_[label]

    def get_labels(self):
        return self.labels_

    def evaluate(self, img, layer_name = 'softmax'):
        scores = self.net_.classify(img, center_only=True)
        if layer_name == 'softmax':
            return scores
        elif layer_name == 'fc7_relu':
            layer_name = 'fc7_neuron_cudanet_out'
        elif layer_name == 'fc7':
            layer_name = 'fc7_cudanet_out'
        elif layer_name == 'fc6_relu':
            layer_name = 'fc6_neuron_cudanet_out'
        elif layer_name == 'fc6':
            layer_name = 'fc6_cudanet_out'
        elif layer_name == 'pool5':
            layer_name = 'pool5_cudanet_out'
        else:
            raise ValueError('layer_name not supported')
        return self.net_.feature(layer_name)

#=============================================================================

class NetworkCaffe(Network):
    """
    Implementation for the Caffe library.
    """
    def __init__(self, model_spec_filename, model_filename,\
                 wnid_words_filename, mean_img_filename, \
                 caffe_mode = 'cpu'):
        # load Caffe model
        # *** TODO ***
        # center_only should be True, but PyCaffe has a bug
        # which makes the software crash :-/
        self.net_ = caffe.imagenet.ImageNetClassifier( \
                            model_spec_filename, model_filename, \
                            center_only = False)
        self.net_.caffenet.set_phase_test()
        if caffe_mode == 'cpu':
            self.net_.caffenet.set_mode_cpu()
        elif caffe_mode == 'gpu':
            self.net_.caffenet.set_mode_gpu()
        else:
            raise ValueError('caffe_mode not recognized')
        # build a dictionary label --> description
        # and a dictionary label --> label_id
        self.dict_label_desc_ = {}
        self.dict_label_id_ = {}
        self.labels_ = []
        fd = open(wnid_words_filename)
        line_number = 0
        for line in fd:
            wnid = line[0:9].strip()
            words = line[10:].strip()
            self.dict_label_desc_[wnid] = words
            self.dict_label_id_[wnid] = line_number
            self.labels_.append(wnid)
            line_number += 1
        fd.close()
        # Load the mean vector from file
        self.net_.mean_img = np.load(os.path.join(os.path.dirname(__file__), mean_img_filename))
        self.net_.mean_img = np.mean(np.mean(self.net_.mean_img,axis=1),axis=0) # mean of 3 channels
        self.net_.mean_img = self.net_.mean_img[::-1]   # it is in BGR convert in RGB

    def get_mean_img(self):
        return self.net_.mean_img
    
    def get_label_id(self, label):
        return self.dict_label_id_[label]

    def get_label_desc(self, label):
        return self.dict_label_desc_[label]

    def get_labels(self):
        return self.labels_

    def evaluate(self, img, layer_name = 'softmax'):
        if layer_name == 'softmax':
            return self.net_.predict(img)
        else:
            raise ValueError('layer_name not supported')