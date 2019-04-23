def named_conf(value, key='', indent=0, step=2):
    ''' Translate python object to named config syntax '''
    section = ' ' * indent + key.strip() + (' ' if key.strip() != '' else '')
    if type(value) is dict:
        if section.strip() != '':
            recurse_print = [named_conf(v, k, indent + step)
                             for (k, v) in value.items()]
            members = "\n".join(recurse_print)
            conf = "{0}{{\n{1}\n{2}}};".format(section, members, ' ' * indent)
        else:
            conf = "\n".join([named_conf(v, k, indent)
                              for (k, v) in value.items()])
    elif type(value) is list:
        if key.strip() != '':
            members = "\n".join([named_conf(v, '', indent + step)
                                 for v in value])
            conf = "{0}{{\n{1}\n{2}}};".format(section, members, ' ' * indent)
        else:
            members = "\n".join([named_conf(v, '', indent) for v in value])
            conf = members
    else:
        conf = "{0}{1};".format(section, '{0}'.format(value))
    return(conf)


def with_key(value, key):
    return(dict([[k, v] for (k, v) in value.items() if k == key]))


def without_key(value, key):
    return(dict([[k, v] for (k, v) in value.items() if k != key]))


class FilterModule(object):
    ''' jinja2 filters '''

    def filters(self):
        return {
            'named_conf': named_conf,
            'with_key': with_key,
            'without_key': without_key
        }
