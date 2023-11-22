# (MORE) PYTHON & VIDEO

In this folder you will find some scripts that modify video calling FFmpeg from Python. Feel free to test them all.

## Before you start...
You must set your own FFmpeg installation location before you run any script that calls FFmpeg. You will find a variable called `ffmpeg_install` in `video_class.py`.
Just type something like `ffmpeg_install = "/home/username/bin/"`. This will also give the location of ffprobe.

This time all the tests must be done in the script: `video_class.py`. It contains the `VideoClass` definition and testing functions for each proposed seminar parts.

When you run the script, it will ask for a video file (`BBB.mp4` by default). Then it will ask which part do you want to run. Just input a number `(1-5)`. Errors are checked so idiots can also run the script.

Run the code for each test, so you can change the input file. I recommend using shorter versions of the video for parts 4 and 5. Part 4 subtitles work best with 9s version.

## Parts summary

#### PART 1
9 seconds are cut from BBB. The 9s output is then passed through FFmpeg to show the motion vectors. (Seems that FFmpeg does not like macroblocks anymore)

> Previous versions of ffmpeg (pre-October 2017) allowed you to analyze macroblocks too, but this option was removed.

#### PART 2
For the second part, BBB is cut into 50s, then substracted audio, then exported audio in 3 different ways (MP3 mono, MP3 stereo low bitrate, AAC) and finally added to a new MP4 package with `FFmpeg`.

#### PART 3
On the third part `FFprobe` is used to count the number of audio tracks of a container. It is useful to try it with the ouput of `PART 2`.

#### PART 4
For the fourth part, some subtitles are added to a video in the shape of printed subtitles, so you cannot get rid of them after they are added.

This was done in a different script and later inheritated to `video_class.py` to call the new function from the test section.

#### PART 5
The last part adds a YUV histogram into a video, so histogram and video are displayed at the same time. This is also implemented in a different script and later imported to `video_class.py` to test.


#### That's it for today. Now just have fun testing these scripts!
