

def relative_path(basedir, path):
    if not basedir.endswith('/'):
        basedir = basedir + '/'

    assert path.startswith(basedir), '%s does not start with %s' % (path, basedir)
    return path[len(basedir):]


def relative_paths(basedir, paths):
    new_paths = []

    if not basedir.endswith('/'):
        basedir = basedir + '/'

    for path in paths:
        new_paths.append(relative_path(basedir, path))

    return new_paths
