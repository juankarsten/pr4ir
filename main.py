'''
Created on Nov 25, 2013

@author: juan
'''

import re
import array

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
    print relevance[1]
    
    # hasil[eksperimen][query][urutan]=(recall,precision)
    hasil_eksperimen={}
    #total_relevan[query]=nilai relevan
    total_relevan={}
    # total_doc[query]= nilai doc
    total_doc={}
    
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
            
            # recall
            recall = total_relevan[query]/all_relevan
            precision = total_relevan[query]/total_doc[query]
            hasil[query][rank]=(recall,precision)
        
        # write eksperimen
        hasil_eksperimen[ii]=hasil
        
    print hasil_eksperimen[1][1]
    print hasil_eksperimen[2][1]