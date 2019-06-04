from scipy import misc
import tensorflow as tf
import numpy as np
import sys
import os
from mvnc import mvncapi as mvnc

class FaceEmbedderMovidiusFacenet:

    def __init__(self, movidius_id=0):

        dir_path = os.path.dirname(os.path.realpath(__file__))

        # Get a list of ALL the sticks that are plugged in
        # we need at least one
        devices = mvnc.EnumerateDevices()
        if len(devices) < movidius_id+1:
            print('Not enough devices found')
            quit()

        # Pick the first stick to run the network
        self.device = mvnc.Device(devices[0])

        # Open the NCS
        self.device.OpenDevice()

        # Read in the graph file to memory buffer
        graphfile = dir_path + "/model/20170512-110547_mvds/facenet_movidius_ncs.graph"
        with open(graphfile, mode='rb') as f:
            graph_in_memory = f.read()

        # create the NCAPI graph instance from the memory buffer containing the graph file.
        self.graph = self.device.AllocateGraph(graph_in_memory)

    def close(self):

        self.graph.DeallocateGraph()
        self.device.CloseDevice()

    def _prewhiten(self, x):

        mean = np.mean(x)
        std = np.std(x)
        std_adj = np.maximum(std, 1.0 / np.sqrt(x.size))
        y = np.multiply(np.subtract(x, mean), 1 / std_adj)
        return y

    def _preprocess_images(self, image_paths):

        img_list = []
        for image in image_paths:
            img = misc.imread(os.path.expanduser(image), mode='RGB')
            prewhitened = self._prewhiten(img)
            img_list.append(prewhitened)
        images = np.stack(img_list)
        return images

    def get_embeddings(self, image_paths):

        # Preprocess images
        images = self._preprocess_images(image_paths)

        # Send images to NCS
        self.graph.LoadTensor(images.astype(np.float16), None)

        # Get results from NCS
        output, userobj = self.graph.GetResult()

        return output