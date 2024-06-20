<?php
echo "Adeshara Brijesh_21012021001". "<br>";
// Fibonacci series with recursion
function fibonacciWithRecursion($n) {
    if ($n <= 1) {
        return $n;
    } else {
        return fibonacciWithRecursion($n - 1) + fibonacciWithRecursion($n - 2);
    }
}

// Fibonacci series without recursion
function fibonacciWithoutRecursion($n) {
    $fib = array();
    $fib[0] = 0;
    $fib[1] = 1;

    for ($i = 2; $i <= $n; $i++) {
        $fib[$i] = $fib[$i - 1] + $fib[$i - 2];
    }

    return $fib[$n];
}

// Measure time for Fibonacci with recursion
$startRecursion = microtime(true);
$n = 10; // Change n to test with different values
echo "Fibonacci series with recursion:<br>";
for ($i = 0; $i < $n; $i++) {
    echo fibonacciWithRecursion($i) . " ";
}
echo "<br>";
$endRecursion = microtime(true);
$timeRecursion = $endRecursion - $startRecursion;

// Measure time for Fibonacci without recursion
$startWithoutRecursion = microtime(true);
echo "Fibonacci series without recursion:<br>";
for ($i = 0; $i < $n; $i++) {
    echo fibonacciWithoutRecursion($i) . " ";
}
echo "<br>";
$endWithoutRecursion = microtime(true);
$timeWithoutRecursion = $endWithoutRecursion - $startWithoutRecursion;

// Output time taken for both methods
echo "Time taken for recursion: " . $timeRecursion . " seconds<br>";
echo "Time taken without recursion: " . $timeWithoutRecursion . " seconds<br>";

// Check which method is more efficient
if ($timeRecursion < $timeWithoutRecursion) {
    echo "Recursion is more efficient.<br>";
} else {
    echo "Recursion is less efficient.<br>";
}
?>
