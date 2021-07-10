for i in `docker ps --all | grep -v CONT | awk -F ' ' '{print $1}'`
do
docker rm $i --force
done
