import cv2
import imutils as imutils
import numpy as np
import pytesseract as pytesseract
import re

class LicensePlateRecognition:

    pytesseract.pytesseract.tesseract_cmd = r'E:\Tess\tesseract.exe'

    def __init__(self, image_path):

        # store the resized image in the object
        self.image =  cv2.imread(image_path, cv2.IMREAD_COLOR)
        self.image = cv2.resize(self.image, (600,400) )

    def get_license_number(self):

        # convert to grey scale
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        # use blurring to remove the noise
        gray = cv2.bilateralFilter(gray, 13, 15, 15)
        # Perform Edge detection
        edged = cv2.Canny(gray, 30, 200)

        # look for contours in the edged image
        contours = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)
        contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
        screenCnt = None

        for c in contours:
            # approximate the contour
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.018 * peri, True)
            # if our approximated contour has four points, then
            # we can assume that we have found our screen
            if len(approx) == 4:
                screenCnt = approx
                break

        if screenCnt is None:
            detected = 0
            print("No contour detected")
        else:
            detected = 1

        if detected == 1:
            cv2.drawContours(self.image, [screenCnt], -1, (0, 0, 255), 3)

        # Masking the part other than the number plate
        mask = np.zeros(gray.shape, np.uint8)
        cv2.drawContours(mask, [screenCnt], 0, 255, -1, )
        cv2.bitwise_and(self.image, self.image, mask=mask)

        # Now crop
        (x, y) = np.where(mask == 255)
        (topx, top_y) = (np.min(x), np.min(y))
        (bottom_x, bottom_y) = (np.max(x), np.max(y))
        Cropped = gray[topx:bottom_x + 1, top_y:bottom_y + 1]

        # Read the number plate
        car_license = pytesseract.image_to_string(Cropped, config='--psm 11')

        # Show the image
        img = cv2.resize(self.image, (500, 300))
        cv2.resize(self.image, (400, 200))
        cv2.imshow('car', img)
        # cv2.imshow('greyscale', gray)
        # cv2.imshow('Cropped', Cropped)

        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # return the updated license plate number found
        updated_car_license = re.search("[A-Z0-9- ]+", car_license)
        return updated_car_license.group()

if __name__ == "__main__":
    license_ob = LicensePlateRecognition("Images/image_3.jpg")
    license_number = license_ob.get_license_number()
    print(license_number) #Code by: BHAVYA SEHGAL
