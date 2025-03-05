# Face-Detector-GUI-Using-Python

A simple **Face detector** built using **Python and OpenCV**.This project detects faces in real-time using a webcam and highlights them with bounding boxes.

![face_detector](https://github.com/ShivanisharmaF128/Face_detector_openCV/blob/main/face%20detection%20image.jpeg)

---

## 📌 Objective

The main objective of this project is to create a **real-time face detection system** using OpenCV’s Haar cascade classifier. This is a great beginner-friendly project to understand** computer vision** and **real-time image processing**in Python.

---

## 📝 Overview

-Captures video from the webcam in real time.
-Converts frames to grayscale for better accuracy in detection.
-Draws bounding boxes around detected faces.
-Press 'Esc' to exit the application.

---


## Code
```sh
python --version

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


```
## 📜 Code Explanation

1. **Loading Haar Cascade** → Loads the pre-trained Haar cascade classifier for face detection.
2. **Video Capture** → Captures real-time video from the webcam.
3. **Grayscale Conversion** → Converts frames to grayscale to enhance detection accuracy.
4. **Face Detection** → Detects faces using `detectMultiScale() `and draws bounding boxes around them.
5. **Exit Mechanism **→ Pressing the 'Esc' key will exit the application and release resources.

---

## 📢 Conclusion

This project is a great way to understand OpenCV and real-time face detection. It provides insight into image processing and object detection techniques in Python.

Feel free to ⭐ star this repository if you find it useful! 😊

---
### 🤝 Contribution
Contributions are always welcome!
If you want to improve the UI or add new features, follow these steps:

- Fork this repository 📌
- Make necessary changes 🛠️
- Create a pull request 🔄

----

###🎉 Final Outcome
![outcome ](https://github.com/ShivanisharmaF128/Face_detector_openCV/blob/main/Output.jfif)

----

###👨‍💻 Author

Shivani Sharma
📌 Passionate about Python, Data Science, and GUI Development.
🌐 Connect with me on LinkedIn.

