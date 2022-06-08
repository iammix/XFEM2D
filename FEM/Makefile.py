import os
import sys
import string

#PATRAN 3 home directory
fname = '../P3HOME.PATH'
fr = open(fname, 'r')
P3_HOME = fr.readline()
print(P3_HOME)
#fr.close

#P3_HOME = 'C:\\MSC.Software\\Patran_x64\\20122'

# Location of include files.
IPATH ='-I'+P3_HOME+'\\customization'

# PERL PATH
PERL_MSC = P3_HOME + '\\Perl_msc\\bin\\perl_msc'

# COMPILE COMMAND PATH
PCLCOMP=PERL_MSC + ' ..\\pclcomp'

# Name of PCL source files except as extension 
PclFiles =[     'Finite_Element_2D',
                'FRAME_CREATE_ELEM_EDIT',
                'FRAME_CREATE_ELEM_ELEMEDGE',
                'FRAME_CREATE_ELEM_BEAMTOSHL',
                'FRAME_DELETE_FEM',
                'FRAME_MODIFY_ELEM_CONNECT',
                'FRAME_MOVE_COPY_NODES',
                'FRAME_MODIFY_ELEM_LINESPLIT',
                'FRAME_MODIFY_ELEM_PATTERN',
                'FRAME_CREATE_MESH_SURFACE',
                'FRAME_CREATE_MPC_RBE2',
                'FRAME_MODIFY_NODE_MOVE',
                'FRAME_MOVE_COPY_ELEM_MIRROR',
                'FRAME_MOVE_COPY_ELEM_TRANS',
                'FRAME_MOVE_COPY_ELEM_ROTATE',
                'FemFx',
                'Pattern_Split',
                'Line_Split',
                'Check_ElementEdge',
                'Count_FEM',
                'SH_Model_Check',
                'ModelChkSelectFile',
                'MatchingElementVector',
                'Local_Mesher',
                'Move_Nodes',
                'Membrane_To_Shell'
          ]

# Name of the target pcl library
PclLibrary='FEM.plb'

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
