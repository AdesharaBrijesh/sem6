<?php
session_start();
include 'db_connect.php';

if (!isset($_SESSION['admin'])) {
    header('Location: admin_login.php');
    exit;
}

if (isset($_GET['id'])) {
    $id = $_GET['id'];
    $sql = "SELECT * FROM students WHERE id='$id'";
    $result = mysqli_query($conn, $sql);
    $student = mysqli_fetch_assoc($result);

    if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        $name = $_POST['name'];
        $branch = $_POST['branch'];
        $enrollment = $_POST['enrollment'];

        $update_sql = "UPDATE students SET name='$name', branch='$branch', enrollment='$enrollment' WHERE id='$id'";
        if (mysqli_query($conn, $update_sql)) {
            $_SESSION['message'] = "Record updated successfully.";
            header('Location: admin_dashboard.php');
        } else {
            $_SESSION['message'] = "Error updating record.";
        }
    }
} else {
    header('Location: admin_dashboard.php');
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Update Student</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h2>Update Student</h2>
        <?php
        if (isset($_SESSION['message'])) {
            echo "<p class='error'>" . $_SESSION['message'] . "</p>";
            unset($_SESSION['message']);
        }
        ?>
        <form action="update_student.php?id=<?php echo $id; ?>" method="POST">
            <label>Name: </label>
            <input type="text" name="name" value="<?php echo $student['name']; ?>" required>
            <label>Branch: </label>
            <select name="branch" required>
                <option value="IT" <?php echo $student['branch'] == 'IT' ? 'selected' : ''; ?>>IT</option>
                <option value="CE" <?php echo $student['branch'] == 'CE' ? 'selected' : ''; ?>>CE</option>
                <option value="IOT" <?php echo $student['branch'] == 'IOT' ? 'selected' : ''; ?>>IOT</option>
            </select>
            <label>Enrollment: </label>
            <input type="text" name="enrollment" value="<?php echo $student['enrollment']; ?>" required>
            <input type="submit" value="Update">
        </form>
        <a href="admin_dashboard.php">Go back</a>
    </div>
</body>
</html>
