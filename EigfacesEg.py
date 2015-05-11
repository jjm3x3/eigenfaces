#!/usr/bin/python

import os
import scipy
import scipy.misc as misc
from scipy import ndimage
#import Image

import numpy as np
import numpy.linalg as lin

# total count of faces
L = 2 #687

# list file directories
basedir = 'D:\\Users\\jmeixner\\Documents\\SchoolWork\\eigFaces\\'
facesdir = basedir + 'fas\\'
flist = os.listdir(facesdir)

# create zero array
arr = np.zeros((L, 43621))

num = -1

# load data matrix out of PGM files
for f in flist:
  num += 1
  # construct target
  tfile = facesdir + str(f)

  print "Opening:", tfile
  l = misc.lena()
  im = misc.imread(tfile)

  #graying out the image
  gray = np.zeros((im.shape[0],im.shape[1]))
  for i in xrange(im.shape[0]):
    for j in xrange(im.shape[1]):
      gray[i,j] = (im[i,j,0] + im[i,j,1] + im[i,j,2]) / 3
      
  #scipy.misc.imsave(basedir + 'tmp\\' + str(f) + '_gray.png',gray)

  print "Storing image in memory matrix"
  for i in xrange(im.shape[0]):
    for j in xrange(im.shape[1]):
      arr[num,(j) + i * im.shape[1]] = gray[i,j]

# subtract the mean image from each image sample
for i in xrange(arr.shape[1]):
  arr[:,i] = arr[:,i] - np.mean(arr,1)

S = np.cov(np.transpose(arr))

# V here are the eigenvecotrs of the covarience matrix
# this makes them the eigen faces
e, V = lin.eig(S)


    # compute SVD of the data matrix
    #print "Computing sparse SVD of data matrix"
    #U, V, T = lin.svd(arr.transpose(), full_matrices=True)

# print eigenfaces to files
print "Writing eigenvectors to disk..."
for i in xrange(L):
  print i
  scipy.misc.imsave(basedir + 'eigFaces\\' + str(i) + '.png', U[:,i].reshape(U.shape[0],1))


