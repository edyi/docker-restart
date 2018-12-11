import subprocess

print('############ SHOW CONTAINER ############')
pscmd = 'docker ps -a'
subprocess.call(pscmd)


print('############ STOP CONTAINER ############')
getid = 'docker ps -a -q'
showid = subprocess.Popen(getid, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
std_out, std_err = showid.communicate()
ctnids = std_out.decode('utf-8').rstrip().split('\n')

print('--- start ---')
for ctnid in ctnids:
    stopctn = "docker stop %s" % (ctnid)
    subprocess.call(stopctn)
else:
    print('--- end ---')


print('############ REMOVE CONTAINER ############') 
getid = 'docker ps -a -q'
showid = subprocess.Popen(getid, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
std_out, std_err = showid.communicate()
ctnids = std_out.decode('utf-8').rstrip().split('\n')

print('--- start ---')
for ctnid in ctnids:
    rmctn = "docker rm %s" % (ctnid)
    subprocess.call(rmctn)
    # rmexec = subprocess.call(rmcmd)
else:
    print('--- end ---')


print('############ SHOW CONTAINER ############')
pscmd = 'docker ps -a'
subprocess.call(pscmd)


print('############ START CONTAINER ############')

run1 = 'docker run --hostname="slave1" --privileged -d -it -p 8081:80 -p 2223:22 --name slave1 slave1:0005 /sbin/init'
subprocess.call(run1)

run2 = 'docker run --hostname="slave2" --privileged -d -it -p 8082:80 -p 2224:22 --name slave2 slave2:0005 /sbin/init'
subprocess.call(run2)

run3 = 'docker run --hostname="slave3" --privileged -d -it -p 8083:80 -p 2225:22 --name slave3 slave3:0005 /sbin/init'
subprocess.call(run3)

run4 = 'docker run --hostname="master" --privileged -d -it -p 8080:80 -p 2222:22 --name master --link slave1:s1 --link slave2:s2 --link slave3:s3 master:0006 /sbin/init'
subprocess.call(run4)
