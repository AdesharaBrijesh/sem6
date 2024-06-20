<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Global Variables Example</title>
</head>
<body>
    <h2>Global Variables Example</h2>
    <form method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
        <label for="name">Enter Your Name:</label><br>
        <input type="text" id="name" name="name"><br>
        <input type="submit" name="submit" value="Submit">
    </form>

    <?php
    // Using $_REQUEST to retrieve form data
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $name = $_REQUEST['name'];
        echo "<p>Using \$_REQUEST: Hello, $name!</p>";
    }

    // Using $_POST to retrieve form data
    if (isset($_POST['name'])) {
        $name = $_POST['name'];
        echo "<p>Using \$_POST: Hello, $name!</p>";
    }

    // Using $_GET to retrieve query parameters
    if (isset($_GET['name'])) {
        $name = $_GET['name'];
        echo "<p>Using \$_GET: Hello, $name!</p>";
    }

    // Using $_ENV to retrieve environment variables
    if (isset($_ENV['USER'])) {
        $user = $_ENV['USER'];
        echo "<p>Using \$_ENV: Hello, $user!</p>";
    }

    // Using $_GLOBALS to access global variables
    $global_var = "I am a global variable!";
    echo "<p>Using \$_GLOBALS: $global_var</p>";

    // Using $_SERVER to access server-related information
    $server_name = $_SERVER['SERVER_NAME'];
    $server_port = $_SERVER['SERVER_PORT'];
    echo "<p>Using \$_SERVER: Server Name - $server_name, Port - $server_port</p>";
    ?>
</body>
</html>
