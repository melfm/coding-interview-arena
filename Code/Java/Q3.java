import java.util.Arrays;

//
// Given a string (for example: "a?bc?def?g"), write a program to generate all the possible strings
// by replacing ? with 0 and 1. 
// Example: 
// Input : a?b?c? 
// Output: a0b0c0, a0b0c1, a0b1c0, a0b1c1, a1b0c0, a1b0c1, a1b1c0, a1b1c1.
//

public class Q3 {
	//
	// Starting point
	//
	public void start() {
		// Data
		String input = "a?bc?def?g";
		
		// Record indices of where '?' char occurs
		// Note this will work only up to 32 '?'s found in the input
		char[] data = input.toCharArray();
		int[] locs = new int[data.length];
		int count = 0;
		for (int i = 0; i < data.length; ++i) {
			if (data[i] == '?') {
				locs[count] = i;
				++count;
			}
		}
		
		// Generate binary sequences for the numberer of '?'s found
		int max = (1 << count) - 1;
		for (int value = 0; value <= max; ++value) {
			char[] binary = generateZeroPaddedBinarySeq(value, count);
			// Place binary digits in places where '?' are found
			for (int i = 0; i < count; ++i) {
				int pos = locs[i];
				data[pos] = binary[i];
			}
			// Print a updated string
			System.out.println("Out: " + new String(data));
		}
	}
	
	//
	// Get a zero padded binary sequence
	//
	char[] generateZeroPaddedBinarySeq(int value, int length) {
		char[] bseq = Integer.toBinaryString(value).toCharArray();
		if (bseq.length >= length) {
			return bseq;
		}
		int diff = length - bseq.length;
		char[] bpad = new char[length];
		Arrays.fill(bpad, '0');
		System.arraycopy(bseq, 0, bpad, diff, bseq.length);
		return bpad;
	}
}
