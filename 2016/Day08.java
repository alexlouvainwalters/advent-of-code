import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import java.util.ArrayList;

public class Day08 {
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

		int rowCount = 6;
		int columnCount = 50;

		char[][] screen = new char[rowCount][columnCount];
		
		for (int i = 0; i < rowCount; i++) {
			for (int j = 0; j < columnCount; j++) {
				screen[i][j] = '.';
			}
		}

		for (String line : inputText) {
			String[] components = line.split(" ");

			if (components[0].equals("rect")) {
				String[] fillCoords = components[1].split("x");

				for (int i = 0; i < Integer.parseInt(fillCoords[1]); i++) {
					for (int j = 0; j < Integer.parseInt(fillCoords[0]); j++) {
						screen[i][j] = '#';
					}
				}
			} else if (components[0].equals("rotate")) {
				if (components[1].equals("row")) {
					char[] tempRow = new char[columnCount];

					for (int i = 0; i < columnCount; i++) {
						tempRow[(i + Integer.parseInt(components[4])) % columnCount] = screen[Integer.parseInt(components[2].substring(2))][i];
					}

					for (int i = 0; i < columnCount; i++) {
						screen[Integer.parseInt(components[2].substring(2))][i] = tempRow[i];
					}
				} else if (components[1].equals("column")) {
					char[] tempColumn = new char[rowCount];

					for (int i = 0; i < rowCount; i++) {
						tempColumn[(i + Integer.parseInt(components[4])) % rowCount] = screen[i][Integer.parseInt(components[2].substring(2))];
					}

					for (int i = 0; i < rowCount; i++) {
						screen[i][Integer.parseInt(components[2].substring(2))] = tempColumn[i];
					}
				}
			}
		}

		int total = 0;

		for (int i = 0; i < rowCount; i++) {
			for (int j = 0; j < columnCount; j++) {
				if (screen[i][j] == '#') {
					total++;
				}
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

		answer = "EOARGPHYAO";

		return answer;
	}

	public static void main(String[] args) {
		System.out.println("Part 1: " + part1("day_08.txt"));
		System.out.println("Part 2: " + part2("day_08.txt"));
	}
}