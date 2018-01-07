package string_manipulation;

public class Q5 {
	
	public String reverse_string(String str_input){
		char[] in_str = str_input.toCharArray();
		int p0 = 0;
		int p1 = in_str.length - 1;
		
		char tmp;
		while( p0 < p1) {
			tmp = in_str[p0];
			in_str[p0] = in_str[p1];
			in_str[p1] = tmp;
			
			p0 ++;
			p1 --;
		}
		
		return new String(in_str);
		
	}

}
