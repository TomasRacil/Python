#!/usr/bin/python
#!python
import itertools

def lexwhile(inputstring):
	space = " \t\n\r"
	punctuation = "()[]{},"
	symbolic = "~!'@#$%^&*-+=|\\:;<>.?/"
	numeric = "0123456789"
	alphanumeric = "abcdefghijklmnopqrstuvwxyz_'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	if inputstring[0] in space:
		for i,c in enumerate(inputstring):
			if c not in space:
				return '', inputstring[i:]
			elif i==len(inputstring)-1:
				return '', ''
	elif inputstring[0] in punctuation:
		return inputstring[0], inputstring[1:]
	elif inputstring[0] in symbolic:
		for i,c in enumerate(inputstring):
			if c not in symbolic:
				return inputstring[:i], inputstring[i:]
			elif i==len(inputstring)-1:
				return inputstring, ''
	elif inputstring[0] in numeric:
		for i,c in enumerate(inputstring):
			if c not in numeric:
				return inputstring[:i], inputstring[i:]
			elif i==len(inputstring)-1:
				return inputstring, ''
	elif inputstring[0] in alphanumeric:
		for i,c in enumerate(inputstring):
			if c not in alphanumeric:
				return inputstring[:i], inputstring[i:]
			elif i==len(inputstring)-1:
				return inputstring, ''
	else:
		print ("Fehler in lexwhile")
def lex(inputstring):
	t, r = lexwhile(inputstring)
	if t and r:
		return [t] + lex(r)
	elif r:
		return lex(r)
	else:
		return [t]
def remove_brackets(inp):
	b=0 
	if inp[0]=='(': 
		for i,t in enumerate(inp):
			if t=='(':
				b+=1
			elif t==')':
				b-=1
				if b==0 and i<(len(inp)-1):
					return inp
				else:
					return inp[1:-1]
	elif inp[0]=='[': 
		for i,t in enumerate(inp):
			if t=='[':
				b+=1
			elif t==']':
				b-=1
				if b==0 and i<(len(inp)-1):
					return inp
				else:
					return inp[1:-1]
	elif inp[0]=='{': 
		for i,t in enumerate(inp):
			if t=='{':
				b+=1
			elif t=='}':
				b-=1
				if b==0 and i<(len(inp)-1):
					return inp
				else:
					return inp[1:-1]
	else:
		return inp

def parse_and(inp):
	inp = remove_brackets(inp)
	if len(inp)<=2:
		return inp
	b = 0
	for i,t in enumerate(inp):
		if t in '([{':
			b += 1
		elif t in '])}':
			b -= 1
		elif t=='/\\' and b==0:
			return [parse_neg(inp[:i]) + ['and'] + parse_and(inp[i+1:])]
	return parse_neg(inp)	

def parse_or(inp):
	inp = remove_brackets(inp)
	if len(inp)<=2:
		return inp
	b = 0
	for i,t in enumerate(inp):
		if t in '([{':
			b += 1
		elif t in '])}':
			b -= 1
		elif t=='\\/' and b==0:
			return [parse_and(inp[:i]) + ['or'] + parse_or(inp[i+1:])]
	return parse_and(inp)

def parse_implies(inp):
	inp = remove_brackets(inp)
	if len(inp)<=2:
		return inp
	b = 0
	for i,t in enumerate(inp):
		if t in '([{':
			b += 1
		elif t in '])}':
			b -= 1
		elif t=='==>' and b==0:
			return [parse_or(inp[:i]) + ['implies'] + parse_implies(inp[i+1:])]
	return parse_or(inp)

def parse(inp):
	inp = remove_brackets(inp)
	if len(inp)<=2:
		return inp
	b = 0
	for i,t in enumerate(inp):
		if t in '([{':
			b += 1
		elif t in '])}':
			b -= 1
		elif t=='<=>' and b==0:
			return [parse_implies(inp[:i]) + ['iff'] + parse(inp[i+1:])]
	return parse_implies(inp)

def parse_neg(inp):
	if len(inp)<=2:
		return inp
	b=0 
	if inp[1]=='(' and inp[0]=='~': 
		for i,t in enumerate(inp[1:]):
			if t=='(':
				b+=1
			elif t==')':
				b-=1
				if b==0 and i<(len(inp)-2):
					return parse_iff(inp)
				else:
					return [['~'] + parse(inp[2:-1])]
	elif inp[1]=='[' and inp[0]=='~': 
		for i,t in enumerate(inp[1:]):
			if t=='[':
				b+=1
			elif t==']':
				b-=1
				if b==0 and i<(len(inp)-2):
					return parse_iff(inp)
				else:
					return [['~'] + parse(inp[2:-1])]
	if inp[1]=='{' and inp[0]=='~': 
		for i,t in enumerate(inp[1:]):
			if t=='{':
				b+=1
			elif t=='}':
				b-=1
				if b==0 and i<(len(inp)-2):
					return parse_iff(inp)
				else:
					return [['~'] + parse(inp[2:-1])]
	else:
		return parse(inp)

def evaluate(fm,dictionary):
	def valuate(var):
		if var in variables:
			return variables[var]
		while True:
			val = raw_input('Valuation of '+ var + ': ')
			if val in ['True', 'true']:
				variables[var]=True
				return True
			elif val in ['False', 'false']:
				variables[var]=False
				return False

	variables = dictionary

	if len(fm)==1:
		if not isinstance(fm[0], str):
			return evaluate(fm[0],variables)
		elif fm[0] in ['True', 'true']:
			return True
		elif fm[0] in ['False', 'false']:
			return False
		else:
			return valuate(fm[0])
	elif len(fm)==2:
		return not evaluate([fm[1]],variables)
	else:
		for i,t in enumerate(fm):
			if t=='and':
				l = evaluate(fm[:i],variables)
				r = evaluate(fm[i+1:],variables)
				if l and r:
					return True
				else:
					return False
			elif t=='or':
				l = evaluate(fm[:i],variables)
				r = evaluate(fm[i+1:],variables)
				if l or r:
					return True
				else:
					return False
			elif t=='implies':
				l = evaluate(fm[:i],variables)
				r = evaluate(fm[i+1:],variables)
				if l and not r:
					return False
				else:
					return True
			elif t=='iff':
				l = evaluate(fm[:i],variables)
				r = evaluate(fm[i+1:],variables)
				if (l and r) or (not l and not r):
					return True
				else:
					return False

def atoms(fm):
	if len(fm)==1:
		if not isinstance(fm[0], str):
			return atoms(fm[0])
		elif fm[0] in ['True','true','False','false']:
			return set([])
		else:
			return set(fm)
	elif len(fm)==2:
		return atoms([fm[1]])
	else:
		for i,t in enumerate(fm):
			if t in ['and','or','implies','iff']:
				return atoms(fm[:i]) | atoms(fm[i+1:])

def onallvaluations(fm):
	at = atoms(fm)
	if not at:
		return evaluate(fm,{})
	for combination in itertools.product([True,False],repeat=len(at)):
		dictionary={}
		for i,var in enumerate(at):
			dictionary[var]=combination[i]
		if not evaluate(fm,dictionary):
			return False
	else:
		return True
def tautology(fm):
	return onallvaluations(fm)
def unsatisfiable(fm):
	return tautology(['~',fm])
def satisfiable(fm):
	return not unsatisfiable(fm)
def entails(alpha, beta):
	return tautology([alpha, 'implies', beta])
def check(fm):
	if tautology(fm):
		return "Tautology"
	elif satisfiable(fm):
		return "Satisfiable"
	else:
		return "Unsatisfiable"


