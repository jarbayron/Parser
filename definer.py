import variables

def lister(self):
    from variables import d
    variables.runner(self)
    global d
    return d

def listmaker(xx,yy,zz):
    global listone,listtwo,listthree
    listone=dict(lister(xx))
    listtwo=dict(lister(yy))
    listthree=dict(lister(zz))
    return listone,listtwo,listthree


