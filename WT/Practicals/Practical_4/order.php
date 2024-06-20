<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Order Page</title>
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

        form {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        .name-inputs, .item-container {
            display: flex;
            align-items: center;
            margin-bottom: 15px;
        }

        .name-inputs label, .item-container label {
            width: 100px;
            font-weight: bold;
        }

        .name-inputs input, .item-container input {
            flex: 1;
            padding: 8px;
            margin-left: 10px;
            border-radius: 4px;
            border: 1px solid #ccc;
        }

        .item-container input[type="number"] {
            width: 80px;
        }

        h3 {
            margin-top: 20px;
            margin-bottom: 10px;
            color: #555;
        }

        input[type="radio"] {
            margin-right: 5px;
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
    </style>
</head>
<body>
    <h2>Place Your Order</h2>

    <?php
    // Read item data from CSV file
    $itemsData = [];
    if (($handle = fopen("items.csv", "r")) !== FALSE) {
        // Skip the header row
        fgetcsv($handle);
        while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
            $itemsData[] = $data;
        }
        fclose($handle);
    }
    ?>

    <form method="post" action="confirmation.php">
        <div class="name-inputs">
            <label for="firstname">First Name:</label>
            <input type="text" id="firstname" name="firstname">
            
            <label for="middlename">Middle Name:</label>
            <input type="text" id="middlename" name="middlename">
            
            <label for="lastname">Last Name:</label>
            <input type="text" id="lastname" name="lastname">
        </div>

        <h3>Grocery Items</h3>

        <?php foreach ($itemsData as $item): ?>
            <div class="item-container">
                <label for="<?php echo $item[0]; ?>"><?php echo $item[0] . ' - &#8377;' . number_format((float)$item[1], 2); ?></label>
                <input type="number" id="<?php echo $item[0]; ?>" name="<?php echo strtolower(str_replace(' ', '_', $item[0])); ?>" value="0" min="0">
            </div>
        <?php endforeach; ?>

        <h3>Payment Method</h3>
        <input type="radio" id="cash" name="payment" value="Cash">
        <label for="cash">Cash</label><br>

        <input type="radio" id="card" name="payment" value="Card">
        <label for="card">Card</label><br>

        <input type="radio" id="paypal" name="payment" value="PayPal">
        <label for="paypal">PayPal</label><br><br>

        <input type="submit" name="submit" value="Submit">
    </form>
</body>
</html>
