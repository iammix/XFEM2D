import os
import sys

# PATRAN 3 home directory
fname = '../P3HOME.PATH'
fr = open(fname, 'r')
P3_HOME = fr.readline()
print(P3_HOME)
fr.close

# Location of include files.
IPATH ='-I'+P3_HOME+'\\customization'

# PERL PATH
PERL_MSC = P3_HOME + '\\Perl_msc\\bin\\perl_msc'

# COMPILE COMMAND PATH
PCLCOMP=PERL_MSC + ' ..\\pclcomp'

# Name of PCL source files except as extension 
PclFiles =[     'RESULT_REPORT_TOOLS',
                'RESULT_OPTION',
                'OptionItemList',
                'OptionItemFilter',
                'OptionItemElemEdge',
                'OptionItemLabelStyle',
                'OptionOnOff'
          ]

# Name of the target pcl library
PclLibrary='Result.plb'

for PclFile in PclFiles:
    # cpp arguments for preprocessing a single pcl source file
    CPPARGS=IPATH +' -C '+ PclFile+'.PCL' +' '+ PclFile+'.CPP'
    os.system('CPP '+ CPPARGS)
    print('CPP '+ CPPARGS)
    os.system(PCLCOMP + ' -pob '+ PclFile+'.CPP')
    os.system(PCLCOMP + ' -m ' + PclLibrary + ' '+PclFile+'.pob ')
    print(PclFile+'.pob'+' -> ' + PclLibrary)
# os.system('del *.cpp')
# os.system('del *.pob')
print('***** Complete ******')
