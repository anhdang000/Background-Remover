from model_configs import *
from demo import inference
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', help='Input video')
FLAGS = parser.parse_args()

input_vid = FLAGS.input

# Read input video
cap = cv2.VideoCapture(input_vid)

# Check if camera opened successfully
if (cap.isOpened() == False):
    print("Unable to read camera feed")

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
out = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

while(True):
    ret, frame = cap.read()

    if ret == True: 
        image, raw_image = preprocessing(image, device, CONFIG)
        labelmap = inference(model, image, raw_image, postprocessor)
        labels = np.unique(labelmap)

        mask = np.zeros((raw_image.shape[0], raw_image.shape[1]))
        for i, label in enumerate(labels):
            mask_inclass = labelmap == label

            class_name = classes[label]
            if class_name in classes_of_interest:
                mask += mask_inclass

        # Create mask
        mask = np.where(mask >= 1, 1, mask)
        mask = (mask * 255).astype(np.uint8)
        mask_3d = np.stack([mask]*3, axis=2)

        # Apply with source
        raw_rgb = raw_image[:, :, ::-1]
        out_frame = np.where(mask_3d == 255, raw_rgb, 255)
        # Write the frame into the file 'output.avi'
        out.write(out_frame)

    # Break the loop
    else:
        break 