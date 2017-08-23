import os
import zipfile

#dirname(__file__)

path = '/Users/apple/Dropbox/Teach/2017/Y10 Programming/Assessment/CAT 1 - Web Design- About me_Submissions'

student_paths = []
with os.scandir(path) as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_dir():
            student_paths.append(os.path.join(path, entry.name))
    print(student_paths)

    for student_path in student_paths:
        print(student_path)
        with os.scandir(student_path) as sdir:
            for entry2 in sdir:
                if not entry2.name.startswith('.') and entry2.is_file():
                    old_basename = os.path.basename(entry2.name).lower()
                    file_ext = os.path.splitext(old_basename)
                    if old_basename[-4:] == 'html' and old_basename != 'index.html':
                        print(student_path)
                        old_filename = os.path.join(student_path, entry2.name)
                        new_filename = os.path.join(student_path, 'index.html')
                        print('old file: ', old_filename)
                        print('new file: ', new_filename)
                        os.rename(old_filename, new_filename)
                    elif file_ext[1] == '.zip':
                        old_filename = os.path.join(student_path, entry2.name)
                    #     with zipfile.ZipFile(old_filename) as myzip:
                    #         myzip.extractall()
                        print('zipfile: ', old_filename)

