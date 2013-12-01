'''
Created on Nov 27, 2013

@author: juan
'''
'''
#hasil[eksperimen][query][urutan] (recall,precision)
    interpolation=[]
    eksperimen = hasil_eksperimen[1][1]
    print eksperimen
    last=0
    for ii in xrange(0,11):
        #untk interpolasi 0
        ii/=10.0
        found = False
        foundrecall=False
        lastrecall = 0
        maksprecision = 0
        for jj in xrange(1,21):
            recall=eksperimen[jj][0]
            precision=eksperimen[jj][1]
            if recall>=ii and precision != 0:
                found=True
                foundrecall = True
                lastrecall=recall
                maksprecision=precision
            if foundrecall and recall == lastrecall:
                if maksprecision <= precision:
                    maksprecision=precision
                    break
        interpolation.append(maksprecision)
        last=maksprecision
        if not found:
            interpolation.append(last)
            
    print "interpolation"
    print interpolation
    
'''