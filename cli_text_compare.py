#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 18:53:27 2020

$$$ Basic functionality:
    1. line by line text-based file comparison
    2. opens output in text or md file
    3. uses list along with set to give proper output as well as preserving the original order

$$$ Future functionality:
    1. Github integration
    2. word by word and character by character text-based file comparison
    3. if possible, pdf comparison and word file comparison
    4. ai, ml and dl might be used

$$$ Bugs:
    1. remove case sensitivity:
        Rachel Elizabeth
        rachel elizabeth
    2. removing spaces:
        uget update-windows
         uget update-windows
        uget  update-windows
        uget update-windows  (space at the end)
    3. show duplicate entries:
        olivia austin
        olivia austin a touch of lust
    4. add partial/obscure similarities:
        olivia austin
        olivia austin a touch of lust
    5. Gui enabled
    6. webapp

@author: beril
"""
import os
import platform
#import pathlib

#os.path.exists('text_file2.txt')
#pathlib.Path('text_file1.txt').exists()

def common(filepath1, filepath2):
    with open(filepath1, 'r', encoding = 'utf-8') as file1:
        fl1 = file1.readlines()
    with open(filepath2, 'r', encoding = 'utf-8') as file2:
        fl2 = file2.readlines()
    with open(filepath1, 'r', encoding = 'utf-8') as file1:
        ccf1 = set(file1) #for same file content
    ccf1.discard('\n')
    with open(filepath2, 'r', encoding = 'utf-8') as file2:
        ccf2 = set(file2)
    ccf2.discard('\n')
    with open(filepath1, 'r', encoding = 'utf-8') as file1:
        with open(filepath2, 'r', encoding = 'utf-8') as file2:
            same = set(file1).intersection(file2) #for proper functionality
    same.discard('\n')
    spot = set()
    if same:
        if same == ccf1 and same == ccf2:
            with open('CompareText_output.md', 'a+', encoding = 'utf-8') as out_common:
                out_common.write('\n\n\n#Both files have same content#\n\n')
                out_common.writelines(line for line in fl1 if line != '\n' and not (line in spot or spot.add(line)))                
            return False
        else:
            with open('CompareText_output.md', 'a+', encoding = 'utf-8') as out_common:
                out_common.write('\n\n\n**Similar content**\n\n')
                out_common.writelines(line for line in fl1 if line in fl2 and line != '\n' and not (line in spot or spot.add(line)))                
            return True
    else:
        with open('CompareText_output.md', 'a+', encoding = 'utf-8') as out_common:
            out_common.write('\n\n\n#No similar content - Totally exclusive file content#\n\n')
        return False
    
def difference1(filepath1, filepath2, cp):
    if cp:
        with open(filepath1, 'r', encoding = 'utf-8') as file1:
            fl1 = file1.readlines()
        with open(filepath2, 'r', encoding = 'utf-8') as file2:
            fl2 = file2.readlines()
        with open(filepath1, 'r', encoding = 'utf-8') as file1:
            with open(filepath2, 'r', encoding = 'utf-8') as file2:
                diff1 = set(file1).difference(file2)
        diff1.discard('\n')
        spot = set()
        if diff1:        
            with open('CompareText_output.md', 'a+', encoding = 'utf-8') as out_diff1:
                out_diff1.write('\n\n\n**Different content in first file**\n\n')
                out_diff1.writelines(line for line in fl1 if not (line in fl2) and not (line in spot or spot.add(line)))                
        else:
            with open('CompareText_output.md', 'a+', encoding = 'utf-8') as out_diff1:
                out_diff1.write('\n\n\n#Nothing different in first file#\n\n')

def difference2(filepath1, filepath2, cp):
    if cp:
        with open(filepath1, 'r', encoding = 'utf-8') as file1:
            fl1 = file1.readlines()
        with open(filepath2, 'r', encoding = 'utf-8') as file2:
            fl2 = file2.readlines()
        with open(filepath1, 'r', encoding = 'utf-8') as file1:
            with open(filepath2, 'r', encoding = 'utf-8') as file2:
                diff2 = set(file2).difference(file1)
        diff2.discard('\n')
        spot = set()
        if diff2:
            with open('CompareText_output.md', 'a+', encoding = 'utf-8') as out_diff2:
                out_diff2.write('\n\n\n**Different content in second file**\n\n')
                out_diff2.writelines(line for line in fl2 if not (line in fl1) and not (line in spot or spot.add(line)))                
        else:
            with open('CompareText_output.md', 'a+', encoding = 'utf-8') as out_diff2:
                out_diff2.write('\n\n\n#Nothing different in second file#\n\n')

#unordered functionality due to sets
'''
def common(filename1,filename2):
    with open(filename1, 'r') as file1:
        cfile = set(file1)
    with open(filename1, 'r') as file1:
        cfill = file1.readlines()
    cfile.discard('\n')
    with open(filename1, 'r') as file1:
        with open(filename2, 'r') as file2:
            same = set(file1).intersection(file2)
    same.discard('\n')
    if same:
        if same == cfile:
            with open('CompareText_output.md', 'a+') as out_common:
                out_common.write('\n\n\n#Both Files have same Content#\n\n')
                for line in cfill:
                    out_common.write(line)
            return False
        else:
            with open('CompareText_output.md', 'a+') as out_common:
                out_common.write('\n\n\n**Similar Content**\n\n')
                for line in same:
                    out_common.write(line)
            return True
    else:
        with open('CompareText_output.md', 'a+') as out_common:
            out_common.write('\n\n\n#No Similar Content - Totally exclusive file content#\n\n')
        return False

def difference1(filename1, filename2, cf):
    if cf:
        with open(filename1, 'r') as file1:
            with open(filename2, 'r') as file2:
                diff1 = set(file1).difference(file2)
        diff1.discard('\n')
        if diff1:        
            with open('CompareText_output.md', 'a+') as out_diff1:
                out_diff1.write('\n\n\n**Different content in first File**\n\n')
                for line in diff1:
                    out_diff1.write(line)
        else:
            with open('CompareText_output.md', 'a+') as out_diff1:
                out_diff1.write('\n\n\n#Nothing different in first File#\n\n')

def difference2(filename1, filename2, cf):
    if cf:
        with open(filename1, 'r') as file1:
            with open(filename2, 'r') as file2:
                diff2 = set(file2).difference(file1)
        diff2.discard('\n')
        if diff2:
            with open('CompareText_output.md', 'a+') as out_diff2:
                out_diff2.write('\n\n\n**Different content in second File**\n\n')
                for line in diff2:
                    out_diff2.write(line)
        else:
            with open('CompareText_output.md', 'a+') as out_diff2:
                out_diff2.write('\n\n\n#Nothing different in second File#\n\n')
'''

def main():
    print(f'\nHello, {os.getlogin()}! \nWelcome to the LineByLine Text Comparison Tool\nOrdering of output contents will be as of first file\nPlease provide the filepaths')
    
    if os.path.isfile('CompareText_output.md'):
        os.remove('CompareText_output.md')
    elif os.path.isfile('CompareText_output.txt'):
        os.remove('CompareText_output.txt')

    while True:
        fp1 = input('\nFirst file: ')
        fp2 = input('\nSecond file: ')    
        if os.path.isfile(fp1) and os.path.isfile(fp2):        
            c = common(fp1,fp2)
            difference1(fp1,fp2,c)
            difference2(fp1,fp2,c)
            print('\nText has been compared and saved in file named \"CompareText_output.md\"')
            if platform.system() == 'Linux':
                #os.system('gedit "{0}"'.format('CompareText_output.md'))
                os.system('gedit CompareText_output.md')                
                #os.system('atom CompareText_output.md')
            elif platform.system() == 'Windows':
                fname = os.path.splitext('CompareText_output.md')[0]
                os.rename('CompareText_output.md', fname + '.txt')
                os.startfile('CompareText_output.txt')                
                #os.system('notepad CompareText_output.md')
                #os.system('notepad "{0}"'.format('CompareText_output.md'))
            else:
                print('\nOutput file is saved in the program directory\n')
            break
        else:
            print('\nInvalid path or file does not exists. Please enter again\n')
            continue

if __name__ == '__main__':
    main()

#end of code