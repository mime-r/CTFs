import zipfile, os
def initial_zip(): 
    zipfile.ZipFile("unzip_me_0.zip", mode='w').write("challenge_flag.txt")
    previous_name = "unzip_me_0.zip"
    # unzip_me_538.zip
    for i in range(1, 539):
        
        new_name = f"unzip_me_{str(i)}.zip"
        zipfile.ZipFile(new_name, mode='w').write(previous_name)
        os.remove(previous_name)
        previous_name = new_name
        print(previous_name)
        
def final_zip():
    previous_name = "unzip_me_539.zip"
    # unzip_me_538.zip
    for i in range(541, 1000):
        
        new_name = f"unzip_me_{str(i)}.zip"
        zipfile.ZipFile(new_name, mode='w').write(previous_name)
        os.remove(previous_name)
        previous_name = new_name
        print(previous_name)
        
        
    
    # zip n = 156




# initial_zip()
final_zip()