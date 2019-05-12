#!/usr/bin/python

import docker
import etcd

dockerCli = docker.from_env()
etcdCli = etcd.Client(host='swarm-node1.lan', port=2379)

try:
    directory = etcdCli.get('/v2/keys/pxc-cluster/clsql/nodes')
    for res in directory.children:
        print res.key
except etcd.EtcdKeyNotFound:
    print "nothing found"


try:
    for container in dockerCli.containers.list():
        if "percona_sqlproxy" in container.name:
            ret = container.exec_run("add_cluster_nodes.sh", stdout=False,stderr=False)
            break

except 	docker.errors.APIError:
    print "[ERROR] Docker API error"