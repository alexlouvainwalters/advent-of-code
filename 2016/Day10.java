import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

public class Day10 {
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

		int chosen = -1;

		HashMap<Integer, ArrayList<Integer>> bots = new HashMap<Integer, ArrayList<Integer>>();
		ArrayList<String> swaps = new ArrayList<String>();

		for (String line : inputText) {
			if (line.contains("gives")) {
				swaps.add(line);
			} else {
				String[] values = line.substring(6).split(" goes to bot ");

				ArrayList<Integer> tempBot = bots.getOrDefault(Integer.parseInt(values[1]), new ArrayList<Integer>());
				tempBot.add(Integer.parseInt(values[0]));
				bots.put(Integer.parseInt(values[1]), tempBot);
			}
		}

		int index = 0;
		while (index < swaps.size()) {
			String swap = swaps.get(index);

			for (int key : new ArrayList<Integer>(bots.keySet())) {
				if (bots.get(key).contains(17) && bots.get(key).contains(61)) {
					chosen = key;
					break;
				}
			}

			if (chosen != -1) {
				break;
			}

			String[] information = swap.substring(4).split(" gives ");
			int bot = Integer.parseInt(information[0]);
			String[] swapDetails = information[1].split(" and ");

			if (bots.containsKey(bot) && bots.get(bot).size() == 2) {
				if (swapDetails[0].contains("bot")) {
					ArrayList<Integer> tempBot = bots.getOrDefault(Integer.parseInt(swapDetails[0].substring(11)), new ArrayList<Integer>());
					tempBot.add(Collections.min(bots.get(bot)));
					bots.put(Integer.parseInt(swapDetails[0].substring(11)), tempBot);
					tempBot = bots.get(bot);
					tempBot.remove(Collections.min(bots.get(bot)));
					bots.put(bot, tempBot);
				} else if (swapDetails[0].contains("output")) {
					ArrayList<Integer> tempBot = bots.get(bot);
					tempBot.remove(Collections.min(bots.get(bot)));
					bots.put(bot, tempBot);
				}

				if (swapDetails[1].contains("bot")) {
					ArrayList<Integer> tempBot = bots.getOrDefault(Integer.parseInt(swapDetails[1].substring(12)), new ArrayList<Integer>());
					tempBot.add(Collections.max(bots.get(bot)));
					bots.put(Integer.parseInt(swapDetails[1].substring(12)), tempBot);
					tempBot = bots.get(bot);
					tempBot.remove(Collections.max(bots.get(bot)));
					bots.put(bot, tempBot);
				} else if (swapDetails[1].contains("output")) {
					ArrayList<Integer> tempBot = bots.get(bot);
					tempBot.remove(Collections.max(bots.get(bot)));
					bots.put(bot, tempBot);
				}

				swaps.remove(index);
				index = 0;
			} else {
				bots.putIfAbsent(bot, new ArrayList<Integer>());
				index++;
			}
		}

		answer = Integer.toString(chosen);

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

		int product = 1;

		HashMap<Integer, ArrayList<Integer>> bots = new HashMap<Integer, ArrayList<Integer>>();
		ArrayList<String> swaps = new ArrayList<String>();

		for (String line : inputText) {
			if (line.contains("gives")) {
				swaps.add(line);
			} else {
				String[] values = line.substring(6).split(" goes to bot ");

				ArrayList<Integer> tempBot = bots.getOrDefault(Integer.parseInt(values[1]), new ArrayList<Integer>());
				tempBot.add(Integer.parseInt(values[0]));
				bots.put(Integer.parseInt(values[1]), tempBot);
			}
		}

		int index = 0;
		int counter = 0;
		while (counter != 3) {
			String swap = swaps.get(index);

			String[] information = swap.substring(4).split(" gives ");
			int bot = Integer.parseInt(information[0]);
			String[] swapDetails = information[1].split(" and ");

			if (bots.containsKey(bot) && bots.get(bot).size() == 2) {
				if (swapDetails[0].contains("bot")) {
					ArrayList<Integer> tempBot = bots.getOrDefault(Integer.parseInt(swapDetails[0].substring(11)), new ArrayList<Integer>());
					tempBot.add(Collections.min(bots.get(bot)));
					bots.put(Integer.parseInt(swapDetails[0].substring(11)), tempBot);
					tempBot = bots.get(bot);
					tempBot.remove(Collections.min(bots.get(bot)));
					bots.put(bot, tempBot);
				} else if (swapDetails[0].contains("output")) {
					int outputCheck = Integer.parseInt(swapDetails[0].substring(swapDetails[0].length() - 2).strip());
					if (outputCheck >= 0 && outputCheck <= 2) {
						product *= Collections.min(bots.get(bot));
						counter++;
					}

					ArrayList<Integer> tempBot = bots.get(bot);
					tempBot.remove(Collections.min(bots.get(bot)));
					bots.put(bot, tempBot);
				}

				if (swapDetails[1].contains("bot")) {
					ArrayList<Integer> tempBot = bots.getOrDefault(Integer.parseInt(swapDetails[1].substring(12)), new ArrayList<Integer>());
					tempBot.add(Collections.max(bots.get(bot)));
					bots.put(Integer.parseInt(swapDetails[1].substring(12)), tempBot);
					tempBot = bots.get(bot);
					tempBot.remove(Collections.max(bots.get(bot)));
					bots.put(bot, tempBot);
				} else if (swapDetails[1].contains("output")) {
					int outputCheck = Integer.parseInt(swapDetails[1].substring(swapDetails[1].length() - 2).strip());
					if (outputCheck >= 0 && outputCheck <= 2) {
						product *= Collections.max(bots.get(bot));
						counter++;
					}
					ArrayList<Integer> tempBot = bots.get(bot);
					tempBot.remove(Collections.max(bots.get(bot)));
					bots.put(bot, tempBot);
				}

				swaps.remove(index);
				index = 0;
			} else {
				bots.putIfAbsent(bot, new ArrayList<Integer>());
				index++;
			}
		}

		answer = Integer.toString(product);

		return answer;
	}

	public static void main(String[] args) {
		System.out.println("Part 1: " + part1("day_10.txt"));
		System.out.println("Part 2: " + part2("day_10.txt"));
	}
}