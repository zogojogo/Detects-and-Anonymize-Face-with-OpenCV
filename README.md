# Detects-and-Anonymize-Face-with-OpenCV
```
docker run -it \
           --env="DISPLAY" \
           --env="QT_X11_NO_MITSHM=1" \
           --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
           --device=/dev/video0:/dev/video0 \ 
           anonymize_face:v1.1
```