"""
PURPOSE: Makes a connection to an instance of InterSystems IRIS Data Platform using PyODBC
"""


import pyodbc


# Get connection details from config file
def get_connection_info(file_name):
    # Initial empty dictionary to store connection details
    connections = {}

    # Open config file to get connection info
    with open(file_name) as f:
        lines = f.readlines()
        for line in lines:
            # remove all white space (space, tab, new line)
            line = ''.join(line.split())

            # get connection info
            connection_param, connection_value = line.split(":")
            connections[connection_param] = connection_value
    return connections


def run():
    # Retrieve connection information from configuration file
    driver = "{InterSystems ODBC}"
    ip = "146.148.58.193"
    port = "26406"
    namespace = "USER"
    username = "tech"
    password = "demo"

    # Create connection to InterSystems IRIS
    connection_string = 'DRIVER={};SERVER={};PORT={};DATABASE={};UID={};PWD={}' \
        .format(driver, ip, port, namespace, username, password)
    connection = pyodbc.connect(connection_string)
    connection.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
    connection.setencoding(encoding='utf-8')
    print("Connected to InterSystems IRIS")


if __name__ == '__main__':
    run()
