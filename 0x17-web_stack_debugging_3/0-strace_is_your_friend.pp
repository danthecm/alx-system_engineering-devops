# fixing the bug that cause internal server error by replacing the typo
service {'apache2':
  ensure  => running,
  enable  => true,
  restart => true,
  }

exec {'sub phpp for php':
  command => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
  path    =>  [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ],
  notify  => Service['apache2'],
  }
