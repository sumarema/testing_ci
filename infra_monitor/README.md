# Infrastructure Monitoring Solution
<h2> Explanation</h2>
<p>Servers used for SSL Offloading or Any other LoadBalancing typically needs</p>
<p>CPU, Memory, Network Interfaces, IOPS.  Additionally for SSL 
Offloading if providers like AVI etc are present we can gleam more
insights using the API Monitoring.
I have considered 2 Solutions for this Use Case</p>

<h3> Solution 1:</h3>
<p>Using Time Series Database, This is a Simple yet powerful tool
The Idea is that Using InfluxDB as TSDB and Simple and Robust 
Telegraf Agent, I have created a Monitoring Setup with help of
Ansible (Created a Playbook) to bring up an Instance of 
InfluxDB, Grafana, In this case the Telegraf Agent is run in a
Docker container. But for our use case we can install the Agent in
the Server which is a LightWeight application. 

Telegraf config "/etc/telegraf/telegraf.conf" Should be Updated with InfluxDB Container IP.
</p>

<h3> Pre-requisites</h3>
<h3>Solution 1 :</h3>
<p>Ansible: latest version</p>
<p>Docker: latest version</p>
<h4>Usage:</h4>
<p>ansible-playbook -i invent.cfg infra_setup.yml --> Install</p>
<p>ansible-playbook -i invent.cfg infra_destroy.yml --> Remove</p>

<h3> Solution 2:</h3>
<p>If we have monitoring requirement of Multiple Hosts and Different criteria
for example Application Availability, API Monitoring, etc
we would be needing more complex setup. That would be Zabbix.
Zabbix is Ideal for SNMP, API monitoring apart from our Use case,
That is monitoring of Server Metrics like Compute/Storage etc.
</p>
<p>Zabbix Setup would require "Zabbix Server", "Zabbix Agent",
"Zabbix Proxy" as bare minimum. 
Once the required infra if provisioned, Zabbix Agent can be installed 
in required Host and The Proxy will be receiving the data from Agent
.
Docker Compose file is available for setting up of the Infra.
</p>


