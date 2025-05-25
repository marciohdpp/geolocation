<?php
ini_set('display_errors', 1);
error_reporting(E_ALL);

// Caminho do log acessível
$logfile = "/var/www/html/logs/php_debug.log";
file_put_contents($logfile, date("c") . " - PHP chamado\n", FILE_APPEND);

$data = json_decode(file_get_contents("php://input"), true);
$lat = escapeshellarg($data["latitude"]);
$lon = escapeshellarg($data["longitude"]);

file_put_contents($logfile, "Latitude: $lat, Longitude: $lon\n", FILE_APPEND);

$python = escapeshellarg("/usr/bin/python3");
$script = escapeshellarg("/var/www/html/script.py");
$cmd = "$python $script $lat $lon 2>&1";

file_put_contents($logfile, "Executando: $cmd\n", FILE_APPEND);

$output = shell_exec($cmd);

file_put_contents($logfile, "Saída Python:\n$output\n", FILE_APPEND);

echo "<pre>$output</pre>";
?>
