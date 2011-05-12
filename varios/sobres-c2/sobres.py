import csv
from string import Template

fields = 'sala alumnos jefe ayudante pregunta revisor'.split()

header = r'''
\documentclass[12pt,spanish]{article}
\usepackage[utf8]{inputenc}
\usepackage{fullpage}
\usepackage{mathpazo}
\begin{document}
  \pagestyle{empty}
  \thispagestyle{empty}
  \LARGE
  \begin{center}
'''

template = Template(r'''
    {
      \fontsize{40}{40}\selectfont \textbf{Pregunta} \\
      \fontsize{100}{90}\selectfont $pregunta \\
      \fontsize{60}{100}\selectfont $sala \\
    }
    \vspace{.5ex}
    $alumnos alumnos \\[4ex]
    Jefe de sala: \textbf{$jefe} \\
    Ayudante: \textbf{$ayudante} \\
    \vfill
    Revisor: \textbf{$revisor}
    \newpage
''')

footer = r'''
  \end{center}
\end{document}
'''

def main():
  in_file = open('sobres.csv')
  out_file = open('sobres.tex', 'w')

  out_file.write(header)

  reader = csv.DictReader(in_file, delimiter=',', fieldnames=fields)
  for i, row in enumerate(reader):
      if i == 0:
          continue
      d = {f: row[f] for f in fields}
      out_file.write(template.substitute(**d))

  out_file.write(footer)

  in_file.close()
  out_file.close()

if __name__ == '__main__':
    main()

