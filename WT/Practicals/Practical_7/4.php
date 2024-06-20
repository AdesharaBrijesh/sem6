<!DOCTYPE html>
<html>
<head>
    <title>Customer Feedback Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 20px;
        }
        #container {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            width: 400px;
            margin: 0 auto;
        }
        input[type="text"], textarea {
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
        .message {
            margin-top: 20px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div id="container">
        <h2>Customer Feedback Form</h2>
        <form method="post">
            <input type="text" name="customer_name" placeholder="Your Name" required><br>
            <input type="text" name="item_purchased" placeholder="Item Purchased" required><br>
            <textarea name="feedback" placeholder="Your Feedback" rows="4" required></textarea><br>
            <input type="submit" name="submit" value="Submit Feedback">
        </form>

        <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            // Retrieve form data
            $customer_name = $_POST['customer_name'];
            $item_purchased = $_POST['item_purchased'];
            $feedback = $_POST['feedback'];

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

            // SQL query to insert feedback into Customer table
            $sql = "INSERT INTO Customer (C_name, Name_Item_purchased, review_product) 
                    VALUES ('$customer_name', '$item_purchased', '$feedback')";

            if ($conn->query($sql) === TRUE) {
                echo "<div class='message'>Feedback submitted successfully. Thank you!</div>";
            } else {
                echo "<div class='message'>Error submitting feedback: " . $conn->error . "</div>";
            }

            // Close connection
            $conn->close();
        }
        ?>
    </div>
</body>
</html>
