import random

import numpy as np
import tensorflow as tf

# i don't know why below import needed

from six.moves import xrange




_buckets = [ (5,10), (10,15), (20,25), (30,40), (40,50) ] 


def read_data(source_path, target_path, max_size=None): 
	""" Read data from source and targt files and put into buckets.

	Args:
	source_path : path to the files with token-ids for the Question (source)	
	target_path : path to the files with token-ids for the Answer (target)

	it must be aligned with the source file : n-th line contains the desired output
	for n-th line from the source_path

	max_size : maximum number of lines to read, all other will be ignored;
		   if 0 or None, data files will be read completely ( no limit )

	Returns:
		data_set : a list of length len(_buckets); 
			   data_set[n] contains a list of (source, target) paris read from the
			   provided data filed that fit into the n-th bucket
			   i.e., such that len(source) < _buckets[n][0] and
			                   len(target) < _buckets[n][1] 
			         source and target are lists of token-ids.
        """

	
	data_set = [  []  for _ in _ buckets ]
	

	
     

   



