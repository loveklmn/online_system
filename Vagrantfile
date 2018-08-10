# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "fedora/27-cloud-base"
  config.vm.box_url = "https://mirrors.tuna.tsinghua.edu.cn/fedora/releases/27/CloudImages/x86_64/images/Fedora-Cloud-Base-Vagrant-27-1.6.x86_64.vagrant-virtualbox.box"
  config.vm.box_download_checksum = "7a37a20f87900c7a9360969658c58e5a3edcac2f5120897ce783cf21b2debbf9"
  config.vm.box_download_checksum_type = :sha256
  config.vm.network "private_network", ip: "192.168.55.33"
  config.vm.synced_folder ".", "/vagrant", create: true, nfs: true
  config.vm.provider "virtualbox" do |vb|
	vb.customize ["setextradata", :id, "VBoxInternal2/SharedFoldersEnableSymlinksCreate/v-root", "1"]
    vb.memory = "1024"
    vb.cpus = 2
  end

  config.vm.provision "shell", inline: <<-SCRIPT
    sudo dnf install -y git
    sudo dnf install -y gcc
    sudo dnf update -v --debugsolver vim-minimal -y
    sudo dnf install -y vim
  SCRIPT

  config.vm.provision "shell", inline: <<-SHELL
  type -fp mysql &>/dev/null || (
    dnf install -y mariadb-server mariadb-devel
    systemctl enable mariadb
    systemctl start mariadb
    mysqladmin -u root password vagrant
  )
  type -fp nginx &>/dev/null || (
    dnf -y install nginx
    systemctl enable nginx
    systemctl start nginx
  )
  SHELL

  config.vm.provision "shell", privileged: false, inline: <<-SHELL
    type -fp conda &>/dev/null || (
    source /home/vagrant/.bashrc
    echo -e "\n\nDownloading Anaconda installer. This may take more than a few minutes."
    curl https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-latest-Linux-x86_64.sh -o /home/vagrant/anaconda.sh --silent
    bash /home/vagrant/anaconda.sh -b -p /home/vagrant/anaconda
    cat >> /home/vagrant/.bashrc << END
# For anaconda
export PATH="/home/vagrant/anaconda/bin:$PATH"
END
    source /home/vagrant/.bashrc
)
  SHELL


  config.vm.provision "shell", privileged: false, inline: <<-SCRIPT
    type -fp node &>/dev/null || (
      curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.11/install.sh | bash
      source /home/vagrant/.bashrc
      nvm install --lts
      npm config set registry https://registry.npm.taobao.org
    )
    type -fp vue &>/dev/null || (
      source /home/vagrant/.bashrc
      npm install -g @vue/cli @vue/cli-init
    )
  SCRIPT

end
