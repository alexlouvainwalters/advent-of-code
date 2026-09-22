import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

import java.math.BigInteger;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class Day05 {
	public static String part1(String inputFile) {
		String answer = "";

		String inputText;
		
		try (BufferedReader br = new BufferedReader(new FileReader(inputFile))) {
			inputText = br.readLine();
		} catch (IOException e) {
			inputText = null;
		}

		String password = "";
		int index = 0;

		try {
			MessageDigest md = MessageDigest.getInstance("MD5");

			while (password.length() != 8) {
				String toHash = inputText + index;
				byte[] messageDigest = md.digest(toHash.getBytes());
				BigInteger signum = new BigInteger(1, messageDigest);
				String hashtext = signum.toString(16);
				
				while(hashtext.length() < 32) {
					hashtext = "0" + hashtext;
				}

				if (hashtext.substring(0, 5).equals("00000")) {
					password += hashtext.charAt(5);
				}

				index++;
			}
		} catch (NoSuchAlgorithmException e) {
			throw new RuntimeException(e);
		}

		answer = password;

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

		String password = "xxxxxxxx";
		int index = 0;

		try {
			MessageDigest md = MessageDigest.getInstance("MD5");

			while (password.contains("x")) {
				String toHash = inputText + index;
				byte[] messageDigest = md.digest(toHash.getBytes());
				BigInteger signum = new BigInteger(1, messageDigest);
				String hashtext = signum.toString(16);
				
				while(hashtext.length() < 32) {
					hashtext = "0" + hashtext;
				}

				if (hashtext.substring(0, 5).equals("00000")) {
					int position = Character.getNumericValue(hashtext.charAt(5));
					char toInsert = hashtext.charAt(6);

					if (position >= 0 && position <= 7 && password.charAt(position) == 'x') {
						password = password.substring(0, position) + toInsert + password.substring(position + 1);
					}
				}

				index++;
			}
		} catch (NoSuchAlgorithmException e) {
			throw new RuntimeException(e);
		}

		answer = password;

		return answer;
	}

	public static void main(String[] args) {
		System.out.println("Part 1: " + part1("day_05.txt"));
		System.out.println("Part 2: " + part2("day_05.txt"));
	}
}