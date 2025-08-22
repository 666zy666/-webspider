from multiprocessing import Process
from ip_commit import run as commit_run
from ip_get import run as get_run
from  proxy_ip_api import run as api_run
def run():
    p1 = Process(target=get_run())
    p2 = Process(target=commit_run())
    p3 = Process(target=api_run())
    p1.start()
    p2.start()
    p3.start()

    pass
if __name__ == "__main__":
    run()

