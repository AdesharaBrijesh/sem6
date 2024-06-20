<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Posts from JSONPlaceholder</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .post {
            margin-bottom: 20px;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        .post h2 {
            margin-top: 0;
            font-size: 1.5em;
            color: #333;
        }
        .post p {
            font-size: 1em;
            line-height: 1.6;
            color: #666;
        }
        .error {
            color: red;
        }
        .api-info {
            margin-bottom: 20px;
        }
        .api-info h1, .api-info p {
            margin: 0;
        }
        .api-info h1 {
            font-size: 2em;
            color: #333;
        }
        .api-info p {
            font-size: 1em;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="api-info">
            <h1>JSONPlaceholder API</h1>
            <p>Usage: A free fake online REST API for testing and prototyping.</p>
        </div>
        <?php
        // JSONPlaceholder API URL for fetching posts
        $apiUrl = "https://jsonplaceholder.typicode.com/posts";

        // Function to get data from the API
        function getApiData($url) {
            $ch = curl_init();
            
            curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
            curl_setopt($ch, CURLOPT_URL, $url);
            
            $response = curl_exec($ch);
            
            if (curl_errno($ch)) {
                echo '<p class="error">Error: ' . curl_error($ch) . '</p>';
                return null;
            }
            
            curl_close($ch);
            
            return json_decode($response, true);
        }

        // Fetch posts data
        $posts = getApiData($apiUrl);

        // Check if data is received
        if (!empty($posts)) {
            echo "<h1>Posts</h1>";
            foreach ($posts as $post) {
                echo "<div class='post'>";
                echo "<h2>" . htmlspecialchars($post['title']) . "</h2>";
                echo "<p>" . nl2br(htmlspecialchars($post['body'])) . "</p>";
                echo "</div>";
            }
        } else {
            echo "<p class='error'>Unable to fetch posts data.</p>";
        }
        ?>
    </div>
</body>
</html>
