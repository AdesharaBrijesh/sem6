<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Print Table</title>
</head>
<body>
    <form action="" method="post">
        <label for="number">Enter a number:</label>
        <input type="number" id="number" name="number" required>
        <input type="submit" value="Print Table">
    </form>

    <?php
    echo "Adeshara Brijesh_21012021001". "<br>";
    // Check if the form is submitted
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        // Retrieve the number from the form
        $number = isset($_POST['number']) ? (int)$_POST['number'] : 0;

        if ($number > 0) {
            echo "<h2>Table of $number</h2>";
            // Print the table of the given number
            for ($i = 1; $i <= 10; $i++) {
                $result = $number * $i;
                echo "$number * $i = $result<br>";
            }
        } else {
            echo "<p>Please enter a valid number.</p>";
        }
    }
    ?>
</body>
</html>
