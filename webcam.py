import cv2

webcam = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not webcam.isOpened():
    raise IOError("Cannot open webcam")

# Loop through frames every 1ms
while True:
    ret, frame = webcam.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Webcam', frame)

    c = cv2.waitKey(1)

    # If esc typed then stop loop
    if c == 27:
        break

# Release the webcam and close any GUI windows
webcam.release()
cv2.destroyAllWindows()