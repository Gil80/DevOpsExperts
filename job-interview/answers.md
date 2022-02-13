Q:
1. Write a dockerfile that packages a python script and runs it as a 
command

A:
1. See `Dockerfile`

Q:
2. Write a docker-compose.yml file that starts wordpress application.

A:
2. See `docker-compose.yaml` file

Q:
3. Write an ansible role that installs 3 packages on the servers, checks if 
the servers are CentOS and if they do it will create an empty file 
under /tmp/this_is_centos

A:
3. 

Q:
10.  What will be the commands to deploy out-of-the-box redis with
master and 3 replicas using helm.

A:
10. create a values.yaml file that edits the default value of `replicaset`.
Example:
```apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis-master
  labels:
    app: redis
spec:
  selector:
    matchLabels:
      app: redis
      role: master
      tier: backend
  replicas: 3
  template:
    metadata:
      labels:
        app: redis
        role: master
        tier: backend
    spec:
      containers:
      - name: master
        image: redis  
        resources:
          requests:
            cpu: 100m
            memory: 100Mi
        ports:
        - containerPort: 6379
```

Then issue command: 
$ `helm repo add bitnami https://charts.bitnami.com/bitnami`

$ `helm install redis bitnami/redis -f redis-deployment-values.yaml`

----

Q:
9. Assuming I have a deployment in kubernetes of NGINX containers,
what will be the commands to scale it from 1 to 3 pods

A:
`kubectl autoscale deployment nginx --min=1 --max=3`

