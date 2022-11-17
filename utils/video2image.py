import cv2
from matplotlib import pyplot as plt

def video2image(video_path, image_dir_path, skip_rate=10, show=False, write=True):
    i = 0
    cap = cv2.VideoCapture(video_path)
    while(1):
        ret, frame = cap.read()
        if ret==False:
            break
        if(i % skip_rate == 0):
            j = int(i/skip_rate)   
            if write:            
                image_path = f"{image_dir_path}/{j}.png" 
                print(f"Saving frame {i} to {image_path}")
                cv2.imwrite(image_path, frame)
            if show:        
                plt.imshow(frame)
                plt.show()
        i += 1
    cap.release()
