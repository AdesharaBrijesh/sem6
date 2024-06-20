<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "globe";

$conn = new mysqli($servername, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$type = $_GET['type'];

if ($type == 'country') {
    $sql = "SELECT id, name FROM countries";
    $result = $conn->query($sql);
    echo '<option value="">Select Country</option>';
    while($row = $result->fetch_assoc()) {
        echo '<option value="'.$row['id'].'">'.$row['name'].'</option>';
    }
} elseif ($type == 'state') {
    $country_id = $_GET['country_id'];
    $sql = "SELECT id, name FROM states WHERE country_id = $country_id";
    $result = $conn->query($sql);
    echo '<option value="">Select State</option>';
    while($row = $result->fetch_assoc()) {
        echo '<option value="'.$row['id'].'">'.$row['name'].'</option>';
    }
} elseif ($type == 'city') {
    $state_id = $_GET['state_id'];
    $sql = "SELECT id, name FROM cities WHERE state_id = $state_id";
    $result = $conn->query($sql);
    echo '<option value="">Select City</option>';
    while($row = $result->fetch_assoc()) {
        echo '<option value="'.$row['id'].'">'.$row['name'].'</option>';
    }
}

$conn->close();
?>
