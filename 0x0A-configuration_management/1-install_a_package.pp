# Install flask from pip3
package { 'python3.8':
  ensure => present,
}

# ensure that pip present
package { 'python3-pip':
  ensure => present,
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Install Werkzeug 
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
