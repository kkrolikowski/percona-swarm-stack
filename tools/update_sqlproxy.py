#!/usr/bin/python

import docker
import requests

dockerCli = docker.from_env()

etcd = requests.get("http://swarm-node1.lan:2379/v2/keys/pxc-cluster/clsql/nodes")
print etcd.text

try:
    for container in dockerCli.containers.list():
        if "percona_sqlproxy" in container.name:
            ret = container.exec_run("add_cluster_nodes.sh", stdout=False,stderr=False)
            break

except 	docker.errors.APIError:
    print "[ERROR] Docker API error"