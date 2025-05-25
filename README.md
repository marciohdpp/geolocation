/var/www/html/
├── index2.html                ← Interface web com JavaScript
├── receiver.php              ← Backend que recebe GPS e chama Python
├── script.py                 ← Script Python para reverse geocode
└── logs/
    ├── php_debug.log         ← Log do backend PHP
    └── script_debug.log      ← Log do script Python

mkdir -p /var/www/html/logs
chmod 777 /var/www/html/logs
chmod +x /var/www/html/script.py 

Abra o site

www.jornaldevarginha.com.br/index2.html

tail -f /var/www/html/logs/php_debug.log
tail -f /var/www/html/logs/script_debug.log
