from PIL import Image
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import textwrap
import json
def f():
    sonname="karakter\\karakter.txt"

    with open(sonname, encoding="utf-16") as aa:
        newdata = json.load(aa)



    img = Image.new('RGB', (2480,3508), (255, 255, 255))
    img.save("cikti\\image.png", "PNG")

    print("Beyaz A4 KK")

    print(type(img))



    base = Image.open("cikti\\image.png").convert("RGB")
    txt = Image.new("RGB", (1400,100), (0,0,0))
    txt.save("cikti\\txt.png", "PNG")



    fnt = ImageFont.truetype("Fate\\font\\Akrobat-Bold.otf", 100)
    fnt2 = ImageFont.truetype("Fate\\font\\Akrobat-Bold.otf", 60)
    fnt3 = ImageFont.truetype("Fate\\font\\Akrobat-Bold.otf", 80)
    fnt4 = ImageFont.truetype("Fate\\font\\Akrobat-Bold.otf", 40)
    fnt5 = ImageFont.truetype("Fate\\font\\Akrobat-Bold.otf", 50)
    fntB = ImageFont.truetype("Fate\\font\\Akrobat-Bold.otf", 130)


    d = ImageDraw.Draw(base)

    base.paste(txt, (0, 250))


    yazi2="KARAKTERİN İSMİ"
    d.text((250,50), yazi2, font=fnt4, fill=(0,0,0,255))
    yazi2=newdata['karakter'][0]["Name"]
    d.text((250/2,100), yazi2, font=fnt3, fill=(0,0,0,255))

    yazi="ASPECT'LER"
    d.text((250,240), yazi, font=fnt, fill=(255,255,255,255))


    yazi2="HIGH CONCEPT"
    d.text((250,400), yazi2, font=fnt2, fill=(0,0,0,255))
    FOREGROUND = (0, 0, 0)
    w=250
    h=400
    text=newdata['karakter'][0]["HCA"]
    lines = textwrap.wrap(text, width=55)
    font_path = "Fate\\font\\Akrobat-Bold.otf"
    font = ImageFont.truetype(font_path, 60, encoding='unic')
    width, height = font.getsize("line")
    y_text = h + height
    for line in lines:
        width, height = font.getsize(line)
        d.text(((w) / 2, y_text), line, font=font, fill=FOREGROUND)
        y_text += height



    yazi2="TROUBLE"
    d.text((250,y_text+height), yazi2, font=fnt2, fill=(0,0,0))
    h=y_text+height+height
    text=newdata['karakter'][0]["TRBL"]
    lines = textwrap.wrap(text, width=55)
    y_text = h
    font_path = "Fate\\font\\Akrobat-Bold.otf"
    font = ImageFont.truetype(font_path, 60, encoding='unic')
    for line in lines:
        width, height = font.getsize(line)
        d.text(((w) / 2, y_text), line, font=font, fill=FOREGROUND)
        y_text += height




    yazi2="RELETIONSHIP"
    d.text((250,y_text+height), yazi2, font=fnt2, fill=(0,0,0))
    h=y_text+height+height
    text=newdata['karakter'][0]["Reletionsphip"]
    lines = textwrap.wrap(text, width=55)
    y_text = h
    font_path = "Fate\\font\\Akrobat-Bold.otf"
    font = ImageFont.truetype(font_path, 60, encoding='unic')
    for line in lines:
        width, height = font.getsize(line)
        d.text(((w) / 2, y_text), line, font=font, fill=FOREGROUND)
        y_text += height

    yazi2="SERBEST ASPECT'LER"
    d.text((250,y_text+height), yazi2, font=fnt2, fill=(0,0,0))
    h=y_text+height+height
    text=newdata['karakter'][0]["serbestaspect1"]
    lines = textwrap.wrap(text, width=55)
    y_text = h
    font_path = "Fate\\font\\Akrobat-Bold.otf"
    font = ImageFont.truetype(font_path, 60, encoding='unic')
    for line in lines:
        width, height = font.getsize(line)
        d.text(((w) / 2, y_text), line, font=font, fill=FOREGROUND)
        y_text += height



    yazi2="SERBEST ASPECT'LER"
    d.text((250,y_text+height), yazi2, font=fnt2, fill=(0,0,0))
    h=y_text+height+height
    text=newdata['karakter'][0]["serbestaspect2"]
    lines = textwrap.wrap(text, width=55)
    y_text = h
    font_path = "Fate\\font\\Akrobat-Bold.otf"
    font = ImageFont.truetype(font_path, 60, encoding='unic')
    for line in lines:
        width, height = font.getsize(line)
        d.text(((w) / 2, y_text), line, font=font, fill=FOREGROUND)
        y_text += height

    
    karab=y_text+height*2
    base.paste(txt, (0,karab))






    sagtaraf=1240
    base.paste(txt, (sagtaraf, 250))
    yazi="STRESS VE CONSEQUENCE"
    d.text((250+sagtaraf,240), yazi, font=fnt, fill=(255,255,255))
    yazi="STRESS'LER"
    d.text((sagtaraf/2+sagtaraf,400), yazi, font=fnt2, fill=(0,0,0))

    yazi="FİZİKSEL"
    d.text((250+sagtaraf,470), yazi, font=fnt3, fill=(0,0,0))
    kare = Image.open("Fate\\kare.jpg").convert("RGB")
    tepelogo=(70,70)
    kare=kare.resize(tepelogo)
    fCount=int(newdata['karakter'][0]["fizikselStress"])
    for i in range(fCount):
        base.paste(kare, (250+sagtaraf+300+i*80, 482))

    yazi="ZİHİNSEL"
    d.text((250+sagtaraf,548), yazi, font=fnt3, fill=(0,0,0))
    zCount=int(newdata['karakter'][0]["mentalStress"])
    for i in range(zCount):
        base.paste(kare, (250+sagtaraf+300+i*80, 560))


    yazi="CONSEQUENCE'LAR"
    d.text((sagtaraf/2+sagtaraf-100,670), yazi, font=fnt2, fill=(0,0,0))
    sayiliste=["2","4","6"]
    conseqisimliste=["HAFİF","ORTALAMA","AĞIR"]
    conseqicerikliste=[newdata['karakter'][0]["conseq1"],newdata['karakter'][0]["conseq2"],newdata['karakter'][0]["conseq3"]]
    for i in range(len(sayiliste)):
        base.paste(kare, (250+sagtaraf, 740+i*180))
        d.text((270+sagtaraf, 740+i*180), sayiliste[i], font=fnt2, fill=(0,0,0))
        d.text((340+sagtaraf,733+i*180), conseqisimliste[i], font=fnt4, fill=(0,0,0))
        d.text((340+sagtaraf,770+i*180), conseqicerikliste[i], font=fnt5, fill=(0,0,0))#Buraya line sistemi yap




    #BURAYA KONTROL KISMI EKLE HANGİ TARAFDAHA UZUNSA ORDAN BAŞLASIN ALT KISIM

    yazi2="STUNTLAR"
    yazikara=y_text+height*2-10
    d.text((250,yazikara), yazi2, font=fnt, fill=(255,255,255))
    h=y_text+height*2+160
    text=newdata['karakter'][0]["stuntlar"]
    text.splitlines()
    linoeofLines=[]
    for i in range(len(text)):
        lines = textwrap.wrap(text, width=55)

    y_text = h
    font_path = "Fate\\font\\Akrobat-Bold.otf"
    font = ImageFont.truetype(font_path, 60, encoding='unic')
    for line in lines:
        width, height = font.getsize(line)
        d.text(((w) / 2, y_text), line, font=font, fill=FOREGROUND)
        y_text += height





    base.paste(txt, (1240,karab))

    yazi="SKILL'LER"
    d.text((250+sagtaraf,yazikara), yazi, font=fnt, fill=(255,255,255))
    Skillisimler=["Akademik","Aldatmaca","Atıcılık","Bağlantılar","Beden","Çeviklik","Empati","Farkındalık","Gizlilik","Gözlem","Hırsızlık","İlim","İrade","Kaynaklar","Kışkırtma","Muhabbet","Sürücülük","Yakın Dövüş","Zanaat"]
    #skillpuanlar=["1","2","3","0","0","0","0","0","0","0","0","0","0","2","0","0","0","0","4"]
    skillpuanlar=newdata['karakter'][0]["skillListesi"]


    for i in range(len(Skillisimler)):
        yazii="+{} {}".format(skillpuanlar[i],Skillisimler[i])
        d.text((250+sagtaraf, h+i*80),yazii , font=fnt2, fill=(0,0,0))





    base.paste(txt, (0,3300))
    circle = Image.open("Fate\\circle.png")
    tepelogo=(300,300)
    circle=circle.resize(tepelogo)
    base.paste(circle, (100, 3200), circle)
    yazi2="REFRESH'LER"
    d.text((430, 3290), yazi2, font=fnt, fill=(255,255,255))




    txt2 = Image.new("RGB", (20,3508), (0,0,0))
    base.paste(txt2, (1400,260))

    yazi2=newdata['karakter'][0]["refresh"]
    d.text((225, 3265), yazi2, font=fntB, fill=(0,0,0))

    #base.show()
    base.save("cikti\\d.png", "PNG")
    return "cikti\\d.png"
