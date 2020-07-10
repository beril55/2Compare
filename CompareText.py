#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 14:49:51 2020

@author: beril
"""

#working syntax - lists preserve order with set removing duplicates 

def common(lst1, lst2):
    seen = set()   
    with open('CompareText_output.md', 'a+') as out:
        out.write('\n#Similar#\n')
        out.writelines(value for value in lst1 if value in lst2 and value != '\n' and not (value in seen or seen.add(value)))

def difference1(lst1, lst2):
    seen = set()    
    with open('CompareText_output.md', 'a+') as out:
        out.write('\n#file1 different#\n')
        out.writelines(value for value in lst1 if not (value in lst2) and not (value in seen or seen.add(value)))

def difference2(lst1, lst2):
    seen = set()    
    with open('CompareText_output.md', 'a+') as out:
        out.write('\n#file2 different#\n')
        out.writelines(value for value in lst2 if not (value in lst1) and not (value in seen or seen.add(value)))

#long syntax
'''
def intersection(lst1, lst2):
    with open('CompareText_output.md', 'a+') as out:
        out.write('\n#Similar#\n')
    for value in lst1:
        if value in lst2:
            if value == '\n':
                pass
            else:
                with open('CompareText_output.md', 'a+') as out:
                    out.write(value)
        else:
            pass

def difference1(lst1, lst2):
    with open('CompareText_output.md', 'a+') as out:
        out.write('\n#file1 different#\n')
    for value in lst1:
        if value in lst2:
            with open('CompareText_output.md', 'a+') as out:
                pass
        else:
            with open('CompareText_output.md', 'a+') as out:
                out.write(value)

def difference2(lst1, lst2):
    with open('CompareText_output.md', 'a+') as out:
        out.write('\n#file2 different#\n')
    for value in lst2:
        if value in lst1:
            with open('CompareText_output.md', 'a+') as out:
                pass
        else:
            with open('CompareText_output.md', 'a+') as out:
                out.write(value)
'''

with open('/home/beril/Desktop/text_file1.txt', 'r') as cop1:
    copf1 = cop1.readlines()
with open('/home/beril/Desktop/text_file2.txt', 'r') as cop2:
    copf2 = cop2.readlines()

#not required
'''
for i, item in enumerate(copf1):
    if item == '\n':
        copf1.pop(i)
for i, item in enumerate(copf2):
    if item == '\n':
        copf2.pop(i)
'''

common(copf1, copf2)
difference1(copf1, copf2)
difference2(copf1, copf2)


#different syntax working but set do not preserve ordered

'''
with open('CompareText_output.md', 'a+') as out:
    out.write('\n\n\n#Refreshed#\n')

def common():            
    with open('text_file1.txt', 'r') as file1:
        with open('text_file2.txt', 'r') as file2:
            same = set(file1).intersection(file2)
    same.discard('\n')
    with open('CompareText_output.md', 'a+') as out_common:
        out_common.write('\n\n\n**Similar Content**\n\n')
        for line in same:
            out_common.write(line)

def differf1():    
    with open('text_file1.txt', 'r') as file1:
        with open('text_file2.txt', 'r') as file2:
            diff1 = set(file1).difference(file2)
    diff1.discard('\n')
    with open('CompareText_output.md', 'a+') as out_diff1:
        out_diff1.write('\n\n\n**Different content in File1**\n\n')
        for line in diff1:
            out_diff1.write(line)

def differf2():
    with open('text_file1.txt', 'r') as file1:
        with open('text_file2.txt', 'r') as file2:
            diff2 = set(file2).difference(file1)
    diff2.discard('\n')
    with open('CompareText_output.md', 'a+') as out_diff2:
        out_diff2.write('\n\n\n**Different content in File2**\n\n')
        for line in diff2:
            out_diff2.write(line)

common()
differf1()
differf2()
'''

#simple syntax working

'''
def common():
    file1 = open("text_file1.txt", "r")
    file2 = open("text_file2.txt", "r")
    out_common = open("common_output.txt", "a+")
    same = set(file1).intersection(file2)
    same.discard("\n")
    for i in same:
        out_common.write("\nCommon::  " + i + "\n")
    file1.close()
    file2.close()
    out_common.close()

def differ_file1():
    file1 = open("text_file1.txt", "r")
    file2 = open("text_file2.txt", "r")
    out_diff1 = open("differf1_output.txt", "a+")
    diff1 = set(file1).difference(file2)
    diff1.discard("\n")
    for i in diff1:
        out_diff1.write("\nDifferent in file1::  " + i + "\n")
    file1.close()
    file2.close()
    out_diff1.close()
 
def differ_file2():
    file1 = open("text_file1.txt", "r")
    file2 = open("text_file2.txt", "r")
    out_diff2 = open("differf2_output.txt", "a+")
    diff2 = set(file2).difference(file1)
    diff2.discard("\n")
    for i in diff2:
        out_diff2.write("\nDifferent in file2::  " + i + "\n")
    file1.close()
    file2.close()
    out_diff2.close()

common()
differ_file1()
differ_file2()
'''

#not working correctly
'''
for i in file1.readlines():
    for j in file2.readlines():
        if i.strip() and i == j:
            #print("\nCommon::  " + i + "\n")
            out.write("\nCommon::  " + i + "\n")
            
        elif i.strip() and j.strip() and i != j:
            #print("\nfile1::  " + i + "\nfile2::  " +j)
            out.write("\nfile1::  " + i + "\nfile2::  " +j)
'''            

#zip not working completely
'''
for i, j in zip(file1, file2):
    if i.strip() and i == j:
        out.write("\nCommon::  " + i + "\n")
        #print(i, end='', file=out)
    elif i.strip() and j.strip() and i != j:
        out.write("\nfile1::  " + i + "\nfile2::  " +j)
'''


