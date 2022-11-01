exec {'sed -i s/class-wp-locale.phpp/class-wp-locale.php/g wp-settings.php':
  cwd  => '/var/www/html/',
  path => ['/bin', '/usr/bin', '/usr/sbin']
}
