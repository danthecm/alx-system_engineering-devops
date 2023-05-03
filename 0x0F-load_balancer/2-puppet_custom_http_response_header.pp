class { 'nginx':
  http_extra_headers => {
    'X-Served-By' => "$hostname",
  },
}
