# -*- coding: utf-8 -*-
import MySQLdb

from conection_factory import Connection_factory

connection = Connection_factory().get_connection()
cursor = connection.cursor()

# executa a query
cursor.execute('SELECT * from cursos')

# itera sobre o resultado
for linha in cursor:
    print(linha)

# fecha a conexão
connection.close()