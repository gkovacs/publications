#!/usr/bin/env python3

from glob import glob

output_file = open('index.html', 'wt')

def write_header():
  header = '''
  <html>
  <head>
  </head>
  <body>
  '''
  for line in header.split('\n'):
    line = line.strip()
    if line == '':
      continue
    output_file.write(line)
    output_file.write('\n')

def write_footer():
  footer = '''
  </body>
  </html>
  '''
  for line in footer.split('\n'):
    line = line.strip()
    if line == '':
      continue
    output_file.write(line)
    output_file.write('\n')

write_header()
for x in sorted(glob('*.pdf')):
  output_file.write('<a href="' + x + '">' + x + '</a><br/>')
  output_file.write('\n')
write_footer()
