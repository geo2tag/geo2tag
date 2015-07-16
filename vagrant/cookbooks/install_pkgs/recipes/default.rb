['mongodb', 'python-pip', 'python-dev', 'git', 'vim', 'apache2', 'libapache2-mod-wsgi'].each do |pkg|
	package pkg do
		action :install
	end
end