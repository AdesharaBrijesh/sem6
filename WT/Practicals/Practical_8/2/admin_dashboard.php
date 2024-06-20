<?php
session_start();
include 'db_connect.php';

if (!isset($_SESSION['admin'])) {
    header('Location: admin_login.php');
    exit;
}

$search = '';
if (isset($_GET['search'])) {
    $search = $_GET['search'];
    $sql = "SELECT * FROM students WHERE name LIKE '%$search%' ORDER BY name";
} else {
    $sql = "SELECT * FROM students ORDER BY name";
}

$result = mysqli_query($conn, $sql);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h2>Admin Dashboard</h2>
        <form action="admin_dashboard.php" method="GET">
            <input type="text" name="search" placeholder="Search by name" value="<?php echo $search; ?>">
            <input type="submit" value="Search">
        </form>
        <table>
            <thead>
                <tr>
                    <th>Enrollment</th>
                    <th>Name</th>
                    <th>Branch</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <?php while ($row = mysqli_fetch_assoc($result)) { ?>
                <tr>
                    <td><?php echo $row['enrollment']; ?></td>
                    <td><?php echo $row['name']; ?></td>
                    <td><?php echo $row['branch']; ?></td>
                    <td>
                        <a href="update_student.php?id=<?php echo $row['id']; ?>">Update</a>
                        <a href="delete_student.php?id=<?php echo $row['id']; ?>" onclick="return confirm('Are you sure you want to delete this record?')">Delete</a>
                    </td>
                </tr>
                <?php } ?>
            </tbody>
        </table>
        <a href="admin_logout.php">Logout</a>
    </div>
</body>
</html>
