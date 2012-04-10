from distutils.core import setup

pkg = 'Extensions.AddStreamUrl'
setup (name = 'enigma2-plugin-extensions-addstreamurl',
	version = '1.0',
	description = 'Add a stream url to channel list',
	packages = [pkg],
	package_dir = {pkg: 'plugin'}
)

