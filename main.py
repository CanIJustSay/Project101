import dropbox
import os
os.system("cls")
accessToken = "sl.A5ntzQAqogFX08p-c9xOv6ThLdYWajgl6AHwPVTf0etDw_mBuwDZTlCahoSm7LWrk16q2F0ac6pzFAz87y9xxRaRPgevD4DRoSfAzRPJGJ7k68LIIyR51EPKA0UUKvMhOB1E1FtlcBw"
def UploadData():
    dbxObj = dropbox.Dropbox(accessToken)
    holdPath = input("Put Path: ")
    f = open(holdPath,"rb")
    dbxObj.files_upload(f.read(),"/Wyatt/dummy.pdf")

UploadData()
