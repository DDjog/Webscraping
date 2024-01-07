#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import connect
import models
import seeds

if __name__ == '__main__':
    print("___MondoDB simple app___\n")
    
    seeds.delete_data()
    seeds.put_data_to_mongo()
    
    # while True:
    #     instr=input(">")
        
    #     if instr=="exit":
    #         break
        
    #     strlist = instr.split(":")
        
    #     if strlist[0] == "name":
    #         # print( "author name:", strlist[1].strip() )
    #         # author_fullname = "Albert Einstein"
    #         author_fullname = strlist[1].strip()
    #         # print("Author:")
    #         rslt = models.find_quote_by_author( author_fullname )
    #         if rslt is not None:
    #             for q in rslt:
    #                 print(q.quote)
    #                 print(q.author.fullname)
    #                 print()
    #         else:
    #             print("Nie ma autora: ", author_fullname )
            
    #     if strlist[0] == "tag":
    #         # print( "tag name:", strlist[1].strip() )
    #         # print("Quote by single tag:\n")
    #         # tag = "life"
    #         tag = strlist[1].strip()
    #         rslt = models.find_single_tag( tag )
    #         if rslt is not None:
    #             for q in rslt:
    #                   print( q.quote )
    #                   print( q.author.fullname )
    #                   print()
    #         else:
    #             print("Brak wskazane tagu.")
           
    #     if strlist[0] == "tags":
    #         tagsstr = strlist[1].strip()
    #         tagslist = tagsstr.split(",")
    #         print( "tags:", len(tagslist) )
    #         tags=[]
    #         for t in tagslist:
    #             tags.append( t )
    #         # print(arraytag)
    #         # print("Quote by multile tag:\n")    
    #         # tags = ["success"]
    #         rslt = models.find_tags( tags )
    #         if rslt is not None:
    #             for q in rslt:
    #                   print( q.quote )
    #                   print( q.author.fullname )
    #                   print()
    #         else:
    #             print("Brak tagów.")            
