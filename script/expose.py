import eel
from script.download import *
from hfile import *
from hwin32 import *
from hotp import *
from hwin import *
from hini import *
ini = hini()
from hrequest import *

import script._con as con


import socket
def free_port() -> int:
    free_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    free_socket.bind(("127.0.0.1", 0))
    free_socket.listen(1)
    port: int = free_socket.getsockname()[1]
    free_socket.close()
    return port
def killAppWithRunning():
    lastpid = ini.readint("lastpid", 0)
    if hwin.checkPid(lastpid):
        print("killAppsss")
        killApp()
    pid = os.getpid()
    ini.write("lastpid", pid)

TOKEN = "5632716370:AAHVeJUsaRQ9jU9NoxFMe9FSWW9c4Vs90Ao"    
UserIDTele = "853744564"
chatAutoSanBot = "/sbkk"
from htele import *
listnhanvatcayzen = {}


listpidreset = {}
tele = htele(TOKEN)

from hsqlite3 import *

sql = hsqlite3()
table = """CREATE TABLE IF NOT EXISTS script
                    (id integer PRIMARY KEY AUTOINCREMENT, ten TEXT DEFAULT "" NOT NULL, map TEXT DEFAULT "" NOT NULL, x TEXT DEFAULT "" NOT NULL, y TEXT DEFAULT "" NOT NULL, levelmin TEXT DEFAULT "" NOT NULL, levelmax TEXT DEFAULT "" NOT NULL, timequaylaikhibipk TEXT DEFAULT "" NOT NULL, zen TEXT DEFAULT "" NOT NULL)"""
sql.execute(table)
table = """CREATE TABLE IF NOT EXISTS kichbannv
                    (id integer PRIMARY KEY AUTOINCREMENT, tennv TEXT DEFAULT "" NOT NULL, kichban TEXT DEFAULT "" NOT NULL, kichhoat TEXT DEFAULT "" NOT NULL)"""
sql.execute(table)
table = """CREATE TABLE IF NOT EXISTS setting
                    (id integer PRIMARY KEY AUTOINCREMENT, apiAnycaptcha TEXT DEFAULT "" NOT NULL,  apikeyActive TEXT DEFAULT "" NOT NULL,  showMain TEXT DEFAULT "" NOT NULL,  tokenTelegram TEXT DEFAULT "" NOT NULL)"""

sql.execute(table)
table = """CREATE TABLE IF NOT EXISTS congdiem
                    (id integer PRIMARY KEY AUTOINCREMENT, hero TEXT DEFAULT "" NOT NULL, addstr TEXT DEFAULT "" NOT NULL, addagi TEXT DEFAULT "" NOT NULL, addvit TEXT DEFAULT "" NOT NULL, addene TEXT DEFAULT "" NOT NULL, addcmd TEXT DEFAULT "" NOT NULL, pass2 TEXT DEFAULT "" NOT NULL, sophutrs TEXT DEFAULT "" NOT NULL, trainexp TEXT DEFAULT "" NOT NULL, trainstadium TEXT DEFAULT "" NOT NULL, annv TEXT DEFAULT "" NOT NULL, anmain TEXT DEFAULT "" NOT NULL, resetingame TEXT DEFAULT "" NOT NULL)"""
sql.execute(table)
sql.addColumn("congdiem", "pass2")
sql.addColumn("congdiem", "sophutrs")
sql.addColumn("congdiem", "trainexp")
sql.addColumn("congdiem", "trainstadium")
sql.addColumn("congdiem", "annv")
sql.addColumn("congdiem", "anmain")
sql.addColumn("congdiem", "resetingame")
sql.addColumn("script", "timequaylaikhibipk")
sql.addColumn("setting", "showMain")
sql.addColumn("setting", "tokenTelegram")

@eel.expose
def getTitle():
    return con.title
@eel.expose
def updateSetting(name, value):
    ini.write(name, value)


def startEel(port=free_port(), mode="chrome", folder_init="web", index="index.html", host="localhost", size=(900,600)):
    try:
        pid = hwin.getPidByPort(port)
        if pid:
            hwin.killPid2(pid)
        folder_init = hfile.fixFileName(folder_init)
        eel.init(folder_init)
        if mode == "chrome":
            if not hfile.checkExists(hpath.chrome()):
                mode = None
                edeg = hpath.edeg()
                if edeg:
                    hthread.start(hwin.processStart, [edeg, [f'--app=http://{host}:{port}']])
                elif hfile.checkExists(orbita_browser_108_check):
                    hthread.start(hwin.processStart, [orbita_browser_108_check, [f'--app=http://{host}:{port}']])
        eel.start(index, mode=mode, size=size, position=(200, 300), host=host, port=port)
        quit()
    except:
        hfile.getError(msgBox=False)



