import cv2


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    while True:
        _, img = cap.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        canny = cv2.Canny(blur, 10, 70)
        _, mask = cv2.threshold(canny, 70, 255, cv2.THRESH_BINARY)
        cv2.imshow('Video feed', mask)

        if cv2.waitKey(1) == 13:
            break

    cap.release()
    cv2.destroyAllWindows()
