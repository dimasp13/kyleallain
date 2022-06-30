# -*- coding: utf-8 -*-
'''
𝐀𝐧𝐭𝐚𝐫𝐞𝐬[𝐃𝐨𝐥𝐥𝐲] 𝙋.𝙆_𝘽𝙊𝙏𝙎 
update 23-11-2021
Thanks to Hello world square
all family famz kebotan
Rework aja sesuka Hati ini juga hasli rewokan kok
ingat kalau hasil rework kamu bagus jangan di jual ya
hargain sc orang saya sendiri hargain yg buat nya
saya cuman me edit ulang
'''

from important import *
from module import *
from setup_args import *
from list_def import *

#=untuk email&passwd nya ada 2 ya, isi dengan email&passwd yang sama=====
listAppType = ['DEPKTOPWIN', 'DEPKTOPMAC', 'IOSIPAD', 'CHROMEOS']
try:
    dollypk = None
    if args.apptype:
        tokenPath = Path('authToken.txt')
        if tokenPath.exists():
            tokenFile = tokenPath.open('r')
        else:
            tokenFile = tokenPath.open('w+')
        savedAuthToken = tokenFile.read().strip()
        authToken = savedAuthToken if savedAuthToken and not args.token else args.token
        idOrToken = authToken if authToken else print("# No one Qr was readed, Lets Scan New QR.")
        try:
            dollypk = LINE("email@gmail.com","pass")  #email & pw
            tokenFile.close()
            tokenFile = tokenPath.open('w+')
            tokenFile.write(dollypk.authToken)
            tokenFile.close()
        except TalkException as talk_error:
            if args.traceback: traceback.print_tb(talk_error.__traceback__)
            sys.exit('(+) Error : %s' % talk_error.reason.replace('_', ' '))
        except Exception as error:
            if args.traceback: traceback.print_tb(error.__traceback__)
            sys.exit('(+) Error : %s' % str(error))
    else:
        for appType in listAppType:
            tokenPath = Path('authToken.txt')
            if tokenPath.exists():
                tokenFile = tokenPath.open('r')
            else:
                tokenFile = tokenPath.open('w+')
            savedAuthToken = tokenFile.read().strip()
            authToken = savedAuthToken if savedAuthToken and not args.token else args.token
            idOrToken = authToken if authToken else print("# No one Qr was readed, Lets Scan New QR.")
            try:
                dollypk = LINE("email@gmail.com","pass")    #email & pw
                tokenFile.close()
                tokenFile = tokenPath.open('w+')
                tokenFile.write(dollypk.authToken)
                tokenFile.close()
                break
            except TalkException as talk_error:
                print ('(+) Error : %s' % talk_error.reason.replace('_', ' '))
                if args.traceback: traceback.print_tb(talk_error.__traceback__)
                if talk_error.code == 1:
                    continue
                sys.exit(1)
            except Exception as error:
                print ('(+) Error : %s' % str(error))
                if args.traceback: traceback.print_tb(error.__traceback__)
                sys.exit(1)
except Exception as error:
    print ('[ System Message ] - Error : %s' % str(error))
    if args.traceback: traceback.print_tb(error.__traceback__)
    sys.exit(1)

if dollypk:
    print ('\n[ Your Auth Token ] -> %s\n' % dollypk.authToken)
else:
    sys.exit('[ System Message ] - Login Failed.')
    
oepoll = OEPoll(dollypk)
call = dollypk
#=================isi aja mid kalian============
creator = ["ued3f3da206923d4e13fe6b07c7d1ce9c"]
owner = ["ued3f3da206923d4e13fe6b07c7d1ce9c"]
admin = ["ued3f3da206923d4e13fe6b07c7d1ce9c"]
staff = ["ued3f3da206923d4e13fe6b07c7d1ce9c"]
mid = dollypk.getProfile().mid
myMid = dollypk.getProfile().mid
Bots = [mid]
AKU = [dollypk]
Team = owner + admin + Bots + staff
Setbot = codecs.open("setting.json","r","utf-8")
Setmain = json.load(Setbot)

welcome = []

responsename = dollypk.getProfile().displayName

settings = {
    "userAgent": ['Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36'],
    "autoblock": False,
    "autoRead": False,
    "welcome": False,
    "javascrift": False,
    "leave": False,
    "expire" : True,
    "nCall" : True,
    "time": time.time(),
    "flood": 0,
    "temp_flood" : False,
    "mid": False,
    "replySticker": False,
    "stickerOn": False,
    "checkContact": False,
    "postEndUrl": False,
    "checkPost": False,
    "setKey": False,
    "restartPoint": False,
    "checkSticker": False,
    "userMentioned": False,
    "listSticker": False,
    "messageSticker": False,
    "changeGroupPicture": [],
    "keyCommand": "",
    "AddstickerTag": {
        "sid": "",
        "spkg": "",
        "status": False
            },
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "myProfile": {
        "displayName": "",
        "coverId": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "mimic": {
        "copy": False,
        "status": False,
        "target": {}
    }, 
    "unsendMessage": False,
    "Picture":False,
    "group":{},
    "changevp": False,
    "changeCover":False,
    "autoLike":{},
    "chatEvent": {},
    "groupPicture":False,
    "changePicture":False,
    "changeProfileVideo": False,
    "ChangeVideoProfilevid":{},
    "ChangeVideoProfilePicture":{},
    "autoJoinTicket":False,
    "SpamInvite":False,
    "displayName": "",
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.200.32.99 Safari/537.36"
    ]
}

wait = {
    "limit": 2,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "postId":False,
    "staff":{},
    "dolly":{},
    "likeOn":{},
    "autoLike": {},
    "status":False,
    "autoBlock": False,
    "Timeline": False,
    "invite":False,
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "Mentionkick":False,
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    'autoJoin':True,
    'autoAdd':True,
    'autoCancel':{"on":True, "members":1},
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "welcomeOn":False,
    "sticker":False,  
    "selfbot":True,
    "AddstickerTag": {
        "sid": "",
        "spkg": "",
        "status": False
            },
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "myProfile": {
            "displayName": "",
            "coverId": "",
            "pictureStatus": "",
            "statusMessage": ""
            },
    "mention":"sider mulu bangsat",
    "Respontag":"jangan tag gw anjing",
    "welcome":"Kam anak anjing",
    "comment":"ᴀᴜᴛᴏʟɪᴋᴇ ʙʏ: \n\n\n\n︻╦̵̵͇̿̿̿̿╤─PANTEK ᵏⁱˡˡᵉʳ",
    "message":"kenapa lu add bangsat\nJangan lupa chat admin\nline.me/ti/p/~nananaaaaa.",
}


read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
mulai = time.time()

liffV1 = {
    "arLiff": True
}

myProfile = {
	"displayName": "",
	"statusMessage": "",
	"pictureStatus": ""
}
try:
    with open("Log_data.json","r",encoding="utf_8_sig") as f:
        msg_dict = json.loads(f.read())
except:
    print("Couldn't read Log data")
    
dollypkProfile = dollypk.getProfile()
myProfile["displayName"] = dollypkProfile.displayName
myProfile["statusMessage"] = dollypkProfile.statusMessage
myProfile["pictureStatus"] = dollypkProfile.pictureStatus

contact = dollypk.getProfile()
backup = dollypk.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus


imagesOpen = codecs.open("image.json","r","utf-8")
images = json.load(imagesOpen)
videosOpen = codecs.open("video.json","r","utf-8")
videos = json.load(videosOpen)
stickersOpen = codecs.open("sticker.json","r","utf-8")
stickers = json.load(stickersOpen)
audiosOpen = codecs.open("audio.json","r","utf-8")
audios = json.load(audiosOpen)
mulai = time.time()

msg_dict = {}
msg_dict1 = {}

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        import urllib,request
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
            
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
    
    
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
    
    
def cloneProfile(mid):
    contact = dollypk.getContact(mid)
    if contact.videoProfile == None:
        dollypk.cloneContactProfile(mid)
    else:
        profile = dollypk.getProfile()
        profile.displayName, profile.statusMessage = contact.displayName, contact.statusMessage
        dollypk.updateProfile(profile)
        pict = dollypk.downloadFileURL('http://dl.profile.line-cdn.net/' + contact.pictureStatus, saveAs="tmp/pict.bin")
        vids = dollypk.downloadFileURL( 'http://dl.profile.line-cdn.net/' + contact.pictureStatus + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = dollypk.getProfileDetail(mid)['result']['objectId']
    dollypk.updateProfileCoverById(coverId)
    
def restoreProfile():
    profile = dollypk.getProfile()
    profile.displayName = settings['myProfile']['displayName']
    profile.statusMessage = settings['myProfile']['statusMessage']
    if settings['myProfile']['videoProfile'] == None:
        profile.pictureStatus = settings['myProfile']['pictureStatus']
        dollypk.updateProfileAttribute(8, profile.pictureStatus)
        dollypk.updateProfile(profile)
    else:
        dollypk.updateProfile(profile)
        pict = dollypk.downloadFileURL('http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'], saveAs="tmp/pict.bin")
        vids = dollypk.downloadFileURL( 'http://dl.profile.line-cdn.net/' + settings['myProfile']['pictureStatus'] + '/vp', saveAs="tmp/video.bin")
        changeVideoAndPictureProfile(pict, vids)
    coverId = settings['myProfile']['coverId']
    dollypk.updateProfileCoverById(coverId)

def allowLiff():
    url = 'https://access.line.me/dialog/api/permissions'
    data = {
        'on': [
            'P',
            'CM'
        ],
        'off': []
    }
    headers = {
        'X-Line-Access': dollypk.authToken,
        'X-Line-Application': dollypk.server.APP_NAME,
        'X-Line-ChannelId': '1602687308',
        'Content-Type': 'application/json'
    }
    requests.post(url, json=data, headers=headers)
def sendTemplate(to, data):
    allowLiff()
    xyz = LiffChatContext(to)
    xyzz = LiffContext(chat=xyz)
    if liffV1["arLiff"]: view = LiffViewRequest('1602687308-GXq4Vvk9', xyzz)
    else: view = LiffViewRequest('1586794970-VKzbNLP7', xyzz)
    token = dollypk.liff.issueLiffView(view)
    url = 'https://api.line.me/message/v3/share'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' % token.accessToken
    }
    data = {"messages":[data]}
    requests.post(url, headers=headers, data=json.dumps(data))
    
def changeProfileVideo(to):
    if settings['changevp']['picture'] == True:
        return dollypk.sendMessage(to, "Foto tidak ditemukan")
    elif settings['changevp']['video'] == True:
        return dollypk.sendMessage(to, "Video tidak ditemukan")
    else:
        path = settings['changevp']['video']
        files = {'file': open(path, 'rb')}
        obs_params = dollypk.genOBSParams({'oid': dollypk.getProfile().mid, 'ver': '2.0', 'type': 'video', 'cat': 'vp.mp4'})
        data = {'params': obs_params}
        r_vp = dollypk.server.postContent('{}/talk/vp/upload.nhn'.format(str(dollypk.server.LINE_OBS_DOMAIN)), data=data, files=files)
        if r_vp.status_code != 201:
            return dollypk.sendMessage(to, "Gagal update profile")
        path_p = settings['changevp']['picture']
        settings['changevp']['status'] = True
        dollypk.updateProfilePicture(path_p, 'vp')

