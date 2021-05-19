from argparse import ArgumentParser
import cv2

parser=ArgumentParser()
parser.add_argument('--input',type=str, help='Video path relevant to the script', required=True)

def main():
    args=parser.parse_args()

    INPUT_VIDEO_PATH=args.input

    print('video is from ' + INPUT_VIDEO_PATH)

    vcap = cv2.VideoCapture(INPUT_VIDEO_PATH)
    counter = 0

    if not vcap.isOpened():
        print("File Cannot be Opened")

    while(True):
        # Capture frame-by-frame
        ret, frame = vcap.read()

        print(vcap.isOpened() , ret)
        if frame is not None:
            # Display the resulting frame
            cv2.imshow('frame',frame)
            cv2.imwrite('frame'+str(counter)+'.jpg',frame)

            # Press q to close the video windows before it ends if you want
            if cv2.waitKey(22) & 0xFF == ord('q'):
                break
        else:
            print("Frame is None")
            break
        counter += 1

    # When everything done, release the capture
    vcap.release()
    cv2.destroyAllWindows()
    print("Video stop")

if __name__ == '__main__':
    main()
