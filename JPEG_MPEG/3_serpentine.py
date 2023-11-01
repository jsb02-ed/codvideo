import imageio.v2 as io

# Getting input image
input_file = input("Input File (default test_resized.jpg): ")
if input_file == "":
    input_file = "test_resized.jpg"

# Add each pixel of the image to a matrix
im = io.imread(input_file)

# Function to traverse matrix in a serpentine way
def serpentine_traversal(matrix):
    result = []
    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows):
        if i % 2 == 0:
            for j in range(cols):
                result.append(matrix[i][j])
        else:
            for j in range(cols - 1, -1, -1):
                result.append(matrix[i][j])
    return result

# Execute traversal function and print result
serpentine = serpentine_traversal(im)
print(serpentine)