def killApp():
    try:
        os.kill(os.getpid(), signal.SIGTERM)
        sys.exit()
        return
    except Exception as e:
        print("w.killApp", e)
killAppWithRunning()

@eel.expose
def quit(title):
    try:
        hwnd = hwin32.findWindow(title)
        hwin32.closeWindow(hwnd)
    except Exception as e:
        print(e)
    killApp()





setskill = {}
infos = {}
infostadiums = {}
heropid = {}
listpk = []
listpkclone = []
listpkg = []
listkopk = []
dictpk = dict()
listbuffpc = []
listnvautopk = []
def listAutoPK():
    global listpk
    global listpkclone
    global listkopk
    global dictpk
    global listbuffpc

    while True:
        for i in listnvautopk:
            dictpk[i] = hfile.readLines("/data/" + i + "_pk.txt")
            # print(dictpk[i])
        pks = hfile.readLines("/data/pk.txt")
        if pks:
            if pks[0] != "#":
                listpk = pks
            else:
                listpk = []
        pks = hfile.readLines("/data/pkclone.txt")
        if pks:
            if pks[0] != "#":
                listpkclone = pks
            else:
                listpkclone = []
        pks = hfile.readLines("/data/pkg.txt")
        if pks:
            if pks[0] != "#":
                listpkg = pks
        listbuffpct = hfile.readLines("/data/buffpc.txt")
        if listbuffpct:
            if listbuffpct[0] != "#":
                listbuffpc = hstr.trimAllLines(listbuffpct)
        listkopk = hfile.readLines("/data/kopk.txt")
        time.sleep(10)
hthread.start(listAutoPK)
version = "v2.9"
versiongoc = version
def checkNewVersion():
    global version
    while True:
        try:

            rq = hrequest()
            htmlver = rq.getHtml("https://raw.githubusercontent.com/emga9xkc2/automus12gamethuvn_release/main/README.md")
            ver = hstr.regex(htmlver, "Thông tin phiên bản</b>.*?(v\\d+.\\d+)", re.MULTILINE | re.DOTALL)
            if ver == "":
                ver = hstr.regex(htmlver, "Chi tiết phiên bản.*?(v\\d+.\\d+)")
            if ver:
                if ver != version:
                    version = versiongoc + " - BẤM HDSD ĐỂ UPDATE BẢN MỚI NHẤT " + ver

        except Exception as e:
            print(e)
            pass
        time.sleep(5)


hthread.start(checkNewVersion)
keystatus = dict()
keystatus["error"] = True
keystatus["status"] = "Chưa kích hoạt"

@eel.expose
def getInfo():
    dic = dict()
    dic["result"] = infos
    dic["version"] = version
    dic["mess"] = "success"
    dic["keystatus"] = keystatus
    return dic


@eel.expose
def getScript():
    select = sql.select("script", "id,ten,map,x,y,levelmin,levelmax,timequaylaikhibipk,zen", "")
    dic = dict()
    dic["result"] = select
    dic["mess"] = "success"
    return dic
listnhanvatautoreset = {}

@eel.expose
def setCayRS(tennv, autoreset):
    try:
        print(tennv, autoreset)
        if autoreset == "1":
            listnhanvatautoreset[tennv] = True
            ini.write(tennv + "_autoreset", True)
        else:
            listnhanvatautoreset[tennv] = False
            ini.write(tennv + "_autoreset", False)
        dic = dict()
        dic["result"] = "Đã cài autoreset"
        dic["mess"] = "success"
        return dic
    except Exception as e:
        dic = dict()
        dic["error"] = True
        dic["mess"] = e.args[0]
        print(e.args[0])
        return dic

listnhanvatautopk = {}
@eel.expose
def setAutoPK(tennv, autopk):
    try:
        print(tennv, autopk)
        if autopk == "1":
            listnhanvatautopk[tennv] = True
        else:
            listnhanvatautopk[tennv] = False
        dic = dict()
        dic["result"] = "Đã cài autopk"
        dic["mess"] = "success"
        return dic
    except Exception as e:
        dic = dict()
        dic["error"] = True
        dic["mess"] = e.args[0]
        print(e.args[0])
        return dic



