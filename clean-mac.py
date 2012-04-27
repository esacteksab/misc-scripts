    mac=str('aA00CcA9e7Ff')
    maclen=len(mac)
    if maclen == 12:
        maclist=list(mac)
     
        positions=2,5,8,11,14
     
        for i in positions:
            maclist.insert(i,':')
     
        newmac=",".join(maclist)
     
        final12mac=newmac.replace(',','').lower()
     
        print final12mac
       
    elif maclen == 17:
        mac17final=mac.replace('-',':').lower()
        print mac17final
    else:
        print "There are only %s characters" % (maclen)

