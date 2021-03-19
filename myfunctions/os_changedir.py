import os

#change downloads designation folder
environment_variables = dict(os.environ)
homepath = environment_variables['HOMEPATH']
downloads_folder = ('c:%s\\downloads' % homepath)
os.chdir(downloads_folder)
