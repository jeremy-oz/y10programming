import glob, re, os

filelist = glob.glob('*.pdf')
pattern = r'_\d\.\d_'
for file in filelist:
    match = re.search(pattern, file)
    if match:
        goodfile = file[match.start(0)+1:]
        print('File change: ', file, 'renamed to', goodfile)
        os.rename(file, goodfile)
