'''
Created on Nov 25, 2013

@author: juan
'''

import re
import pylab as pl
from sympy.physics.quantum.circuitplot import matplotlib


if __name__ == '__main__':
    all_relevan = 20.0
    
    #relevance[query]=[array dok]
    relevance={}
    
    file = open('relevance judgement.txt','r')
    for line in file:
        lines=re.split("\s+", line)
        query=int(lines[0])
        dok = lines[1]
        if not query in relevance:
            relevance[query]=[dok]
        else:
            relevance[query].append(dok)
    #print relevance[1]
    
    # hasil[eksperimen][query][urutan]=(recall,precision)
    hasil_eksperimen={}
    #total_relevan[query]=nilai relevan
    total_relevan={}
    # total_doc[query]= nilai doc
    total_doc={}
    #no5relevan
    relevanlima=0.0
    limatotal=0.0
    
    for ii in xrange(1,6):
        filein = open("Hasil_Eksperimen%d.txt"%(ii),'r')
        hasil={}
        
        for line in filein:
            lines=re.split("\s+", line)
            query=int(lines[0])
            doc=lines[1]
            rank=int(lines[2])
            
            if rank > 20:
                continue
            
            if not query in hasil:
                hasil[query]={}
                total_relevan[query]=0.0
                total_doc[query]=0.0
            
            total_doc[query]+=1
            if doc in relevance[query]:
                total_relevan[query]+=1
                #no 5
                if ii == 1:
                    relevanlima+=1.0
            #no 5
            if ii == 1:
                limatotal+=1.0
            # recall
            recall = total_relevan[query]/all_relevan
            precision = total_relevan[query]/total_doc[query]
            hasil[query][rank]=(recall,precision)
            
        
        # write eksperimen
        hasil_eksperimen[ii]=hasil
        
    for ii in xrange(1,21):
        print hasil_eksperimen[3][26][ii]
    #print hasil_eksperimen[2][1]
    
    
    
    
    print "INTERPOLATIONNNNNNNNNNNNNN.............."
    #hasil[eksperimen][query][urutan] (recall,precision)
    
    pl.figure("precision-recall kelima eksperimen")
    color=['b','r','g','c','m','y']
    for zz in xrange(1,6):
        interpolation=[0 for ll in xrange(0,11)]
        for kk in hasil_eksperimen[1].iterkeys():
            eksperimen = hasil_eksperimen[zz][kk]
            for ii in xrange(0,11):
                #untk interpolasi 0
                ii/=10.0
                found = False
                maksprecision = -1
                for jj in xrange(1,21):
                    recall=eksperimen[jj][0]
                    precision=eksperimen[jj][1]
                    if recall>=ii and recall <= ii+0.1:
                        found=True
                        if maksprecision <= precision:
                            maksprecision = precision
                if found:
                    interpolation[int(ii*10)]+=maksprecision
                    last=maksprecision
                else:
                    interpolation[int(ii*10)]+=0.0            
        interpolation=[interpolation[ll]/50.0 for ll in xrange(0,11)]
        print interpolation
        
        pl.plot([xx/10.0 for xx in xrange(0,11)],interpolation,color[zz-1]+'o-',label="eksperimen "+str(zz))
    pl.axis([0,1,0,1])
    pl.legend()
    pl.show()
    
        
    
    
    print ""
    print "NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO 3"
    for ii in hasil_eksperimen.iterkeys():
        eksperimen=hasil_eksperimen[ii]
        avg_recall=0.0
        avg_precision=0.0
        total=0.0
        for jj in eksperimen.iterkeys():
            avg_recall+=round(eksperimen[jj][20][0],2)
            avg_precision+=round(eksperimen[jj][20][1],2)
            total+=1
        print "Average Recall "+str(ii)+" "+str(avg_recall/total)
        
    #hasil[eksperimen][query][urutan] (recall,precision)
    for ii in hasil_eksperimen.iterkeys():
        eksperimen=hasil_eksperimen[ii]
        avg_precision=0.0
        total_query=0.0
        for jj in eksperimen.iterkeys():
            last_recall=0.0
            query_precision=0.0
            total=0.0
            for kk in eksperimen[jj].iterkeys():
                my_recall=eksperimen[jj][kk][0]
                if my_recall != last_recall:
                    query_precision+=eksperimen[jj][kk][1]
                    total+=1
                    last_recall=my_recall
            if total == 0:
                query_precision=0
            else:
                query_precision/=total
            avg_precision+=query_precision
            total_query+=1
        print "Average Precision "+str(ii)+" "+str(avg_precision/total_query)
        
        
        
    print ""
    print "NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO 4"
    #init
    eksperimen=hasil_eksperimen[1]
    avg_recall=[0 for jj in eksperimen.iterkeys()]
    avg_recall.append(0)
    avg_precision=[0 for jj in eksperimen.iterkeys()]
    avg_precision.append(0)
    
    
    #hasil[eksperimen][query][urutan] (recall,precision)
    # eksperimen ke-
    for ii in hasil_eksperimen.iterkeys():
        eksperimen=hasil_eksperimen[ii]
        # query ke-
        total=0
        for jj in eksperimen.iterkeys():
            avg_recall[jj]+=round(eksperimen[jj][20][0],2)
            #avg_precision[jj]+=round(eksperimen[jj][20][1],2)
            total+=1
    
    
    #hasil[eksperimen][query][urutan] (recall,precision)
    for ii in xrange(1,51):
        #avg_recall[jj]+=round(eksperimen[jj][20][0],2)
        for jj in xrange(1,6):
            last_recall = 0.0
            total=0.0
            avg_prec_q=0
            for kk in xrange(1,21):
                my_recall = hasil_eksperimen[jj][ii][kk][0]
                if my_recall != last_recall:
                    last_recall=my_recall
                    total+=1
                    avg_prec_q+=hasil_eksperimen[jj][ii][kk][1]
            if total != 0 :
                avg_precision[ii]+=avg_prec_q/total
        #avg_precision[ii]/=5
    
                    
    maks=-1
    maksexp=0
    min=10000
    minexp=0
    
    maks_prec=-1
    maksexp_prec=0
    min_prec=10000
    minexp_prec=0
    for jj in eksperimen.iterkeys():
        avg_recall[jj]/=len(hasil_eksperimen)
        avg_precision[jj]/=len(hasil_eksperimen)
        total+=1
        print "Average Recall query ke-"+str(jj)+" "+str(avg_recall[jj])
        print "Average Precision query ke-"+str(jj)+" "+str(avg_precision[jj])
       
        if maks <= avg_recall[jj]:
            maks=avg_recall[jj]
            maksexp=jj
        
        if min >= avg_recall[jj]:
            min=avg_recall[jj]
            minexp=jj
            
        if maks_prec <= avg_precision[jj]:
            maks_prec=avg_precision[jj]
            maksexp_prec=jj
        
        if min_prec >= avg_precision[jj]:
            min_prec=avg_precision[jj]
            minexp_prec=jj
    print "maks recall %.2f %d  "%(maks,maksexp)
    print "min recall %.2f %d  "%(min,minexp)
    
    print "maks precision %.2f %d  "%(maks_prec,maksexp_prec)
    print "min precision %.2f %d  "%(min_prec,minexp_prec)
    
    print ""
    print "MICRO AVERAGE"
    print relevanlima/limatotal