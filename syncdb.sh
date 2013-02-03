# Check the models
echo 'Validating models'
echo ''
python manage.py validate
OUT=$?
if [ $OUT -ne 0 ];then
   exit
fi

# Clear the database
echo ''
echo 'CLEARING DATABASE'
echo ''
python manage.py sqlclear fantasygithub | python manage.py dbshell

# Make the database
echo ''
echo 'CREATING DATABASE'
echo ''
python manage.py syncdb

