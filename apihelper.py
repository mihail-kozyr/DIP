def help(object, spacing=10, collapse=1):
    """Print methods and doc string.

    Takes module, class, list, dictionary, or string."""
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print("\n".join(["%s %s" %
          (method.ljust(spacing),
           processFunc(strl(getattr(object, method).__doc__)))
        for method in methodList
        ]))

if __name__ == '__main__':
    print(help.__doc__)
