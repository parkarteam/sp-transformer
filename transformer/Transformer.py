import goslate
import numpy as np

class Transformer():
    def __init__(self):
    	self.gs = goslate.Goslate()



    def transform_input(self, text_msg, feature_names=None):
               return np.array([text_msg[0]])

