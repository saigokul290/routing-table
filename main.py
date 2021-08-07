from tabulate import tabulate
def subnet_size(p_no):  #function for range of ip network
    sum=int(p_no)+3
    i=1
    while True:
        rang=2**i
        if rang>=sum:
            break
        else:
            i+=1
    return rang,i
def ip_assigning(rang,ip_addr,subnet,room_no,network_des):  #displaying the ip address
    ip=dict()
    ip["room_no"]=room_no
    ip["network_destionation"]=ip_addr[:10]+str(network_des)
    ip["gateway"]=ip_addr[:10]+str(network_des+rang-2)
    ip["broad_cast"]=ip_addr[:10]+str(network_des+rang-1)
    ip["subnet_mask"]=subnet
    return ip
def sub_range(ip_addr):#for range of ip address
    j = []
    for i in ip_addr:
        s = bin(int(i))
        if len(s[1:]) != 8:
            a = 8 - len(s)
            j.append(s[2:] + a * '0')
        else:
            continue
    n = ''
    for j in j:
        n = n + j
    i = -1
    fin = ''
    while n[i] != '1':
        fin = fin + (n[i])
        i -= 1
    fin = '1' + fin
    i, integer = 0, 0
    size = len(fin)
    while i < len(fin):
        integer += int(fin[size - 1 - i]) * pow(2, i)
        i += 1
    return integer
def subnet_mask(CIDR):
    lsIP = []
    ans = 0
    IP = [1] * CIDR
    for i in range(len(IP)):
        iIdx = i % 8
        if iIdx == 0:
            if i >= 8:
                lsIP.append(ans)
                ans = 0
        ans += pow(2, 7 - iIdx)
    lsIP.append(ans)

    [lsIP.append(0) for i in range(4 - len(lsIP))]
    return(str(lsIP[0]) + '.' + str(lsIP[1]) + '.' + str(lsIP[2]) + '.' + str(lsIP[3]))
if __name__=="__main__":
    loop=int(input("enter the number of rooms"))
    router_table = []
    j=0
    network_des = 0
    ip_addr = input('enter the ip adddress of the network')
    while j!=loop:
        room_no=input("enter the room no")
        interface=input('enter the interface of the respected input')
        pc_no=input('enter the no of pc in respective room')
        rang, i = subnet_size(pc_no)
        ip_range = sub_range(ip_addr.split('.'))
        CIDR = 32 - i
        subnet = subnet_mask(CIDR)
        ip_assign = ip_assigning(rang, ip_addr, subnet,room_no,network_des)

        print(network_des)
        router_table.append(ip_assign)
        j+=1
        network_des +=rang

    print(tabulate(router_table,headers="keys"))