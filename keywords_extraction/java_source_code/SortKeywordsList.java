import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.Set;
import java.util.TreeSet;

public class SortKeywordsList {

	public static void main(String[] args) throws Exception {

		try(BufferedReader reader = new BufferedReader(new FileReader("/home/hao/Documents/Simple-NLP/resources/candidate_keywords"));
				BufferedWriter writer = new BufferedWriter(new FileWriter("/home/hao/Documents/Simple-NLP/resources/candidate_keywords_sorted"))) {

			String line = null;
			Set<String> words = new TreeSet<>();
			while((line = reader.readLine()) != null) {
				words.add(line);
			}

			for(String word : words) {
				writer.write(word);
				writer.newLine();
			}

		}
	}
}
