import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import java.util.ArrayList;

import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class Day03 {
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
		
		int count = 0;

		for (String line : inputText) {
			Pattern p = Pattern.compile("\\d+");
			Matcher m = p.matcher(line);

			ArrayList<Integer> sides = new ArrayList<Integer>();

			while (m.find()) {
				sides.add(Integer.parseInt(m.group()));
			}

			int max = 0;
			int total = 0;

			for (int side : sides) {
				if (side > max) {
					max = side;
				}
				total += side;
			}

			if (max * 2 < total) {
				count++;
			}
		}

		answer = Integer.toString(count);

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

		int count = 0;

		ArrayList<ArrayList<Integer>> triangles = new ArrayList<ArrayList<Integer>>();
		ArrayList<Integer> sides = new ArrayList<Integer>();

		for (String line : inputText) {
			Pattern p = Pattern.compile("\\d+");
			Matcher m = p.matcher(line);

			while (m.find()) {
				sides.add(Integer.parseInt(m.group()));
			}

			if (sides.size() == 9) {
				for (int i = 0; i < 3; i++) {
					ArrayList<Integer> tempTriangle = new ArrayList<Integer>();
					tempTriangle.add(sides.get(i));
					tempTriangle.add(sides.get(i + 3));
					tempTriangle.add(sides.get(i + 6));

					triangles.add(tempTriangle);
				}

				sides.clear();
			}
		}

		for (ArrayList<Integer> triangle : triangles) {
			int max = 0;
			int total = 0;

			for (int side : triangle) {
				if (side > max) {
					max = side;
				}
				total += side;
			}

			if (max * 2 < total) {
				count++;
			}
		}

		answer = Integer.toString(count);

		return answer;
	}

	public static void main(String[] args) {
		System.out.println("Part 1: " + part1("day_03.txt"));
		System.out.println("Part 2: " + part2("day_03.txt"));
	}
}