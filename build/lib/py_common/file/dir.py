import os

def create_dir(path):
    '''Standard mkdir extended fith exception handling'''
    #Check if folder exists
    if not os.path.exists(path):
        try:
            #Creating dir if not existing
            os.makedirs(path)     
        except PermissionError:
            #logger.exception(f"Permission denied during directory creation: {path}")
            print(f"Permission denied during directory creation: {path}")
            raise Exception()
        except Exception as e:
            #logger.exception(f"ERROR:  {e}")
            print(f"ERROR:  {e}")
            raise Exception()
        else:
            #logger.info(f"SUCCESS: Directory {path} succesfully created")
            print(f"SUCCESS: Directory {path} succesfully created")
    else:
        #Skipp if folder exist
        #logger.info(f"SKIP: Path already exist: {path}")
        print(f"SKIP: Path already exist: {path}")