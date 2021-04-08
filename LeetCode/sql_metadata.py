import sql_metadata
from sql_metadata import generalize_sql
generalize_sql('SELECT /* Test */ foo FROM bar WHERE id in (1, 2, 56)')