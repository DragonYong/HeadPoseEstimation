BASE_MODEL=/media/turing/D741ADF8271B9526/BASE_MODEL
python estimate_head_pose.py \
    --CAM=0 \
    --DNN_MODEL=$BASE_MODEL/FACEDETECTOR/HeadPoseEstimation/res10_300x300_ssd_iter_140000.caffemodel \
    --DNN_PROTO=$BASE_MODEL/FACEDETECTOR/HeadPoseEstimation/deploy.prototxt \
    --SAVE_MODEL=$BASE_MODEL/FACEDETECTOR/HeadPoseEstimation/pose_model