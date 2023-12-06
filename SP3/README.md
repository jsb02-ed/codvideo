# SP3 - Final exercises

In this folder you will find some scripts that do different stuff with video, python, FFmpeg and Docker. Everything is explained in the document.

## Before you start...
You must set your own FFmpeg installation location before you run any script that calls FFmpeg. You will find a variable called `ffmpeg_install` in `video_converter.py`.
Just type something like `ffmpeg_install = "/home/username/bin/"`. This will also give the location of ffprobe.

#### RUNNING PARTS 1 & 2
This time all the exercises are pretty different. You must use: `test_video_converter` for exercises 1-2. This calls the script containing `VideoConverter` definition, where all the functions for both exercises are implemented.

When you run the script, it will ask for a video file (`BBB_cut_9_sec.mp4` by default). Then it will ask which part do you want to run. Just input a number `(1-2)`. Errors are checked so idiots can also run the script.

Run the code for each test, so you can change the input file.

#### RUNNING PART 3
Part 3 can be found in the subfolder `\build`. Specifically, you will find the executable file named `gui.py`. Just launch this file to launch the gui. Everything else is kind of magic.

#### RUNNING PART 4
I feel part 4 (Docker) is more experimenting than handing in a runnable script. You will find a copy of the docker I used in the subfolder `/docker-ffmpeg` and a list of the instructions I used to build and run it in a file called `docker_followed_steps.txt`.

## Parts summary

#### PART 1
Here I am converting video into VP8, VP9, h265 & AV1 using FFmpeg. There is a function `select_codec()` to (you guessed) select the code. Then the function `convert_into(input, codec)` is called and the magic happens.

#### PART 2
For the second part, a comparison is generated between the two videos you select. Function `video_comparison(left, right)`is called. VP8 and VP9 are compared by default in the test script.

#### PART 3
On the third part a GUI is created. I used the `tkinter` library to create it along with a script named `Tkinter-Designer` (by Parth Jadhav) which allowed me to design most of the GUI with Figma editor, so the interface looks nicer.

You are allowed to graphically select 2 video files to later compare them as in the previous exercises (empty selections are checked). In the background, the interface calls `video_comparison_display(left, right)`, a modified of the previous `video_comparison(left, right)` which runs `FFplay` at the end of the comparison generation to watch it directly on scree.

You will find some screenshots in the `/gui_screenshots` folder.

#### PART 4
The last part is to play with Docker. I absolutely played with Docker. For this part I looked for a Docker image containing FFmpeg installed. I know I could have generated it from scratch, but I felt more realistic to just take one that a really high amount of people use.

I found taking images from Docker Hub really easy, but I decided to go to the GitHub folder of the chosen image `linuxserver/docker-ffmpeg` and compile it by myself. This took a lot of time, but I'm happy to have learnt that compiling a Docker is not Rocket Science. As stated before, you will find the followed steps in `docker_followed_steps.txt`. After creating the Docker, I just tried to cut 5s of a video.


#### That's it for today. Now just have fun testing these scripts!
