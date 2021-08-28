## Importing Necessary Modules
import requests # to get image from the web
import shutil # to save it locally

## Set up the image URL and filename
comic = input("comic name:- ").lower().replace(' ','-')
chapter = input("chapter numner:- ")

pg01 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/01.jpg"
pg02 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/02.jpg"
pg03 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/03.jpg"
pg04 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/04.jpg"
pg05 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/05.jpg"
pg06 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/06.jpg"
pg07 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/07.jpg"
pg08 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/08.jpg"
pg09 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/09.jpg"
pg10 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/10.jpg"
pg11 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/11.jpg"
pg12 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/12.jpg"
pg13 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/13.jpg"
pg14 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/14.jpg"
pg15 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/15.jpg"
pg16 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/16.jpg"
pg17 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/17.jpg"
pg18 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/18.jpg"
pg19 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/19.jpg"
pg20 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/20.jpg"
pg21 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/21.jpg"
pg22 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/22.jpg"
pg23 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/23.jpg"
pg24 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/24.jpg"
pg25 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/25.jpg"
pg26 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/26.jpg"
pg27 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/27.jpg"
pg28 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/28.jpg"
pg29 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/29.jpg"
pg30 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/30.jpg"
pg31 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/31.jpg"
pg32 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/32.jpg"
pg33 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/33.jpg"
pg34 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/34.jpg"
pg35 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/35.jpg"
pg36 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/36.jpg"
pg37 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/37.jpg"
pg38 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/38.jpg"
pg39 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/39.jpg"
pg40 = f"https://readcomicsonline.ru/uploads/manga/{comic}/chapters/{chapter}/40.jpg"

name1 = pg01.split("/")[-1]
name2 = pg02.split("/")[-1]
name3 = pg03.split("/")[-1]
name4 = pg04.split("/")[-1]
name5 = pg05.split("/")[-1]
name6 = pg06.split("/")[-1]
name7 = pg07.split("/")[-1]
name8 = pg08.split("/")[-1]
name9 = pg09.split("/")[-1]
name10 = pg10.split("/")[-1]
name11 = pg11.split("/")[-1]
name12 = pg12.split("/")[-1]
name13 = pg13.split("/")[-1]
name14 = pg14.split("/")[-1]
name15 = pg15.split("/")[-1]
name16 = pg16.split("/")[-1]
name17 = pg17.split("/")[-1]
name18 = pg18.split("/")[-1]
name19 = pg19.split("/")[-1]
name20 = pg20.split("/")[-1]
name21 = pg21.split("/")[-1]
name22 = pg22.split("/")[-1]
name23 = pg23.split("/")[-1]
name24 = pg24.split("/")[-1]
name25 = pg25.split("/")[-1]
name26 = pg26.split("/")[-1]
name27 = pg27.split("/")[-1]
name28 = pg28.split("/")[-1]
name29 = pg29.split("/")[-1]
name30 = pg30.split("/")[-1]
name31 = pg31.split("/")[-1]
name32 = pg32.split("/")[-1]
name33 = pg33.split("/")[-1]
name34 = pg34.split("/")[-1]
name35 = pg35.split("/")[-1]
name36 = pg36.split("/")[-1]
name37 = pg37.split("/")[-1]
name38 = pg38.split("/")[-1]
name39 = pg39.split("/")[-1]
name39 = pg40.split("/")[-1]

# Open the url image, set stream to True, this will return the stream content.
r1 = requests.get(pg01, stream = True)
r2 = requests.get(pg02, stream = True)
r3 = requests.get(pg03, stream = True)
r4 = requests.get(pg04, stream = True)
r5 = requests.get(pg05, stream = True)
r6 = requests.get(pg06, stream = True)
r7 = requests.get(pg07, stream = True)
r8 = requests.get(pg08, stream = True)
r9 = requests.get(pg09, stream = True)
r10 = requests.get(pg10, stream = True)
r11 = requests.get(pg11, stream = True)
r12 = requests.get(pg12, stream = True)
r13 = requests.get(pg13, stream = True)
r14 = requests.get(pg14, stream = True)
r15 = requests.get(pg15, stream = True)
r16 = requests.get(pg16, stream = True)
r17 = requests.get(pg17, stream = True)
r18 = requests.get(pg18, stream = True)
r19 = requests.get(pg19, stream = True)
r20 = requests.get(pg20, stream = True)
r21 = requests.get(pg21, stream = True)
r22 = requests.get(pg22, stream = True)
r23 = requests.get(pg23, stream = True)
r24 = requests.get(pg24, stream = True)
r25 = requests.get(pg25, stream = True)
r26 = requests.get(pg26, stream = True)
r27 = requests.get(pg27, stream = True)
r28 = requests.get(pg28, stream = True)
r29 = requests.get(pg29, stream = True)
r30 = requests.get(pg30, stream = True)
r31 = requests.get(pg31, stream = True)
r32 = requests.get(pg32, stream = True)
r33 = requests.get(pg33, stream = True)
r34 = requests.get(pg34, stream = True)
r35 = requests.get(pg35, stream = True)
r36 = requests.get(pg36, stream = True)
r37 = requests.get(pg37, stream = True)
r38 = requests.get(pg38, stream = True)
r39 = requests.get(pg39, stream = True)
r40 = requests.get(pg40, stream = True)

