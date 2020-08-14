from pathlib import Path, PurePath

def get_file_uid(filename, prefix):
    file_basename = PurePath(filename).name
    file_suffix = PurePath(filename).suffix
    basename = file_basename.replace(file_suffix, '')
    basename = basename.replace('-','_')
    uid = '{prefix}_{basename}'.format(prefix=prefix, basename=basename)
    return uid
    