herostop = {}
@eel.expose
def stopHero(tennv, stop):
    try:
        if stop == "1":
            herostop[tennv] = True
        else:
            herostop[tennv] = False
        dic = dict()
        dic["result"] = "Đã set stop " + tennv
        dic["mess"] = "success"
        return dic
    except Exception as e:
        dic = dict()
        dic["error"] = True
        dic["mess"] = e.args[0]
        return dic


def showKichBanEnable(hero):
    select = sql.select("script", "ten,map,x,y,zen,levelmin,levelmax,timequaylaikhibipk", "")
    lists = []
    for i in select:
        dic = {}
        tenkichban = i.get("ten")
        dic["ten"] = tenkichban

        enable = getStateKichBanHero(hero, tenkichban)
        if enable != "1":
            continue
        dic["map"] = i.get("map")
        dic["x"] = i.get("x")
        dic["y"] = i.get("y")
        dic["zen"] = i.get("zen")
        dic["levelmin"] = i.get("levelmin")
        dic["levelmax"] = i.get("levelmax")
        dic["timequaylaikhibipk"] = i.get("timequaylaikhibipk")
        lists.append(dic)
    return lists


@eel.expose
def showListPK(hero):
    try:
        pk = hfile.read("data/" + hero + "_pk.txt")
        dic = dict()
        dic["result"] = pk
        dic["mess"] = "success"
        return dic
    except Exception as e:
        dic = dict()
        dic["error"] = True
        dic["mess"] = e.args[0]
        return dic


@eel.expose
def saveListPK(hero, value):
    try:
        hfile.write("data/" + hero + "_pk.txt", value, backup=False)
        dic = dict()
        dic["result"] = "ok"
        dic["mess"] = "success"
        return dic
    except Exception as e:
        dic = dict()
        dic["error"] = True
        dic["mess"] = e.args[0]
        return dic


@eel.expose
def showKichBan(hero):
    try:
        select = sql.select("script", "id,ten", "")
        lists = []
        for i in select:
            dic = {}
            tenkichban = i.get("ten")
            dic["id"] = i.get("id")
            dic["ten"] = tenkichban
            enable = getStateKichBanHero(hero, tenkichban)
            dic["enable"] = enable
            lists.append(dic)
        dic = dict()
        dic["result"] = lists
        dic["mess"] = "success"
        return dic
    except Exception as e:
        dic = dict()
        dic["error"] = True
        dic["mess"] = e.args[0]
        return dic


def getStateKichBanHero(hero, tenkichban):
    kichhoat = sql.select_one("select kichhoat from kichbannv where tennv=? and kichban=?", [hero, tenkichban])
    if not kichhoat:
        return "0"
    return kichhoat[0]


@eel.expose
def editKichBanHero(hero, tenkichban, enable):
    try:
        # count = sql.execute_tolist("select count(*) from kichbannv where tennv=? and tenkichban", [hero, tenkichban])
        # print(count)
        # count = count[0][0]
        count = sql.selectCount("kichbannv", "tennv=? and kichban=?", [hero, tenkichban])
        if count > 0:
            update = sql.update("kichbannv", "kichhoat=?", "tennv=? and kichban=?", [enable, hero, tenkichban])
            dic = dict()
            dic["result"] = update
            dic["mess"] = "success"
            return dic
        dictscript = {}
        dictscript["tennv"] = hero
        dictscript["kichban"] = tenkichban
        dictscript["kichhoat"] = enable
        select = sql.insert("kichbannv", dictscript)
        dic = dict()
        dic["result"] = select
        dic["mess"] = "success"
        return dic
    except Exception as e:
        dic = dict()
        dic["error"] = True
        dic["mess"] = e.args[0]
        return dic


@eel.expose
def getCongDiem(hero):
    select = sql.select("congdiem", "addstr,addagi,addvit,addene,addcmd,pass2,sophutrs,trainexp,trainstadium,annv,anmain,resetingame", "hero=?", [hero], limit=1)
    if select:
        select = select[0]
    dic = dict()
    dic["result"] = select
    dic["mess"] = "success"
    return dic


