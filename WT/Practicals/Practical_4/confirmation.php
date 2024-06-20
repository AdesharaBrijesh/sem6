<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order Confirmation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 20px;
        }

        h2 {
            margin-bottom: 20px;
            color: #333;
        }

        table {
            border-collapse: collapse;
            width: 100%;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        th, td {
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }

        th {
            background-color: #f2f2f2;
        }

        .total-price-row td {
            font-weight: bold;
        }

        p {
            margin-bottom: 10px;
        }

        form {
            margin-top: 20px;
        }

        input[type="submit"] {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        input[type="submit"]:hover {
            background-color: #45a049;
        }

        /* Red cancel button */
        input[name="cancel"] {
            background-color: #f44336; /* Red color */
        }
    </style>
</head>
<body>
    <h2>Order Confirmation</h2>
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $firstname = $_POST['firstname'];
        $middlename = $_POST['middlename'];
        $lastname = $_POST['lastname'];
        $itemsData = [];
        if (($handle = fopen("items.csv", "r")) !== FALSE) {
            // Skip the header row
            fgetcsv($handle);
            while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
                $itemsData[] = $data;
            }
            fclose($handle);
        }

        echo "<p><strong>Name: $firstname $middlename $lastname</strong></p>";

        // Display table header
        echo "<table>";
        echo "<tr>";
        echo "<th>Item</th>";
        echo "<th>Price</th>";
        echo "<th>Quantity</th>";
        echo "<th>Gross</th>";
        echo "</tr>";

        $totalPrice = 0; // Initialize total price

        foreach ($itemsData as $item) {
            $itemName = strtolower(str_replace(' ', '_', $item[0]));
            $quantity = $_POST[$itemName];
            if ($quantity > 0) { // Only display if quantity is greater than zero
                $price = (float) $item[1];
                $subtotal = $quantity * $price;
                $totalPrice += $subtotal;

                echo "<tr>";
                echo "<td>{$item[0]}</td>";
                echo "<td>$" . number_format($price, 2) . "</td>";
                echo "<td>$quantity</td>";
                echo "<td>$" . number_format($subtotal, 2) . "</td>";
                echo "</tr>";
            }
        }

        // Display total price row
        echo "<tr class='total-price-row'>";
        echo "<td colspan='3'><strong>Total Price to Pay</strong></td>";
        echo "<td><strong>$" . number_format($totalPrice, 2) . "</strong></td>";
        echo "</tr>";

        echo "</table>";

        // Display selected payment method
        $payment = $_POST['payment'];
        echo "<p><strong>Payment Method: $payment</strong></p>";
    } else {
        echo "<p>Sorry, no order details found.</p>";
    }
    ?>
    <form method="post" action="order.php">
        <input type="submit" name="confirm" value="Confirm Order">
        <input type="submit" name="cancel" value="Cancel Order">
    </form>
</body>
</html>
