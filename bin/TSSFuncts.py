#!/bin/env python3

#Written By Taylor Nielson

import sys, os, numpy as np

inputs = {}
coords = []

def default():
        iF = open(os.path.expanduser("~/TSS/bin/.default"), "r")
        line = iF.readline()
        while line:
                if "spin" in line:
                        inputs["spin"] = line.split(':')[1]
                elif "multiplicity" in line:
                        inputs["mult"] = line.split(':')[1]
                elif "basis" in line:
                        inputs["basis"] = line.split(':')[1]
                elif "method" in line:
                        inputs["method"] = line.split(':')[1]
                elif "batch" in line:
                        inputs["batch"] = line.split(':')[1]
                elif "m-basis" in line:
                        inputs["m-basis"] = line.split(':')[1]
                elif "m-method" in line:
                        inputs["m-method"] = line.split(':')[1]
                elif "denfit" in line:
                        inputs["denfit"] = line.split(':')[1]
                line = iF.readline()
        iF.close()
        return inputs

def parseInput(inputFile, inputs):
	name = inputFile.split('.')[0]
	extension = inputFile.split('.')[1]
	if extension == "in":
		pass
	else:
		sys.exit("input file wasn't a .in file")
	iF = open(inputFile, "r")
	line = iF.readline()
	while line:
		#Required - Default in file
		if "spin" in line:
			inputs["spin"] = line.split(':')[1]
		 #Required - Default in file
		elif "multiplicity" in line:
			inputs["mult"] = line.split(':')[1]
		 #Required - Default in file
		elif "basis" in line:
			inputs["basis"] = line.split(':')[1]
		 #Required - Default in file
		elif "method" in line:
			inputs["method"] = line.split(':')[1]
		 #Required - Gaussian has a default
		elif "temperature" in line:
			inputs["temperature"] = line.split(':')[1]
		#Not Required, Gaussian Defaults to Gas
		elif "solvent" in line:
			inputs["solvent"] = line.split(':')[1]
		 #Required - Default in file
		elif "batch" in line:
			inputs["batch"] = line.split(':')[1]
		 #Required - Default in file
		elif "m-basis" in line:
			inputs["m-basis"] = line.split(':')[1]
		 #Required - Default in file
		elif "m-method" in line:
			inputs["m-method"] = line.split(':')[1]	
		#Required, default not in file
		elif "library" in line:
			inputs["library"] = line.split(':')[1]
		#Not Required, Gaussian Defaults to gas
		elif "solvent_model" in line:
			inputs["solvent_model"] = line.split(':')[1]
		 #Required - Default in file
		elif "denfit" in line:
			inputs["denfit"] = line.split(':')[1]
		#Not Required
		elif "subtract" in line:
			parseChanges(line, "subtract", inputs)
		#Not Required
		elif "substitute" in line:
			parseChanges(line, "substitute", inputs)
		#Not Required
		elif "add" in line:
			parseChanges(line, "add", inputs)
		else:
			#Temporary to check the functionality of buildCom Function
			coords.append(line)
		line = iF.readline()
	iF.close()
	return inputs, coords


def parseChanges(line, option, inputs):
	split_line = line.split(':')[1]
	split_line = split_line[1:-2]
	split_again = split_line.split(',')
	if option == "subtract":
		inputs["subtract"] = [val for val in split_again]
	elif option == "substitute":
		inputs["substitute"] = [val for val in split_again]
	elif option == "add":
		inputs["add"] = [val for val in split_again]


def buildCom(inputs, coords):
	oF = open("TSS.com", 'w')
	#need to error check and to check whether the input has the desired info or if the defaults are going to be used
	#
	#if inputs["mult"] == "":
 	#	inputs["mult"] = 2
	#
	oF.write("opt=modred freq=noraman " + inputs["method"].strip() + "/" + inputs["basis"].strip() + " integral = ultrafine")
	oF.write("\n\n")
	oF.write("TSS")
	oF.write("\n\n")
	oF.write(inputs["mult"].strip() + " " + inputs["spin"])
	for coord in coords:
		oF.write(coord)
	oF.write("\n")
	oF.write("\n")
	oF.write("\n")
	oF.write("\n")
	oF.close()

def buildInputs(library, library_location):
	if library is True:
		buildLibraryInputs(library_location)
	else:
		buildGuessedInputs()

