import java.io.BufferedWriter;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class MainClass {
	
	public static void main(String[] args) throws Exception {
		checkName("ccg.bib", "ccg_new.bib");
	}

	private static void checkName(String infile, String outfile) throws IOException {
		String content = IOManager.readContentNoTrim(infile);
		int p = 0;
		while (p < content.length()) {
			String patternStr = "author\\s*=";
			Pattern pattern = Pattern.compile(patternStr);
			Matcher matcher = pattern.matcher(content);
			if(matcher.find(p)){
				p = matcher.start();
			} else {
				break;
			}
			int start = content.indexOf("{", p);
			int end = content.indexOf("}", p);
			//if (start > end) {
			//	System.out.println(content.substring(p, p + 100));
			//}
			String authors = content.substring(start + 1, end);
			if (authors.contains(",")) {
				System.out.print(authors + "\t");
				String authors_new = authors.replaceAll(",", " and");
				System.out.print(authors_new + "\n");
				content = content.substring(0, start + 1) + authors_new + content.substring(end, content.length());
				p = start + authors_new.length();
			} else {
				p = end;
			}
		}
		
		BufferedWriter bw = IOManager.openWriter(outfile);
		bw.write(content);
		bw.close();
	}
}
