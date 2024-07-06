3 no

router-1

Router>en
Router#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#int fa 0/0
Router(config-if)#ip add 192.168.0.65 255.255.255.224
Router(config-if)#no shut

Router(config-if)#
%LINK-5-CHANGED: Interface FastEthernet0/0, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/0, changed state to up

Router(config-if)#int fa 1/0
Router(config-if)#ip add 192.168.0.129 255.255.255.248
Router(config-if)#no shut

Router(config-if)#
%LINK-5-CHANGED: Interface FastEthernet1/0, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet1/0, changed state to up

Router(config-if)#int se 2/0
Router(config-if)#ip add 192.168.0.137 255.255.255.252
Router(config-if)#clock rate 250000
Router(config-if)#no shut

%LINK-5-CHANGED: Interface Serial2/0, changed state to down
Router(config-if)#ip dhcp pool IT
Router(dhcp-config)#net 192.168.0.64 255.255.255.224
Router(dhcp-config)#default-router 192.168.0.65
Router(dhcp-config)#
Router(dhcp-config)#ip dhcp pool server
Router(dhcp-config)#net 192.168.0.128 255.255.255.248
Router(dhcp-config)#default-router 192.168.0.129
Router(dhcp-config)#ex
Router(config)#
%LINK-5-CHANGED: Interface Serial2/0, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface Serial2/0, changed state to up
%DHCPD-4-PING_CONFLICT: DHCP address conflict:  server pinged 192.168.0.65.

Router(config)#router rip
Router(config-router)#version 2
Router(config-router)#net 192.168.0.64
Router(config-router)#net 192.168.0.128
Router(config-router)#net 192.168.0.136
Router(config-router)#^Z


router-2
Router>en
Router#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#hostname R2
R2(config)#int fa 0/0
R2(config-if)#ip add 192.168.0.97 255.255.255.224
R2(config-if)#no shut

R2(config-if)#
%LINK-5-CHANGED: Interface FastEthernet0/0, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/0, changed state to up

R2(config-if)#int fa 1/0
R2(config-if)#ip add 192.168.0.1 255.255.255.192
R2(config-if)#no shut

R2(config-if)#
%LINK-5-CHANGED: Interface FastEthernet1/0, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet1/0, changed state to up

R2(config-if)#int fa 2/0
%Invalid interface type and number
R2(config)#int se 2/0
R2(config-if)#ip add 192.168.0.138 255.255.255.252
R2(config-if)#no shut

R2(config-if)#
%LINK-5-CHANGED: Interface Serial2/0, changed state to up

R2(config-if)#ip 
%LINEPROTO-5-UPDOWN: Line protocol on Interface Serial2/0, changed state to up

% Incomplete command.
R2(config-if)#ip dhcp pool sales
R2(dhcp-config)#net 192.168.0.96 255.255.255.252
R2(dhcp-config)#net 192.168.0.96 255.255.255.224
R2(dhcp-config)#default-router 192.168.0.97
R2(dhcp-config)#
R2(dhcp-config)#ip dhcp pool MTS
R2(dhcp-config)#net 192.168.0.0 255.255.255.192
R2(dhcp-config)#default-router 192.168.0.1
R2(dhcp-config)#ex
R2(config)#%DHCPD-4-PING_CONFLICT: DHCP address conflict:  server pinged 192.168.0.1.
%DHCPD-4-PING_CONFLICT: DHCP address conflict:  server pinged 192.168.0.97.

R2(config)#router rip
R2(config-router)#version 2
R2(config-router)#net 192.168.0.0
R2(config-router)#net 192.168.0.96
R2(config-router)#net 192.168.0.136
R2(config-router)#^Z
R2#


4no--

router1__

Router>en
Router#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#hostname R1
R1(config)#int fa 0/0
R1(config-if)#ip add 192.168.0.1 255.255.255.192
R1(config-if)#no shut

R1(config-if)# 
R1(config-if)#int fa 1/0
R1(config-if)#ip add 192.168.0.65 255.255.255.192
R1(config-if)#no shut

R1(config-if)# 
R1(config-if)#int se 2/0
R1(config-if)#ip add 10.10.10.1 255.255.255.252
R1(config-if)#clock rate 250000
R1(config-if)#no shut
%LINK-5-CHANGED: Interface FastEthernet0/0, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/0, changed state to up

%LINK-5-CHANGED: Interface FastEthernet1/0, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet1/0, changed state to up


%LINK-5-CHANGED: Interface Serial2/0, changed state to down
R1(config-if)#ip dhcp pool mis
R1(dhcp-config)#net 192.168.0.64 255.255.255.192
R1(dhcp-config)#default-router 192.168.0.65
R1(dhcp-config)#dns-server 192.168.0.4
R1(dhcp-config)#^Z
R1#
%SYS-5-CONFIG_I: Configured from console by console

R1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#router rip
R1(config-router)#version 2
R1(config-router)#net 192.168.0.0
R1(config-router)#net 192.168.0.64
R1(config-router)#net 10.10.10.0
R1(config-router)#no auto-summary
R1(config-router)#^Z

router2---

Router>en
Router#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
Router(config)#hostname R2
R2(config)#int fa 0/0
R2(config-if)#ip add 192.168.0.129 255.255.255.192
R2(config-if)#no shut

R2(config-if)#int fa 1/0
R2(config-if)#ip add 192.168.0.193 255.255.255.192
R2(config-if)#no shut

R2(config-if)#int se 2/0
R2(config-if)#ip add 10.10.10.2 255.255.255.252
R2(config-if)#no shut

R2(config-if)#
R2(config-if)#ip dhcp pool operation
R2(dhcp-config)#net 192.168.0.128 255.255.255.192
R2(dhcp-config)#default-router 192.168.0.129
R2(dhcp-config)#dns-server 192.168.0.4
R2(dhcp-config)#
R2(dhcp-config)#ip dhcp pool sales
R2(dhcp-config)#net 192.168.0.192 255.255.255.192
R2(dhcp-config)#default-router 192.168.0.193
R2(dhcp-config)#dns-server 192.168.0.4
%LINK-5-CHANGED: Interface FastEthernet0/0, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet0/0, changed state to up

%LINK-5-CHANGED: Interface FastEthernet1/0, changed state to up

%LINEPROTO-5-UPDOWN: Line protocol on Interface FastEthernet1/0, changed state to up

%LINK-5-CHANGED: Interface Serial2/0, changed state to up
^Z
R2#
%SYS-5-CONFIG_I: Configured from console by console
^Z
R2#
R2#co
%LINEPROTO-5-UPDOWN: Line protocol on Interface Serial2/0, changed state to u
R2#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R2(config)#router rip
R2(config-router)#version 2
R2(config-router)#net 192.168.0.128
R2(config-router)#net 192.168.0.192
R2(config-router)#net 10.10.10.0
R2(config-router)#no auto-summary
R2(config-router)#^Z
