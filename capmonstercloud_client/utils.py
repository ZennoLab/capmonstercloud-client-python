import os


def getDefaultVersionPath() -> str:
    script_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(script_dir, 'version.txt')

def parseVersion(versionFile: str = getDefaultVersionPath(),
                 ) -> str:
    
    if not os.path.exists(versionFile):
        raise FileNotFoundError(f'Version file py path {versionFile} not found.')
        
    elif not os.path.isfile(versionFile):
        raise ValueError(f'Version file {versionFile} is not file')
        
    else:
        with open(versionFile, 'r') as f:
            version = f.read()
        return version