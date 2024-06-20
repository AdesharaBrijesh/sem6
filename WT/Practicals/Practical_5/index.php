<!DOCTYPE html>
<html>
<head>
    <title>String Manipulation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        #container {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            width: 400px;
        }
        h2 {
            text-align: center;
        }
        input[type="text"], select {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            padding: 14px 20px;
            margin: 8px 0;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div id="container">
        <h2>String Manipulation</h2>
        <form method="post">
            <input type="text" name="input_string" placeholder="Enter a string">
            <select name="operation" id="operation" onchange="toggleInputBox()">
                <option value="length">Calculate Length of String</option>
                <option value="lowercase">Convert to Lowercase</option>
                <option value="uppercase">Convert to Uppercase</option>
                <option value="whitespace">Calculate White Spaces</option>
                <option value="words_lines_characters">Calculate Words, Lines, and Characters</option>
                <option value="specific_word_position">Find Position of Specific Word</option>
                <option value="replace_word">Replace Word</option>
                <option value="occurrence_of_vowels">Calculate Occurrence of Vowels</option>
            </select>
            <input type="text" name="word_input" id="word_input" style="display:none;" placeholder="Enter word">
            <input type="text" name="new_word_input" id="new_word_input" style="display:none;" placeholder="Enter new word">
            <input type="submit" value="Submit">
        </form>
        <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $input_string = $_POST['input_string'];
            $operation = $_POST['operation'];

            // Get word input if operation is finding or replacing a word
            $word_input = isset($_POST['word_input']) ? $_POST['word_input'] : '';
            $new_word_input = isset($_POST['new_word_input']) ? $_POST['new_word_input'] : '';

            echo "<p>Your String: $input_string</p>";

            switch ($operation) {
                case 'length':
                    echo "<p>Length of the string: " . calculateStringLength($input_string) . "</p>";
                    break;
                case 'lowercase':
                    echo "<p>Lowercase string: " . convertToLowercase($input_string) . "</p>";
                    break;
                case 'uppercase':
                    echo "<p>Uppercase string: " . convertToUppercase($input_string) . "</p>";
                    break;
                case 'whitespace':
                    echo "<p>Number of white spaces: " . calculateWhitespace($input_string) . "</p>";
                    break;
                case 'words_lines_characters':
                    $result = calculateWordsLinesCharacters($input_string);
                    echo "<p>Number of words: " . $result['words'] . "</p>";
                    echo "<p>Number of lines: " . $result['lines'] . "</p>";
                    echo "<p>Number of characters: " . $result['characters'] . "</p>";
                    break;
                case 'specific_word_position':
                    echo "<p>Position of the word '$word_input': " . findWordPosition($input_string, $word_input) . "</p>";
                    break;
                case 'replace_word':
                    echo "<p>String after replacing '$word_input' with '$new_word_input': " . replaceWord($input_string, $word_input, $new_word_input) . "</p>";
                    break;
                case 'occurrence_of_vowels':
                    echo "<p>Occurrence of vowels: ";
                    print_r(calculateVowelOccurrence($input_string));
                    echo "</p>";
                    break;
                default:
                    echo "<p>Please select a valid operation.</p>";
                    break;
            }
        }

        function calculateStringLength($str) {
            return strlen($str);
        }

        function convertToLowercase($str) {
            return strtolower($str);
        }

        function convertToUppercase($str) {
            return strtoupper($str);
        }

        function calculateWhitespace($str) {
            return substr_count($str, ' ');
        }

        function calculateWordsLinesCharacters($str) {
            $words = str_word_count($str);
            $lines = substr_count($str, "\n") + 1; // Counting lines by counting newline characters
            $characters = strlen($str);
            return array('words' => $words, 'lines' => $lines, 'characters' => $characters);
        }

        function findWordPosition($str, $word) {
            return strpos($str, $word);
        }

        function replaceWord($str, $old_word, $new_word) {
            return str_replace($old_word, $new_word, $str);
        }

        function calculateVowelOccurrence($str) {
            $vowels = array('a', 'e', 'i', 'o', 'u');
            $occurrences = array();
            foreach ($vowels as $vowel) {
                $occurrences[$vowel] = substr_count(strtolower($str), $vowel);
            }
            return $occurrences;
        }
        ?>
        <script>
            function toggleInputBox() {
                var operation = document.getElementById("operation").value;
                var wordInput = document.getElementById("word_input");
                var newWordInput = document.getElementById("new_word_input");
                if (operation == "specific_word_position" || operation == "replace_word") {
                    wordInput.style.display = "block";
                    newWordInput.style.display = "block";
                } else {
                    wordInput.style.display = "none";
                    newWordInput.style.display = "none";
                }
            }
        </script>
    </div>
</body>
</html>
