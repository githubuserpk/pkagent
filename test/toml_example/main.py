import tomllib
from pprint import pprint

def load_toml() -> dict:
    """Load toml data from file """

    with open('config.toml', 'rb') as f:
        toml_data: dict = tomllib.load(f)
        return toml_data
    

if __name__ == '__main__':
    data: dict = load_toml()
    pprint(data, sort_dicts=False)

    

