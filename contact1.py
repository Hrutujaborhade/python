contact={1:{'name':'vidhi','email':'vidhi.joshi@gmail.com','phoneno':'9862736478','Address':'xyz street,mulund east'},
        2:{'name':'hrutuja','email':'hrutuborhade@gmail.com','phoneno':'9371836478','Address':'pqr street,vikhroli west'},
        3:{'name':'sahil','email':'sahilb@gmail.com','phoneno':'9087236478','Address':'abc street,vashi west'}}

i=input("enter name or emailid or number : ")
for cid,cinfo in contact.items():
    for key in cinfo:
         if (i==cinfo[key]):
             for i in cinfo:
                 print(i+":",cinfo[i])
         
         
         
        
