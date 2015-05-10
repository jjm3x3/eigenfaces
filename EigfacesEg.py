#!/usr/bin/python

import os
import scipy
import scipy.misc as misc
from scipy import ndimage
#import Image

import numpy as np
import numpy.linalg as lin

# total count of faces
L = 687

# list file directories
basedir = 'D:\\Users\\jmeixner\\Documents\\SchoolWork\\fas'
flist = os.listdir(basedir)

# create zero array
arr = np.zeros((L, 512))

num = 0

# load data matrix out of PGM files
for f in flist:
  # construct target
  tfile = basedir + str(f)

  #try:
    print "Opening:", tfile
    l = misc.lena()
    im = misc.imread(basedir + f)
    
    print "Storing image in memory matrix"
    for i in xrange(im.size):
      pix = np.zeros(262144,1) 
      for j in xrange(512):
        pix += im[i]
        end
      print pix
      print type(pix)
      arr[i,:] = pix
      num += 1
 # except :
  #  pass

arr = arr / 256

print arr

# subtract the mean image from each image sample
for i in xrange(arr.shape[0]):
  arr[i,:] = arr[i,:] - arr.mean(0)

# compute SVD of the data matrix
print "Computing sparse SVD of data matrix"
U, V, T = lin.svd(arr.transpose(), full_matrices=False)

# print eigenfaces to files
print "Writing eigenvectors to disk..."
for i in xrange(L):
  scipy.misc.imsave(basedir + str(i) + '.png', U[:,i].reshape(192,128))

