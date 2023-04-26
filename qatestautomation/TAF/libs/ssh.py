import paramiko
import argparse


class Ssh:
    def __init__(self, hostname, username, password=None, key_path=None):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.key_path = key_path
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def exec_command(self, command):
        self.ssh.connect(hostname=self.hostname, username=self.username,
                         password=self.password, key_filename=self.key_path)
        try:
            stdin, stdout, stderr = self.ssh.exec_command(command)
            output = stdout.readlines()
        finally:
            self.ssh.close()
        return "".join(output)

    def upload_to_remote(self, local_path, remote_path):
        """
        Copy a local file (``localpath``) to the SFTP server as ``remotepath``.
        :param str localpath: the local file to copy
        :param str remotepath: the destination path on the SFTP server. Note
            that the filename should be included. Only specifying a directory
            may result in an error.
        """
        self.ssh.connect(hostname=self.hostname, username=self.username,
                         password=self.password, key_filename=self.key_path)
        try:
            ftp_client = self.ssh.open_sftp()
            ftp_client.put(local_path, remote_path)
            ftp_client.close()
        finally:
            self.ssh.close()

    def download_from_remote(self, remote_path, local_path):
        """
        Copy a local file (``localpath``) to the SFTP server as ``remotepath``.
        :param str localpath: the local file to copy
        :param str remotepath: the destination path on the SFTP server. Note
            that the filename should be included. Only specifying a directory
            may result in an error.
        """
        self.ssh.connect(hostname=self.hostname, username=self.username,
                         password=self.password, key_filename=self.key_path)
        try:
            ftp_client = self.ssh.open_sftp()
            ftp_client.get(remote_path, local_path)
            ftp_client.close()
        finally:
            self.ssh.close()


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("user")
    parser.add_argument("ip")
    parser.add_argument("key")
    args = parser.parse_args()
    user = args.user
    host = args.ip
    key = args.key
    host = "10.62.70.102"
    user = "hxm"
    key = r"PATH_TO_KEY CHANGE ME"
    qa_server = Ssh(host, user, None, key)
    print(qa_server.exec_command("ls"))
