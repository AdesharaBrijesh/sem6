<?php
echo "Adeshara Brijesh_21012021001". "<br>";
function daysInMonth($month) {
    // Ensure the month parameter is between 1 and 12
    if ($month < 1 || $month > 12) {
        return "Invalid month. Please provide a month between 1 and 12.";
    }

    // Define an array with the number of days in each month
    $daysInMonth = [
        1 => 31, // January
        2 => 28, // February
        3 => 31, // March
        4 => 30, // April
        5 => 31, // May
        6 => 30, // June
        7 => 31, // July
        8 => 31, // August
        9 => 30, // September
        10 => 31, // October
        11 => 30, // November
        12 => 31  // December
    ];

    // Return the number of days for the given month
    return $daysInMonth[$month];
}

// Example usage:
$month = 6; // June
echo "Number of days in month $month is: " . daysInMonth($month);
?>
