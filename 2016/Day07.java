import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import java.util.ArrayList;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day07 {
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

		outer:
		for (String line : inputText) {
			boolean abba = false;

			for (int i = line.length() - 4; i >= 0; i--) {
				if (line.charAt(i) == line.charAt(i + 3) 
					&& line.charAt(i + 1) == line.charAt(i + 2)
					&& line.charAt(i) != line.charAt(i + 1)
				) {
					String tempLine = line.substring(0, i) + "X" + line.substring(i + 4);

					Pattern p = Pattern.compile("\\[[a-z]*X[a-z]*\\]");
					Matcher m = p.matcher(tempLine);

					if (m.find()) {
						continue outer;
					}

					abba = true;
				}
			}

			if (abba) {
				total++;
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

		int total = 0;

		outer:
		for (String line : inputText) {
			ArrayList<String> abaList = new ArrayList<String>();
			ArrayList<String> babList = new ArrayList<String>();

			for (int i = line.length() - 3; i >= 0; i--) {
				if (line.charAt(i) == line.charAt(i + 2)
					&& line.charAt(i) != line.charAt(i + 1)
				) {
					String tempLine = line.substring(0, i) + "X" + line.substring(i + 3);

					Pattern p = Pattern.compile("\\[[a-z]*X[a-z]*\\]");
					Matcher m = p.matcher(tempLine);

					if (m.find()) {
						babList.add(line.substring(i, i + 3));
					} else {
						abaList.add(line.substring(i, i + 3));
					}
				}
			}

			for (String aba : abaList) {
				for (String bab : babList) {
					if (aba.charAt(0) == bab.charAt(1) && aba.charAt(1) == bab.charAt(0)) {
						total++;

						continue outer;
					}
				}
			}
		}

		answer = Integer.toString(total);

		return answer;
	}

	public static void main(String[] args) {
		System.out.println("Part 1: " + part1("day_07.txt"));
		System.out.println("Part 2: " + part2("day_07.txt"));
	}
}