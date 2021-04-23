rm -f function.zip

# Ensure that AWS will have the correct permissions to run any file in the package
chmod -R 755 package

# Zip the resources
cd package
zip -r ../function.zip .
cd ..

# Add the actual python function
zip -g function.zip lambda_function.py

# Add ccg.bib
zip -g function.zip ../../ccg.bib

# Make sure the zip itself has the correct permissions. Not sure if this is absolutely necessary
chmod 755 function.zip