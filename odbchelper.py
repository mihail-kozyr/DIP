def buildConnectionsString(params):
    """Build a connection string from a dictionary of parameters.
       
       return string.
    """

    return ";".join(["%s=%s" % (k, v) for k, v in params.items()])

if __name__ == "__main__":
    myParams = {"host": "vm-cb2-bi.vm-p.rdtex.ru",
                "port": 1521,
                "service_name": "orcl"
                }

    print(buildConnectionsString(myParams))