if r1.status_code == 200:
    r1.raw.decode_content = True
    with open(name1,'wb') as f:
        shutil.copyfileobj(r1.raw, f)  
    print('Image sucessfully Downloaded: ',name1)
else:
    print('An error occured! Image cannot be retreived')
    
    
if r2.status_code == 200:
    r2.raw.decode_content = True
    with open(name2,'wb') as f:
        shutil.copyfileobj(r2.raw, f)  
    print('Image sucessfully Downloaded: ',name2)
else:
    print('')   
    
    
if r3.status_code == 200:
    r3.raw.decode_content = True
    with open(name3,'wb') as f:
        shutil.copyfileobj(r3.raw, f)  
    print('Image sucessfully Downloaded: ',name3)
else:
    print('')
    
    
if r4.status_code == 200:
    r4.raw.decode_content = True
    with open(name4,'wb') as f:
        shutil.copyfileobj(r4.raw, f)  
    print('Image sucessfully Downloaded: ',name4)
else:
    print('')
    
    
if r5.status_code == 200:
    r5.raw.decode_content = True
    with open(name5,'wb') as f:
        shutil.copyfileobj(r5.raw, f)  
    print('Image sucessfully Downloaded: ',name5)
else:
    print('')
    
    
if r6.status_code == 200:
    r6.raw.decode_content = True
    with open(name6,'wb') as f:
        shutil.copyfileobj(r6.raw, f)  
    print('Image sucessfully Downloaded: ',name6)
else:
    print('')
    
    
if r7.status_code == 200:
    r7.raw.decode_content = True
    with open(name7,'wb') as f:
        shutil.copyfileobj(r7.raw, f)  
    print('Image sucessfully Downloaded: ',name7)
else:
    print('')
    
    
if r8.status_code == 200:
    r8.raw.decode_content = True
    with open(name8,'wb') as f:
        shutil.copyfileobj(r8.raw, f)  
    print('Image sucessfully Downloaded: ',name8)
else:
    print('')
    
    
if r9.status_code == 200:
    r9.raw.decode_content = True
    with open(name9,'wb') as f:
        shutil.copyfileobj(r9.raw, f)  
    print('Image sucessfully Downloaded: ',name9)
else:
    print('')
    
    
if r10.status_code == 200:
    r10.raw.decode_content = True
    with open(name10,'wb') as f:
        shutil.copyfileobj(r10.raw, f)  
    print('Image sucessfully Downloaded: ',name10)
else:
    print('')
    
    
if r11.status_code == 200:
    r11.raw.decode_content = True
    with open(name11,'wb') as f:
        shutil.copyfileobj(r11.raw, f)  
    print('Image sucessfully Downloaded: ',name11)
else:
    print('')
    
    
if r12.status_code == 200:
    r12.raw.decode_content = True
    with open(name12,'wb') as f:
        shutil.copyfileobj(r12.raw, f)  
    print('Image sucessfully Downloaded: ',name12)
else:
    print('')
    
    
if r13.status_code == 200:
    r13.raw.decode_content = True
    with open(name13,'wb') as f:
        shutil.copyfileobj(r13.raw, f)  
    print('Image sucessfully Downloaded: ',name13)
else:
    print('')
    
    
if r14.status_code == 200:
    r14.raw.decode_content = True
    with open(name14,'wb') as f:
        shutil.copyfileobj(r14.raw, f)  
    print('Image sucessfully Downloaded: ',name14)
else:
    print('')
    
    
if r15.status_code == 200:
    r15.raw.decode_content = True
    with open(name15,'wb') as f:
        shutil.copyfileobj(r15.raw, f)  
    print('Image sucessfully Downloaded: ',name15)
else:
    print('')
    
    
if r16.status_code == 200:
    r16.raw.decode_content = True
    with open(name16,'wb') as f:
        shutil.copyfileobj(r16.raw, f)  
    print('Image sucessfully Downloaded: ',name16)
else:
    print('')
    
    
if r17.status_code == 200:
    r17.raw.decode_content = True
    with open(name17,'wb') as f:
        shutil.copyfileobj(r17.raw, f)  
    print('Image sucessfully Downloaded: ',name17)
else:
    print('')
    
    
if r18.status_code == 200:
    r18.raw.decode_content = True
    with open(name18,'wb') as f:
        shutil.copyfileobj(r18.raw, f)  
    print('Image sucessfully Downloaded: ',name18)
else:
    print('')
    
    
if r19.status_code == 200:
    r19.raw.decode_content = True
    with open(name19,'wb') as f:
        shutil.copyfileobj(r19.raw, f)  
    print('Image sucessfully Downloaded: ',name19)
else:
    print('')
    
    
