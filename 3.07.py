#### learning with Project : 
################## ---------------- Seperating diff types of files ----------------------##################

import os,shutil

dictExtensions = {
'image_extensions   ' : ('.jpg','.png','.jpeg'),
'audio_extensions   ' : ('.mp3','.m4a','.wav','.flac'),
'video_extensions   ' : ('.mp4','.mkv','MKV','.flv','.mpeg'),
'document_extensions' : ('.txt','.pdf','.docx','.pptx','.csv'),
'other_extensions   ' : ('.py','.xmp','.zip','.dat','.theme','.xml','.sh','.sed')
}


folderPath = input('Enter complete path of folder : ') # /home/jerry/🃏 Start/python 0.p/0.p1


def fileFinder(folderPath,fileExtension):
    # files = []
    # for filE in os.listdir(folderPath):
    #     for extension in fileExtension:
    #         if filE.endswith(extension):
    #             files.append(filE)
    # return files 

    return [filE for filE in os.listdir(folderPath) for extension in fileExtension if filE.endswith(extension)]
    
for extensiontype , extensiontuple in dictExtensions.items():
    folder_name = extensiontype.split('_')[0] + ' Files'
    folder_path = os.path.join(folderPath,folder_name)
    os.mkdir(folder_path)

    for item in fileFinder(folderPath,extensiontuple):
        item_prev_path = os.path.join(folderPath,item)
        item_new_path = os.path.join(folder_path,item)
        shutil.move(item_prev_path,item_new_path)

    # print(f'{extensiontype} : {fileFinder(folderPath,dictExtensions[extensiontype])}')






######### limitations : TODO
#
# 1) if folder already available it shows error
# 2) if no file is their for particular typed still it creates useless folder
#