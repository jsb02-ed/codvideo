from video_converter import VideoConverter

# TESTING CLASS
video_converter = VideoConverter()

# Selecting part to test
def select_test_part():
    print("WELCOME! You can select to test Part 1 - Video Codec converter // Part 2 - 2-video comparator")
    test_part = input("Test Part (1 or 2): ")
    if test_part not in ("1", "2"):
        print("ERROR! Input must be (1 or 2)")
        test_part = select_test_part()
        return test_part
    else:
        return test_part

test_part = select_test_part()

print(f"\n--------------------------------------------")
print(f"             SELECTED TEST: {test_part}")
print(f"--------------------------------------------\n")

# Initiating tests

# PART 1
if test_part == "1":
    # Getting input file and setting default
    input_file = input("Input File (default BBB_cut_9_sec.mp4): ")
    if input_file == "":
        input_file = "BBB_cut_9_sec.mp4"

    codec = video_converter.select_codec()
    video_converter.convert_into(input_file, codec)

# PART 2
elif test_part == "2":
    input_right = input("Input first file for comparison (default BBB_cut_9_sec_VP8.webm): ")
    if input_right == "":
        input_right = "BBB_cut_9_sec_VP8.webm"

    input_left = input("Input second file for comparison (default BBB_cut_9_sec_VP9.webm): ")
    if input_left == "":
        input_left = "BBB_cut_9_sec_VP9.webm"

    video_converter.video_comparison(input_right, input_left)