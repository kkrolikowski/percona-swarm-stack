#!/usr/bin/python

import docker
import requests
import json


dockerCli = docker.from_env()

etcd = requests.get("http://swarm-node1.lan:2379/v2/keys/pxc-cluster/clsql")

if etcd.status_code == 200:
    etcd_json = json.loads(etcd.text)
    for nodes in etcd_json.node.nodes:
        print nodes.key

try:
    for container in dockerCli.containers.list():
        if "percona_sqlproxy" in container.name:
            ret = container.exec_run("add_cluster_nodes.sh", stdout=False,stderr=False)
            break

except 	docker.errors.APIError:
    print "[ERROR] Docker API error"