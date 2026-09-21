import java.util.HashSet;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import java.lang.Math;

public class Day01 {
	public static String part1(String inputFile) {
		String answer = "";
		
		String inputText;
		
		try (BufferedReader br = new BufferedReader(new FileReader(inputFile))) {
			inputText = br.readLine();
		} catch (IOException e) {
			inputText = null;
		}
		
		int vertical = 0;
		int horizontal = 0;
		int direction = 0;
		
		String[] moves = inputText.strip().split(", ");
		
		for (String move : moves) {
			if (move.charAt(0) == 'R') {
				direction++;
			} else if (move.charAt(0) == 'L') {
				direction += 3;
			}
			
			if (direction % 4 == 0) {
				vertical += Integer.parseInt(move.substring(1));
			} else if (direction % 4 == 1) {
				horizontal += Integer.parseInt(move.substring(1));
			} else if (direction % 4 == 2) {
				vertical -= Integer.parseInt(move.substring(1));
			} else if (direction % 4 == 3) {
				horizontal -= Integer.parseInt(move.substring(1));
			}
		}
		
		answer = Integer.toString(Math.abs(vertical) + Math.abs(horizontal));
		
		return answer;
	}
	
	public static String part2(String inputFile) {
		String answer = "";
		
		String inputText;
		
		try (BufferedReader br = new BufferedReader(new FileReader(inputFile))) {
			inputText = br.readLine();
		} catch (IOException e) {
			inputText = null;
		}
		
		int vertical = 0;
		int horizontal = 0;
		int direction = 0;
		
		String[] moves = inputText.strip().split(", ");
		
		for (String move : moves) {
			if (move.charAt(0) == 'R') {
				direction++;
			} else if (move.charAt(0) == 'L') {
				direction += 3;
			}
			
			if (direction % 4 == 0) {
				vertical += Integer.parseInt(move.substring(1));
			} else if (direction % 4 == 1) {
				horizontal += Integer.parseInt(move.substring(1));
			} else if (direction % 4 == 2) {
				vertical -= Integer.parseInt(move.substring(1));
			} else if (direction % 4 == 3) {
				horizontal -= Integer.parseInt(move.substring(1));
			}
		}
		
		answer = Integer.toString(Math.abs(vertical) + Math.abs(horizontal));
		
		return answer;
	}

	public static void main(String[] args) {
		System.out.println("Part 1: " + part1("day_01.txt"));
		System.out.println("Part 2: " + part2("day_01.txt"));
	}
}