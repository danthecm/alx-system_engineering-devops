# Kills a program named killmenow

exec { 'killmenow':
  command => 'pkill -9 killmenow',
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => 'pgrep killmenow',
}
