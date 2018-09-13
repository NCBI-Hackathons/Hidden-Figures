import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;

public class KeywordCategories {

	public static void main(String[] args) throws Exception {

		Map<String, String> typeMap = new HashMap<>();

		typeMap.put("a", "material");
		typeMap.put("b", "analysis");
		typeMap.put("c", "procedure");
		typeMap.put("d", "advice");
		typeMap.put("e", "manuscript");
		typeMap.put("f", "coordination");

		Map<String, Set<String>> typeToKeywords = new TreeMap<>();

		try (BufferedReader reader = new BufferedReader(new FileReader("/home/haoyu/Documents/Simple-NLP/resources/candidate_keywords.txt"));
				BufferedWriter writer = new BufferedWriter(new FileWriter("/home/haoyu/Documents/Simple-NLP/resources/keywords_in_categories.txt"))) {

			String line = null;

			while ((line = reader.readLine()) != null) {
				String[] content = line.split(":");

				typeToKeywords.computeIfAbsent(content[1], k -> new TreeSet<>()).add(content[0]);
			}

			typeToKeywords.keySet().stream().forEach(key -> {
				try {
					writer.write(typeMap.get(key) + ": " + String.join(";", typeToKeywords.get(key)));
					writer.newLine();
				}
				catch (IOException e) {
					e.printStackTrace();
				}
			});

		}

	}
}
