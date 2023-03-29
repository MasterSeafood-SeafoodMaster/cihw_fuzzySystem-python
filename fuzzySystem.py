import random
import numpy as np

def fuzzifier(ds):
	if ds<10:
		return "near"
	elif ds>=10 and ds<20:
		return "middle"
	elif ds>=20:
		return "far"

def fuzzy_rule_base(r, f, l):
	rules_mat = [0, 0, 0]
	sensor_mat = [fuzzifier(r), fuzzifier(f), fuzzifier(l)]

	
	if sensor_mat[0]=="near":
		rules_mat[0] = -40*2
	elif sensor_mat[0]=="middle":
		rules_mat[0] = -20*2
	elif sensor_mat[0]=="far":
		rules_mat[0] = 0

	if sensor_mat[1]=="near":
		rules_mat[1] = random.randint(-1, 1)*40*2
	elif sensor_mat[1]=="middle":
		rules_mat[1] = random.randint(-1, 1)*20*2
	elif sensor_mat[1]=="far":
		rules_mat[1] = random.randint(-1, 1)*0

	if sensor_mat[2]=="near":
		rules_mat[2] = 40*2
	elif sensor_mat[2]=="middle":
		rules_mat[2] = 20*2
	elif sensor_mat[2]=="far":
		rules_mat[2] = 0

	#print(rules_mat)
	return rules_mat

def defuzzifier(rules_mat):
	return np.array(rules_mat).mean()

def fuzzy_system(r, f, l):
	return defuzzifier(fuzzy_rule_base(r, f, l))

#print(fuzzy_system(5, 20, 20))