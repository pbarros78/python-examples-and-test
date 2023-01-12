import cv2

# Lists to store the bounding box coordinates
top_left_corner=[]
bottom_right_corner=[]

# function which will be called on mouse input
def drawRectangle(action, x, y, flags, *userdata):
    # Referencing global variables 
    global top_left_corner, bottom_right_corner, frame
    # Mark the top left corner when left mouse button is pressed
    if action == cv2.EVENT_LBUTTONDOWN:
        if len(top_left_corner) > 0 and len(bottom_right_corner) > 0:
            top_left_corner=[]
            bottom_right_corner=[]
        top_left_corner = [(x,y)]
    if action == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if len(top_left_corner) > 0:
            bottom_right_corner = [(x,y)]
    # When left mouse button is released, mark bottom right corner
    elif action == cv2.EVENT_LBUTTONUP:
        bottom_right_corner = [(x,y)]    
    # Draw the rectangle
    if len(bottom_right_corner) > 0:
        cv2.rectangle(frame, top_left_corner[0], bottom_right_corner[0], (0,255,0),2, 8)
    cv2.imshow("Video",frame)
 
# # Read Images
# image = cv2.imread("../Input/sample.jpg")
# # Make a temporary image, will be useful to clear the drawing
# temp = image.copy()
# # Create a named window
# cv2.namedWindow("Window")
# # highgui function called when mouse events occur
# cv2.setMouseCallback("Window", drawRectangle)

#def main(args):

#cap = cv2.VideoCapture(0) #default camera
cap = cv2.VideoCapture('rtsp://admin:87651234@192.168.1.102:8554/profile0') #IP Camera

while(True):
    ret, frame = cap.read()
    frame=cv2.resize(frame, (960, 540))
    temp = frame.copy()
    cv2.namedWindow("Video")
    cv2.setMouseCallback("Video", drawRectangle)
    #cv2.imshow('Capturing',frame)
    
    key = cv2.waitKey(1)
    if key == ord('q'): #click q to stop capturing
        break
    if key == ord('c'):
        frame= temp.copy()
        cv2.imshow("Video", frame)

cap.release()
cv2.destroyAllWindows()
#return 0

#if __name__ == '__main__':
#    import sys
#    sys.exit(main(sys.argv))