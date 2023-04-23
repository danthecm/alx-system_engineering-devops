file { '/home/ubuntu/.ssh/config':
  ensure => present,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0600',
  content => "
    Host 35.153.66.143
        IdentityFile ~/.ssh/school
        PasswordAuthentication no
  ",
}