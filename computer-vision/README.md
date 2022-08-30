opencv
======

Install OpenCV
--------------

```
$ which python
/home/jwrr/anaconda3/bin/python

$ python --version
Python 3.8.5

python 1_opencv.py 
Traceback (most recent call last):
  File "1_opencv.py", line 2, in <module>
    import cv2
ModuleNotFoundError: No module named 'cv2'
```

* Try installing opencv

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install libopencv-dev python3-opencv -y
```

* Still fails
* Try installing using coda

```
conda install -condaforge opencv
```

* Solving environment takes forever and would probably fail.
* Create new conda enviroment

```
conda create -n opencv4
conda activate opencv4
conda install -c conda-forge opencv
```

Try running again and boom... it works!

```
$ python3 1_opencv.py
4.6.0
```




