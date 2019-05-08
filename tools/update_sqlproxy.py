#!/usr/bin/python

import docker

dockerCli = docker.from_env()

try:
    for container in dockerCli.containers.list():
        if "percona_sqlproxy" in container.name:
            ret = container.exec_run("add_cluster_nodes.sh", stdout=False,stderr=False)
            print ret
            break

except 	docker.errors.APIError:
    print "[ERROR] Docker API error"