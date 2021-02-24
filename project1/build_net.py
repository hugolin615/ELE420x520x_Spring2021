#!/usr/bin/python
 
 
from mininet.net import Mininet
from mininet.node import Controller, OVSController, RemoteController, OVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.topo import Topo
import os
import os.path

def main():
    setLogLevel('info')

    ### DON't CHANGE as we use default SDN controller
    net = Mininet(controller=Controller, switch=OVSSwitch )
    c1 = net.addController( 'c1', controller=Controller)

    # Build a network of the following topology
    #   h1---s1---s2---s3---h3   
    #              |
    #              h2

    ## TODO: added nodes: switches and hosts
    ## using mininnet python API addSwitch and addHost
    ##  Remember to set IP address in addHost

    ## TODO: added links connecting nodes
    ## using mininet python API addLink

    ## DON't CHANGE
    # build networt, start mininet, and enter mininet CLI console
    net.build()
    net.start()
    CLI(net)

    net.stop()


if __name__ == "__main__":
    main() 
