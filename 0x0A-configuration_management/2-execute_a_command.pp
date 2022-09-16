# kills the program 'killmenow'
exec { 'kill-killmenow':
  command => '/usr/bin/pkill killmenow'
}
