import com.univocity.parsers.common.processor.BeanListProcessor;
import com.univocity.parsers.csv.CsvParser;
import com.univocity.parsers.csv.CsvParserSettings;
import com.univocity.parsers.csv.CsvWriter;
import com.univocity.parsers.csv.CsvWriterSettings;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;
import java.util.stream.Collectors;

public class MeshExtractor {

	private static Set<String> stopwords = new HashSet<>(
			Arrays.asList("is", "are", "the", "was", "were", "on", "for", "by", "it", "we", "he", "she", "as", "and", "thank", "like", "of", "", "to", "dr",
					"author", "kind", "university", "also", "at", "in", "wish", "thankful", "authors", "his", "her", "she", "he"));

	private static Map<String, String> typeMap = new HashMap<>();

	private static Map<String, String> keywordToTypeMap = new HashMap<>();

	private static Map<String, Integer> typeToCount = new TreeMap<>();

	static {
		typeMap.put("a", "material");
		typeMap.put("b", "analysis");
		typeMap.put("c", "procedure");
		typeMap.put("d", "advice");
		typeMap.put("e", "manuscript");
		typeMap.put("f", "coordination");
	}

	public static void main(String[] args) throws Exception {

		Set<String> keywords = new HashSet<>();

		try (BufferedReader reader = new BufferedReader(new FileReader("/home/hao/Documents/Simple-NLP/resources/candidate_keywords.txt"))) {
			String line = null;
			while ((line = reader.readLine()) != null) {
				if (!line.isEmpty()) {
					String[] content = line.split(":");

					keywords.add(content[0]);

					keywordToTypeMap.put(content[0], content[1]);
				}
			}
		}

		keywords.remove("");

		CsvParserSettings settings2 = new CsvParserSettings();

		settings2.setMaxCharsPerColumn(20000);
		BeanListProcessor<GenderedSentence> rowProcessor2 = new BeanListProcessor<>(GenderedSentence.class);

		settings2.setProcessor(rowProcessor2);

		settings2.setHeaderExtractionEnabled(true);

		CsvParser parser2 = new CsvParser(settings2);

		parser2.parse(new FileReader("/home/hao/Documents/Simple-NLP/resources/complete_gendered_sentences.csv"));

		List<GenderedSentence> beans2 = rowProcessor2.getBeans();

		CsvWriter csvWriter = new CsvWriter(new FileWriter("/home/hao/Documents/Simple-NLP/resources/keywords_extracted_full.csv"), new CsvWriterSettings());

		csvWriter.writeHeaders("filename", "Is Female (Weighted)", "Names", "Keywords", "Category", "Text");

		int count = 0;

		for (GenderedSentence genderBean : beans2) {

			String text = genderBean.getSentence();

			Set<String> extractedKeywords = getKeywords(text, keywords);

			Set<String> types = new TreeSet<>();

			if (!extractedKeywords.isEmpty()) {
				if (count % 1000 == 0) {
					System.out.println("Processed: " + count);
				}
				count++;
				//				System.out.println("Keywords: " + extractedKeywords);

				extractedKeywords.forEach(word -> types.add(keywordToTypeMap.get(word)));
				types.forEach(type -> typeToCount.merge(type, 1, Integer::sum));
			}

			Set<String> fullnameTypes = new TreeSet<>(types.stream().map(type -> typeMap.get(type)).collect(Collectors.toList()));

			csvWriter.writeRow(genderBean.getFilnName(), genderBean.getFemale(), genderBean.getNames(), String.join(";", extractedKeywords),
					String.join(";", fullnameTypes), genderBean.getSentence());
		}

		csvWriter.close();

		System.out.println("Number of sentences: " + beans2.size());

		System.out.println("Total number of sentences that have keywords: " + count);

		try (BufferedWriter writer = new BufferedWriter(new FileWriter("/home/hao/Documents/Simple-NLP/resources/tally_keywords_full.txt"))) {

			writer.write("Total number of sentences: " + beans2.size());
			writer.newLine();
			writer.write("Total number of sentences that contain keywords: " + count);
			writer.newLine();
			writer.newLine();
			for (Map.Entry<String, Integer> entry : typeToCount.entrySet()) {
				System.out.printf("%s%s%d%n", typeMap.get(entry.getKey()), ":", entry.getValue());
				writer.write(String.format("%s%s%d%n", typeMap.get(entry.getKey()), ":", entry.getValue()));
			}
		}

	}

	private static Set<String> getKeywords(String text, Set<String> keywords) {

		Set<String> words = new TreeSet<>();

		Set<String> tokens = new HashSet<>(Arrays.asList(text.toLowerCase().split("\\s+")));

		removeStopWords(tokens);

		for (String token : tokens) {
			token = token.replaceAll("[.,()]", "");
			if (keywords.contains(token)) {
				words.add(token);
			}
		}

		return words;

	}

	private static void removeStopWords(Set<String> tokens) {
		tokens.removeAll(stopwords);
	}
}
