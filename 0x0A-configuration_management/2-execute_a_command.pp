# Kills the killmenow process.

exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
  path    => '/usr/local/bin/:/usr/bin:/bin/',
  Ieturns => [0, 1],
}
