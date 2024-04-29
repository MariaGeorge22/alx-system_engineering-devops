# Define a class for configuring the custom header
class nginx_custom_header {

  # Get the hostname of the server
  $hostname = Facter['fqdn']

  # Include the nginx module if not already included
  if ! { Package { name => 'nginx' }  } {
    include nginx
  }

  # Configure the server block to add the custom header
  nginx::server {
    server_name  localhost;

    location / {
      # Add the custom header
      add_header X-Served-By $hostname;
      # Existing configuration for your website or application can go here
    }
  }

  # Restart Nginx service to apply the changes
  Service { name => 'nginx' ; ensure => running ; restart => true }
}
