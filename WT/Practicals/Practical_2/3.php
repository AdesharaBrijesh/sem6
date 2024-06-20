<?php
echo "Adeshara Brijesh_21012021001". "<br>";
// Get the current hour
date_default_timezone_set('Asia/Kolkata');
$h = date('G', time());
// Define messages based on the time of day
if ($h >= 5 && $h < 12) {
    echo "Current time : ". $h . "<br>"." Good Morning";
} elseif ($h >= 12 && $h < 17) {
    echo "Current time : ". $h . "<br>"." Good Afternoon";
} elseif ($h >= 17 && $h < 21) {
    echo "Current time : ". $h . "<br>"." Good Evening";
} else {
    echo "Current time : ". $h . "<br>"." Good Night";
}
?>