if r20.status_code == 200:
    r20.raw.decode_content = True
    with open(name20,'wb') as f:
        shutil.copyfileobj(r20.raw, f)  
    print('Image sucessfully Downloaded: ',name20)
else:
    print('')
    
    
if r21.status_code == 200:
    r21.raw.decode_content = True
    with open(name21,'wb') as f:
        shutil.copyfileobj(r21.raw, f)  
    print('Image sucessfully Downloaded: ',name21)
else:
    print('')
    
    
if r22.status_code == 200:
    r22.raw.decode_content = True
    with open(name11,'wb') as f:
        shutil.copyfileobj(r22.raw, f)  
    print('Image sucessfully Downloaded: ',name22)
else:
    print('')
    
    
    
if r23.status_code == 200:
    r23.raw.decode_content = True
    with open(name23,'wb') as f:
        shutil.copyfileobj(r23.raw, f)  
    print('Image sucessfully Downloaded: ',name23)
else:
    print('')
    
    
if r24.status_code == 200:
    r24.raw.decode_content = True
    with open(name24,'wb') as f:
        shutil.copyfileobj(r24.raw, f)  
    print('Image sucessfully Downloaded: ',name24)
else:
    print('')
    
    
if r25.status_code == 200:
    r25.raw.decode_content = True
    with open(name25,'wb') as f:
        shutil.copyfileobj(r25.raw, f)  
    print('Image sucessfully Downloaded: ',name25)
else:
    print('')
    
    
if r26.status_code == 200:
    r26.raw.decode_content = True
    with open(name26,'wb') as f:
        shutil.copyfileobj(r26.raw, f)  
    print('Image sucessfully Downloaded: ',name26)
else:
    print('')
    
    
if r27.status_code == 200:
    r27.raw.decode_content = True
    with open(name27,'wb') as f:
        shutil.copyfileobj(r27.raw, f)  
    print('Image sucessfully Downloaded: ',name27)
else:
    print('')
    
    
if r28.status_code == 200:
    r28.raw.decode_content = True
    with open(name28,'wb') as f:
        shutil.copyfileobj(r28.raw, f)  
    print('Image sucessfully Downloaded: ',name28)
else:
    print('')
    
    
if r29.status_code == 200:
    r29.raw.decode_content = True
    with open(name29,'wb') as f:
        shutil.copyfileobj(r29.raw, f)  
    print('Image sucessfully Downloaded: ',name29)
else:
    print('')
    
    
if r30.status_code == 200:
    r30.raw.decode_content = True
    with open(name30,'wb') as f:
        shutil.copyfileobj(r30.raw, f)  
    print('Image sucessfully Downloaded: ',name30)
else:
    print('')
    
    
if r31.status_code == 200:
    r31.raw.decode_content = True
    with open(name31,'wb') as f:
        shutil.copyfileobj(r31.raw, f)  
    print('Image sucessfully Downloaded: ',name31)
else:
    print('')
    
    
if r32.status_code == 200:
    r32.raw.decode_content = True
    with open(name11,'wb') as f:
        shutil.copyfileobj(r32.raw, f)  
    print('Image sucessfully Downloaded: ',name32)
else:
    print('')
    
    
    
if r33.status_code == 200:
    r33.raw.decode_content = True
    with open(name33,'wb') as f:
        shutil.copyfileobj(r33.raw, f)  
    print('Image sucessfully Downloaded: ',name33)
else:
    print('')
    
    
if r34.status_code == 200:
    r34.raw.decode_content = True
    with open(name34,'wb') as f:
        shutil.copyfileobj(r34.raw, f)  
    print('Image sucessfully Downloaded: ',name34)
else:
    print('')
    
    
if r35.status_code == 200:
    r35.raw.decode_content = True
    with open(name35,'wb') as f:
        shutil.copyfileobj(r35.raw, f)  
    print('Image sucessfully Downloaded: ',name35)
else:
    print('')
    
    
if r36.status_code == 200:
    r36.raw.decode_content = True
    with open(name36,'wb') as f:
        shutil.copyfileobj(r36.raw, f)  
    print('Image sucessfully Downloaded: ',name36)
else:
    print('')
    
    
if r37.status_code == 200:
    r37.raw.decode_content = True
    with open(name37,'wb') as f:
        shutil.copyfileobj(r37.raw, f)  
    print('Image sucessfully Downloaded: ',name37)
else:
    print('')
    
    
if r38.status_code == 200:
    r38.raw.decode_content = True
    with open(name38,'wb') as f:
        shutil.copyfileobj(r38.raw, f)  
    print('Image sucessfully Downloaded: ',name38)
else:
    print('')
    
    
if r39.status_code == 200:
    r39.raw.decode_content = True
    with open(name39,'wb') as f:
        shutil.copyfileobj(r39.raw, f)  
    print('Image sucessfully Downloaded: ',name39)
else:
    print('')
    
    
if r40.status_code == 200:
    r40.raw.decode_content = True
    with open(name40,'wb') as f:
        shutil.copyfileobj(r40.raw, f)  
    print('Image sucessfully Downloaded: ',name40)
else:
    print('')         