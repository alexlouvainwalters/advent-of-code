import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import java.util.ArrayList;

public class Day02 {
	public static String part1(String inputFile) {
		String answer = "";
		
		ArrayList<String> inputText = new ArrayList<String>();
		
		try (BufferedReader br = new BufferedReader(new FileReader(inputFile))) {
			String line;
			while ((line = br.readLine()) != null) {
				inputText.add(line);
			}
		} catch (IOException e) {
			inputText = null;
		}
		
		String code = "";
		int current = 5;

		for (String line : inputText) {
			for (char direction : line.toCharArray()) {
				if (direction == 'U' && current > 3) {
					current -= 3;
				} else if (direction == 'D' && current < 7) {
					current += 3;
				} else if (direction == 'L' && current % 3 != 1) {
					current--;
				} else if (direction == 'R' && current % 3 != 0) {
					current++;
				}
			}

			code += current;
		}

		answer = code;

		return answer;
	}
	
	public static String part2(String inputFile) {
		String answer = "";
		
		ArrayList<String> inputText = new ArrayList<String>();
		
		try (BufferedReader br = new BufferedReader(new FileReader(inputFile))) {
			String line;
			while ((line = br.readLine()) != null) {
				inputText.add(line);
			}
		} catch (IOException e) {
			inputText = null;
		}
		
		String code = "";
		int current = 5;

		for (String line : inputText) {
			for (char direction : line.toCharArray()) {
				if (
					direction == 'U'
					&& current > 5
					&& current < 13
					&& current != 9
				) {
					current -= 4;
				} else if (
					direction == 'U'
					&& (current == 3 || current == 13)
				) {
					current -= 2;
				} else if (
					direction == 'D'
					&& current > 1
					&& current < 9
					&& current != 5
				) {
					current += 4;
				} else if (
					direction == 'D'
					&& (current == 1 || current == 11)
				) {
					current += 2;
				} else if (
					direction == 'L'
					&& current > 2
					&& current < 13
					&& current != 5
					&& current != 10
				) {
					current--;
				} else if (
					direction == 'R'
					&& current < 12
					&& current != 1
					&& current != 4
					&& current != 9
				) {
					current++;
				}
			}

			if (current >= 10 && current <= 13) {
				code += (char) (current + 55);
			} else {
				code += current;
			}
		}

		answer = code;

		return answer;
	}

	public static void main(String[] args) {
		System.out.println("Part 1: " + part1("day_02.txt"));
		System.out.println("Part 2: " + part2("day_02.txt"));
	}
}