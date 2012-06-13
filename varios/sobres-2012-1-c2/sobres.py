from csv import DictReader
from string import Template

#fields = 'sala alumnos jefe ayudante pregunta revisor'.split()
fields = 'fila sala alumnos jefe pregunta corrector paralelo apellidos profesor'.split()

header = r'''
\documentclass[12pt,spanish]{article}
\usepackage[utf8]{inputenc}
\usepackage{fullpage}
\usepackage{mathpazo}
\usepackage[margin=.5in]{geometry}
\parskip 6ex

\begin{document}
  \pagestyle{empty}
  \thispagestyle{empty}
'''

template = Template(r'''
  \fbox{
    \begin{minipage}[t]{.25\textwidth}
      \LARGE\centering
      \fontsize{20}{30}\selectfont \textbf{Pregunta} \\
      \fontsize{100}{80}\selectfont $pregunta \\
      \fontsize{12}{60}\selectfont $jefe \\
      \fontsize{30}{30}\selectfont $sala
      \vspace{.3ex}
    \end{minipage}
  }
  \hspace{1em}
  \begin{minipage}[t]{.70\textwidth}
    \textbf{Paralelo$s:} $paralelo ($profesor)$apellidos. \\
    \textbf{Cantidad:} $alumnos alumnos. \\
    \textbf{Corrector:} $corrector. \\
    \textbf{Observaciones:}
  \end{minipage}

''')

footer = r'''
\end{document}
'''

def main():
  in_file = open('sobres.csv')
  out_file = open('sobres.tex', 'w')

  out_file.write(header)

  reader = DictReader(in_file, delimiter=',', fieldnames=fields)
  for i, row in enumerate(reader):
      if i == 0:
          continue
      if i % 4 == 0:
          out_file.write(r'\newpage')
          continue

      d = {f: row[f] for f in fields}

      if d['apellidos']:
          d['apellidos'] = ', apellidos {}'.format(d['apellidos'])
      if ',' in d['paralelo']:
          d['paralelo'] = d['paralelo'].replace(',', ' y ')
          d['s'] = 's'
      else:
          d['s'] = ''
      if not d['jefe']:
          d['jefe'] = r'-'

      out_file.write(template.substitute(**d))

  out_file.write(footer)

  in_file.close()
  out_file.close()

if __name__ == '__main__':
    main()

