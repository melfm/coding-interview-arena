package string_manipulation;

import java.util.ArrayList;
import java.util.Arrays;

public class Q2 {

	/************************************************************************
	 * 1. Scan original string and count number of ?s in the string. Also make
	 * note of locations of ?s 2. Generate binary sequences for values from 0 to
	 * 2 ^ COUNT, where COUNT is the number of ?s in the string. 3. For each
	 * binary sequence, replace ?s in the original string with 0s and 1s. Use of
	 * the locations will improve efficiency of the replacement operations ..
	 * instead of having to scan the string over and over again.
	 ************************************************************************/
	
	ArrayList<String> detectAndGenerateOnesZeros(String s){
		// Go thru the string and search for ?
		char[] chars = s.toCharArray();
		int qcounter = 0;
		ArrayList<Integer> indices = new ArrayList<Integer>();
		for (int i = 0; i < chars.length; ++i) {
			// Keep pointers to locations of ?s
			if (chars[i] == '?') {
				qcounter++;
				indices.add(i);
			}
		}
		int max = 2 ^ qcounter - 1;
		ArrayList<String>res = new ArrayList<String>();
		char[] newPaddedBin = new char[max];
		for (int i = 0; i <= max; ++i) {
			String binary = Integer.toBinaryString(i);
			if(binary.length() < max){
			// Do the padding here
			newPaddedBin= Arrays.copyOf(binary.toCharArray(), max);
				
			}
			String elem = replaceQsInOriginalString(newPaddedBin,chars,indices);
			res.add(elem);
		}
		return res;
	}

	String replaceQsInOriginalString(char[] inputB,char[] inputS,ArrayList<Integer> indices) {
		
		int bcounter = 0;
		for (int i = 0; i < indices.size(); ++i) {
			int targetIndex = indices.get(i);
			inputS[targetIndex] = inputB[bcounter];
			bcounter++;
		}
		
		return inputS.toString();
	}

	//************************************************************************
}