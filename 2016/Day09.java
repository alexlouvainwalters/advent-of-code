import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import java.util.ArrayList;

public class Day09 {
	public static String part1(String inputFile) {
		String answer = "";
		
		String inputText;
		
		try (BufferedReader br = new BufferedReader(new FileReader(inputFile))) {
			inputText = br.readLine();
		} catch (IOException e) {
			inputText = null;
		}

		int length = 0;
		int start = 0;
		String code = "";
		boolean encoding = false;

		for (int i = 0; i < inputText.length(); i++) {
			if (!encoding) {
				if (inputText.charAt(i) == '(') {
					encoding = true;
					start = i + 1;
				}
			} else {
				if (inputText.charAt(i) == ')') {
					encoding = false;
					code = inputText.substring(start, i);

					String[] values = code.split("x");
					int sequenceLength = Integer.parseInt(values[0]);
					int copies = Integer.parseInt(values[1]);

					if (inputText.length() - i >= sequenceLength) {
						length += sequenceLength * copies;
					} else {
						length += inputText.length() - i * copies;
					}

					i += sequenceLength;
				}
			}
		}

		answer = Integer.toString(length);

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

		long length = 0L;
		int start = 0;
		String code = "";
		boolean encoding = false;

		ArrayList<String> inputTextBacklog = new ArrayList<String>();
		ArrayList<Integer> multiplierBacklog = new ArrayList<Integer>();

		String inputTextCurrent = inputText;
		int positionCurrent = 0;
		int multiplierCurrent = 1;

		inputTextBacklog.add(inputTextCurrent);
		multiplierBacklog.add(multiplierCurrent);

		outer:
		while (positionCurrent < inputTextCurrent.length() && inputTextBacklog.size() >= 0) {
			if (!encoding) {
				if (inputTextCurrent.charAt(positionCurrent) == '(') {
					encoding = true;
					start = positionCurrent + 1;
				} else {
					length += multiplierCurrent;
				}
			} else {
				if (inputTextCurrent.charAt(positionCurrent) == ')') {
					encoding = false;
					code = inputTextCurrent.substring(start, positionCurrent);

					String[] values = code.split("x");
					int sequenceLength = Integer.parseInt(values[0]);
					int copies = Integer.parseInt(values[1]);

					if (inputTextCurrent.substring(positionCurrent + 1, positionCurrent + sequenceLength + 1).contains("x")) {
						inputTextBacklog.set(inputTextBacklog.size() - 1, inputTextCurrent.substring(positionCurrent + sequenceLength + 1));
						
						inputTextCurrent = inputTextCurrent.substring(positionCurrent + 1, positionCurrent + sequenceLength + 1);
						positionCurrent = 0;
						multiplierCurrent *= copies;

						inputTextBacklog.add(inputTextCurrent);
						multiplierBacklog.add(copies);

						continue;
					} else {
						length += sequenceLength * multiplierCurrent * copies;
						positionCurrent += sequenceLength;
					}
				}
			}

			positionCurrent++;
			while (positionCurrent >= inputTextCurrent.length()) {
				if (inputTextBacklog.size() == 1) {
					break outer;
				}

				inputTextBacklog.remove(inputTextBacklog.size() - 1);
				
				inputTextCurrent = inputTextBacklog.get(inputTextBacklog.size() - 1);
				positionCurrent = 0;
				multiplierCurrent /= multiplierBacklog.remove(multiplierBacklog.size() - 1);
			}
		}

		answer = Long.toString(length);

		return answer;
	}

	public static void main(String[] args) {
		System.out.println("Part 1: " + part1("day_09.txt"));
		System.out.println("Part 2: " + part2("day_09.txt"));
	}
}