import requests
from lxml import html
from bs4 import BeautifulSoup
def karakk(link):
    originlink=link
    html_content = requests.get(originlink).text


    characterName=html_content[html_content.find('placeholder="Karakter İsmi" value='):html_content.find('disabled>')]
    characterName=characterName.replace('placeholder="Karakter İsmi" value=',"")
    characterName=characterName.replace("'","") #bunu değiştir

    aspectHighConsept=html_content[html_content.find('name="high_concept" value='):html_content.find('disabled>\r\nTrouble')]
    aspectHighConsept=aspectHighConsept.replace('name="high_concept" value=',"")
    aspectHighConsept=aspectHighConsept.replace("'","") #bunu deiştir +1. ve -1. sıraları sil

    aspectTrouble=html_content[html_content.find('name="trouble" value='):html_content.find('disabled>\r\nRelationship')]
    aspectTrouble=aspectTrouble.replace('name="trouble" value=',"")
    aspectTrouble=aspectTrouble.replace("'","") #bunu deiştir +1. ve -1. sıraları sil

    aspectRelationship=html_content[html_content.find('name="relationship" value='):html_content.find('disabled>\r\nSerbest Aspect\'ler:\r\n<input type="text" class="form-control" name="aspect1"')]
    aspectRelationship=aspectRelationship.replace('name="relationship" value=',"")
    aspectRelationship=aspectRelationship.replace("'","") #bunu deiştir +1. ve -1. sıraları sil

    aspectSerbestA1=html_content[html_content.find('name="aspect1" value='):html_content.find('disabled>\r\nSerbest Aspect\'ler:\r\n<input type="text" class="form-control" name="aspect2')]
    aspectSerbestA1=aspectSerbestA1.replace('name="aspect1" value=',"")
    aspectSerbestA1=aspectSerbestA1.replace("'","") #bunu deiştir +1. ve -1. sıraları sil

    aspectSerbestA2=html_content[html_content.find('name="aspect2" value='):html_content.find('disabled>\r\n</div>\r\n<div class="col-lg-6 col-sm-12 mt-5">')]
    aspectSerbestA2=aspectSerbestA2.replace('name="aspect2" value=',"")
    aspectSerbestA2=aspectSerbestA2.replace("'","") #bunu deiştir +1. ve -1. sıraları sil

    stressPhysical=html_content[html_content.find('Fiziksel <input type="checkbox" '):html_content.find('Zihinsel <input type="checkbox"')]
    stressPhysicalCount=stressPhysical.count("checked name")


    stressMental=html_content[html_content.find('Zihinsel <input type="checkbox"'):html_content.find('Consequence\'lar</center></div>')]
    stressMentalCount=stressMental.count("checked name")

    consequence1=html_content[html_content.find('name="consequence1" placeholder="Hafif"'):html_content.find('disabled></div>\r\n<div class="mt-5">4<input type="text" class="form-control" name="consequence2"')]
    consequence1=consequence1.replace('name="consequence1" placeholder="Hafif" style="display:inline-block;width: calc(100% - 10px);" value=',"")
    consequence1=consequence1.replace("'","") #bunu deiştir +1. ve -1. sıraları sil

    consequence2=html_content[html_content.find('name="consequence2" placeholder="Ortalama" style="display:inline-block;width: calc(100% - 10px);" value='):html_content.find('disabled></div>\r\n<div class="mt-5">6<input type="text" class="form-control" name="consequence3"')]
    consequence2=consequence2.replace('name="consequence2" placeholder="Ortalama" style="display:inline-block;width: calc(100% - 10px);" value=',"")
    consequence2=consequence2.replace("'","") #bunu deiştir +1. ve -1. sıraları sil

    consequence3=html_content[html_content.find('name="consequence3" placeholder="Ağır" style="display:inline-block;width: calc(100% - 10px);" value='):html_content.find('disabled></div>\r\n<div class="mt-5">2<input type="text" class="form-control" name="consequence3" placeholder="Hafif"')]
    consequence3=consequence3.replace('name="consequence3" placeholder="Ağır" style="display:inline-block;width: calc(100% - 10px);" value=',"")
    consequence3=consequence3.replace("'","") #bunu deiştir +1. ve -1. sıraları sil



    stunts=html_content[html_content.find('<textarea class="form-control" style="min-height:500px;" name="regular_stunts" disabled>'):html_content.find('</textarea>\r\n<div class="mt-2" style="position:relative;" id="zoomalan">')]
    stunts=stunts.replace('<textarea class="form-control" style="min-height:500px;" name="regular_stunts" disabled>',"")
    stunts=stunts.replace("'","") #bunu deiştir +1. ve -1. sıraları sil

    refreshs=html_content[html_content.find('name="refresh" style="display:inline-block;height:80px;width: 80px;border-radius:80px;position:absolute;top:5px;border:4px solid black;text-align:center;font-size:38px;background:white;" value='):html_content.find('disabled>\r\n<input type="number" placeholder="-" name="fate_point" ')]
    refreshs=refreshs.replace('name="refresh" style="display:inline-block;height:80px;width: 80px;border-radius:80px;position:absolute;top:5px;border:4px solid black;text-align:center;font-size:38px;background:white;" value=',"")
    refreshs=refreshs.replace("'","") #bunu deiştir +1. ve -1. sıraları sil

    fatepuanları=html_content[html_content.find('name="fate_point" style="display:inline-block;height:80px;width: 80px;border-radius:80px;position:absolute;bottom:5px;right:0;border:4px solid black;text-align:center;font-size:38px;" value='):html_content.find(' disabled>\r\n<div style="background:black;color:white;padding:5px 80px 5px 5px;text-align:right;margin-top:45px;">Fate Puanları</div>')]
    fatepuanları=fatepuanları.replace('name="fate_point" style="display:inline-block;height:80px;width: 80px;border-radius:80px;position:absolute;bottom:5px;right:0;border:4px solid black;text-align:center;font-size:38px;" value=',"")
    fatepuanları=fatepuanları.replace("'","") #bunu deiştir +1. ve -1. sıraları sil

    skills=html_content[html_content.find('<div class="mt-5"><a style="display:inline-block;line-height: 50px;font-weight: 700;font-size: 22px;color:#757575;">Akademik'):html_content.find('</div>\r\n</div>\r\n</div>\r\n      </div>\r\n\t  \t  </form>\r\n    </section>\r\n\t\t    <footer class="py-8 py-md-11 bg-gray-200">\n')]
    skillsCount=skills.count("value=")
    skillist=[]
    while True:
        skill=skills[skills.find("value=")+7:skills.find("value=")+8]
        skills=skills[skills.find("value=")+8:]
        skillist.append(skill)
        if "value=" not in skills:
            break
    if skillsCount==len(skillist):
        print("NP")
    else:
        print("Listede sorun")

    print("fin")

    """------------------------------------------------------------------------------------------------------------------------"""

    from PIL import Image
    from PIL import ImageFont
    from PIL import ImageDraw
    import sys
    import os
    import datetime

    x = datetime.datetime.now()
    yil=x.year
    ay=x.month
    gun=x.day

    pathorigin=os.getcwd()

    #klasorname=str(gun)+"_"+str(ay)+"_"+str(yil)
    klasorname="karakter"
    pat=pathorigin+"//"+klasorname
    sonname=pathorigin+"//"+klasorname+"//"+klasorname+".txt"
    try:
        os.makedirs(pat)
    except:
        print("dosyavar")


    import json
    data={}
    data["karakter"]=[]
    data["karakter"].append({
        "Name":characterName,
        "HCA":aspectHighConsept,
        "TRBL":aspectTrouble,
        "Reletionsphip":aspectRelationship,
        "serbestaspect1":aspectSerbestA1,
        "serbestaspect2":aspectSerbestA2,
        "fizikselStress":stressPhysicalCount,
        "mentalStress":stressMentalCount,
        "conseq1":consequence1,
        "conseq2":consequence2,
        "conseq3":consequence3,
        "stuntlar":stunts,
        "refresh":refreshs,
        "fatePuanları":fatepuanları,
        "skillListesi":skillist
    })
    with open (sonname,"w", encoding="utf-16") as outfile:
        json.dump(data,outfile)



"""    print("fin")
    with open(sonname, encoding="utf-16") as aa:
        newdata = json.load(aa)
    print("aaa")"""