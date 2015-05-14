#encoding: utf-8

import os
import commands
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

# Change this to the testcase dir!
TEST_CASE_DIR = '/tmp/test_case'


def write_file(filename, context):
    try:
        with open(filename, 'a') as f:
            f.write('%s' % context)
        print 'write to file successfully!\n'
    except Exception as e:
        print 'write to file error'


def read_file(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            return lines
    except Exception as e:
        print 'file does not exist'


def order_num(test_type, module_num, submod_num, case_order):
    case_num = test_type + module_num + submod_num + '{:0>2d}'.format(case_order)
    return case_num

def order_case():
    module_dirs = os.listdir(TEST_CASE_DIR)
    # if is file, not module
    test_type = '01'
    module_num = 0
    for module_dir in module_dirs:
        submod_num = 0
        if os.path.isfile(TEST_CASE_DIR + '/' + module_dir):
#            module_dirs.remove(module_dir)
            pass
        else:
            module_num += 1
            submod_files = os.listdir(TEST_CASE_DIR + '/' + module_dir)
#            if len(submod_files) != 0:
            for submod_file in submod_files:
                i = 0
                table_line = 0
                table_num = 0
                case_order = 0
                first_write = 1
                contexts = read_file(TEST_CASE_DIR + '/' + module_dir + '/' + submod_file)
                if submod_file.split('.')[0] == module_dir:
                    # is main file (readme file)
                    for context in contexts:
                        if '---' not in context:
                            i += 1
                        else:
                            i += 1
                            table_line = 1
                            write_file(TEST_CASE_DIR + '/' + module_dir + '/' + submod_file, context)
                            continue
                        if table_line and context != '' and context != '\n':
                            tmp_context = context.split('|')
                            tmp_context[3] = order_num('', '', '', module_num)
#                            tmp_context[3] = 'change_me'
                            context = '|'.join(tmp_context)
                        elif table_line and (context == '' or context == '\n'):
                            case_order = 0
                            table_line = 0
                        if first_write:
                            with open(TEST_CASE_DIR + '/' + module_dir + '/' + submod_file, 'w') as f:
                                f.write('%s' % context)
                            first_write = 0
                        else:
                            write_file(TEST_CASE_DIR + '/' + module_dir + '/' + submod_file, context)
                            
                else:
                    submod_num += 1
                    for context in contexts:
                        if '---' not in context:
                            i += 1
                        else:
                            i += 1
                            table_line = 1
                            write_file(TEST_CASE_DIR + '/' + module_dir + '/' + submod_file, context)
                            continue
                        if table_line and context != '' and context != '\n':
                            if table_num == 0:
                                case_order += 1
                                tmp_context = context.split('|')
                                tmp_context[1] = order_num('', '', '', submod_num)
#                                tmp_context[1] = 'change_me'
                                context = '|'.join(tmp_context)
                            else:
                                case_order += 1
                                tmp_context = context.split('|')
                                m_num = order_num('', '', '', module_num)
                                s_num = order_num('', '', '', submod_num)
                                tmp_context[1] = order_num(test_type, m_num, s_num, case_order)
#                                tmp_context[1] = 'change_me'
                                context = '|'.join(tmp_context)
                        elif table_line and (context == '' or context == '\n'):
                            case_order = 0
                            table_line = 0
                            table_num += 1
                        if first_write:
                            with open(TEST_CASE_DIR + '/' + module_dir + '/' + submod_file, 'w') as f:
                                f.write('%s' % context)
                            first_write = 0
                        else:
                            write_file(TEST_CASE_DIR + '/' + module_dir + '/' + submod_file, context)
                        


order_case()
