import skvideo.io
import numpy as np
import sys

sys.path.append('/home/josep/codvideo/')
from JPEG_MPEG.dct_encoder_decoder import DCTConverter

class VideoConverter(DCTConverter):
    
    def convertVideo(self, file):
        videodata = skvideo.io.vread(file)
        one_frame = (videodata[1, :, :, 0] + videodata[1, :, :, 1] + videodata[1, :, :, 2]) / 3
        return one_frame

if __name__ == "__main__":
    original_video = "BigBuckBunny_short.mp4"
    converter = VideoConverter()
    
    original_data = converter.convertVideo(original_video)

    encoded_data = converter.encode(original_data)
    print("\nencoded_data: ", encoded_data)

    decoded_data = converter.decode(encoded_data)
    print("\ndecoded_data: ", decoded_data)

    is_equal = np.allclose(original_data, decoded_data)
    print(f"\nOriginal data and decoded data match: {is_equal}")