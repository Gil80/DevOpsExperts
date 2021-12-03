cd /tmp
rm -r zipme
mkdir zipme
cd zipme/
echo 1 > 1.txt
echo 1 > 2.txt
echo 1 > 3.txt
tar -cvf archived.tar $( find . -name "*.txt")
tar -czvf zipped-archive.tar $( find . -name "*.txt")
ls -l
rm *.txt
ls -l
mkdir untar-archived
tar -xf archived.tar --directory untar-archived

mkdir unzipped-archive
tar -xzf zipped-archive.tar --directory unzipped-archive
ls -l

