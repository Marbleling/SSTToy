import glob
import pdftotext

files = glob.glob('files/*')
for file in files:
    f = open(file, 'rb')
    reader = pdftotext.PDF(f)

    text = reader[0].split('\n')
    title = text[0].strip()
    author = text[1].strip()

    file_title = 'texts/' + title + '-' + author + '.txt'

    w = open(file_title, 'w')
    w.writelines(reader[0])

    print(file_title)