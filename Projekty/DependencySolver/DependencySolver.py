# File name: DependencySolver.py
# Description: Install necessary dependencies and return system back to its original state.
# Author: Tomáš Ráčil
# Date: 20-11-2020

import argparse
import glob
import logging
import os
import pkg_resources
import sys
import subprocess


def parse_arguments():
    """Read arguments from a command line."""
    parser = argparse.ArgumentParser(description='Arguments get parsed via --commands') 
    parser.add_argument('-v', metavar='verbosity', type=int, default=2, help='Verbosity of logging: 0 -critical, 1- error, 2 -warning, 3 -info, 4 -debug')
    parser.add_argument('-r', metavar='requirements', type=str, default="pckgs.txt", help='Path to file with required packages')
    parser.add_argument('-p', metavar='python', type=str, default="main.py", help='Path to file python script')
    parser.add_argument('-c', metavar='command', nargs='*', default=['pipenv', 'run', 'python'], help='Command to run script')

    args = parser.parse_args()
    #verbose = {0: logging.CRITICAL, 1: logging.ERROR, 2: logging.WARNING, 3: logging.INFO, 4: logging.DEBUG}
    #logging.basicConfig(format='%(message)s', level=verbose[args.v], stream=sys.stdout)
    
    return args


def findMissing(requirements):
	"""Identify missing dependencies"""
	requiredPckgs=set(line.strip() for line in open(requirements))
	#requiredPckgs = {'opencv-python', 'numpy'}
	installed = {pkg.key for pkg in pkg_resources.working_set}
	pipenvInstalled='pipenv' in installed
	missingPckgs = (requiredPckgs - installed)!=set()
	#print(missingPckgs, pipenvInstalled, requiredPckgs)
	return missingPckgs, pipenvInstalled, requiredPckgs

def solveRequirements(missingMain,pipenvExist,requiredPckgs):
	"""Function which takes care of dependencies"""
	if missingMain:
		if not pipenvExist: 
			subprocess.run([sys.executable, '-m', 'pip', 'install', 'pipenv'],capture_output=True)
		
		checkPckgsSubproces = subprocess.run(['pipenv','run','python', "-c", "import pkg_resources;print({pkg.key for pkg in pkg_resources.working_set})"], capture_output=True, text=True)
		installed=eval(checkPckgsSubproces.stdout)
		missingVenv = requiredPckgs - installed
		if missingVenv: 
			subprocess.run([sys.executable, '-m', 'pipenv', 'install', *missingVenv],capture_output=True)	
			if checkPckgsSubproces.stderr == '':
				return missingVenv, True
			else:
				return missingVenv, False
	else:
		return {}, True

def revertBack(pipenvInstalled,missingVenv,venvExist):
	"""Function for reverting changes back to its original state"""
	if not missingVenv=={}:
		if venvExist:
			subprocess.run(['pipenv', 'uninstall', *missingVenv], capture_output=True)
			subprocess.run(['pipenv', 'clean'], capture_output=True)
		else:
			subprocess.run(['pipenv', '--rm'], capture_output=True)
			for f in glob.glob('Pipfile*'):
				os.remove(f)
			if not pipenvInstalled:
				subprocess.run([sys.executable, '-m', 'pip', 'uninstall', 'pipenv'], capture_output=True, text=True,input='y')	

def main(args):
	"""Main function"""
	missingPckgs, pipenvInstalled,requiredPckgs = findMissing(args.r)
	missingVenv,venvExist = solveRequirements(missingPckgs, pipenvInstalled, requiredPckgs)
	subprocess.run([*args.c, args.p] if missingPckgs else ['python', args.p])
	if missingPckgs:
		revertBack(pipenvInstalled,missingVenv,venvExist)

if __name__ == '__main__':
    args = parse_arguments()
    main(args)