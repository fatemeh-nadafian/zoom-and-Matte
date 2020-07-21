import cv2                                                                              # Imoport library cv2 and numpy """
import numpy as np

def mouse_callback(event,x,y,flags,param):                                              #  A function that takes the coordinates of the click point by the mouse and creates a square,showing that part of the image is zoomed in and opaque ""                              
    if event==cv2.EVENT_LBUTTONDBLCLK:                                                  # If the user double-clicks on a part of the image, the following commands will be executed """
       rectangle = cv2.rectangle(image, (x-30,y-30), (x+30,y+30), (0,0,0),1)            # Draw a square with a length and width of 60 that the center of the square is the coordinates of the mouse click on the image """
       mask=np.zeros((image.shape[0],image.shape[1]), dtype='uint8')                    # Create a presentation with the dimensions of the original image """ 
       cv2.rectangle(mask,(x-30,y-3),(x+30,y+30),(255,255,255),-1)                      # Create a solid white square in the presentation, with the coordinates and dimensions of the square we created with the mouse click in the main image """
       
       masked=cv2.bitwise_and(image,image,mask=mask)                                    # Bit to mask the image and extract a square from the image and show it in the presentation and """
       blurred = np.hstack([cv2.GaussianBlur(masked, (7, 7), 0)])                       # Blur the selected square """
       cv2.imshow('blur',blurred)                                                       # Show blurred photo """
       zoom=cv2.resize(masked,(masked.shape[1]+160,masked.shape[0]+210))                # Zoom in on the selected square """
       cv2.imshow('zoom',zoom)                                                          # Show zoomed image """

image=cv2.imread('photo4.jpg')                                                             # Capture input image """                       
cv2.namedWindow('image')                                                                # Create a new window to keep the original image """
cv2.setMouseCallback('image',mouse_callback)                                            # Using the setMouseCallback function, I set the mouse controller for the created window """

while(True):                                                                            # Create an infinite loop to display the image and create a square on it until the user presses the enter key and the program closes. """ 
    cv2.imshow('image',image)
    if cv2.waitKey(1) & 0xff==13:
        break
cv2.destroyAllWindows()                                                                 # Eliminate windows that take up memory space """