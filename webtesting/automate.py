import multiprocessing as mp
import sys,os

def run(x):
	os.system('npm start index.html "%s"'%x)

data = ['arg1','arg2']

mp.Pool().map(run,data)
