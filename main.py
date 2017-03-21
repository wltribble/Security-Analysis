#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
  Name: Will Tribble
  Student ID: 10540462
  Email: wltribbl@go.olemiss.edu
  Course Information: CSCI 343 - Section 01
  Program Source File Name: main.py
  Programming Assignment: 03
  References:
  Program Description: this program takes surveillance footage and highlights areas of certain degrees of motion
  Due Date: Friday, 3/10/2017, 11:59 am

  In keeping with the honor code policies of the University of Mississippi, the School of
  Engineering, and the Department of Computer and Information Science, I affirm that I have
  neither given nor received assistance on this programming assignment. This assignment
  represents my individual, original effort.
  ... My Signature is on File.
"""
# import statements
from PIL import Image
import matplotlib.pyplot as mplot
import numpy as np
import os

# reading in the photos, creating a blank average image list, and initializing file count to 0
files = os.listdir("starbucks")
avg_img = []
file_ct = 0

# getting the input for standard deviation threshold
sdev_threshold = input("\nEnter your change threshold: ")

# looping through the photo files to create the average image
for i in range(0, len(files)):
    if "jpg" in files[i]:
        img = Image.open("starbucks/" + files[i])
        img = np.float32(img)
        file_ct += 1
        try:
            avg_img += img
        except:
            avg_img = img
avg_img /= file_ct
avg_img = avg_img.clip(0,255)

# calculating the variance sum
for i in range(0, len(files)):
    if "jpg" in files[i]:
        img = Image.open("starbucks/" + files[i])
        img = np.float32(img)
        variance = img - avg_img
        variance *= variance
        try:
            sumVariance += variance
        except:
            sumVariance = variance

# calculating the standard deviation
sdev = np.sqrt(sumVariance / file_ct)
sdev = sdev.clip(0,255)
sdev = np.uint8(sdev)

# convert average image to normal configuration
avg_img = np.uint8(avg_img)

# initializing the highlighted image to the average image
highlighted_img = avg_img
# checking whether each pixel in the standard deviation image is above the standard deviation threshold
for row in range(len(avg_img)):
    for col in range(len(avg_img[row])):
        # count to make sure all 3 RGB values are above the threshold
        if (sum(sdev[row][col]) > float(sdev_threshold)):
            highlighted_img[row][col] = [255.0, 0.0, 0.0]
        else:
            continue

# displaying the image
mplot.imshow(highlighted_img)
mplot.show()
