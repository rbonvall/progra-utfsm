def dia(d):
    return (2010, 6, d)

resultados_por_grupo = {
  'A': {
    ('Sudafrica', 'Mexico'):    (dia(11), (1, 1)),
    ('Uruguay',   'Francia'):   (dia(11), (0, 0)),
    ('Sudafrica', 'Uruguay'):   (dia(16), (0, 3)),
    ('Francia',   'Mexico'):    (dia(17), (0, 2)),
    ('Mexico',    'Uruguay'):   (dia(22), (0, 1)),
    ('Francia',   'Sudafrica'): (dia(22), (1, 2)),
  },
  'B': {
    ('Corea del Sur', 'Grecia'):        (dia(12), (2, 0)),
    ('Argentina',     'Nigeria'):       (dia(12), (1, 0)),
    ('Argentina',     'Corea del Sur'): (dia(17), (4, 1)),
    ('Grecia',        'Nigeria'):       (dia(17), (2, 1)),
    ('Nigeria',       'Corea del Sur'): (dia(22), (2, 2)),
    ('Grecia',        'Argentina'):     (dia(22), (0, 2)),
  },
  'C': {
    ('Inglaterra', 'EEUU'):       (dia(12), (1, 1)),
    ('Argelia',    'Eslovenia'):  (dia(13), (0, 1)),
    ('Eslovenia',  'EEUU'):       (dia(18), (2, 2)),
    ('Inglaterra', 'Argelia'):    (dia(18), (0, 0)),
    ('Eslovenia',  'Inglaterra'): (dia(23), (0, 1)),
    ('EEUU',       'Argelia'):    (dia(23), (1, 0)),
  },
  'D': {
    ('Serbia', 'Ghana'):       (dia(13), (0, 1)),
    ('Alemania', 'Australia'): (dia(13), (4, 0)),
    ('Alemania', 'Serbia'):    (dia(18), (0, 1)),
    ('Ghana', 'Australia'):    (dia(19), (1, 1)),
    ('Ghana', 'Alemania'):     (dia(23), (0, 1)),
    ('Australia', 'Serbia'):   (dia(23), (2, 1)),
  },
  'E': {
    ('Holanda', 'Dinamarca'): (dia(14), (2, 0)),
    ('Japon', 'Camerun'):     (dia(14), (1, 0)),
    ('Holanda', 'Japon'):     (dia(19), (1, 0)),
    ('Camerun', 'Dinamarca'): (dia(19), (1, 2)),
    ('Dinamarca', 'Japon'):   (dia(24), (1, 3)),
    ('Camerun', 'Holanda'):   (dia(24), (1, 2)),
  },
  'F': {
    ('Italia', 'Paraguay'):          (dia(14), (1, 1)),
    ('Nueva Zelanda', 'Eslovaquia'): (dia(15), (1, 1)),
    ('Eslovaquia', 'Paraguay'):      (dia(20), (0, 2)),
    ('Italia', 'Nueva Zelanda'):     (dia(20), (1, 1)),
    ('Eslovaquia', 'Italia'):        (dia(24), (3, 2)),
    ('Paraguay', 'Nueva Zelanda'):   (dia(24), (0, 0)),
  },
  'G': {
    ('Costa de Marfil', 'Portugal'):        (dia(15), (0, 0)),
    ('Brasil', 'Corea del Norte'):          (dia(15), (2, 1)),
    ('Brasil', 'Costa de Marfil'):          (dia(20), (3, 1)),
    ('Portugal', 'Corea del Norte'):        (dia(20), (7, 0)),
    ('Portugal', 'Brasil'):                 (dia(25), (0, 0)),
    ('Corea del Norte', 'Costa de Marfil'): (dia(25), (0, 3)),
  },
  'H': {
    ('Honduras', 'Chile'):  (dia(16), (0, 1)),
    ('Espana', 'Suiza'):    (dia(16), (0, 1)),
    ('Suiza', 'Chile'):     (dia(21), (0, 1)),
    ('Espana', 'Honduras'): (dia(21), (2, 0)),
    ('Espana', 'Chile'):    (dia(25), (2, 1)),
    ('Suiza', 'Honduras'):  (dia(25), (0, 0)),
  },
}
