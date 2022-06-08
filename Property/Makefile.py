import os
import sys

# PATRAN 3 home directory
P3_HOME = 'C:\\MSC.Software\\Patran_x64\\20122'

# Location of include files.
IPATH ='-I'+P3_HOME+'\\customization'

# PERL PATH
PERL_MSC = P3_HOME + '\\Perl_msc\\bin\\perl_msc'

# COMPILE COMMAND PATH
PCLCOMP=PERL_MSC + ' ..\\pclcomp'

# Name of PCL source files except as extension 
PclFiles =[     'PropFx',
                'profile_definition',
                'Profile_List',
                'property_reduction',
                'change_material',
                'Property_Type_Convert',
                'Property_2D',
                'get_2D_Ass_1D',
                'section_profile_list',
                'print_region_list',
                'Property_FringePlot',
                'Lumped_Beam',
                'Property_VIB',
                'Modify_Property',
                'Property_TOOLS',
                'gui_material_listbox',
                'Prop_TREE'
#                'Prop_TREE2'
#                'Property_TREE_View',
          ]

# Name of the target pcl library
PclLibrary='Property.plb'

for PclFile in PclFiles:
    # cpp arguments for preprocessing a single pcl source file
    CPPARGS=IPATH +' -C '+ PclFile+'.PCL' +' '+ PclFile+'.CPP'
    os.system('CPP '+ CPPARGS)
    print('CPP '+ CPPARGS)
    os.system(PCLCOMP + ' -pob '+ PclFile+'.CPP')
    os.system(PCLCOMP + ' -m ' + PclLibrary + ' '+PclFile+'.pob ')
    print(PclFile+'.pob'+' -> ' + PclLibrary)
#os.system('del *.cpp')
# os.system('del *.pob')
print('***** Complete ******')
