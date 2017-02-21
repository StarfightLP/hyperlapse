import cv2

def ToVideo(image_files, output_file, fps, codec = 'DIVX'):
    if len(image_files) < 1 or not output_file or  not (fps > 0 and fps <= 240):
        raise TypeError
    fourcc = cv2.VideoWriter_fourcc(*codec) # DIVX should work on all platforms; https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
    width, height = GetImageSize(imagefiles[0])
    vidout = cv2.VideoWriter(output_file, fourcc, fps, (width, height), True)
    
    for image_file in image_files:
        vidout.write(cv2.imread(image_file))
    
    vidout.release()

def GetImageSize(image):
    frame = cv2.imread(image)
    height, width, channels = frame.shape
    return width, height
