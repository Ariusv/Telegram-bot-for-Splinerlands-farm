import subprocess
import time
import psutil

class ProcessAdministrator:
    def __init__(self):
        self.pid = None
    def start(self):
        self.process=subprocess.Popen("node main.js", creationflags=subprocess.CREATE_NEW_CONSOLE)
        self.pid = self.process.pid
    def kill(self, pid):
        if psutil.pid_exists(pid):
            subprocess.call('taskkill /F /T /PID %i' % pid)
