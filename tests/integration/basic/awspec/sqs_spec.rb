require 'spec_helper'

describe sqs('jobs-queue'), region: 'ap-south-1' do
  it { should exist }
  its(:queue_url) { should eq 'https://sqs.ap-south-1.amazonaws.com/486391667947/jobs-queue' }
  its(:queue_arn) { should eq 'arn:aws:sqs:ap-south-1:486391667947:jobs-queue' }
  its(:visibility_timeout) { should eq '30' }
  its(:maximum_message_size) { should eq '262144' }
  its(:message_retention_period) { should eq '345600' }
  its(:delay_seconds) { should eq '0' }
  its(:receive_message_wait_time_seconds) { should eq '0' }
end
