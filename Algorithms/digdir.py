from os import scandir


start_dir = '/Users/apple/Github/Tale'

def digdir(start_dir):
    for f in scandir(start_dir):
        if f.is_dir():
            digdir(f)
        elif f.is_file():
            print(f.name)


digdir(start_dir)