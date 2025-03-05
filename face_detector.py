import cv2

# Load the Haar cascade file correctly
a = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Corrected function name
b = cv2.VideoCapture(0)

while True:
    c_rec, d_image = b.read()
    if not c_rec:
        print("Failed to capture image")
        break
    
    e = cv2.cvtColor(d_image, cv2.COLOR_BGR2GRAY)
    f = a.detectMultiScale(e, 1.3, 6)

    for (x1, y1, w1, h1) in f:
        cv2.rectangle(d_image, (x1, y1), (x1 + w1, y1 + h1), (255, 0, 0), 5)

    cv2.imshow('img', d_image)  # Move this outside the for loop

    h = cv2.waitKey(40) & 0xff
    if h == 27:  # Press 'Esc' to exit
        break

# Release resources outside the loop
b.release()
cv2.destroyAllWindows()
