# JPEG - MPEG

In this folder you will find some scripts that do some stuff with images and FFmpeg. Let's get started!

## Before you start...
You must set your own FFmpeg installation location before you run any script that calls FFmpeg. You will find a variable called `ffmpeg` at the beggining of each script needing this change.
Just type something like `ffmpeg = "/home/username/bin/ffmpeg"`

There is a very useful script named `F_run_all.py`. You can just run this one and it will automatically run each other script sequentially.

## Scripts summary

#### 1_rgb_yuv.py
This script translates 3 RGB values to the 3 YUV corresponding values. That's it! Input of each channel of RGB must be in range [0,1].

#### 2_ffmpeg_resize.py
The second script resizes any image you want to a new desired resolution. On the back, it calls FFmpeg to do the operation.

#### 3_serpentine.py
The third script reads an image through a serpentine pattern. Input any image and it will return the 3 RGB values for each pixel ordered in a serpentine way.

#### 4_rgb_bw.py
The fourth script inputs an image `your_image.jpg` and has two outputs:
- `your_image_bw.jpg`: returns the same image but black and white.
- `your_image_bw_compressed.jpg`: returns the maximum compressed version of the black and white image.
Both operations are done calling FFmpeg.

#### 5_run_length_encoding.py
The fifth script encodes and decodes a byte sequence using run legth encoding. You must modify the script to change the example encoded/decoded bits.

#### 6_dct_encoder_decoder.py
The last numbered script encodes and decodes a random 32x32 matrix using DCT and later checks whether the decoded version is the same as the original.

## About `test.jpg`
The test image was taken in September 2021 in Balaguer (Lleida), when I organized a hybrid live concert together with my band and a lot of friends.

Although the streaming was not perfect, it was a great experience and we learnt a lot. If you are interested, you can find the live recording in https://www.youtube.com/watch?v=FVhKLR_j4Go. We promise we have improved a lot since then!

#### That's it for today. Now just have fun testing these scripts!
