#install a package any version
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
