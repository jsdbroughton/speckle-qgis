import sys
import os.path
import subprocess

from plugin_utils.subprocess_call import subprocess_call
from speckle.logging import logger
from speckle.utils import get_qgis_python_path


def setup():
    plugin_dir = os.path.dirname(__file__)
    pythonExec = get_qgis_python_path()

    try:
        import pip
    except:
        logger.log("Pip not installed, setting up now")
        getPipFilePath = os.path.join(plugin_dir, "plugin_utils/get_pip.py")
        exec(open(getPipFilePath).read())

        # just in case the included version is old
        subprocess_call([pythonExec, "-m", "pip", "install", "--upgrade", "pip"])

    pkgVersion = "2.6.4" #"2.5.3"
    pkgName = "specklepy"
    try:
        import specklepy
    except Exception as e:
        logger.log("Specklepy not installed")
        subprocess_call(
            [pythonExec, "-m", "pip", "install", f"{pkgName}=={pkgVersion}"]
        )

    # Check if specklpy needs updating
    try:
        subprocess_call(
            [
                pythonExec,
                "-m",
                "pip",
                "install",
                "--upgrade",
                f"{pkgName}=={pkgVersion}",
            ]
        )
    except Exception as e:
        logger.logToUser(e.with_traceback)
