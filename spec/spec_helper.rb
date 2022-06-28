require 'awspec'
require 'inspec'

require 'awspec'

# These are the defaults, but you can change them.
Awspec.configure do |config|
  config.client_backoff 0.0
  config.client_backoff_limit 30
  config.client_iteration 1
end
