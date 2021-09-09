# Detects-and-Anonymize-Face-with-OpenCV
## Installation Guide
### Pull the Image
First pull the image with this command

```docker pull zogojogo/anonymize_face:latest```

If the image already pulled, then run the anonymize container with this command. After that we will linked to the bash shell of the container.

```
docker run -it --rm \
           --env="DISPLAY" \
           --env="QT_X11_NO_MITSHM=1" \
           --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
           --device=/dev/video0:/dev/video0 \ 
           zogojogo/anonymize_face:latest \
```

If we already in the bash shell and working directory, we can directly run the program. But before that maybe u can check the directory by ```ls``` command. So there are few option to run the program, we can choose whether to use images as the input or use our webcam as the input. The purpose is still the same to anonymize the detected faces. This is the main structure to run the program. 

``` python main.py <image/webcam mode> <image_path> <image_outputs> ```
### Images as Input
First to use images as input mode we need to pass ```1```in the first argument after ```main.py```.

The second argument is the image path. You could manually download the image via ```Wget``` or ```curl``` but I already provide the samples to test the program. The sample images are provided in the repository so we can use them as the input. There are 5 samples to try with various situation, ```img1.jpg```, ```img2.jpg```, ```img3.jpg```, ```img4.jpg```, and ```img5.jpg```. 

The third argument is how the output will become. There are 4 option so I will breakdown here.

- ```1``` will output the detected faces and the bounding box
- ```2``` will output the Gaussian Blur applied in the detected faces
- ```3``` will output the Mosaic Blur applied in the detected faces
- ```4``` will output all of them

So for the example to run the program is shown below :

```python main.py 1 img1.jpg 4```

### Webcam as Input
To use webcam as the input we just pass ```2``` in the first argument and then pass zero value to the second and third argument. This feature is still buggy because we still need to pass second and third argument to run the program. But because it's still demo so, better than nothing ;)

Command to run with webcam : 

```python main.py 2 0 0```