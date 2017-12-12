import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import com.wcohen.ss.JaroWinkler;
import com.wcohen.ss.api.StringDistance;

public class TextClassification {
	public static void main(String[] args) throws IOException{
		//SentenceSimilarityAssessor s = new SentenceSimilarityAssessor();
		String[] str = {"5 o Clock_Shadow", "Arched Eyebrows", "Attractive", "Bags Under Eyes", "Bald", "Bangs",
						"Big Lips", "Big Nose", "Black Hair", "Blond Hair", "Blurry", "Brown Hair", "Bushy Eyebrows",
						"Chubby", "Double Chin", "Eyeglasses", "Goatee", "Gray Hair", "Heavy Makeup", "High Cheekbones",
						"Male", "Mouth Slightly Open", "Mustache", "Narrow Eyes", "No Beard", "Oval Face", "Pale Skin",
						"Pointy Nose", "Receding Hairline", "Rosy Cheeks", "Sideburns", "Smiling", "Straight Hair",
						"Wavy Hair", "Wearing Earrings", "Wearing Hat", "Wearing Lipstick", "Wearing Necklace", "Wearing Necktie", "Young"}; 
		String []input_list = {"Blond Hair","Black Hair","Brown Hair","Male","Mustache","Young","Eyeglasses","Pale Skin","Bald"};
		///////////////////////////how to input? /////////////////////////////
		
		String file_name = "list_attr_images.txt";
		BufferedReader br = new BufferedReader(new FileReader("input.txt"));
		String input = br.readLine();
		String[] tokenized_input = input.split(",");
		for(int i=0; i<tokenized_input.length; i++)
			tokenized_input[i] = tokenized_input[i].replaceAll("_"," ");
		
		int[] result_binary = new int[40];
		JaroWinkler jaro = new JaroWinkler();
		StringDistance distanceChecker = jaro.getDistance();
		for (int i=0; i<40; i++)
			result_binary[i] = -1;
		
		for(int i=0; i<tokenized_input.length; i++) {
			double max = 0;
			int _index_to_match=0;
			for(int j=0; j<input_list.length; j++) {
				double tmp = distanceChecker.score(input_list[j], tokenized_input[i]);
				if(tmp > max) {
					max = tmp;
					for(int k=0; k<str.length; k++) {
						if(str[k].equals(input_list[j])) {
							_index_to_match = k;
							break;
						}
					}
					
				}
			}
			result_binary[_index_to_match] = 1;
			
		}
		BufferedWriter output = new BufferedWriter(new FileWriter(file_name));
		int num=1;
		String formattedInt = String.format("%d", num);
		output.write(formattedInt);
		output.newLine();
		for(int i=0; i<str.length; i++) {
			output.write(str[i]);
			output.write(" ");
		}
		output.newLine();
		output.write("000001.jpg");
		for(int i=0; i<str.length; i++) {
			String formattedText = String.format("%3d", result_binary[i]);
			output.write(formattedText);
		}
		output.close();
		System.out.println("Done!");
	}
}
