# Copyright (c) 2021, Oracle and/or its affiliates.
# Licensed under the Universal Permissive License v 1.0 as shown at https://oss.oracle.com/licenses/upl.
#
import sys
#======================================================= 
# Function for undeployment
#======================================================= 
def unDeploy(appName,target):
   print 'Undeploying .........'
   try:
     stopApplication(appName)
     undeploy(appName, target)
   except Exception, ex:
     print ex.toString()
    
#======================================================== 
# Main program here...
# Target you can change as per your need
#========================================================  
def usage():
    argsList = ' -domainName <domainUID> -adminServerName <adminServerName> -adminURL <adminURL> -username <username> -password <password>'
    argsList=argsList + ' -soaClusterName <soaClusterName>' + ' -wlsMonitoringExporterTosoaCluster <wlsMonitoringExporterTosoaCluster>'
    argsList=argsList + ' -osbClusterName <osbClusterName>' + ' -wlsMonitoringExporterToosbCluster <wlsMonitoringExporterToosbCluster>'
    print sys.argv[0] + argsList
    sys.exit(0)

if len(sys.argv) < 1:
    usage()

# domainName will be passed by command line parameter -domainName.
domainName = "soainfra"

# adminServerName will be passed by command line parameter  -adminServerName
adminServerName = "AdminServer"

# adminURL will be passed by command line parameter  -adminURL
adminURL = "soainfra-adminserver:7001"

# soaClusterName will be passed by command line parameter  -soaClusterName
soaClusterName = "soaClusterName"

# wlsMonitoringExporterTosoaCluster will be passed by command line parameter -wlsMonitoringExporterTosoaCluster
wlsMonitoringExporterTosoaCluster = "false"

# osbClusterName will be passed by command line parameter -osbClusterName
osbClusterName = "osbClusterName"

# wlsMonitoringExporterToosbCluster will be passed by command line parameter -wlsMonitoringExporterToosbCluster
wlsMonitoringExporterToosbCluster = "false"

# username will be passed by command line parameter  -username
username = "weblogic"

# password will be passed by command line parameter -password
password = "Welcome1"


i=1
while i < len(sys.argv):
   if sys.argv[i] == '-domainName':
       domainName = sys.argv[i+1]
       i += 2
   elif sys.argv[i] == '-adminServerName':
       adminServerName = sys.argv[i+1]
       i += 2
   elif sys.argv[i] == '-adminURL':
       adminURL = sys.argv[i+1]
       i += 2
   elif sys.argv[i] == '-username':
       username = sys.argv[i+1]
       i += 2
   elif sys.argv[i] == '-password':
       password = sys.argv[i+1]
       i += 2
   elif sys.argv[i] == '-soaClusterName':
       soaClusterName = sys.argv[i+1]
       i += 2
   elif sys.argv[i] == '-wlsMonitoringExporterTosoaCluster':
       wlsMonitoringExporterTosoaCluster = sys.argv[i+1]
       i += 2
   elif sys.argv[i] == '-osbClusterName':
       osbClusterName = sys.argv[i+1]
       i += 2
   elif sys.argv[i] == '-wlsMonitoringExporterToosbCluster':
       wlsMonitoringExporterToosbCluster = sys.argv[i+1]
       i += 2

   else:
       print 'Unexpected argument switch at position ' + str(i) + ': ' + str(sys.argv[i])
       usage()
       sys.exit(1)

# Undeploy
connect(username, password, 't3://' + adminURL)
unDeploy('wls-exporter-adminserver',adminServerName)
if 'true' == wlsMonitoringExporterTosoaCluster:
   unDeploy('wls-exporter-soa',soaClusterName)

if 'true' == wlsMonitoringExporterToosbCluster:
   unDeploy('wls-exporter-osb',osbClusterName)

disconnect()
exit() 
