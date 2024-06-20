<?php
session_start();
include 'db_connect.php';

if (!isset($_SESSION['username'])) {
    header('Location: login.php');
    exit;
}

$enrollment = $_SESSION['enrollment'];
$sql = "SELECT photo FROM students WHERE enrollment='$enrollment'";
$result = mysqli_query($conn, $sql);
$row = mysqli_fetch_assoc($result);
$photo = $row['photo'];
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h2>Welcome, <?php echo htmlspecialchars($_SESSION['username']); ?>!</h2>
        <p>Enrollment: <?php echo htmlspecialchars($_SESSION['enrollment']); ?></p>
        <div class="profile-picture">
            <img src="<?php echo htmlspecialchars($photo); ?>" alt="Profile Picture">
        </div>
        <p><a href="edit_profile.php">Edit Profile</a></p>
        <p><a href="logout.php">Logout</a></p>
    </div>
</body>
</html>
