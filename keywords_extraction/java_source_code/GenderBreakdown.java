import com.univocity.parsers.common.processor.BeanListProcessor;
import com.univocity.parsers.csv.CsvParser;
import com.univocity.parsers.csv.CsvParserSettings;

import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.OptionalDouble;

public class GenderBreakdown {

	public static void main(String[] args) throws Exception {

		CsvParserSettings settings = new CsvParserSettings();

		settings.setMaxCharsPerColumn(20000);
		BeanListProcessor<GenderedSentence> rowProcessor = new BeanListProcessor<>(GenderedSentence.class);

		settings.setProcessor(rowProcessor);

		settings.setHeaderExtractionEnabled(true);

		CsvParser parser2 = new CsvParser(settings);

		parser2.parse(new FileReader("/home/hao/Documents/Simple-NLP/resources/keywords_extracted_full.csv"));

		List<GenderedSentence> beans = rowProcessor.getBeans();

		Map<String, List<Double>> typeToWeight = new HashMap<>();

		for (GenderedSentence bean : beans) {

			String femaleStr = bean.getFemale();
			String categoryStr = bean.getCategory();
			if (femaleStr != null && !femaleStr.isEmpty() && categoryStr != null && !categoryStr.isEmpty()) {

				List<String> categories = Arrays.asList(categoryStr.split(";"));
				categories.forEach(category -> typeToWeight.computeIfAbsent(category, k -> new ArrayList<>()).add(Double.parseDouble(femaleStr)));
			}

		}

		try (BufferedWriter writer = new BufferedWriter(new FileWriter("/home/hao/Documents/Simple-NLP/resources/female_weight_in_keyword_categories.txt"))) {

			for (String key : typeToWeight.keySet()) {

				OptionalDouble average = typeToWeight.get(key).stream().mapToDouble(a -> a).average();

				writer.write(key + ": " + average.getAsDouble());
				writer.newLine();
			}
		}

	}

}
