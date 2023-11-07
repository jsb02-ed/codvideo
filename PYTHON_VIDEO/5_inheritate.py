import skvideo.io  
import numpy as np

import sys
print('Original sys.path:', sys.path)
sys.path.append('/home/josep/codvideo/')
print('Updated sys.path:', sys.path)
from JPEG_MPEG.dct_encoder_decoder import DCTConverter


class VideoConverter(DCTConverter):
    
    # Convert video into a single frame
    def convertVideo(self, file):
        videodata = skvideo.io.vread(file)
        print (np.shape(videodata))
        one_frame = (videodata[1, :, :, 0] + videodata[1, :, :, 1] + videodata[1, :, :, 2])/3
        return one_frame

# Example usage:
if __name__ == "__main__":
    original_video = "BigBuckBunny_short.mp4"
    converter = VideoConverter()
    
    # Convert video into matrix
    original_data = converter.convertVideo(original_video)

    # Encode the data using DCT
    encoded_data = converter.encode(original_data)
    print("\nencoded_data: ", encoded_data)

    # Decode the encoded data
    decoded_data = converter.decode(encoded_data)
    print("\ndecoded_data: ", decoded_data)

    # Check if the original and decoded data match
    is_equal = np.allclose(original_data, decoded_data)
    print(f"\nOriginal data and decoded data match: {is_equal}")