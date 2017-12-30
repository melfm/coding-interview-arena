package string_manipulation;

public class Q4 {

	/************************************************************************
	 * Write a program to find the number of occurrences of a given search word
	 * in a two-dimensional array of characters given that the word can go up,
	 * down, left, right, and around 90 degree bends?
	 * 
	 * 
	 * Ex: Count of occurrences of SNAKES [5x4] S N B S N B A K E A B K B B K S
	 * E B S E The answer is 3.
	 * 
	 * */
	// Global word counter
	int matchesFound = 0;

	int searchCrossWord(char[][] crossWord, char word[]) {

		for (int i = 0; i < crossWord.length; ++i) {
			for (int j = 0; j < crossWord[i].length; ++j) {
				if (crossWord[i][j] == word[0]) {
					// call the recursive function
					searchSnake(crossWord, word, i, j, 0);
				}
			}
		}
		return matchesFound;

	}
	
	boolean searchSnake(char[][] crossWord, char word[], int i, int j, int pos) {
		// Check for bounds; return if out of matrix bounds
		if (i < 0 || j < 0 || i >= crossWord.length || j >= crossWord[i].length) {
			return false;
		}

		// Check if current word character matches the one in matrix
		if (crossWord[i][j] != word[pos]) {
			return false;
		}

		// Check if end of word has been reached
		if (pos == word.length - 1) {
			// End of word, so increment matchesFound
			matchesFound++;
			return true; // FIXED: Need to return once a match is found!!! ;)
		}

		searchSnake(crossWord, word, i, j - 1, pos + 1);
		searchSnake(crossWord, word, i - 1, j, pos + 1);
		searchSnake(crossWord, word, i, j + 1, pos + 1);
		searchSnake(crossWord, word, i + 1, j, pos + 1);
		return true;
	}
}
