<?php
// function isPrime($num) {
//     if ($num <= 1) {
//         return false;
//     }
//     for ($i = 2; $i <= sqrt($num); $i++) {
//         if ($num % $i == 0) {
//             return false;
//         }
//     }
//     return true;
// }

// function listPrimesInRange($start, $end) {
//     echo "Prime numbers between $start and $end are:\n";
//     for ($i = $start; $i <= $end; $i++) {
//         if (isPrime($i)) {
//             echo $i . " ";
//         }
//     }
// }

// // Example usage:
// $start = 1;
// $end = 100;
// listPrimesInRange($start, $end);

// another way

echo "Adeshara Brijesh_21012021001". "<br>";
$range=100;
echo "The Range is: ".$range."<br>";
for($i=1; $i<=$range; $i++){
    $flag=true;
    for($j=2; $j<$i; $j++ ){
        if($i % $j == 0){
            $flag=false;
        }
    }
    if($flag){
        echo $i." ";
    }
}
?>