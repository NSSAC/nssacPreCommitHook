# Git pre-commit modifying file content 

## Changed existing or new file:
* if file changed in working directory: 
  * create backup copy
  * create patch between working directory and index
  * git checkout -force $f
* modify $f
* git add $f
* if file changed in working directory: 
  * try: apply patch
  * except: restore backup copy
  * finally: delete backup copy  

## Deleted file:
* do nothing
