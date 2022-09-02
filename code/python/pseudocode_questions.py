
"""
More of an image processing question.
Rotating Image By Any Angle.
https://gautamnagrawal.medium.com/rotating-image-by-any-angle-shear-transformation-using-only-numpy-d28d16eb5076

1) Recall 2D representation of (x,y) in terms of cos and sin angles
2) Formula for calculating the new dimensions after rotation
3) Aliasing problem

# Define the height and width of the new image that is to be formed
new_height  = round(abs(image.shape[0]*cosine)+abs(image.shape[1]*sine)) + 1
new_width  = round(abs(image.shape[1]*cosine)+abs(image.shape[0]*sine)) + 1

output = np.zeros((new_height,new_width,image.shape[2]))

# Find the centre of the image about which we have to rotate the image
# With respect to the old image
original_centre_height = round(((image.shape[0] + 1)/2) - 1)
original_centre_width = round(((image.shape[1] + 1)/2) - 1)

# Find the centre of the new image that will be obtained
# with respect to the new image
new_centre_height= round(((new_height+1)/2) - 1)
new_centre_width= round(((new_width+1)/2) - 1)

for i in range(height):
    for j in range(width):
        # co-ordinates of pixel with respect to the centre of original image
        y = image.shape[0]-1-i-original_centre_height
        x = image.shape[1]-1-j-original_centre_width

        # co-ordinate of pixel with respect to the rotated image
        new_y=round(-x*sine + y*cosine)
        new_x=round(x*cosine + y*sine)

        # The image will be rotated and the center will change too
        new_y=new_centre_height-new_y
        new_x=new_centre_width-new_x

        #Prevent any errors in the processing
        if 0 <= new_x < new_width and 0 <= new_y < new_height and new_x>=0 and new_y>=0:
            output[new_y,new_x,:]=image[i,j,:]

Aliasing problem: Multiplying by sines and cosines on the integer
coordinates of the source image gives real number results,
and these have to be rounded back to integers again to be plotted.
This means the same destination location is addressed more than once,
and sometimes certain pixels are missed completely. Oversampling or AreaMapping
are some solutions. See the link above.
"""