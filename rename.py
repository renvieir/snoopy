from datetime import datetime
import os, re

# Patterns and commands
regex = r"(?P<d1>\d{2}-\d{2}-\d{2}).*(?P<d2>\d{2}-\d{2}-\d{2}).*(?P<num>\d{4})"
mkdir = 'mkdir {}'
mv = 'mv {0} {1}'
date_pattern1 = '%d-%m-%y'      
date_pattern2 = '%Y%m%d'


def rename_dirs():
    dict_dir = get_dict_of_directories()
    for key in dict_dir:
        rename_dir(key, dict_dir[key])

def get_dict_of_directories():
    dirlist = os.listdir('.')
    dirlist = [d for d in dirlist if os.path.isdir(d)]    
    dict_dir = {}
    for dir_ in dirlist:
        m = re.match(regex, dir_)
        if (m):
            dit = m.groupdict()        
            if (dit['num'] not in dict_dir):
                dict_dir[dit['num']] = []
            dict_dir[dit['num']].append(dir_)
    return dict_dir

def rename_dir(key, dirs):
    # cria diretorio 1772
    print key, dirs
    os.system(mkdir.format(key))
    for dir_ in dirs:
        m = re.match(regex, dir_)
        dit = m.groupdict()
        d1 = datetime.strptime(dit['d1'], date_pattern1).strftime(date_pattern2)
        d2 = datetime.strptime(dit['d2'], date_pattern1).strftime(date_pattern2)
        dname = '{0}.{1}'.format(d1, d2)
        try:
            os.rename(dir_, dname)
            os.system(mv.format(dname, key))
        except:
            pass

if __name__ == '__main__':
    os.chdir('Camera trap 2012 02')
    ld = os.listdir('.')
    ld = [d for d in ld if os.path.isdir(d)]

    # loop over dir list 
    for d in ld:
        print 'changing files of '+d+' ...'
        os.chdir(d) # now we are inside of '201201'
        rename_dirs()
        os.chdir('..')


