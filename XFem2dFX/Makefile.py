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
PclFiles =[     'xfem_angles_2elm',                                                       
                'xfem_delete_empty_group',
                'xfem_get_3nds_normal',                                                   
                'xfem_get_beam_ori',
                'xfem_get_elems_ass_nodes',                                               
                'xfem_get_elem_normal',
                'xfem_get_groups',                                                        
                'xfem_get_layer_id',                                                      
                'xfem_get_mat_name_ass_elem',
                'xfem_get_result_data',
                'xfem_get_result_id',
                'xfem_get_word_name_from_id',
                'xfem_load_group_list',                                                
                'xfem_load_result_cases',                                                 
                'xfem_str_from_vector',
                'xfem_str_from_coordinate',
                'xfem_vector',                                                      
                'xfem_word_dat',
                'xfem_get_elems_ass_1d',
                'xfem_get_lc_sc_from_rc',
                'xfem_get_elements_infos',
                'xfem_load_loadcases',
                'xfem_get_material_list',
                'xfem_p3list',
                'xfem_get_thickness',
                'xfem_get_shell_element_stress',
                'list_in_bracket_from_xyz',
                'ui_databox_set',
                'ui_FileSelectBox',
                'ui_select_frame_set',
                'ui_group_list',
		'ui_loadcases_list',
                'ui_resultcases_list',
                'ui_profile_list',
                'ui_material_list',
                'ui_checkbox_set',
                'ui_lbc_list',
                'ui_region_list'
                ]

# Name of the target pcl library
PclLibrary='XFem2dFx.plb'

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
