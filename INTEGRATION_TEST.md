# Infra integration testing using  awspec 

## Common steps
- download and install rvm and ruby
- Using gem install bundler
-  ```gem install bundler```
- create Gemfile with following contents in directory where kitchen is required. In this case its preprod env ::

```

source 'https://rubygems.org'
gem 'nokogiri'
gem 'rspec', :require => 'spec'
gem 'awspec'
gem 'inspec', ">= 4.37.8"
gem "rake"
gem "rubyzip", ">= 1.3.0"
```
- run ```BUNDLE_GEMFILE=Gemfile bundler install``` command to install all packages.

# AWSSpec setup
- code for awspec is available in tests/integration/basic/awspec
- code can also be setup in spec/ directory

# AWSSpec setup with Rake
- Install Rake gem
- Add Rakefile
- Add spec*.rb file to spec directory. Include spec_helper.rb file as well.
- run following commands ::


```sh
bundle exec rspec tests/integration/basic/awspec

```

```
AWS_PROFILE=pahal bundle exec rspec spec
AWS_PROFILE=pahal bundle exec rake spec/
```

```
AWS_PROFILE=pahal bundle exec rspec tests/
AWS_PROFILE=pahal bundle exec rake tests/
```
