import numpy.random as rnd
import os
import cv2
def random_bbox(H, W,max_H, max_W):
    x1 = rnd.randint(0,W)
    y1 = rnd.randint(0,H)
    x2 = rnd.randint(x1,x1+max_W)
    y2 = rnd.randint(y1,y1+max_H)
    return (x1, y1, x2, y2)
    
def rip_frames(vid_path, out_path=None):
    '''
    Brief:
        Parses a video file and saves each frame as a png.

    Parameters:
        vid_path (string) Path to video file.
        out_path (string) Path where frame png file will be saved.

    Returns:
        None
    '''

    if out_path == None:
        print("Please specify a directory to save frames")
    else:
        if os.path.exists(out_path):
            vidcap = cv2.VideoCapture(vid_path)
            success,image = vidcap.read()
            count = 0
            print("Ripping frames...")
            while success:
                if (count % 100) == 0:
                    path = os.path.join(out_path, f"{vid_path.split('/')[-1].split('.')[0]}.{count}.0.png")
                    box = random_bbox(image.shape[0],image.shape[1],500,500)
                    try:
                        cv2.imwrite(path, image[box[1]:box[3], box[0]:box[2]])
                    except:
                        pass
                success,image = vidcap.read()
                count += 1
            print("Saved {} frames to {}.".format(count, out_path))
        else:
            print("Specified directory does not exist")

if __name__ == "__main__":
    for i in range(6,23):
        rip_frames(f"raw_data/video/{i}.mp4","generated_data/dataset/test/not_ship")