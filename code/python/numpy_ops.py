import numpy as np
from itertools import product

def subsample_trajectory_v1(trajectory, stride=1, offset=1):

    diffs = []
    trajectory = np.array(trajectory)

    length = len(trajectory) - 1 if len(trajectory) % stride == 0 else int(len(trajectory) / stride)

    for i in range(offset, length):
        diff = tuple(np.abs(trajectory[i] - trajectory[i + stride]))
        diffs.append(diff)

    return diffs


def subsample_trajectory_v2(trajectory, stride=1, offset=1):
    diffs = []
    trajectory = np.array(trajectory)
    length = (len(trajectory) - offset) // stride

    for i in range(length):
        # First index is for skipping
        index = offset + i * stride
        # Ensure no out-of-bounds access
        if index + stride < len(trajectory):
            # Second index is just a simple stride addition
            diff = tuple(np.abs(trajectory[index] - trajectory[index + stride]))
            diffs.append(diff)

    return diffs



def function_along_axis(func1d, axis, arr):
    """
    Apply a 1D function along a specified axis of a NumPy array.
    
    Parameters:
        func1d (callable): A function that takes a 1D array and returns a transformed 1D array.
        axis (int): The axis along which to apply the function.
        arr (np.ndarray): The input NumPy array.
        
    Returns:
        np.ndarray: Transformed array with function applied along `axis`.
    """
    # Get the shape of the input array
    arr_shape = arr.shape
    # Shape before axis
    Ni = arr_shape[:axis]
    # Shape after axis
    Nk = arr_shape[axis+1:]

    # Generate an example 1D slice to determine output shape
    def get_sample_slice(arr, axis):
        """Extract a single slice along the specified axis."""
        index = [0] * arr.ndim
        index[axis] = slice(None)
        return arr[tuple(index)]

    sample_output = func1d(get_sample_slice(arr, axis))
    output_shape = Ni + sample_output.shape + Nk
    
    # Initialize output array
    out = np.empty(output_shape, dtype=sample_output.dtype)
    
    # Iterate over all possible indices except the chosen axis
    for ii in product(*[range(n) for n in Ni]):
        for kk in product(*[range(n) for n in Nk]):
            # Extract 1D slice along axis
            arr_slice = arr[ii + (slice(None),) + kk]
            
            # Apply function to 1D slice
            transformed_slice = func1d(arr_slice)
            
            # Assign result to output array
            for jj in product(*[range(n) for n in transformed_slice.shape]):
                out[ii + jj + kk] = transformed_slice[jj]

    return out

