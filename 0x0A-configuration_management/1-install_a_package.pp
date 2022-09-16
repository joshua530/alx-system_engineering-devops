# installs flask using pip3
package { 'flask':
  name    => 'flask',
  command => '/usr/bin/pip3 install Flask==2.1.0',
}
