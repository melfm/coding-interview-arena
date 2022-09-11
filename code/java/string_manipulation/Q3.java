package string_manipulation;

public class Q3 {
	/************************************************************************
	 * Given a string with multiple spaces write a function to "in-place" trim
	 * all spaces leaving a single space between words Cannot split because it
	 * might involve copying p1 = font p2 = behind
	 * 
	 * 1) p1 keeps scanning 2) if p1 is not a space, p1 copies back to p2, and
	 * p2 is incremented 3) then after a word, if there is a space, u copy back
	 * 1 space
	 * 
	 * maybe we need a flag to say ..we have come out of a word!! then i was
	 * thinking if .. can do without a flag ..since the start can be like
	 * special ..
	 * 
	 * e.g. _ _ _ Hello _ _ _ World _ _ _ Hello _ World _ _ _ _ _ _ _ _ _
	 */

	char[] helloSpaceWorld(String input) {

		int front = 0; // p1
		int behind = 0; // p2
		char[] charInput = input.toCharArray();

		while (front < charInput.length) {
			// if p1 is not a space, p1 copies back to p2
			if (charInput[front] != '_') {
				// p1 copies back to p2
				// p2 is incremented
				charInput[behind] = charInput[front];
				// Check if we are at the end of the word
				charInput[front] = '_';
				behind++;
				int temp = front;
				if (temp < charInput.length - 1)
					temp++;
				if (charInput[temp] == '_') {
					charInput[behind] = '_';
					behind++;
				}

			}

			front++;
		}

		return charInput;
	}
}
