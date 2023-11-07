import numpy as np
import scipy.fftpack as fft

class DCTConverter:
    def __init__(self, block_size=8):
        self.block_size = block_size

    def encode(self, data):
        # Ensure data is a 2D numpy array
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise ValueError("Input data should be a 2D numpy array")

        # Perform DCT encoding block by block
        encoded_data = np.empty_like(data)
        for i in range(0, data.shape[0], self.block_size):
            for j in range(0, data.shape[1], self.block_size):
                block = data[i:i + self.block_size, j:j + self.block_size]
                encoded_block = fft.dct(fft.dct(block, axis=0, norm='ortho'), axis=1, norm='ortho')
                encoded_data[i:i + self.block_size, j:j + self.block_size] = encoded_block

        return encoded_data

    def decode(self, encoded_data):
        # Ensure encoded_data is a 2D numpy array
        if not isinstance(encoded_data, np.ndarray) or encoded_data.ndim != 2:
            raise ValueError("Encoded data should be a 2D numpy array")

        # Perform DCT decoding block by block
        decoded_data = np.empty_like(encoded_data)
        for i in range(0, encoded_data.shape[0], self.block_size):
            for j in range(0, encoded_data.shape[1], self.block_size):
                encoded_block = encoded_data[i:i + self.block_size, j:j + self.block_size]
                decoded_block = fft.idct(fft.idct(encoded_block, axis=0, norm='ortho'), axis=1, norm='ortho')
                decoded_data[i:i + self.block_size, j:j + self.block_size] = decoded_block

        return decoded_data

# Example usage:
if __name__ == "__main__":
    original_data = np.random.rand(32, 32)  # Sample data
    print("orginal_data: ", original_data)
    converter = DCTConverter()
    
    # Encode the data using DCT
    encoded_data = converter.encode(original_data)
    print("\nencoded_data: ", encoded_data)

    # Decode the encoded data
    decoded_data = converter.decode(encoded_data)
    print("\ndecoded_data: ", decoded_data)

    # Check if the original and decoded data match
    is_equal = np.allclose(original_data, decoded_data)
    print(f"\nOriginal data and decoded data match: {is_equal}")