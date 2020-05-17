
vobla=set()
n=0
with open('cook.txt','r',encoding='utf8') as document:
        for line in document:
             print ('cook_book =','{ ')
             for text in document:
                 text = text.strip()
                 co=len(text)
                 #print(f'text= {text}')
                 if (text != 0) and (len(text) > 2) and ('|' not in text):
                     n = 0
                     key = text
                     print (f"'{key}':")
                     n = 1
                 elif ('|' in text):
                         vobla.add(text)
                         print (f'vobla= {vobla}')
                         if n == 1:
                             vobla = set()

       
       
        #while co != 0:
            