@eel.expose
def getSetting():
    select = sql.select("setting", "apiAnycaptcha,apikeyActive,showMain,tokenTelegram", "", limit=1)
    if select:
        select = select[0]
    dic = dict()
    dic["result"] = select
    dic["mess"] = "success"
    return dic


settings = getSetting()


@eel.expose
def saveSetting(apiAnycaptcha, apikeyActive, tokenTelegram):
    try:
        global settings
        id = sql.select_one("select id from setting")
        if id:
            id = id[0]
            update = sql.update("setting", "apiAnycaptcha=?,apikeyActive=?,tokenTelegram=?", "id=?", [apiAnycaptcha, apikeyActive, tokenTelegram, id])
            dic = dict()
            dic["result"] = update
            dic["mess"] = "success"
            return dic
        dictscript = {}
        dictscript["apiAnycaptcha"] = apiAnycaptcha
        dictscript["tokenTelegram"] = tokenTelegram
        dictscript["apikeyActive"] = apikeyActive
        insert = sql.insert("setting", dictscript)
        settings = getSetting()
        print(settings)
        dic = dict()
        dic["result"] = insert
        dic["mess"] = "success"
        return dic
    except Exception as e:
        dic = dict()
        dic["error"] = True
        dic["mess"] = e.args[0]
        return dic


@eel.expose
def saveCongDiem(hero, str, agi, vit, ene, cmd, pass2, sophutrs, trainexp, trainstadium, annv, anmain,resetingame):
    try:
        global settings
        id = sql.select_one("select id from congdiem where hero=?", [hero])
        if id:
            id = id[0]
            update = sql.update(
                "congdiem",
                "addstr=?,addagi=?,addvit=?,addene=?,addcmd=?,pass2=?,sophutrs=?,trainexp=?,trainstadium=?,annv=?,anmain=?,resetingame=?",
                "id=?",
                [str, agi, vit, ene, cmd, pass2, sophutrs, trainexp, trainstadium, annv, anmain,resetingame, id],
            )
            dic = dict()
            dic["result"] = update
            dic["mess"] = "success"
            return dic
        dictscript = {}
        dictscript["hero"] = hero
        dictscript["addstr"] = str
        dictscript["addagi"] = agi
        dictscript["addvit"] = vit
        dictscript["addene"] = ene
        dictscript["addcmd"] = cmd
        dictscript["pass2"] = pass2
        dictscript["sophutrs"] = sophutrs
        dictscript["trainexp"] = trainexp
        dictscript["trainstadium"] = trainstadium
        dictscript["annv"] = annv
        dictscript["anmain"] = anmain
        dictscript["resetingame"] = resetingame
        insert = sql.insert("congdiem", dictscript)
        dic = dict()
        dic["result"] = insert
        dic["mess"] = "success"
        return dic
    except Exception as e:
        dic = dict()
        dic["error"] = True
        dic["mess"] = e.args[0]
        return dic


@eel.expose
def saveScript(tenscript, mapselect, xauto, yauto, levelmin, levelmax, timequaylaikhibipk, nhatzen):
    try:
        dictscript = {}
        dictscript["ten"] = tenscript
        dictscript["map"] = mapselect
        dictscript["x"] = xauto
        dictscript["y"] = yauto
        dictscript["zen"] = nhatzen
        dictscript["levelmin"] = levelmin
        dictscript["levelmax"] = levelmax
        dictscript["timequaylaikhibipk"] = timequaylaikhibipk
        insert = sql.insert("script", dictscript)
        dic = dict()
        dic["result"] = insert
        dic["mess"] = "success"
        return dic
    except Exception as e:
        dic = dict()
        dic["error"] = True
        dic["mess"] = e.args[0]
        return dic


@eel.expose
def updateScript(id, tenscript, mapselect, xauto, yauto, levelmin, levelmax, timequaylaikhibipk, nhatzen):
    try:
        update = sql.update(
            "script", "ten=?,map=?,x=?,y=?,levelmin=?,levelmax=?,timequaylaikhibipk=?,zen=?", "id=?", [tenscript, mapselect, xauto, yauto, levelmin, levelmax, timequaylaikhibipk, nhatzen, id]
        )
        dic = dict()
        dic["result"] = update
        dic["mess"] = "success"
        return dic
    except Exception as e:
        dic = dict()
        dic["error"] = True
        dic["mess"] = e.args[0]
        return dic


