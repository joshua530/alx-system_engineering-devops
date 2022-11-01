# Fixes typo error in wp configuration

exec {'sed -i s/.phpp/.php/g wp-settings.php':
  cwd  => '/var/www/html/',
  path => ['/bin', '/usr/bin', '/usr/sbin']
}
