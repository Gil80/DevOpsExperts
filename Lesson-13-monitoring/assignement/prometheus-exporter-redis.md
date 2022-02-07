#### install prometheus operator and grafana using helm (prometheus stack)
##### add repos
`helm repo add prometheus-community https://prometheus-community.github.io/helm-chart`s`
`helm repo add stable https://kubernetes-charts.storage.googleapis.com/`
`helm repo update`

##### install chart
`helm install prometheus prometheus-community/kube-prometheus-stack`

##### install prometheus
`helm install prometheus stable/prometheus-operator`

##### expose grafana
`kubectl port-forwrad prometheus-grafana-{pod} -c grafana 3000`

username: admin
password: taken from https://github.com/helm/charts/tree/master/stable/prometheus-operator

##### expose prometheus
`kubectl port-forward prometheus-kube-prometheus-operator{pod} 9090`



#### install redis-exporter
###### add repos
    helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
    helm repo update

###### install chart
    helm install redis-exporter prometheus-community/prometheus-redis-exporter -f redis/values.yaml

###### Link to chart
[https://github.com/prometheus-community/helm-charts/tree/main/charts/prometheus-redis-exporter]


#### port-forwardings
###### Prometheus-UI
    kubectl port-forward service/prometheus-kube-prometheus-prometheus 9090
    
###### Alert Manager UI
    kubectl port-forward svc/prometheus-kube-prometheus-alertmanager 9093

###### Grafana
    kubectl port-forward deployment/prometheus-grafana 3000

###### Grafana Dashboard credentials
    user: admin
    pwd: prom-operator (from values.yaml file set as default)

###### redis-exporter 
    kubectl port-forward service/redis-exporter-prometheus-redis-exporter 9121
