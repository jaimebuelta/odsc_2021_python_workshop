import sh

# Needs to set the -o to overwrite the result
sh.unzip('-o', 'zipped_file.zip')
