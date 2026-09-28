import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import java.util.ArrayList;
import java.util.LinkedHashMap;

public class Day06 {
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

		String trueMessage = "";

		LinkedHashMap<Character, Integer> frequency = new LinkedHashMap<Character, Integer>();

		for (int i = 0; i < inputText.get(0).length(); i++) {
			for (String message : inputText) {
				frequency.put(message.charAt(i), frequency.getOrDefault(message.charAt(i), 0) + 1);
			}

			char selected = '0';
			int max = 0;

			for (char letter : frequency.keySet()) {
				if (frequency.get(letter) > max) {
					selected = letter;
					max = frequency.get(letter);
				}
			}

			frequency.clear();
			trueMessage += selected;
		}

		answer = trueMessage;

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

		String trueMessage = "";

		LinkedHashMap<Character, Integer> frequency = new LinkedHashMap<Character, Integer>();

		for (int i = 0; i < inputText.get(0).length(); i++) {
			for (String message : inputText) {
				frequency.put(message.charAt(i), frequency.getOrDefault(message.charAt(i), 0) + 1);
			}

			char selected = '0';
			int min = Integer.MAX_VALUE;

			for (char letter : frequency.keySet()) {
				if (frequency.get(letter) < min) {
					selected = letter;
					min = frequency.get(letter);
				}
			}

			frequency.clear();
			trueMessage += selected;
		}

		answer = trueMessage;

		return answer;
	}

	public static void main(String[] args) {
		System.out.println("Part 1: " + part1("day_06.txt"));
		System.out.println("Part 2: " + part2("day_06.txt"));
	}
}