def mentionMembers(to, mids=[]):
    if myMid in mids: mids.remove(myMid)
    parsed_len = len(mids)//20+1
    result = '┏━「 DAFTAR MEMBER 」\n'
    mention = '@fahmiadrn.\n'
    no = 0
    for point in range(parsed_len):
        mentionees = []
        for mid in mids[point*20:(point+1)*20]:
            no += 1
            result += '┣ %i. %s' % (no, mention)
            slen = len(result) - 12
            elen = len(result) + 3
            mentionees.append({'S': str(slen), 'E': str(elen - 4), 'M': mid})
            if mid == mids[-1]:
                result += '┗ https://bit.ly/3fQltZi\n'
        if result:
            if result.endswith('\n'): result = result[:-1]
            dollypk.sendMessage(to, result, {'MENTION': json.dumps({'MENTIONEES': mentionees})}, 0)
        result = ''

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Sider User「{}」\nHaii ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(dollypk.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        dollypk.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        dollypk.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Member Masuk「{}」\nHaii  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = dollypk.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome"]+"\nNama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(dollypk.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        dollypk.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        dollypk.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = dollypk.getAllContactIds()
        gid = dollypk.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"▪jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" wib\n▪Jumblah Group : "+str(len(gid))+"\n▪Teman : "+str(len(teman))+"\n▪Expired : In "+hari+"\n▪Version :Lupa Njir\n▪Creator: 𝐀𝐧𝐭𝐚𝐫𝐞𝐬[𝐃𝐨𝐥𝐥𝐲] \n▪Team:𝙋.𝙆°𝙏𝙀𝘼𝙈𝘽𝙊𝙏𝙎\n\n        Supported by\n▪Aki Devan\n▪ELFOX\n▪Ben[𝐃𝐚𝐢𝐥𝐲 𝐔𝐬𝐞]\n▪IGO[BALWEL]\n▪𝐁𝐓𝐑 𝐟𝐚𝐦𝐢𝐥𝐲\n▪All Member FAMZ KEBOTAN\n\n        𝙋.𝙆°𝘽𝙊𝙏𝙎 2020\n\n▪Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n▪Runtime : \n • "+bot
        dollypk.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        dollypk.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        

def sendMention1(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        dollypk.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        dollypk.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def removeCmd(cmd, text):
	key = Setmain["keyCommand"]
	rmv = len(key + cmd) + 1
	return text[rmv:]

def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            cmd = pesan.replace(settings["keyCommand"],"")
        else:
            cmd = "Undefined command"
    else:
        cmd = text.lower()
    return cmd

        
def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd
 

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "    ☆𝙋.𝙆°𝙏𝙀𝘼𝙈𝘽𝙊𝙏𝙎☆" + "\n" + \
                  "▪"+ key + "pepek[mentionall]\n" + \
                  "▪"+ key + "about\n" + \
                  "▪"+ key + "cvp\n" + \
                  "▪"+ key + "changedualurl:\n" + \
                  "▪"+ key + "ceklimit/cek\n" + \
                  "▪"+ key + "creator\n" + \
                  "▪"+ key + "glist\n" + \
                  "▪"+ key + "ginfo\n" + \
                  "▪"+ key + "settings\n" + \
                  "▪"+ key + "broadcast:\n" + \
                  "▪"+ key + "reboot\n" + \
                  "▪"+ key + "refresh\n" + \
                  "▪"+ key + "kibar\n" + \
                  "▪"+ key + "admin\n" + \
                  "▪"+ key + "admindel\n" + \
                  "▪"+ key + "staff\n" + \
                  "▪"+ key + "staffdell\n" + \
                  "▪" + key + "unsend on/off\n" + \
                  "▪"+ key + "autoblock on/off\n" + \
                  "▪"+ key + "bot on/off\n" + \
                  "▪"+ key + "autojoin on/off\n" + \
                  "▪"+ key + "jointicket on/off\n" + \
                  "▪"+ key + "welcome on/off\n" + \
                  "▪"+ key + "updatebot\n"
    return helpMessage

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if dollypk.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            dollypk.reissueGroupTicket(op.param1)
                            X = dollypk.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            dollypk.updateGroup(X)
                            dollypk.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                except:
                    pass
#====================================================================== PROTECTUPDATEGROUP
        if op.type == 13:
            if mid in op.param3:
                G = dollypk.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    dollypk.acceptGroupInvitation(op.param1)
                else:
                    if wait["autoJoin"] == True:
                        dollypk.acceptGroupInvitation(op.param1)
                    else:
                        pass
            else:
                Inviter = op.param3.replace(" ",'')
                InviterX = Inviter.split(",")
                for taged in InviterX:
                    if taged in wait['blacklist']:
                        try:
                            dollypk.cancelGroupInvitation(op.param1,[taged])                           
                            wait['blacklist'][op.param2] = True
                        except:
                            pass
#____________________________________________________________________
        if op.type == 13:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                if op.param2 in Team:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            dollypk.cancelGroupInvitation(op.param1,[op.param2])
                            dollypk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            if op.param3 not in wait["blacklist"]:
                                dollypk.cancelGroupInvitation(op.param1,[op.param2])
                                dollypk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                if op.param3 not in wait["blacklist"]:
                                    dollypk.cancelGroupInvitation(op.param1,[op.param2])
                                    dollypk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass
                return
#____________________________________________________________________
        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Bots:
                    pass
                ginfo = dollypk.getGroup(op.param1)
                contact = dollypk.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                dollypk.sendImageWithURL(op.param1, image)

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                if op.param2 in Team:
                    pass
                if op.param2 in Team:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        dollypk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            dollypk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                dollypk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass
                return
#____________________________________________________________________
        if op.type == 19:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                if op.param2 in Team:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        dollypk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            dollypk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                dollypk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass
                return
#____________________________________________________________________
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Bots and op.param2 not in owner:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        dollypk.sendMessage(op.param1, wait["message"])
                        
        if op.type == 5:
            if wait['autoBlock'] == True:
                try:
                    usr = dollypk.getContact(op.param2)
                    dollypk.sendMessage(op.param1, "Haii {} Sorry Auto Block , Komen di TL dulu ya kalo akun asli baru di unblock".format(dollypk.displayName))
                    dollypk.talk.blockContact(0, op.param1)
                    wait["Blacklist"][op.param2] = True
                except Exception as e:
                	print (e)
                        
        if op.type == 5:
            print ("[ 5 ] NOTIFIED AUTO BLOCK CONTACT")
            if settings["autoblock"] == True:
                dollypk.sendMessage(op.param1, "Bangsat{} \nSorry auto block tolonglu block balik".format(str(dollypk.getContact(op.param1).displayName)))
                dollypk.blockContact(op.param1)
                dollypk.sendMessage(op.param1, "nyaman nyaman nyaman nyaman nyaman nyaman    ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.👿.👿.👿 ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.\n❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.\n❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.".format(str(dollypk.getContact(op.param1).displayName)))
                dollypk.blockContact(op.param1)
                    
        if op.type == 55:
            if op.param1 in read["readPoint"]:
                if op.param2 not in read["readMember"][op.param1]:
                    read["readMember"][op.param1].append(op.param2)
                            
        
        
        if op.type == 55:
            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = dollypk.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n " + Name
                        teambotmaxZ={'previewUrl': "http://dl.profile.line-cdn.net/"+dollypk.getContact(op.param2).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': '𝙋.𝙆°𝙏𝙀𝘼𝙈𝘽𝙊𝙏𝙎', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': dollypk.getContact(op.param2).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.line.naver.jp/os/p/"+op.param2,'MSG_SENDER_NAME':  dollypk.getContact(op.param2).displayName,}
                        dollypk.sendMessage(op.param1, dollypk.getContact(op.param2).displayName, teambotmaxZ, 19)


        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                if op.param2 in Bots:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                if op.param2 in Team:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        dollypk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            dollypk.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            try:
                                dollypk.kickoutFromGroup(op.param1,[op.param2])
                            except:
                                pass
                return

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = dollypk.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        contact = dollypk.getContact(op.param2)
                        image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                        dollypk.sendImageWithURL(op.param1, image)
                        
        if op.type == 65:
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = dollypk.getGroup(at)
                                ryan = dollypk.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "📧Gambar Dihapus 📧\n Pengirim : "
                                ret_ = " Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                dollypk.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                dollypk.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = dollypk.getGroup(at)
                                ryan = dollypk.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "📧 Pesan Dihapus 📧\n"
                                ret_ += " Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\n Pesannya : {}".format(str(msg_dict[msg_id]["text"]))
                                dollypk.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = dollypk.getGroup(at)
                                ryan = dollypk.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "📧 Sticker Dihapus 📧\n"
                                ret_ += " Pengirim : {}".format(str(ryan.displayName))
                                ret_ += "\n Nama Grup : {}".format(str(ginfo.name))
                                ret_ += "\n Waktu Ngirim : {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                dollypk.sendMessage(at, str(ret_))
                                dollypk.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)
                              
        if op.type == 26:           
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    dollypk.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 16:
                  if msg.toType in (2,1,0):
                     try:
                         mat = msg.contentMetadata["postEndUrl"].split('userMid=')[1].split('&postId=')
                         dollypk.likePost(mat[0], mat[1], 1003)
                         dollypk.createComment(mat[0], mat[1], "Share mulu anjing\nyaudah gw ikutan dah\n\n︻╦̵̵͇̿̿̿̿╤─PANTEK ᵏⁱˡˡᵉʳ \nHadir di mari\n🔹️Ready all bot line\n🔹️coin line\n🔹️follower Instagram\n🔹️Ready vps\nkepoin aja\nline.me/ti/p/~antares_zonk\nline.me/ti/p/~Justfake__")
                     except Exception as e:
                         dollypk.sendMessage(msg.to, str(e))  
                            
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 2:
               if msg.toType == 0:
                    to = msg._from
               elif msg.toType == 2:
                    to = msg.to
               if msg.contentType == 16:
                    if wait["Timeline"] == True:
                            ret_ = "「 ᴅᴇᴛᴀɪʟ ᴘᴏsᴛɪɴɢᴀɴ 」"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = dollypk.getContact(sender)
                                auth = "\n• 🔹️༓ᴘᴇɴᴜʟɪs : {}".format(str(contact.displayName))
                            else:
                                auth = "\n• 🔹️ ༓ᴘᴇɴᴜʟɪs : {}".format(str(msg.contentMetadata["serviceName"]))
                            ret_ += auth
                            if "stickerId" in msg.contentMetadata:
                                stck = "\n• 🔹️༓sᴛɪᴄᴋᴇʀ : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n• 🔹️༓ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\n• 🔹️༓Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n• 🔹️༓Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\n• 🔹️༓Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                    ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\n• 🔹️༓Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\n• 🔹️༓Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "text" in msg.contentMetadata:
                                text = "\n• 🔹️༓Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                purl = "\n• 🔹️༓Post URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += purl
                                ret_ += text
                                url = msg.contentMetadata['postEndUrl']
                            dollypk.sendMessage(to, str(ret_))
                            dollypk.likePost(purl[25:58], purl[66:], likeType=1005)
                            dollypk.createComment(purl[25:58], purl[66:], wait["comment"])
        
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    dollypk.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\nãLink Stickerã" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    dollypk.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = dollypk.getContact(msg.contentMetadata["mid"])
                        path = dollypk.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        dollypk.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        dollypk.sendImageWithURL(msg.to, image)
                        
               if msg.contentType == 0:
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 1:
                    path = dollypk.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambarnya dibawah',"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n Sticker Info "
                   ret_ += "\n Sticker ID : {}".format(stk_id)
                   ret_ += "\n Sticker Version : {}".format(stk_ver)
                   ret_ += "\n Sticker Package : {}".format(pkg_id)
                   ret_ += "\n Sticker Url : line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = dollypk.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 7:
                if settings["stickerOn"] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        r = s.get("https://store.line.me/stickershop/product/{}/id".format(urllib.parse.quote(pkg_id)))
                        soup = BeautifulSoup(r.content, 'html5lib')
                        data = soup.select("[dollypkass~=mdBtn01Txt]")[0].text
                        if data == 'Lihat Produk Lain':
                            ret_ = " Sticker Info "
                            ret_ += "\n🔴 STICKER ID : {}".format(stk_id)
                            ret_ += "\n🔴 STICKER PACKAGES ID : {}".format(pkg_id)
                            ret_ += "\n🔴 STICKER VERSION : {}".format(stk_ver)
                            ret_ += "\n🔴STICKER URL : line://shop/detail/{}".format(pkg_id)
                            dollypk.sendMessage(msg.to, str(ret_))
                            query = int(stk_id)
                            if type(query) == int:
                               data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                               path = dollypk.downloadFileURL(data)
                               dollypk.sendImage(msg.to,path)
                        else:
                            ret_ = " Sticker Info "
                            ret_ += "\n🔴 PRICE : "+soup.findAll('p', attrs={'dollypkass':'mdCMN08Price'})[0].text
                            ret_ += "\n🔴 AUTHOR : "+soup.select("a[href*=/stickershop/author]")[0].text
                            ret_ += "\n🔴 STICKER ID : {}".format(str(stk_id))
                            ret_ += "\n🔴 STICKER PACKAGES ID : {}".format(str(pkg_id))
                            ret_ += "\n🔴 STICKER VERSION : {}".format(str(stk_ver))
                            ret_ += "\n🔴 STICKER URL : line://shop/detail/{}".format(str(pkg_id))
                            ret_ += "\n🔴 DESCRIPTION :\n"+soup.findAll('p', attrs={'dollypkass':'mdCMN08Desc'})[0].text
                            dollypk.sendMessage(msg.to, str(ret_))
                            query = int(stk_id)
                            if type(query) == int:
                               data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                               path = dollypk.downloadFileURL(data)
                               dollypk.sendImage(msg.to,path)
                      
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    dollypk.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = dollypk.getContact(msg.contentMetadata["mid"])
                        path = dollypk.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        dollypk.sendMessage(msg.to,"  Contact Info \n🔹️ Nama : " + msg.contentMetadata["displayName"] + "\n MID : " + msg.contentMetadata["mid"] + "\n Status Msg : " + contact.statusMessage + "\n Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        dollypk.sendImageWithURL(msg.to, image)
               if msg.contentType == 13:
                if msg._from in owner or msg._from in admin or msg._from in mid:
                  if wait["invite"] == True:
                    msg.contentType = 0
                    contact = dollypk.getContact(msg.contentMetadata["mid"])
                    invite = msg.contentMetadata["mid"]
                    groups = dollypk.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if invite in wait["blacklist"]:
                            dollypk.sendMessage(msg.to, "🔹️ke BL bro... cban dlu baru invite lagi🔹️")
                            break
                        else:
                            targets.append(invite)
                    if targets == []:
                        pass
                    else:
                         for target in targets:
                             try:
                                  dollypk.findAndAddContactsByMid(target)
                                  dollypk.inviteIntoGroup(msg.to,[target])
                                  ryan = dollypk.getContact(target)
                                  zx = ""
                                  zxc = ""
                                  zx2 = []
                                  xpesan =  " Sukses Invite \nNama "
                                  ret_ = "Ketik Invite off jika sudah done"
                                  ry = str(ryan.displayName)
                                  pesan = ''
                                  pesan2 = pesan+"@x\n"
                                  xlen = str(len(zxc)+len(xpesan))
                                  xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                  zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                  zx2.append(zx)
                                  zxc += pesan2
                                  text = xpesan + zxc + ret_ + ""
                                  dollypk.sendMessage(msg.to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                  wait["invite"] = False
                                  break
                             except:
                                  dollypk.sendMessage(msg.to,"Anda terkena limit")
                                  wait["invite"] = False
                                  break
                            
        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Bots:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          dollypk.kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              dollypk.kickoutFromGroup(msg.to, [msg._from])
                          except:
                              pass
               if msg.contentMetadata and 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["detectMention"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           TEAMBOTPROTECT = dollypk.getContact(msg._from)
                           sendMention1(msg.to, TEAMBOTPROTECT.mid, "", wait["Respontag"])
                           dollypk.sendMessage(msg.to, None, contentMetadata={"STKID":"52002769","STKPKGID":"11537","STKVER":"1"}, contentType=7)
                           break
               if msg.contentMetadata and 'MENTION' in msg.contentMetadata.keys() != None:
                if msg._from not in Bots:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Bots:
                           dollypk.mentiontag(msg.to,[msg._from])
                           dollypk.sendMessage(msg.to, "No tag me....")
                           dollypk.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    dollypk.sendMessage(msg.to,"Cek ID Sticker\n\nSTKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    dollypk.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = dollypk.getContact(msg.contentMetadata["mid"])
                        path = dollypk.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        dollypk.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        dollypk.sendImageWithURL(msg.to, image)
                        
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    dollypk.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    dollypk.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = dollypk.getContact(msg.contentMetadata["mid"])
                        path = dollypk.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        dollypk.sendMessage(msg.to,"Nama : " + msg.contentMetadata["displayName"] + "\nMID : " + msg.contentMetadata["mid"] + "\nStatus Msg : " + contact.statusMessage + "\nPicture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        dollypk.sendImageWithURL(msg.to, image)
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in owner or msg._from in admin or msg._from in mid:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        dollypk.sendMessage(msg.to,"Already in bot")
                        wait["addbots"] = False
                    else:
                        target = msg.contentMetadata["mid"]
                        dollypk.findAndAddContactsByMid(target)
                        midd = (target)
                        Bots.append(midd)
                        dollypk.sendMessage(msg.to, dollypk.getContact(target).displayName + " has been promoted Bot by " + dollypk.getContact(msg._from).displayName)
                        target = {}
                        wait["addbots"] = False
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        target = msg.contentMetadata["mid"]
                        midd = (target)
                        Bots.remove(midd)
                        dollypk.sendMessage(msg.to, dollypk.getContact(target).displayName + " has been Expel Bot by " + dollypk.getContact(msg._from).displayName)
                        target = {}
                        wait["dellbots"] = False
                    else:
                        wait["dellbots"] = False
                        dollypk.sendMessage(msg.to,"Nothing in bot")
#ADD STAFF
                 if msg._from in owner or msg._from in admin or msg._from in mid:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        dollypk.sendMessage(msg.to,"Already in stafflist")
                        wait["addstaff"] = False
                    else:
                        target = msg.contentMetadata["mid"]
                        dollypk.findAndAddContactsByMid(target)
                        midd = (target)
                        staff.append(midd)
                        dollypk.sendMessage(msg.to, dollypk.getContact(target).displayName + " has been promoted Staff by " + dollypk.getContact(msg._from).displayName)
                        target = {}
                        wait["addstaff"] = False
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        target = msg.contentMetadata["mid"]
                        midd = (target)
                        staff.remove(midd)
                        dollypk.sendMessage(msg.to, dollypk.getContact(target).displayName + " has been Expel Staff by " + dollypk.getContact(msg._from).displayName)
                        target = {}
                        wait["dellstaff"] = False
                    else:
                        wait["dellstaff"] = False
                        dollypk.sendMessage(msg.to,"Nothing in staff")
#ADD ADMIN
                 if msg._from in owner or msg._from in admin or msg._from in mid:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        dollypk.sendMessage(msg.to,"Already in Admin")
                        wait["addadmin"] = False
                    else:
                        target = msg.contentMetadata["mid"]
                        dollypk.findAndAddContactsByMid(target)
                        midd = (target)
                        admin.append(midd)
                        dollypk.sendMessage(msg.to, dollypk.getContact(target).displayName + " has been promoted Admin by " + dollypk.getContact(msg._from).displayName)
                        target = {}
                        wait["addadmin"] = False
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        target = msg.contentMetadata["mid"]
                        midd = (target)
                        admin.remove(midd)
                        dollypk.sendMessage(msg.to, dollypk.getContact(target).displayName + " has been Expel Admin by " + dollypk.getContact(msg._from).displayName)
                        target = {}
                        wait["delladmin"] = False
                    else:
                        wait["delladmin"] = False
                        dollypk.sendMessage(msg.to,"Nothing in admin")
#ADD BLACKLIST
                 if msg._from in owner or msg._from in admin or msg._from in mid:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        dollypk.sendMessage(msg.to,"Already in blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        dollypk.sendMessage(msg.to,"Succes add to blacklist")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        dollypk.sendMessage(msg.to,"Succes delete blacklist")
                    else:
                        wait["dblacklist"] = True
                        dollypk.sendMessage(msg.to,"Nothing in blacklist")
#TALKBAN
                 if msg._from in owner or msg._from in admin or msg._from in mid:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        dollypk.sendMessage(msg.to,"Already in Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        dollypk.sendMessage(msg.to,"Succes add to Talkban")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        dollypk.sendMessage(msg.to,"Succes delete Talkban")
                    else:
                        wait["Talkdblacklist"] = True
                        dollypk.sendMessage(msg.to,"Nothing in Talkban")
#UPDATE FOTO
               if msg.contentType == 1:
                  if msg._from in owner or msg._from in admin or msg._from in mid:
                     if settings["Addimage"]["status"] == True:
                         path = dollypk.downloadObjectMsg(msg.id)
                         images[settings["Addimage"]["name"]] = str(path)
                         f = codecs.open("image.json","w","utf-8")
                         json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                         dollypk.sendMessage(msg.to, "ᴅᴏɴᴇ ɢᴀᴍʙᴀʀ {}".format(str(settings["Addimage"]["name"])))
                         settings["Addimage"]["status"] = False
                         settings["Addimage"]["name"] = ""
               if msg.contentType == 2:
                  if msg._from in owner or msg._from in admin or msg._from in mid:
                     if settings["Addvideo"]["status"] == True:
                         path = dollypk.downloadObjectMsg(msg.id)
                         videos[settings["Addvideo"]["name"]] = str(path)
                         f = codecs.open("video.json","w","utf-8")
                         json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                         dollypk.sendMessage(msg.to, "Berhasil menambahkan video {}".format(str(settings["Addvideo"]["name"])))
                         settings["Addvideo"]["status"] = False
                         settings["Addvideo"]["name"] = ""
               if msg.contentType == 7:
                  if msg._from in owner or msg._from in admin or msg._from in mid:
                     if settings["Addsticker"]["status"] == True:
                         stickers[settings["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                         f = codecs.open("sticker.json","w","utf-8")
                         json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                         dollypk.sendMessage(msg.to, "ᴅᴏɴᴇ sᴛɪᴄᴋᴇʀ {}".format(str(settings["Addsticker"]["name"])))
                         settings["Addsticker"]["status"] = False
                         settings["Addsticker"]["name"] = ""
               if msg.contentType == 3:
                  if msg._from in owner or msg._from in admin or msg._from in mid:
                     if settings["Addaudio"]["status"] == True:
                         path = dollypk.downloadObjectMsg(msg.id)
                         audios[settings["Addaudio"]["name"]] = str(path)
                         f = codecs.open("audio.json","w","utf-8")
                         json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                         dollypk.sendMessage(msg.to, "Berhasil menambahkan mp3 {}".format(str(settings["Addaudio"]["name"])))
                         settings["Addaudio"]["status"] = False
                         settings["Addaudio"]["name"] = ""
               if msg.contentType == 0:
                  if settings["autoRead"] == True:
                      dollypk.sendChatChecked(msg.to, msg_id)
                  if text is None:
                      return
                  else:
                         for sticker in stickers:
                            if text.lower() == sticker:
                               sid = stickers[text.lower()]["STKID"]
                               spkg = stickers[text.lower()]["STKPKGID"]
                               dollypk.sendSticker(to, spkg, sid)
                         for image in images:
                            if text.lower() == image:
                               dollypk.sendImage(msg.to, images[image])
                         for audio in audios:
                            if text.lower() == audio:
                               dollypk.sendAudio(msg.to, audios[audio])
                         for video in videos:
                            if text.lower() == video:
                               dollypk.sendVideo(msg.to, videos[video])
               if msg.contentType == 13:
                 if msg._from in owner or msg._from in admin or msg._from in mid:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        sendTextTemplate1(msg.to,"Already in bot")
                        wait["addbots"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        sendTextTemplate1(msg.to,"Succes add bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        sendTextTemplate1(msg.to,"Succes delete bot")
                    else:
                        wait["dellbots"] = True
                        sendTextTemplate1(msg.to,"Nothing in bot")
                        
               if msg.contentType == 1:
                 if msg._from in owner or msg._from in admin or msg._from in mid:
                    if Setmain["Addimage"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = dollypk.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            path = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % Setmain["Img"])
                            with open(path, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            dollypk.sendMessage(msg.to, "Succes add picture")
                        Setmain["Img"] = {}
                        Setmain["Addimage"] = False
                      
               if msg.contentType == 2:
                   if msg._from in owner or msg._from in admin or msg._from in mid:
                       if msg._from in settings["ChangeVideoProfilevid"]:
                            settings["ChangeVideoProfilePicture"][msg._from] = True
                            del settings["ChangeVideoProfilevid"][msg._from]
                            dollypk.downloadObjectMsg(msg_id,'path','video.mp4')
                            dollypk.sendMessage(msg.to,"Send gambarnya...")
                            
               if msg.contentType == 1:
                   if msg._from in owner or msg._from in admin or msg._from in mid:
                       if msg._from in settings["ChangeVideoProfilePicture"]:
                            del settings["ChangeVideoProfilePicture"][msg._from]
                            dollypk.downloadObjectMsg(msg_id,'path','image.jpg')
                            dollypk.nadyacantikimut('video.mp4','image.jpg')
                            dollypk.sendMessage(msg.to,"Change Video Profile Success!!!")
                            
               if msg.contentType == 2:
               	if settings["changevp"] == True:
               		contact = dollypk.getProfile()
               		path = dollypk.downloadFileURL("https://obs.line-scdn.net/{}".format(contact.pictureStatus))
               		path1 = dollypk.downloadObjectMsg(msg_id)
               		settings["changevp"] = False
               		changeVideoAndPictureProfile(path, path1)
               		dollypk.sendMessage(to, "ᴅᴏɴᴇ vɪᴅᴇᴏ ᴘʀᴏғɪʟᴇ")

               if msg.toType == 2:
                 if msg._from in owner or msg._from in admin or msg._from in staff:
                   if settings["groupPicture"] == True:
                     path = dollypk.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     dollypk.updateGroupPicture(msg.to, path)
                     dollypk.sendMessage(msg.to, "Succes change pict group")

               if msg.contentType == 1:
                   if msg._from in owner or msg._from in admin or msg._from in mid:
                       if mid in Setmain["PKfoto"]:
                            path = dollypk.downloadObjectMsg(msg_id)
                            del Setmain["PKfoto"][mid]
                            dollypk.updateProfilePicture(path)
                            dollypk.sendMessage(msg.to,"Succes change pict")

               if msg.contentType == 0:
                    if Setmain["autoRead"] == True:
                        dollypk.sendChatChecked(msg.to, msg_id)
                        print ("Read")
                    if text is None:
                        return
                    else:
                        cmd = command(text)

                        if cmd == ".help":
                                      Help = help()
                                      data = {
                                                             "type": "text",
                                                             "text": "{}".format(str(Help)),
                                                             "sentBy": {
                                                             "label": "{}".format(dollypk.getContact(myMid).displayName),
                                                             "iconUrl": "https://obs.line-scdn.net/{}".format(dollypk.getContact(myMid).pictureStatus),
                                                             "linkUrl": "https://line.me/ti/p/~nananaaaaa.",
                                                             }
                                                       }
                                      sendTemplate(to, data)
                                                                                       
                        if cmd == "chatbot on":
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["selfbot"] = True
                                dollypk.sendMessage(msg.to, "Chatbot has been enable")
                                
                        elif cmd == "chatbot off":
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["selfbot"] = False
                                dollypk.sendMessage(msg.to, "Chatbot has been disable")
                                            
                   
                        if cmd == "cek":
                            if msg._from in admin or msg._from in owner:
                               try:dollypk.inviteIntoGroup(to, ["u0120d12ccc0e2b89703a26684b190212"]);has = "OK"
                               except:has = "NOT"
                               try:dollypk.kickoutFromGroup(to, ["u0120d12ccc0e2b89703a26684b190212"]);has1 = "OK"
                               except:has1 = "NOT"
                               if has == "OK":sil = "sangek"
                               else:sil = "lemas"
                               if has1 == "OK":sil1 = "sangek"
                               else:sil1 = "lemas"
                               dollypk.sendMessage(to, "Status:\nKick : {} \nInvite : {}".format(sil1,sil))

                        if cmd == "ceklimit":
                          if wait["selfbot"] == True:
                            if msg._from in owner:
                               if msg.toType != 2: return dollypk.sendMessage(to, 'use this command only on group chat')
                               cek = {"kick": "", "invite": "", "cancel": "", "add": ""}
                               try:dollypk.cancelGroupInvitation(to, ["u0448ea6ec32bdb3fb4b21805f9487b91"]);cek["cancel"] = "「✔️」"
                               except:cek["cancel"] = "「❌」"
                               time.sleep(0.8)
                               try:dollypk.kickoutFromGroup(to, [myMid]);cek["kick"] = "「✔️」"
                               except:cek["kick"] = "「❌」"
                               time.sleep(0.8)
                               try:dollypk.inviteIntoGroup(to, [myMid]);cek["invite"] = "「✔️」"
                               except:cek["invite"] = "「❌」"
                               time.sleep(0.8)
                               idben = dollypk.getProfile().userid
                               try:dollypk.findContactsByUserid(idben);cek["add"] = "「✔️」"
                               except:cek["add"] = "「❌」"
                               res = "Status :"
                               res += '\n   - %s Kick' % cek["kick"]
                               res += '\n   - %s Invite' % cek["invite"]
                               res += '\n   - %s Cancel' % cek["cancel"]
                               res += '\n   - %s Add' % cek["add"]
                               dollypk.sendMessage(to, res)
                               
                        elif cmd.startswith(".gettoken"):
                             if msg._from in owner or msg._from in admin or msg._from in staff:
                                try:
                                    sep = text.split(" ")
                                    auth = text.replace(sep[0] + " ","")
                                    r = requests.get("http://beta.moe.team/api/generateAuthToken?auth={}&apikey=f3XdIQlolsA7iJnxF3DADnkYye5IuxtFLqVsFxvcxQBSe2qDraEy7un8ZD6xxiTu".format(str(auth)))
                                    data=r.text
                                    data=json.loads(r.text)
                                    ret_ = "「 Token Primery 」"
                                    ret_ += "\n\nStatus : "+str(data["message"])
                                    ret_ += "\nToken : "+str(data["result"])
                                    dollypk.sendMessage(to, ret_)
                                except Exception as error:
                                    dollypk.sendMessage(to, str(error))
                               
                     
                        elif cmd == "settings":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)                                
                                md = "   ☆Status SelfbotS☆\n"                                
                                if wait["sticker"] == True: md+="▪[ON] sᴛɪᴄᴋᴇʀ✔️\n"
                                else: md+="▪[OFF] sᴛɪᴄᴋᴇʀ❌\n"
                                if wait["contact"] == True: md+="▪[ON] ᴄᴏɴᴛᴀᴄᴛ✔️\n"
                                else: md+="▪[OFF] ᴄᴏɴᴛᴀᴄᴛ❌\n"
                                if wait["detectMention"] == True: md+="▪[ON] ʀᴇsᴘᴏɴ✔️\n"
                                else: md+="▪[OFF] ʀᴇsᴘᴏɴ❌\n"
                                if wait["autoJoin"] == True: md+="▪[ON] ᴀᴜᴛᴏᴊᴏɪɴ✔️\n"
                                else: md+="▪[OFF] ᴀᴜᴛᴏᴊᴏɪɴ❌\n"
                                if settings["autoJoinTicket"] == True: md+="▪[ON] ᴊᴏɪɴᴛɪᴄᴋᴇᴛ✔️\n"
                                else: md+="▪[OFF] ᴊᴏɪɴᴛɪᴄᴋᴇᴛ❌\n"
                                if wait["autoBlock"] == True: md+="▪[ON] autoblock ✔️\n"
                                else: md+="▪[OFF] autoblock ❌\n"
                                if settings["unsendMessage"] == True: md+="▪[ON] ᴜɴsᴇɴᴅ✔️\n"
                                else: md+="▪[OFF] ᴜɴsᴇɴᴅ❌\n"
                                if wait["autoAdd"] == True: md+="▪[ON] ᴀᴜᴛᴏᴀᴅᴅ✔️\n"
                                else: md+="▪[OFF] ᴀᴜᴛᴏᴀᴅᴅ❌\n"
                                if msg.to in welcome: md+="▪[ON] ᴡᴇʟᴄᴏᴍᴇ✔️\n"
                                else: md+="▪[OFF] ᴡᴇʟᴄᴏᴍᴇ❌\n"
                                if wait["autoLeave"] == True: md+="▪[ON] ᴀᴜᴛᴏʟᴇᴀᴠᴇ✔️\n"
                                else: md+="▪[OFF] ᴀᴜᴛᴏʟᴇᴀᴠᴇ❌\n"
                                dollypk.sendMessage(msg.to, md+"\n│ᴛᴀɴɢɢᴀʟ : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n│ᴊᴀᴍ  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")   
                                
                          
                        elif cmd == "creator" or text.lower() == 'creator':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                dollypk.sendMessage(msg.to,"Creator Kami Yang receh nya minta ampun")
                                ma = ""
                                for i in creator:
                                    ma = dollypk.getContact(i)
                                    dollypk.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == ".about" or cmd == "about":
                          if wait["selfbot"] == True:
                               sendMention(msg.to, sender, "▪Info P.K_BotS\n\n")
                               dollypk.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "me" or text.lower() == 'me':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': msg._from}
                               dollypk.sendMessage(msg.to, None, contentMetadata={'mid': msg._from}, contentType=13)
                               
                        elif text.lower() == "bot":
                               dollypk.sendMessage(msg.to, "Mampir lah wkwk\n\n 	https://bit.ly/3fQltZi")  	
	                               
                        elif text.lower() == "kam":
                               dollypk.sendMessage(msg.to, "┏━━━━•❅•°•❈•°•❅•━━━━┓\n         welcome anak anjing\n           gk suka cabut sana\n┗━━━━•❅•°•❈•°•❅•━━━━┛")                              
 
                        elif cmd == "creator":
                          if wait["selfbot"] == True:
                               dollypk.sendMessage(msg.to, "Ni Creator kami yang receh nya minta ampun")
                               dollypk.sendContact(to, "u3a4cc9a5d0da4077d7dc6cd4f405517c")
                               
                        elif cmd == "promo" or text.lower() == 'order':
                          if wait["selfbot"] == True:                            
                               dollypk.sendMessage(msg.to, "    ☆OPEN ORDER☆\n☆Protect by golang\n▪200K = 7 Bot\n▪150K = 5 bot\n▪Nambah assis 25k/bot\n▪bisa order 1 atau 2 bot=30k/bot\n☆Bot Banchat setelah pemakaian 1 minggu kalian ganti sndri 5K/Bot. 🤪\n\n☆Protect Cl Bot by python\n▪100k = 5 Bot\n\n☆Protect asis 6 bot\n▪70K/bulan\n\n▪Pembuatan Bot kuis=30K/Bulan\nSoal,Nick Bot Atas nama kalian. Bot kuis di lengkapi mention member alias Tagall\n\n☆Open Order\n▪Sc War/protect CL 𝐕¹\n▪Thread\n▪Harga Pelajar \n\n☆Open Order\n▪Sc War/protect CL 𝐕²\n▪Footer Reply\n▪Thread\n▪kick dan bypass (JS)\n▪Harga Kepoin aja murah kok\n\n☆Open Jasa protect Room\n▪30k= 1 Room/bulan for admin [5 Bot by golang]\n\n☆Open order token primary\n▪7K / token saling add\n▪ pembuatan 1 nomer 1 token\n\n🔹️VPS LINODE \n1 Core 2GB = 50k \n2 Core 4GB = 110K \n4 Core 8GB = 210K \n6 Core 16GB = 360K\n\nContact person\n\nline.me/ti/p/~nananaaaaa.\n\nline.me/ti/p/~sepikurindu_\n\nline.me/ti/p/~gajebangetsi\n\n▪PC OA Juga Bisa\nhttps://lin.ee/69O2AWf")
                               dollypk.sendContact(to, "u3a4cc9a5d0da4077d7dc6cd4f405517c")
                               dollypk.sendContact(to, "ub42d40a08a3920ec7f6268af5f1c9bb6")
                               
                        elif cmd == "virtex":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               dollypk.sendMessage(msg.to, "nyaman nyaman nyaman nyaman nyaman nyaman    ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.👿.👿.👿 ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.\n❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.\n❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.")                               

                        elif ("Get id " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = dollypk.getContact(key1)
                               dollypk.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               dollypk.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Profile " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = dollypk.getContact(key1)
                               dollypk.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMid : " +key1+"\nStatus Msg"+str(mi.statusMessage))
                               dollypk.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(dollypk.getContact(key1)):
                                   dollypk.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   dollypk.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif cmd == "mybot":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': mid}
                               dollypk.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                              ginvited = dollypk.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      dollypk.rejectGroupInvitation(gid)
                                  dollypk.sendMessage(to, "Succes reject {} ".format(str(len(ginvited))))
                              else:
                                  dollypk.sendMessage(to, "Nothing")

                        elif text.lower() == "rchat":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               try:
                                   dollypk.removeAllMessages(op.param2)
                                   dollypk.sendMessage(msg.to,"Done")
                               except:
                                   pass

                        elif cmd.startswith("bcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = dollypk.getGroupIdsJoined()
                               for group in saya:
                                   dollypk.sendMessage(group,"Bcast 🔹️︻╦̵̵͇̿̿̿̿╤─PANTEK ᵏⁱˡˡᵉʳ \n" + str(pesan))
                                                           
                        elif text.lower() == "cek name":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               dollypk.sendMessage(msg.to, "sᴛᴀᴛᴜs ɴᴀᴍᴇ \n\n" + str(Setmain["keyCommand"]) + " ")
                               
                        elif cmd.startswith("name: "):
                          if msg._from in owner or msg._from in admin or msg._from in mid:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = dollypk.getProfile()
                                profile.displayName = string
                                dollypk.updateProfile(profile)
                                dollypk.sendMessage(msg.to,"Nama Baru " + string + "")  

                        elif text.lower() == "reset ɴame":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               Setmain["keyCommand"] = ""
                               dollypk.sendMessage(msg.to, "Done silahkan di cek")

                        elif cmd == "reboot":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               dollypk.sendMessage(msg.to, "Sabar lah Kau")
                               Setmain["restartPoint"] = msg.to
                               restartBot(0.1)
                               dollypk.sendMessage(msg.to, "Done Restart njing ya")
                            
                        elif cmd == "time":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               eltime = time.time() - mulai
                               bot = "Active " +waktu(eltime)
                               dollypk.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in owner or msg._from in admin or msg._from in staff:
                            try:
                                G = dollypk.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(dollypk.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                dollypk.sendMessage(msg.to, "Group Info\n\nNama Group : {}".format(G.name)+ "\nID Group : {}".format(G.id)+ "\nPembuat : {}".format(G.creator.displayName)+ "\nWaktu Dibuat : {}".format(str(timeCreated))+ "\nJumlah Member : {}".format(str(len(G.members)))+ "\nJumlah Pending : {}".format(gPending)+ "\nGroup Qr : {}".format(gQr)+ "\nGroup Ticket : {}".format(gTicket))
                                dollypk.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                dollypk.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                dollypk.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup: "):
                          if msg._from in owner or msg._from in admin or msg._from in mid:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = dollypk.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = dollypk.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(dollypk.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += "GROUP INFO \n"
                                ret_ += "\nNama Group : {}".format(G.name)
                                ret_ += "\nID Group : {}".format(G.id)
                                ret_ += "\nPembuat : {}".format(gCreator)
                                ret_ += "\nWaktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\nJumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\nJumlah Pending : {}".format(gPending)
                                ret_ += "\nGroup Qr : {}".format(gQr)
                                ret_ += "\nGroup Ticket : {}".format(gTicket)
                                ret_ += ""
                                dollypk.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem: "):
                          if msg._from in owner or msg._from in admin or msg._from in mid:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = dollypk.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = dollypk.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " ""+ str(no) + ". " + mem.displayName
                                dollypk.sendMessage(to,"Group Name : " + str(G.name) + " \n\nMember List \n" + ret_ + "\n\nTotal %i Members" % len(G.members))
                            except:
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in owner or msg._from in admin or msg._from in mid:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = dollypk.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = dollypk.getGroup(i)
                                if ginfo == group:
                                    dollypk.leaveGroup(i)
                                    dollypk.sendMessage(msg.to,"Leave in groups " +str(ginfo.name))

                        elif cmd == "flist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               ma = ""
                               a = 0
                               gid = dollypk.getAllContactIds()
                               for i in gid:
                                   G = dollypk.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.displayName+ "\n"
                               dollypk.sendMessage(msg.to,"🔹️FRIEND LIST\n\n"+ma+"\nTotal"+str(len(gid))+"Friends")
                               
                        
                        elif cmd == "glist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               ma = ""
                               a = 0
                               gid = dollypk.getGroupIdsJoined()
                               for i in gid:
                                   G = dollypk.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "" + str(a) + ". " +G.name+ "\n"
                               dollypk.sendMessage(msg.to,"🔹️GROUP LIST\n\n"+ma+"\nTotal"+str(len(gid))+" Groups")

                        elif cmd == "curl":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                if msg.toType == 2:
                                   X = dollypk.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   dollypk.updateGroup(X)
                                   dollypk.sendMessage(msg.to, "Url closed")

                        elif cmd == "ourl":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                if msg.toType == 2:
                                   x = dollypk.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      dollypk.updateGroup(x)
                                   gurl = dollypk.reissueGroupTicket(msg.to)
                                   dollypk.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#                                                     
                        elif cmd.startswith("unsend99 "):
                          if msg._from in owner or msg._from in admin or msg._from in mid:
                            args = cmd.replace("unsend99 ","")
                            mes = 0
                            try:
                                mes = int(args[1])
                            except:
                                mes = 1
                            M = dollypk.getRecentMessagesV2(to, 101)
                            MId = []
                            for ind,i in enumerate(M):
                                if ind == 0:
                                    pass
                                else:
                                    if i._from == dollypk.profile.mid:
                                        MId.append(i.id)
                                        if len(MId) == mes:
                                            break
                            def unsMes(id):
                                dollypk.unsendMessage(id)
                            for i in MId:
                                thread1 = threading.Thread(target=unsMes, args=(i,))
                                thread1.start()
                                thread1.join()
                            dollypk.sendMessage(msg.to, "Success unsend {} message".format(len(MId))) 
 #===========BOT UPDATE SC NEW============#                                                                  
                        elif cmd == "changedualurl":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                dollypk.sendMessage(msg.to,"Send Picture")

                        elif cmd == "upbot":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                settings["changePicture"] = True
                                dollypk.sendMessage(msg.to,"Send Picture")
                                
                        elif cmd == "upfoto":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                Setmain["PKfoto"][mid] = True
                                dollypk.sendMessage(msg.to,"Send picture")
                                
                        elif cmd == "cvp":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                settings["ChangeVideoProfilevid"][msg._from] = True
                                dollypk.sendMessage(msg.to,"Share video buruan")
                                
                          elif cmd.startswith("changedualurl: "):
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                sep = msg.text.split(" ")
                                url = msg.text.replace(sep[0] + " ","")                            
                                dollypk.downloadFileURL(url,'path','video.mp4')
                                settings["ChangeVideoProfilePicture"][msg._from] = True
                                dollypk.sendMessage(msg.to, "Mana foto nya")

#===========BOT UPDATE============#
                        elif cmd == 'pepek':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in Bots:
                               members = []
                               if msg.toType == 1:
                                   room = dollypk.getCompactRoom(to)
                                   members = [mem.mid for mem in room.contacts]
                               elif msg.toType == 2:
                                   group = dollypk.getCompactGroup(to)
                                   members = [mem.mid for mem in group.members]
                               else:
                                   return dollypk.sendReplyMessage(msg.id, to, 'Failed mentionall members, use this command only on room or group chat')
                               if members:
                                   mentionMembers(to, members)

                        elif cmd == "botlist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                a = 0
                                for m_id in Bots:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +dollypk.getContact(m_id).displayName + "\n"
                                dollypk.sendMessage(msg.to,"🔹️Botlist🔹️\n\n\n"+ma+"\n%s Bots" %(str(len(Bots))))

                        elif cmd == "stafflist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in owner:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +dollypk.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +dollypk.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +dollypk.getContact(m_id).displayName + "\n"
                                dollypk.sendMessage(msg.to,"🔹️Adminlist🔹️\n\n🔹️Owner\n"+ma+"\n🔹️Admin\n"+mb+"\n🔹️Staff:\n"+mc+"\n%s Adminlist" %(str(len(owner)+len(admin)+len(staff))))
                  
                        elif cmd == "protectlist":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                me = ""
                                mf = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                e = 0
                                f = 0            
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +dollypk.getGroup(group).name + "\n"
                                gid = protectinvite
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +dollypk.getGroup(group).name + "\n"
                                gid = protectantijs
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +dollypk.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +dollypk.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    e = e + 1
                                    end = '\n'
                                    me += str(e) + ". " +dollypk.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    f = f + 1
                                    end = '\n'
                                dollypk.sendMessage(msg.to,"🔹️Prolist P.K_BotS🔹️\n\n🔒ᴘʀᴏᴛᴇᴄᴛ ǫʀ:\n"+ma+"\n🔒ᴘʀᴏᴛᴇᴄᴛ ɪɴᴠɪᴛᴇ:\n"+mb+"\n🔒ᴘʀᴏᴛᴇᴄᴛᴀɴᴛɪᴋɪᴄᴋᴇʀ:\n"+mc+"\n🔒ᴘʀᴏᴛᴇᴄᴛᴋɪᴄᴋ:\n"+md+"\n🔒ᴘʀᴏᴛᴇᴄᴛᴄᴀɴᴄᴇʟ:\n"+me+"\n🔒ᴘʀᴏᴛᴇᴄᴛᴊᴏɪɴ:\n"+mf+"\n\n🔹️Prolist %s GroupPro🔹️" %(str(len(protectqr)+len(protectinvite)+len(protectantijs)+len(protectcancel)+len(protectkick)+len(protectjoin))))

                        elif cmd == "rname":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                dollypk.sendMessage(msg.to,responsename)

                        elif cmd == ".bye":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                G = dollypk.getGroup(msg.to)
                                dollypk.sendMessage(msg.to, "Cabut Dulu Bray di group"+str(G.name))
                                dollypk.leaveGroup(msg.to)

                        elif cmd.startswith("leave "):
                            if msg._from in admin or msg._from in owner:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = dollypk.getGroupIdsJoined()
                                for i in gid:
                                    h = dollypk.getGroup(i).name
                                    if h == ng:
                                        dollypk.sendMessage(i, " Silahkan invite Ownernya ")
                                        dollypk.leaveGroup(i)
                                        dollypk.sendMessage(to,"Succes leave group " +h)

                        elif cmd == "speed" or cmd == "sp":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               start = time.time()
                               dollypk.sendMessage(to, "Sabar Pantek")
                               elapsed_time = time.time() - start
                               dollypk.sendMessage(to,"%s"%str(round(elapsed_time,4)))

                        elif cmd == "list on":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['PKreadPoint'][msg.to] = msg_id
                                 Setmain['PKreadMember'][msg.to] = {}
                                 dollypk.sendMessage(msg.to, "Lurking berhasil diaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "list off":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['PKreadPoint'][msg.to]
                                 del Setmain['PKreadMember'][msg.to]
                                 dollypk.sendMessage(msg.to, "Lurking berhasil dinoaktifkan\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "list sider":
                          if msg._from in owner or msg._from in admin or msg._from in mid:
                            if msg.to in Setmain['PKreadPoint']:
                                if Setmain['PKreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['PKreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ List sider ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(dollypk.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        dollypk.sendMessage1(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['PKreadPoint'][msg.to]
                                        del Setmain['PKreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['PKreadPoint'][msg.to] = msg.id
                                    Setmain['PKreadMember'][msg.to] = {}
                                else:
                                    dollypk.sendMessage(msg.to, "User kosong tidak terdetect")
                            else:
                                dollypk.sendMessage(msg.to, "Ketik List on dulu")

                        elif cmd == "cctv on":
                          if wait["selfbot"] == True:
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  dollypk.sendMessage(msg.to, "Cek sider diaktifkan\n\nDate "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "cctv off":
                          if wait["selfbot"] == True:
                           if msg._from in owner or msg._from in admin or msg._from in staff:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  dollypk.sendMessage(msg.to, "Cek sider dinonaktifkan\n\nDate "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nTime  "+ datetime.strftime(timeNow,'%H:%M:%S')+" ")
                              else:
                                  dollypk.sendMessage(msg.to, "Sudak tidak aktif")
                                                     
                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      dollypk.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 1000:
                                  for var in range(0,jumlah):
                                      dollypk.sendMessage(midd, str(Setmain["PKmessage1"]))

                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              msgs = msg.text.replace('ID line: ','')
                              conn = dollypk.findContactsByUserid(msgs)
                              if True:
                                  dollypk.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  dollypk.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)    
                                        
                        elif cmd.startswith("add friend "):
                        	if msg._from in owner or msg._from in admin or msg._from in mid:
                                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                            dollypk.findAndAddContactsByMid(str(ls))
                                        dollypk.sendMessage(to, "Success Add Friend "+dollypk.getContact(str(ls)).displayName)
                                        
                        elif cmd.startswith("delfriend "):
                          if msg._from in owner or msg._from in admin or msg._from in mid:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                   dollypk.deleteContact(ls)
                                dollypk.sendMessage(to, "Succes Delete Contact \n")
                                
                        elif cmd == "mykey":
                            dollypk.sendMessage(to, "KeyCommand Saat ini adalah [ {} ]".format(str(settings["keyCommand"])))
                            
                        elif cmd.startswith('inviteme '):
                              if msg._from in owner or msg._from in admin or msg._from in mid:    
                               text = msg.text.split()
                               number = text[1]
                               if number.isdigit():
                                groups = dollypk.getGroupIdsJoined()
                                if int(number) < len(groups) and int(number) >= 0:
                                    groupid = groups[int(number)]
                                    group = dollypk.getGroup(groupid)
                                    target = sender
                                    try:
                                        dollypk.getGroup(groupid)
                                        dollypk.findAndAddContactsByMid(target)
                                        dollypk.inviteIntoGroup(groupid, [target])
                                        dollypk.sendMessage(msg.to,"Succes invite to " + str(group.name))
                                    except:
                                        dollypk.sendMessage(msg.to,"I no there baby")                                                                                                       
                        elif cmd.startswith("idcontact "):
                        	if msg._from in owner or msg._from in admin or msg._from in mid: 
                                   if 'MENTION' in msg.contentMetadata.keys()!= None:
                                        names = re.findall(r'@(\w+)', text)
                                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                        mentionees = mention['MENTIONEES']
                                        lists = []
                                        for mention in mentionees:
                                            if mention["M"] not in lists:
                                                lists.append(mention["M"])
                                        for ls in lists:
                                                contact = dollypk.getContact(ls)
                                                mi_d = contact.mid
                                                dollypk.sendContact(msg.to, mi_d)
                                                
                        elif cmd.startswith("contact "):
                        	if msg._from in owner or msg._from in admin or msg._from in mid: 
                                       sep = cmd.split(" ")
                                       asu = cmd.replace(sep[0] + " ","")
                                       try:
                                          dollypk.sendContact(to, asu)
                                       except:
                                          pass
                                
                        elif cmd.startswith("clone "):
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                             if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                for mention in mentionees:
                                    contact = mention["M"]
                                    break
                                try:
                                    dollypk.cloneContactProfile(contact)
                                    ryan = dollypk.getContact(contact)
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan =  "「 clone Profile 」\nTarget nya "
                                    ret_ = "Berhasil clone profile target"
                                    ry = str(ryan.displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@x \n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    text = xpesan + zxc + ret_ + ""
                                    dollypk.sendMessage(to, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                except:
                                    dollypk.sendMessage(msg.to, "Gagal clone profile")
                                    
                        elif text.lower() == 'restore':
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              try:
                                  dollypkProfile.displayName = str(myProfile["displayName"])
                                  dollypkProfile.statusMessage = str(myProfile["statusMessage"])
                                  dollypkProfile.pictureStatus = str(myProfile["pictureStatus"])
                                  dollypk.updateProfileAttribute(8, dollypkProfile.pictureStatus)
                                  dollypk.updateProfile(dollypkProfile)
                                  dollypk.sendMessage(msg.to, sender, "「 Restore Profile 」\nNama ", " \nBerhasil restore profile")
                              except:
                                  dollypk.sendMessage(msg.to, "Gagal restore profile")
                                  
                        elif cmd == 'listblock':
                          if msg._from in owner or msg._from in admin or msg._from in mid:
                            blockedlist = dollypk.getBlockedContactIds()
                            kontak = dollypk.getContacts(blockedlist)
                            num=1
                            msgs="List Blocked"
                            for ids in kontak:
                                msgs+="\n[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n\nTotal Blocked : %i" % len(kontak)
                            dollypk.sendMessage(to, msgs)
#===========welcome============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = ""
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = dollypk.getGroup(msg.to)
                                       msgs = ""
                                  dollypk.sendMessage(msg.to, "Welcome Has Been Active")
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = dollypk.getGroup(msg.to)
                                         msgs = ""
                                    else:
                                         ginfo = dollypk.getGroup(msg.to)
                                         msgs = ""
                                    dollypk.sendMessage(msg.to, "Welcome has been Deactive")
#===========KICKOUT============
                        elif ("Kick " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       if target not in owner:
                                           if target not in admin:
                                               if target not in staff:
                                                   if target not in Team:
                                                       try:
                                                           dollypk.kickoutFromGroup(msg.to, [target])
                                                           print ("kicker1 kick user")
                                                       except:
                                                           dollypk.sendMessage(msg.to,"limit")

                        elif cmd.startswith('kickname '):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                imnoob = 'kickall.js gid={} token={}'.format(to, dollypk.authToken)
                                if name == '':
                                    return
                                group = dollypk.getCompactGroup(to)
                                list = []
                                for member in group.members:
                                    contact = dollypk.getContact(member.mid)
                                    if name in contact.displayName.lower():
                                        list.append(contact.mid)
                                if list:
                                    for a in list:
                                        dollypk.kickoutFromGroup(to, [a])
                                else:
                                    dollypk.sendReplyMessage(msg.id, to, "'{}' not found".format(name))

                        elif cmd.startswith('.skill '):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                if name == '':
                                    return
                                group = dollypk.getCompactGroup(to)
                                list = []
                                imnoob = 'kickall.js gid={} token={}'.format(to, dollypk.authToken)
                                for member in group.members:
                                    contact = dollypk.getContact(member.mid)
                                    if name in contact.displayName.lower():
                                        list.append(contact.mid)
                                if list:
                                    for abc in list:
                                    	if abc not in Team and abc not in Bots and abc not in owner and abc not in admin:
                                            imnoob += " uik={}".format(abc)
                                    execute_js(imnoob)
                                    time.sleep(0.8)
                                else:
                                    dollypk.sendReplyMessage(msg.id, to, "'{}' not found".format(name))

                        elif cmd.startswith('cancelname '):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                if name == '':
                                    return
                                group = dollypk.getCompactGroup(to)
                                list = []
                                for member in group.invitee:
                                    contact = dollypk.getContact(member.mid)
                                    if name in contact.displayName.lower():
                                        list.append(contact.mid)
                                if list:
                                    for a in list:
                                        dollypk.cancelGroupInvitation(to, [a])
                                else:
                                    dollypk.sendReplyMessage(msg.id, to, "'{}' not found".format(name))

                        elif cmd.startswith('invitename '):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                                sep = text.split(" ")
                                name = text.replace(sep[0] + " ","")
                                if name == '':
                                    return
                                friend = dollypk.getAllContactIds()
                                list = []
                                for teman in friend:
                                    contact = dollypk.getContact(teman)
                                    if name in contact.displayName.lower():
                                        list.append(contact.mid)
                                if list:
                                    for a in list:
                                        dollypk.inviteIntoGroup(to, [a])
                                else:
                                    dollypk.sendReplyMessage(msg.id, to, "'{}' not found".format(name))   

                        elif ".cancelall" in msg.text:
                           if wait["kicker1"] == True:
                            if msg._from in owner:
                             if msg.toType == 2:
                                group = dollypk.getGroup(msg.to)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for _dn in gMembMids:
                                  if _dn not in admin and _dn not in asist["whitelist"]:
                                    dollypk.unsendMessage(msg.id)
                                    dollypk.cancelGroupInvitation(msg.to,[_dn])
                                    time.sleep(0.8)
                            else:
                                pass
                           else:
                               pass

                        elif (".reinv " in msg.text):
                           if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               for x in key["MENTIONEES"]:
                                   if x["M"] not in Bots and x["M"] not in owner and x["M"] not in admin and x["M"] not in asist["whitelist"]:
                                       try:
                                           ban["blacklist"].append(x["M"])
                                           dollypk.kickoutFromGroup(msg.to, [x["M"]])
                                           dollypk.findAndAddContactsByMid([x["M"]])
                                           time.sleep(0.8)
                                           dollypk.inviteIntoGroup(msg.to,[x["M"]])
                                       except:
                                           dollypk.sendReplyMessage(msg.id, to,"limit")
                                   else:
                                       dollypk.sendReplyMessage(msg.id, to,"cannot kick someone who in stafflist")

                        elif (".vkick " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               for x in key["MENTIONEES"]:
                                   if x["M"] not in Bots and x["M"] not in owner and x["M"] not in admin and x["M"] not in asist["whitelist"]:
                                       try:
                                           ban["blacklist"].append(x["M"])
                                           dollypk.kickoutFromGroup(msg.to, [x["M"]])
                                           dollypk.findAndAddContactsByMid([x["M"]])
                                           time.sleep(0.8)
                                           dollypk.inviteIntoGroup(msg.to,[x["M"]])
                                           dollypk.cancelGroupInvitation(msg.to,[x["M"]])
                                           dollypk.inviteIntoGroup(msg.to,[x["M"]])
                                       except:
                                           dollypk.sendReplyMessage(msg.id, to,"limit")
                                   else:
                                       dollypk.sendReplyMessage(msg.id, to,"cannot kick someone who in stafflist")

                        elif (".Gkick " in msg.text):
                           if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               for x in key["MENTIONEES"]:
                                   if x["M"] not in Bots and x["M"] not in owner and x["M"] not in admin and x["M"] not in asist["whitelist"]:
                                       try:
                                           ban["blacklist"].append(x["M"])
                                           dollypk.kickoutFromGroup(msg.to, [x["M"]])
                                           dollypk.findAndAddContactsByMid([x["M"]])
                                           time.sleep(0.8)
                                           dollypk.inviteIntoGroup(msg.to,[x["M"]])
                                           dollypk.cancelGroupInvitation(msg.to,[x["M"]])
                                       except:
                                           dollypk.sendReplyMessage(msg.id, to,"limit")
                                   else:
                                       dollypk.sendReplyMessage(msg.id, to,"cannot kick someone who in stafflist")

                        elif ".kickall" in msg.text:
                         if wait["selfbot"] == True:
                          if msg._from in owner:
                           if msg.toType == 2:
                              print("ok")
                              _name = msg.text.replace(".kickall","")
                              gs = dollypk.getGroup(msg.to)
                              targets = []
                              for g in gs.members:
                                 if _name in g.displayName:
                                     targets.append(g.mid)
                              if targets == []:
                                 dollypk.unsendMessage(msg.id)
                                 dollypk.sendMessage(msg.to,"Tidak Ditemukan.")
                              else:
                                  for target in targets:
                                   if target not in admin and target not in owner and target not in Bots:
                                      try:
                                          klist=[ben]
                                          kickers=random.choice(klist)
                                          kickers.kickoutFromGroup(msg.to,[target])
                                          print (msg.to,[g.mid])
                                      except Exception as e:
                                          dollypk.sendReplyMessage(msg.id, to,"limit")
                                          break
                                      time.sleep(0.8)
                          else:
                              pass
                         else:
                             pass

#===========KICKALL / BYPASS============
                        elif cmd.startswith(".bypass no"):
                          if msg._from in owner:
                           if wait["selfbot"] == True:
                            number = msg.text.replace(".bypass no","")
                            groups = dollypk.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                xyz = dollypk.getGroup(group)
                                try:
                                    if xyz.invitee == None:pends = []
                                    else:pends = [c.mid for c in xyz.invitee]
                                    targp = []
                                    for x in pends:
                                        if x not in ["u3a4cc9a5d0da4077d7dc6cd4f405517c",dollypk.profile.mid]:targp.append(x)
                                    mems = [c.mid for c in xyz.members]
                                    targk = []
                                    for x in mems:
                                        if x not in ["u3a4cc9a5d0da4077d7dc6cd4f405517c",dollypk.profile.mid]:targk.append(x)
                                    imnoob = 'dual.js gid={} token={}'.format(group, dollypk.authToken)
                                    for x in targp:imnoob += ' uid={}'.format(x)
                                    for x in targk:imnoob += ' uik={}'.format(x)
                                    execute_js(imnoob)
                                    time.sleep(0.8)
                                except:
                                    if xyz.invitee == None:pends = []
                                    else:pends = [c.mid for c in xyz.invitee]
                                    targp = []
                                    for x in pends:
                                        if x not in ["u3a4cc9a5d0da4077d7dc6cd4f405517c",dollypk.profile.mid]:targp.append(x)
                                    mems = [c.mid for c in xyz.members]
                                    targk = []
                                    for x in mems:
                                        if x not in ["u3a4cc9a5d0da4077d7dc6cd4f405517c",dollypk.profile.mid]:targk.append(x)
                                    imnoob = 'dual.js gid={} token={}'.format(group, dollypk.authToken)
                                    for x in targp:imnoob += ' uid={}'.format(x)
                                    for x in targk:imnoob += ' uik={}'.format(x)
                                    execute_js(imnoob)
                                    time.sleep(0.8)
                                dollypk.sendReplyMessage(msg.id, to, "Berhasil bypass di group " + xyz.name)
                            except Exception as error:
                                dollypk.sendMessage(to, str(error))
                           else:
                               pass
                          else:
                              pass

                        elif cmd.startswith(".kickall no"):
                          if msg._from in owner:
                           if wait["selfbot"] == True:
                            number = msg.text.replace(".kickall no","")
                            groups = dollypk.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                xyz = dollypk.getGroup(group)
                                try:
                                    if xyz.invitee == None:pends = []
                                    else:mems = [c.mid for c in xyz.members]
                                    targk = []
                                    for x in mems:
                                        if x not in ["u3a4cc9a5d0da4077d7dc6cd4f405517c",dollypk.profile.mid]:targk.append(x)
                                    imnoob = 'kickall.js gid={} token={}'.format(group, dollypk.authToken)                                    
                                    for x in targk:imnoob += ' uik={}'.format(x)
                                    execute_js(imnoob)
                                    time.sleep(0.8)
                                except:
                                    if xyz.invitee == None:pends = []
                                    mems = [c.mid for c in xyz.members]
                                    targk = []
                                    for x in mems:
                                        if x not in ["u3a4cc9a5d0da4077d7dc6cd4f405517c",dollypk.profile.mid]:targk.append(x)
                                    imnoob = 'kickall.js gid={} token={}'.format(group, dollypk.authToken)                                   
                                    for x in targk:imnoob += ' uik={}'.format(x)
                                    execute_js(imnoob)
                                    time.sleep(0.8)
                                dollypk.sendReplyMessage(msg.id, to, "Berhasil kickall di group " + xyz.name)
                            except Exception as error:
                                dollypk.sendMessage(to, str(error))
                           else:
                               pass
                          else:
                              pass                                                           
#===========ADMIN ADD============#
                        elif ("Staff " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           staff.append(target)
                                           dollypk.sendMessage(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ sᴛᴀғғ")
                                       except:
                                           pass

                        elif ("Bot " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           Bots.append(target)
                                           dollypk.sendMessage(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ʙᴏᴛ")
                                       except:
                                           pass

                        elif ("Admin " in msg.text):
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           admin.append(target)
                                           dollypk.sendMessage(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ admin")
                                       except:
                                           pass
                                           
                        elif ("Admindell " in msg.text):
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           admin.remove(target)
                                           dollypk.sendMessage(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢʜᴀᴘᴜs  admin")
                                       except:
                                           pass                  

                        elif ("Staffdell " in msg.text):
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           staff.remove(target)
                                           dollypk.sendMessage(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢʜᴀᴘᴜs sᴛᴀғғ")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           Bots.remove(target)
                                           dollypk.sendMessage(msg.to,"ʙᴇʀʜᴀsɪʟ ᴍᴇɴɢʜᴀᴘᴜs ʙᴏᴛs")
                                       except:
                                           pass
                                           
                        elif cmd == "admin on" or text.lower() == 'admin:on':
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["addadmin"] = True
                                dollypk.sendMessage(msg.to,"Send Contact")

                        elif cmd == "admin off" or text.lower() == 'adminexpl:on':
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["delladmin"] = True
                                dollypk.sendMessage(msg.to,"Send contact")

                        elif cmd == "staff on" or text.lower() == 'staff:on':
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["addstaff"] = True
                                dollypk.sendMessage(msg.to,"Send contact")

                        elif cmd == "staff off" or text.lower() == 'staffexpl:on':
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["dellstaff"] = True
                                dollypk.sendMessage(msg.to,"Send contact")

                        elif cmd == "bot on" or text.lower() == 'bot:on':
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["addbots"] = True
                                dollypk.sendMessage(msg.to,"Send contact")

                        elif cmd == "bot off" or text.lower() == 'botexpl:on':
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["dellbots"] = True
                                dollypk.sendMessage(msg.to,"Kirim kontaknya...")

                        elif cmd == ".refresh" or text.lower() == 'refresh':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                dollypk.sendMessage(msg.to,"Done refresh")

                        elif cmd == "admin" or text.lower() == 'contact admin':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                for i in admin:
                                    ma = dollypk.getContact(i)
                                    dollypk.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "staff" or text.lower() == 'contact staff':
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                                ma = ""
                                for i in staff:
                                    ma = dollypk.getContact(i)
                                    dollypk.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == ".me" or text.lower() == 'contact bot':
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                ma = ""
                                for i in Bots:
                                    ma = dollypk.getContact(i)
                                    dollypk.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#        
                        elif cmd == "timeline on" or text.lower() == 'timeline on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["Timeline"] = True
                                dollypk.sendMessage(msg.to,"detect timeline on")

                        elif cmd == "timeline off" or text.lower() == 'timeline off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["Timeline"] = False
                                dollypk.sendMessage(msg.to,"detect timleline off ")
                                
                        elif cmd == "autoblock on" or text.lower() == 'blockadd on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["autoblock"] = True
                                dollypk.sendMessage(msg.to,"autoblock berhasil di hidupkan")

                        elif cmd == "autoblock off" or text.lower() == 'blockadd off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["autoblock"] = False
                                dollypk.sendMessage(msg.to,"autoblock berhasil di matikan")
                                
                        elif cmd == "unsend on" or text.lower() == 'unsend on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                settings["unsendMessage"] = True
                                dollypk.sendMessage(msg.to,"detect unsend diaktifkan")

                        elif cmd == "unsend off" or text.lower() == 'unsend off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                settings["unsendMessage"] = False
                                dollypk.sendMessage(msg.to,"detect unsend dinonaktifkan")
                                
                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["contact"] = True
                                dollypk.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["contact"] = False
                                dollypk.sendMessage(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["detectMention"] = True
                                dollypk.sendMessage(msg.to,"Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["detectMention"] = False
                                dollypk.sendMessage(msg.to,"Auto respon dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["autoJoin"] = True
                                dollypk.sendMessage(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["autoJoin"] = False
                                dollypk.sendMessage(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["autoAdd"] = True
                                dollypk.sendMessage(msg.to,"Auto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["autoAdd"] = False
                                dollypk.sendMessage(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["sticker"] = True
                                dollypk.sendMessage(msg.to,"Deteksi sticker diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["sticker"] = False
                                dollypk.sendMessage(msg.to,"Deteksi sticker dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                settings["autoJoinTicket"] = True
                                dollypk.sendMessage(msg.to,"Join ticket diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                settings["autoJoinTicket"] = False
                                dollypk.sendMessage(msg.to,"Join ticket dinonaktifkan")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban:on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           dollypk.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass
                                           
                          elif "Invite " in msg.text:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]                                                                                                                                
                               targets = []
                               for x in key["MENTIONEES"]:                                                                                                                                  
                                   targets.append(x["M"])
                               for target in targets:                                                                                                                                       
                                   try:
                                      dollypk.findAndAddContactsByMid(target)
                                      dollypk.inviteIntoGroup(msg.to,[target])
                                   except:
                                       pass 

                        elif ("Untalkban:on " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           dollypk.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["Talkwblacklist"] = True
                                dollypk.sendMessage(msg.to,"Send contact")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["Talkdblacklist"] = True
                                dollypk.sendMessage(msg.to,"Send contact")
                                
                        
                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Team:
                                       if target not in Bots:
                                           if target not in owner:
                                               if target not in admin:
                                                   if target not in staff:
                                                       try:
                                                           wait["blacklist"][target] = True
                                                           dollypk.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                                       except:
                                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in staff:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           dollypk.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["wblacklist"] = True
                                dollypk.sendMessage(msg.to,"Send contact")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                                wait["dblacklist"] = True
                                dollypk.sendMessage(msg.to,"Send contact")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                              if wait["blacklist"] == {}:
                                dollypk.sendMessage(msg.to,"Kosong bangke")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +dollypk.getContact(m_id).displayName + "\n"
                                dollypk.sendMessage(msg.to,"Blacklist\n\n"+ma+"\n %s User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                              if wait["Talkblacklist"] == {}:
                                dollypk.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +dollypk.getContact(m_id).displayName + "\n"
                                dollypk.sendMessage(msg.to," Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "blc" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                              if wait["blacklist"] == {}:
                                    dollypk.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = dollypk.getContact(i)
                                        dollypk.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'cban':
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                              wait["blacklist"] = {}
                              ragets = dollypk.getContacts(wait["blacklist"])
                              mc = ""
                              dollypk.sendMessage(msg.to,"Succes clearall baned" + mc)
#===========COMMAND SET============#
                        elif 'Spesan: ' in msg.text:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              spl = msg.text.replace('Spesan: ','')
                              if spl in [""," ","\n",None]:
                                  dollypk.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  dollypk.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Swelcome: ' in msg.text:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              spl = msg.text.replace('Swelcome: ','')
                              if spl in [""," ","\n",None]:
                                  dollypk.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  dollypk.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Srespon: ' in msg.text:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              spl = msg.text.replace('Srespon: ','')
                              if spl in [""," ","\n",None]:
                                  dollypk.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  dollypk.sendMessage(msg.to, "「Respon Msg」\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Sspam: ' in msg.text:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              spl = msg.text.replace('Sspam: ','')
                              if spl in [""," ","\n",None]:
                                  dollypk.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["PKmessage1"] = spl
                                  dollypk.sendMessage(msg.to, "「Spam Msg」\nSpam Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Ssider: ' in msg.text:
                           if msg._from in owner or msg._from in admin or msg._from in mid:
                              spl = msg.text.replace('Ssider: ','')
                              if spl in [""," ","\n",None]:
                                  dollypk.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  dollypk.sendMessage(msg.to, "「Sider Msg」\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))
                                  
                                  
                        elif text.lower() == "cek message":
                          if wait["selfbot"] == True:
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               dollypk.sendMessage(msg.to, "Msg add:\n「 " + str(wait["message"]) + " 」")
                               dollypk.sendMessage(msg.to, "Msg welcome:\n「 " + str(wait["welcome"]) + " 」")
                               dollypk.sendMessage(msg.to, "Msg Respon:\n「 " + str(wait["Respontag"]) + " 」")
                               dollypk.sendMessage(msg.to, "Msg welcome:\n「 " + str(Setmain["PKmessage1"]) + " 」")
                               dollypk.sendMessage(msg.to, "Msg sider:\n「 " + str(wait["mention"]) + " 」")

                        elif text.lower() == "cpesan":
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               dollypk.sendMessage(msg.to, "「Pesan Msg」\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cwelcome":
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               dollypk.sendMessage(msg.to, "「Welcome Msg」\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")

                        elif text.lower() == "crespon":
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               dollypk.sendMessage(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cspam":
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               dollypk.sendMessage(msg.to, "「Spam Msg」\nSpam Msg mu :\n\n「 " + str(Setmain["PKmessage1"]) + " 」")

                        elif text.lower() == "csider":
                            if msg._from in owner or msg._from in admin or msg._from in mid:
                               dollypk.sendMessage(msg.to, "「Sider Msg」\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")
                                                      
#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in admin or msg._from in owner or msg._from in mid:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = dollypk.findGroupByTicket(ticket_id)
                                     dollypk.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     dollypk.sendMessage(msg.to, "Masuk : %s" % str(group.name))

    except Exception as error:
        print (error)
        
def runningProgram():
    if Setmain['restartPoint'] is not None:
        try:
            dollypk.sendMessage(settings['restartPoint'], 'BOT ON AGAIN')
        except TalkException:
            pass
        Setmain['restartPoint'] = None
    while True:
        try:
            ops = oepoll.singleTrace(count=50)
        except TalkException as talk_error:
            logError(talk_error)
            if talk_error.code in [7, 8, 20]:
                sys.exit(1)
            continue
        except KeyboardInterrupt:
            sys.exit('[ SYSTEM MESSAGE : *KEYBOARD INTERRUPT.')
        except Exception as error:
            logError(error)
            continue
        if ops:
            for op in ops:
                bot(op)
                oepoll.setRevision(op.revision)

if __name__ == '__main__':
    print ("LOGIN READY")
    print ("PROSES")
    print ("︻╦̵̵͇̿̿̿̿╤─PANTEK ᵏⁱˡˡᵉʳ ")
    print ("======1%\n=======50%\n=========100%")
    print (" ᴛʜᴀɴᴋs ᴛᴏ ᴀʟʟᴀʜ sᴡᴛ ")
    print (" ᴛʜᴀɴᴋs ᴛᴏ ᴘʏ³ ")
    print (" ᴋᴇᴇᴘ sᴛᴀʏ ᴀɴᴅ ʀᴜʟʟᴇs ")
    print ("\n\
    = = = = = = = = = = = =        =====               === \n\
    = = = = = = = = = = = = =      =====            === \n\
    =======          ====== =      =====         === \n\
    =======           ====== =     =====      ===\n\
    =======           =======      =====    === \n\
    =======           ======       ===== ===\n\
    =================              ===== ===\n\
    ================               =====     ===\n\
    =======                        =====      ===  \n\
    =======                        =====         ===\n\
    =======                        =====           ===\n\
    =======                        =====             === \n")
    print("LOGIN SUKSES")
    print ("SELFBOT SIAP DI GUNAKAN\n own=Antares[Dolly]\n\n")
    runningProgram()
      
            
    
