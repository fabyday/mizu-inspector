import subprocess
import sys


class BridgeCreateHelper():
    """
        create bridge subprocess
    """
    @staticmethod
    def create_bridge_process():
        sys.executable("python -m mizu.server")


