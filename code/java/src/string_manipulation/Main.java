package string_manipulation;

import java.util.Arrays;


public class Main {

	public static void main(String[] args) {
		
		/************************************/
		Q1 question_one = new Q1();
		System.out.println("Question 1:");
		question_one.start();
		
		
		/************************************/
		Q2 question_two = new Q2();
		// Data
		String input = "a?bc?def?g??";
		question_two.detectAndGenerateOnesZeros(input);
		

		/************************************/
		Q3 question_three = new Q3();
		String helloWorld = "___Hello__World____";
		char[] helloWordRes = question_three.helloSpaceWorld(helloWorld);
		System.out.println("Question 3:");
		System.out.println("char[] b: " + Arrays.toString(helloWordRes));
		
		
		/************************************/
		Q4 question_four = new Q4();
		// Data
		char matrix[][] = new char[][] {
				{'S', 'N', 'B', 'S', 'N'},
				{'B', 'A', 'K', 'E', 'A'},
				{'B', 'K', 'B', 'B', 'K'},
				{'S', 'E', 'B', 'S', 'E'}
		};
		char word[] = "SNAKES".toCharArray();
		int matches = question_four.searchCrossWord(matrix, word);
		System.out.println("Question 4:");
		System.out.println(matches);


		/************************************/
		Q5 question_five = new Q5();
		// Data
		String fruit = "Apple";
		String fruit_reversed = question_five.reverse_string(fruit);
		System.out.println("Question 5:");
		System.out.println(fruit_reversed);

	}

}
