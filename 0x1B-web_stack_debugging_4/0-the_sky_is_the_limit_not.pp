# fixes file limit for server

exec { 'changes file limit':
  command => 'sed -i s/15/10000/ /etc/default/nginx && service nginx restart',
  path    => ['/bin/', '/usr/bin', '/usr/sbin']
}
