Páginas web
===========

Una página web es simplemente un archivo de texto con extensión ``.html``
cuyo contenido sigue un conjunto de reglas que describen
la estructura de un documento.

Como ejemplo,
usted puede usar su navegador para ver el código de esta misma página
haciendo clic con el botón derecho y buscando

Para hacer una página web sencilla,
usted puede crear un archivo como el siguiente:

.. code-block:: none

    <!doctype html>
    <body>

      Mi primera pagina.

    </body>

Haga la prueba: copie este texto en un editor de texto,
guárdelo con el nombre ``pagina.html``,
y ábralo con su navegador web.
Usted debería poder ver el texto ``Mi primera pagina``.

1. Para crear una tabla en una página web,
   se hace de la siguiente manera:

   .. code-block:: none

       <table>
         <tr>
           <td> A </td>
           <td> B </td>
           <td> C </td>
         </tr>
         <tr>
           <td> D </td>
           <td> E </td>
           <td> F </td>
         </tr>
       </table>

   Haga la prueba:
   en el archivo ``pagina,html``,
   reemplace la parte que dice ``Mi primera pagina``
   con el texto de arriba.
   Al abrir la página nuevamente en el navegador,
   usted debería ver una tabla de dos filas y tres columnas.

   Escriba un programa
   que genere una página web llamada ``multiplicacion.html``
   que tenga una tabla de multiplicar de 20 × 20.
