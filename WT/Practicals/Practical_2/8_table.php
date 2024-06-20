<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Generated Table</title>
    <style>
        table {
            border-collapse: collapse;
        }

        table, th, td {
            border: 1px solid black;
            padding: 5px;
        }
    </style>
</head>
<body>
    <?php
    // Retrieve the number of rows and columns from the form
    $rows = isset($_POST['rows']) ? (int)$_POST['rows'] : 0;
    $cols = isset($_POST['cols']) ? (int)$_POST['cols'] : 0;

    if ($rows > 0 && $cols > 0) {
        echo "Adeshara Brijesh_21012021001". "<br>";
        echo "<h2>Generated Table</h2>";
        echo "<table>";

        // Generate the table with the specified number of rows and columns
        for ($i = 1; $i <= $rows; $i++) {
            echo "<tr>";
            for ($j = 1; $j <= $cols; $j++) {
                echo "<td>Row $i, Col $j</td>";
            }
            echo "</tr>";
        }

        echo "</table>";
    } else {
        echo "<h2>Error: Invalid number of rows or columns.</h2>";
    }
    ?>
</body>
</html>
