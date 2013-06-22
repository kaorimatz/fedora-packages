Vagrant.configure('2') do |config|
  config.vm.box = 'dummy'

  config.vm.provider :aws do |aws, override|
    aws.access_key_id = ENV['AWS_ACCESS_KEY_ID']
    aws.secret_access_key = ENV['AWS_SECRET_ACCESS_KEY']
    aws.keypair_name = 'key'
    aws.instance_type = 't1.micro'
    aws.region = 'ap-northeast-1'
    aws.security_groups = ['build-rpm']

    packages = %w{
      @development-tools
      rpm-build
      rpmdevtools
      rsync
      tar
      yum-utils
    }
    aws.user_data = <<-USER_DATA
#cloud-config
bootcmd:
  - yum update -y
  - yum install -y #{packages.join(' ')}
  - echo 'Defaults:ec2-user !requiretty' > /etc/sudoers.d/99-vagrant-cloud-init-requiretty
    USER_DATA

    override.ssh.username = 'ec2-user'
    override.ssh.private_key_path = '~/.ssh/aws-key.pem'
  end

  fedora_amis = {
    'fc17.x86_64' => 'ami-45bd3444',
    'fc18.x86_64' => 'ami-33b23b32',
    'fc19.x86_64' => 'ami-4539b044',
  }
  fedora_amis.each do |name, ami_id|
    config.vm.define name do |override|
      override.vm.provider :aws do |aws|
        aws.ami = ami_id
      end
    end
  end
end
