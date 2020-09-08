import numpy as np
import click
class Transformer():
    def __init__(self):
    	print(" Starting transformer...")

    def transform_input(self, text_msg, feature_names=None):
            click.echo('inside transform_input text_msg: %s' %text_msg)    
            click.echo('inside transform_input processed value: %s' %np.array([text_msg[0]]))    
            return np.array([text_msg[0]])

