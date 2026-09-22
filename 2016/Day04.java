import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import java.util.Arrays;
import java.util.ArrayList;
import java.util.LinkedHashMap;

public class Day04 {
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
		
		int total = 0;

		for (String line : inputText) {
			String name = "";
			int id = -1;
			String checksum = "";

			for (String component : line.split("-")) {
				if (component.contains("[")) {
					String[] comb = component.split("\\[");
					id = Integer.parseInt(comb[0]);
					checksum = comb[1].substring(0, comb[1].length() - 1);
				} else {
					name += component;
				}
			}

			char[] splitName = name.toCharArray();
			Arrays.sort(splitName);
			String sortedName = new String(splitName);

			LinkedHashMap<Character, Integer> frequency = new LinkedHashMap<Character, Integer>();

			for (char letter : sortedName.toCharArray()) {
				frequency.put(letter, frequency.getOrDefault(letter, 0) + 1);
			}

			for (int i = 0; i < 5; i++) {
				char selected = '0';
				int max = 0;

				for (char letter : frequency.keySet()) {
					if (frequency.get(letter) > max) {
						selected = letter;
						max = frequency.get(letter);
					}
				}

				if (checksum.charAt(0) == selected) {
					checksum = checksum.substring(1);
					frequency.remove(selected);
				} else {
					break;
				}
			}

			if (checksum.equals("")) {
				total += id;
			}
		}

		answer = Integer.toString(total);

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

		outer:
		for (String line : inputText) {
			String name = "";
			String shortName = "";
			int id = -1;
			String checksum = "";

			for (String component : line.split("-")) {
				if (component.contains("[")) {
					String[] comb = component.split("\\[");
					id = Integer.parseInt(comb[0]);
					checksum = comb[1].substring(0, comb[1].length() - 1);
					name = name.substring(0, name.length() - 1);
				} else {
					name += component + " ";
					shortName += component;
				}
			}

			char[] splitName = shortName.toCharArray();
			Arrays.sort(splitName);
			String sortedName = new String(splitName);

			LinkedHashMap<Character, Integer> frequency = new LinkedHashMap<Character, Integer>();

			for (char letter : sortedName.toCharArray()) {
				frequency.put(letter, frequency.getOrDefault(letter, 0) + 1);
			}

			for (int i = 0; i < 5; i++) {
				char selected = '0';
				int max = 0;

				for (char letter : frequency.keySet()) {
					if (frequency.get(letter) > max) {
						selected = letter;
						max = frequency.get(letter);
					}
				}

				if (checksum.charAt(0) == selected) {
					checksum = checksum.substring(1);
					frequency.remove(selected);
				} else {
					break;
				}
			}

			if (checksum.equals("")) {
				String unencrypted = "";

				for (char encrypted : name.toCharArray()) {
					if (encrypted == ' ') {
						unencrypted += " ";
					} else {
						int alphabetPos = ((int) encrypted) - 96;
						int shiftedPos = (alphabetPos + id) % 26;
						if (shiftedPos == 0) {
							shiftedPos += 26;
						}
						unencrypted += (char) (shiftedPos + 96);
					}
				}

				if (unencrypted.contains("north")) {
					answer = Integer.toString(id);

					break outer;
				}
			}
		}

		return answer;
	}

	public static void main(String[] args) {
		System.out.println("Part 1: " + part1("day_04.txt"));
		System.out.println("Part 2: " + part2("day_04.txt"));
	}
}