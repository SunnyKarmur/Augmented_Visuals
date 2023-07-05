"""

Sunny Karmur: Augmented Visuals with Homography


"""


import cv2
import numpy as np

from Augmented_Visuals_Homography_Source.homography import computeHomography, warp_and_augment, warp_and_augment_advanced

if __name__ == '__main__' : 
    # Read source image.
    im_logo = cv2.imread('C:/Users/sunny/Desktop/workshop/Github_projects/Augmented_Visuals_Homography/data/logo_Gators.png') # Please add your path to input image

    # Corners of the logo: (0, 0), (w, h), (w, 0), (0, h)
    pts_logo = np.array([[0, 0],[500, 0],[500, 275],[0, 280]]) 

    # Read destination image.
    im_dst = cv2.imread('C:/Users/sunny/Desktop/workshop/Github_projects/Augmented_Visuals_Homography/data/game_fl.jpg') # Please add your path to input image

    # Destination points (use Get_mouse_clicks.py to get these points)
    pts_dst = np.array([[280, 658],[723, 514],[1080,529],[879,748]])

    # Calculate Homography
    H = computeHomography(pts_logo, pts_dst) 

    # Warp source image to destination based on homography
    im_warped, im_out = warp_and_augment(im_logo, im_dst, H)

    # bonus feature warp function
    im_warped_advanced, im_out_advanced = warp_and_augment_advanced(im_logo, im_dst, H)

    # write output images
    cv2.imwrite("C:/Users/sunny/Desktop/workshop/Github_projects/Augmented_Visuals_Homography/images/AR_warped.jpg", im_warped) # Please add your path to output image
    cv2.imwrite("C:/Users/sunny/Desktop/workshop/Github_projects/Augmented_Visuals_Homography/images/AR_out.jpg", im_out)       # Please add your path to output image

    # bonus feature
    cv2.imwrite("C:/Users/sunny/Desktop/workshop/Github_projects/Augmented_Visuals_Homography/images/AR_warped_advanced.jpg", im_warped_advanced)    # Please add your path to output image
    cv2.imwrite("C:/Users/sunny/Desktop/workshop/Github_projects/Augmented_Visuals_Homography/images/AR_out_advanced.jpg", im_out_advanced)        # Please add your path to output image

