import java.util.Random;
import java.util.ArrayList;

import static spark.Spark.*;

public class RandomQuoteGenerator {
    public static void main(String[] args) {
        // Define the quotes
        ArrayList<String> quotes = new ArrayList<>();
        quotes.add("The best way to predict your future is to create it. - Abraham Lincoln");
        quotes.add("Believe you can and you're halfway there. - Theodore Roosevelt");
        quotes.add("Strive not to be a success, but rather to be of value. - Albert Einstein");
        quotes.add("The only way to do great work is to love what you do. - Steve Jobs");
        quotes.add("You miss 100% of the shots you don't take. - Wayne Gretzky");

        // Set up the web server
        port(4567);

        get("/", (req, res) -> {
            // Get a random quote
            Random random = new Random();
            int randomIndex = random.nextInt(quotes.size());
            String quote = quotes.get(randomIndex);

            // Render the quote as HTML
            String html = "<h1>" + quote + "</h1>";
            return html;
        });
    }
}
