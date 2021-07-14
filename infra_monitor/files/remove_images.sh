for i in `docker images | grep -v IMA | awk -F ' ' '{print $3}'`
do
docker rmi --force $i
done

