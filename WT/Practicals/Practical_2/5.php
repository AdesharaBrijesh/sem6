<?php
echo "Adeshara Brijesh_21012021001". "<br>";
// Initialize variables
$sum = 0;
$count = 0;
$number = 1;

// Loop until we count 100 odd numbers
while ($count < 100) {
    // Check if the number is odd
    if ($number % 2 != 0) {
        // Add the odd number to the sum
        $sum += $number;
        // Increment the count of odd numbers
        $count++;
    }
    // Move to the next number
    $number++;
}

// Another method to calculate
// $sum = 0;
// for($i=1; $i<200; $i=$i+2){
//     if ($i % 2 != 0) {
//             $sum += $i;
//     }
// }

// Output the sum of the first 100 odd numbers
echo "The sum of the first 100 odd numbers is: $sum";

?>
