# Setup ssh config using puppet
file { ''/etc/ssh/ssh_config':
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