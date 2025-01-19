import cv2

def main():
    video = cv2.VideoCapture(1)

    if not video.isOpened():
        print("Error: Could not open video stream or file")
        return

    while True:
        ret, frame = video.read()
        if ret:
            cv2.imshow("Age-Gender", frame)
        k = cv2.waitKey(1)
        if k == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()