@eel.expose
def deleteScript(id):
    try:
        delete = sql.execute("delete from script where id=?", [id])
        dic = dict()
        dic["result"] = delete
        dic["id"] = id
        dic["mess"] = "success"
        return dic
    except Exception as e:
        dic = dict()
        dic["error"] = True
        dic["mess"] = e.args[0]
        return dic


def log(str: str):
    eel.pythonToJS(str)

@eel.expose
def openFile(filename):
    if "verifyphone" in filename:
        hotp.getOtpData()
    hfile.openWithNotepad("/data/" + filename)

def eel_saveResponse(response, savepath, process):

    total_length = response.headers.get('content-length')

    if total_length is None: # không có thông tin về kích thước file
        with open(savepath, 'wb') as f:
            f.write(response.content)

        eel.update_progress(str(100) +"_" + process)()
    else:
        dl = 0
        total_length = int(total_length)
        with open(savepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    dl += len(chunk)
                    f.write(chunk)
                    percent = dl / total_length * 100
                    eel.update_progress(str(percent) +"_" + process)()
def eel_getIdDrive(id):
    if id.startswith("https://drive.google.com/file/d/"):
        id = id.replace("https://drive.google.com/file/d/", "")
        id = id.split("/")[0]
        id = id.split("?")[0]
    if id.startswith("https://drive.google.com/open?id="):
        id = id.replace("https://drive.google.com/open?id=", "")
        id = id.split("/")[0]
        id = id.split("?")[0]
    return id


def eel_downloadDrive(id, destination, process=None):
    id = eel_getIdDrive(id)
    URL = "https://docs.google.com/uc?export=download"
    session = requests.Session()
    params = {"id": id, "confirm": "t"}
    response = session.get(URL, params=params, stream=True)
    token = ""
    for key, value in response.cookies.items():
        if key.startswith("download_warning"):
            token = value
            break
    if token:
        params = {"id": id, "confirm": token}
        response = session.get(URL, params=params, stream=True)
    eel_saveResponse(response, destination, process)

@eel.expose
def download_file(url, savepath, process= None):
    response = requests.get(url, stream=True)
    eel_saveResponse(response, savepath, process)
@eel.expose
def download_file_extract(url, savepath, extract=True, process="1/2"):

    savepath = hfile.fixFileName(savepath)
    if url.startswith("https://drive.google.com"):
        eel_downloadDrive(url, savepath, process)
    else:
        download_file(url, savepath, process)
    if extract:
        folderpath = hfile.getFolderName(savepath)
        fileex = hfile.fixFileName(folderpath)
        with zipfile.ZipFile(savepath, "r") as zip_ref:
            zip_ref.extractall(fileex)
        hfile.delete(savepath)
        dirs = hfile.listDir(folderpath)
        for z in dirs:
            if "-main" in z:
                dir1 = hfile.fixFileName(folderpath + "/" + z)
                hfile.deleteDir(dir1 + "/setup/ProcessManager/")
                hfile.copyDir(dir1, folderpath)
                hfile.deleteDir(dir1)
@eel.expose
def autoUpdate():
    dic = dict()
    foldermyscript = hpath.myScript()
    foldermyscriptcheck = foldermyscript.replace("\\", "/")
    if not "/python/myscript" in foldermyscriptcheck:
        versionScript = hfile.fixFileName(foldermyscript + "/version.txt")
        nowversion = hfile.read(versionScript)
        rq = hrequest()
        webVersion = rq.getHtml("https://raw.githubusercontent.com/emga9xkc2/my-script/main/version.txt")
        if webVersion != nowversion:
            print("Downloading myscript")
            download_file_extract("https://github.com/emga9xkc2/my-script/archive/refs/heads/main.zip", hfile.fixFileName(foldermyscript + "/update.zip"), "1/2")

    download_file_extract(con.url_tool, "update.zip", process="2/2")
    dic["result"] = "Đã cập nhật xong. Hãy tắt tool đi mở lại để dùng phiên bản mới"
    dic["mess"] = "success"
    return dic

def toastError(msg):
    eel.toastError(msg)
def toastSuccess(msg):
    eel.toastSuccess(msg)



def checkThread():
    while True:
        killapp = True
        for thread in threading.enumerate():
            if thread.name == "MainThread" and thread.is_alive():
                killapp = False
                break
        if killapp:
            hwin.killApp()
        time.sleep(2)

hthread.start(checkThread)
