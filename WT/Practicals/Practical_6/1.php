<!DOCTYPE html>
<html>
<head>
    <title>Student Registration Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        #container {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            width: 400px;
        }
        h2 {
            text-align: center;
        }
        input[type="text"], select, input[type="file"] {
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
        .error {
            color: red;
            font-size: 12px;
        }
    </style>
</head>
<body>
    <div id="container">
        <h2>Student Registration Form</h2>
        <form method="post" enctype="multipart/form-data">
            <input type="text" name="enrollment_no" placeholder="Enrollment No." required><br>
            <input type="text" name="full_name" placeholder="Full Name" required><br>
            <select name="gender" required>
                <option value="">Select Gender</option>
                <option value="male">Male</option>
                <option value="female">Female</option>
            </select><br>
            <input type="text" name="mobile" placeholder="Mobile" required><br>
            <input type="text" name="email" placeholder="Email" required><br>
            <input type="text" name="address" placeholder="Address"><br>
            <input type="file" name="profile_photo" accept="image/*" required><br>
            <input type="submit" name="submit" value="Register">
        </form>

        <?php
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            // Validate and store data
            $errors = array();

            $enrollment_no = $_POST['enrollment_no'];
            $full_name = $_POST['full_name'];
            $gender = $_POST['gender'];
            $mobile = $_POST['mobile'];
            $email = $_POST['email'];
            $address = $_POST['address'];
            $profile_photo = $_FILES['profile_photo']['name'];
            $tmp_profile_photo = $_FILES['profile_photo']['tmp_name'];

            // Validate full name
            if (!preg_match("/^[a-zA-Z\s]+$/", $full_name)) {
                $errors['full_name'] = "Invalid full name";
            }

            // Validate mobile
            if (!preg_match("/^[0-9]{10}$/", $mobile)) {
                $errors['mobile'] = "Invalid mobile number";
            }

            // Validate email
            if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
                $errors['email'] = "Invalid email address";
            }

            // Validate profile photo
            $allowed_extensions = array('jpg', 'jpeg', 'png', 'gif');
            $file_extension = strtolower(pathinfo($profile_photo, PATHINFO_EXTENSION));
            if (!in_array($file_extension, $allowed_extensions)) {
                $errors['profile_photo'] = "Invalid file format. Allowed formats: jpg, jpeg, png, gif";
            }

            // If no errors, store data in CSV file
            if (empty($errors)) {
                $csv_data = array($enrollment_no, $full_name, $gender, $mobile, $email, $address, $profile_photo);
                $file = fopen("student_data.csv", "a");
                fputcsv($file, $csv_data);
                fclose($file);
                move_uploaded_file($tmp_profile_photo, "profile_photos/$profile_photo");
                echo "<p>Registration successful!</p>";
            } else {
                // Display validation errors
                echo "<div class='error'>";
                foreach ($errors as $error) {
                    echo "<p>$error</p>";
                }
                echo "</div>";
            }
        }
        ?>
    </div>
</body>
</html>
