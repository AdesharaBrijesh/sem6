<!DOCTYPE html>
<html>
<head>
    <title>Customer Information</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 20px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>
    <h2>Customer Information</h2>

    <?php
    // Connect to MySQL server
    $servername = "localhost"; // Change this if MySQL server is running on a different host
    $username = "root"; // Your MySQL username
    $password = ""; // Your MySQL password
    $database = "WT_P7"; // Your MySQL database name

    $conn = new mysqli($servername, $username, $password, $database);

    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // SQL query to retrieve data from Customer table
    $sql = "SELECT * FROM Customer";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        // Output data in table format
        echo "<table>";
        echo "<tr><th>C_Id</th><th>C_name</th><th>Name_Item_purchased</th><th>review_product</th></tr>";
        while($row = $result->fetch_assoc()) {
            echo "<tr>";
            echo "<td>" . $row["C_Id"] . "</td>";
            echo "<td>" . $row["C_name"] . "</td>";
            echo "<td>" . $row["Name_Item_purchased"] . "</td>";
            echo "<td>" . $row["review_product"] . "</td>";
            echo "</tr>";
        }
        echo "</table>";
    } else {
        echo "No data found.";
    }

    // Close connection
    $conn->close();
    ?>
</body>
</html>
