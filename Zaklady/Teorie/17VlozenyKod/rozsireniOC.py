from distutils.core import setup, Extension

module1 = Extension('exmod',
	include_dirs = ['usr/local/include'],
	libraries=['pthread'],
	sources=['rozsirujiciModul.c'])
#C:\Microsoft\AndroidNDK64\android-ndk-r16b\prebuilt\windows-x86_64\include\python2.7
setup (name = 'exmod',
	version = '1.0',
	description = 'Ukázkový modul',
	author = 'TomasRacil',
	url = 'https://github.com/TomasRacil',
	ext_modules = [module1])