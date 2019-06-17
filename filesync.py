import pysftp
import os

def transfer():
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    host = input("enter IP: ")
    user = input("enter ID: ")
    pwd = input("enter password: ")
    with pysftp.Connection(host, username = user, password= pwd, cnopts=cnopts) as sftp:
        sftp.put_r(os.path.dirname(__file__), "Desktop/sync", preserve_mtime=True)
transfer()

