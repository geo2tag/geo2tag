PROPSFILE = 'propsfile'
MODE_AW = 'aw'


def write_env_var(variable, value):
    print 'write_env_var'
    f = open(PROPSFILE, MODE_AW)
    f.write(variable + '=' + value + '\n')
    f.close()
