from __future__ import division, print_function, absolute_import

import argparse
import os
import numpy as np
import cv2
import tensorflow as tf
from configuration import Config
from data.dataloader import DetectionDataset, DataLoader

def print_model_summary(network):
    sample_inputs = tf.random.normal(shape=(Config.batch_size, Config.get_image_size()[0], Config.get_image_size()[1], Config.image_channels))
    sample_outputs = network(sample_inputs, training=True)
    network.summary()
    
if __name__ == "__main__":
    gpu = tf.config.list_physical_devices("GPU: 0")

    #get MOT dataset
    train_dataset = DetectionDataset()
    train_data, train_size = train_dataset.generate_datatset()

    data_loader = DataLoader()
    steps_per_epoch = tf.math.ceil(train_size / Config.batch_size)
    
    centernet = CenterNet()
    print_model_summary(centernet)

    