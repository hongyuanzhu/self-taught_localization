import os
from network import *
from configuration import *
import unittest


class NetworkDecafTest(unittest.TestCase):
    def setUp(self):
        self.conf = Configuration()
        self.net  = NetworkDecaf(self.conf.ilsvrc2012_decaf_model_spec,\
                                 self.conf.ilsvrc2012_decaf_model,\
                                 self.conf.ilsvrc2012_classid_wnid_words)

    def tearDown(self):
        self.net = None

    def test_get_label_id(self):
        self.assertEqual(self.net.get_label_id('n04201297'), 0)
        self.assertEqual(self.net.get_label_id('n03063599'), 1)
        self.assertEqual(self.net.get_label_id('n03961711'), 999)

    def test_get_label_desc(self):
        self.assertEqual(self.net.get_label_desc('n04201297'), 'shoji')
        self.assertEqual(self.net.get_label_desc('n03063599'), 'coffee mug')
        self.assertEqual(self.net.get_label_desc('n03961711'), 'plate rack')

    def test_get_labels(self):
        labels = self.net.get_labels()
        self.assertEqual(labels[0], 'n04201297')
        self.assertEqual(labels[1], 'n03063599')
        self.assertEqual(labels[999], 'n03961711')

    def test_evaluate(self):
        img = np.asarray(io.imread('ILSVRC2012_val_00000001_n01751748.JPEG'))
        scores = self.net.evaluate(img, layer_name = 'softmax')
        self.assertAlmostEqual(scores[0], 6.9254136e-09, places=5)
        self.assertAlmostEqual(scores[999], 1.2282071e-08, places=5)
        self.assertAlmostEqual(max(scores), 0.36385602, places=5)
        scores = self.net.evaluate(img, layer_name = 'fc6_relu')
        self.assertEqual(scores.shape[0], 1)
        self.assertEqual(scores.shape[1], 4096)
        self.assertAlmostEqual(scores[0,0], 0.0)
        self.assertAlmostEqual(scores[0,3], 6.447751, places=5)
        self.assertAlmostEqual(scores[0,564], 7.011354, places=5)
        self.assertAlmostEqual(scores[0,3530], 18.45673, places=5)

#=============================================================================

class NetworkCaffeTest(unittest.TestCase):
    def setUp(self):
        self.conf = Configuration()
        self.net = NetworkCaffe(self.conf.ilsvrc2012_caffe_model_spec,\
                                self.conf.ilsvrc2012_caffe_model,\
                                self.conf.ilsvrc2012_caffe_wnids_words,\
                                self.conf.ilsvrc2012_caffe_avg_image)

    def tearDown(self):
        self.net = None

    def test_get_label_id(self):
        self.assertEqual(self.net.get_label_id('n01440764'), 0)
        self.assertEqual(self.net.get_label_id('n01443537'), 1)
        self.assertEqual(self.net.get_label_id('n15075141'), 999)

    def test_get_label_desc(self):
        self.assertEqual(self.net.get_label_desc('n01440764'), \
                         'tench, Tinca tinca')
        self.assertEqual(self.net.get_label_desc('n01443537'), \
                         'goldfish, Carassius auratus')
        self.assertEqual(self.net.get_label_desc('n15075141'), \
                         'toilet tissue, toilet paper, bathroom tissue')

    def test_get_labels(self):
        labels = self.net.get_labels()
        self.assertEqual(labels[0], 'n01440764')
        self.assertEqual(labels[1], 'n01443537')
        self.assertEqual(labels[999], 'n15075141')

    def test_evaluate(self):
        img = np.asarray(io.imread('ILSVRC2012_val_00000001_n01751748.JPEG'))
        scores = self.net.evaluate(img, layer_name = 'softmax')
        self.assertAlmostEqual(scores[0], 1.11658719e-05, places=5)
        self.assertAlmostEqual(scores[999], 2.23165166e-08, places=5)
        self.assertAlmostEqual(max(scores), 0.361389, places=5)

#=============================================================================

if __name__ == '__main__':
    unittest.main()