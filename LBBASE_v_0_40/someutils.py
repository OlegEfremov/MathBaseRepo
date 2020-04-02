import os


def get_env_variable(var_name, default=False):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    """
    Get the environment variable or return exception
    :param var_name: Environment Variable to lookup
    """
    try:
        return os.environ[var_name]
    except KeyError:
        import io
        import configparser
        env_file = os.environ.get('PROJECT_ENV_FILE', base_dir + "/.env")
        try:
            config = io.StringIO()
            config.write("[DATA]\n")
            config.write(open(env_file).read())
            config.seek(0, os.SEEK_SET)
            cp = configparser.ConfigParser()
            cp.read_file(config)
            value = dict(cp.items('DATA', raw=True))[var_name.lower()]

            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            elif value.startswith("'") and value.endswith("'"):
                value = value[1:-1]

            os.environ.setdefault(var_name, value)

            if value == 'False':
                value = False
            elif value == 'True':
                value = True

            return value
        
        except (KeyError, IOError):
            if default is not False:
                return default
            from django.core.exceptions import ImproperlyConfigured
            error_msg = "Either set the env variable '{var}' or place it in your " \
                        "{env_file} file as '{var} = VALUE'"
            raise ImproperlyConfigured(error_msg.format(var=var_name, env_file=env_file))
