import dropbox
class transferData:
    def __init__(self,accesstoken):
        self.accesstoken=accesstoken

    def upload_file(self,filefrom,fileto):
        dbx=dropbox.Dropbox(self.accesstoken)  
        f=open(filefrom,"rb")
        dbx.files_upload(f.read(),fileto)     


def main():
    accesstoken="ZLlY8_JnWSEAAAAAAAAAAZjJcmJzPAd8uMtVhg8JIroDAHd5450Ei98aa4wdXBth"
    transferdata=transferData(accesstoken)
    filefrom=input("Enter the file path to transfer")
    fileto=input("Enter the full path to upload to dropbox")
    transferdata.upload_file(filefrom,fileto)
    print("File has been moved")

main()



