
baseAutoZ = '"main.exe"+010477E4'
baseListHero = '"main.exe"+010399E4'
from hmem import *
from hwin import *
from script._server import *
from script._con import *
from script.expose import *
from script.muweb import *

print("a")
listitemkhongban = hfile.readLines("data/itemkhongban.txt")


testmove = hfile.checkExists("testmove.txt")
lockbando = threading.Lock()
khoangcach = {}

khoangcach["hoaxichlong"] = "100 0 0 0 25 0 0 0 0 0 0 0 6,7"
khoangcach["trieuhoiqua"] = "190 0 0 0 50 0 0 0 15 0 0 0 6,7"
khoangcach["bangquyen"] = "0 0 0 0 15 0 0 0 20 0 0 0 4,6"
khoangcach["kimcangquyen"] = "90 0 0 0 20 0 0 0 15 0 0 0 4,6"
khoangcach["tianangluong"] = "85 0 0 0 130 0 0 0 7 0 0 0 6"
khoangcach["muabangtuyet"] = "80 0 0 0 100 0 0 0 5 0 0 0 6"
khoangcach["muasaobang"] = "70 0 0 0 150 0 0 0 0 0 0 0 6"
khoangcach["muasaobangmaster"] = "17 0 0 0 165 0 0 0 0 0 0 0 6 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 150 0 0 0 0 0 0 0 4 0 0 0 1 0 0 0 4 0 0 0 13 0 0 0 0 0 0 0 ? 133"

khoangcach["luongnuocxanh"] = "80 0 0 0 140 0 0 0 0 0 0 0 6"
khoangcach["dongbang"] = "10 0 0 0 38 0 0 0 0 0 0 0 6"
khoangcach["tamtien"] = "110 0 0 0 12 0 0 0 9 0 0 0 7"
khoangcach["tanconglienhoan"] = "0 0 0 0 5 0 0 0 0 0 0 0 6 0 0 0 0 0 0 0 0 0 0"
khoangcach["tanconglienhoanmaster"] = "0 0 0 0 9 0 0 0 0 0 0 0 6 0 0 0 0 0 0 0 0 0 0"
dictphimbamcuoicung = {}
from ahk import AHK
from ahk.window import Window
from ahk.window import Control
from reload import *
ahk = AHK()

heroAutoPk = {}
def autoPKThread(pid):
    if heroAutoPk.get(pid, False):
        return
    heroAutoPk[pid] = True
    def start():
        
        self = s12tl(pid)
        self.win = Window.from_pid(ahk, pid=pid)
        self.namehero = self.getNameHero()
        while True:        
            try:
                if self.getTrongThanh():
                    time.sleep(1)
                    continue
                self.server = self.getServer()
                if self.server == 1 or self.server == 2 or self.server == 3 or self.server == 4 or self.server == 10 or self.server == 18:
                    time.sleep(1)
                    continue
                self.xoaToi()
                xhero, yhero = self.getPosHero()

                # xhero = xhero - 1
                self.batAutoZ(True)
                # self.endAuto(0)
                for i in range(0, 50):
                    zkill = 0
                    while True:
                        if not listnhanvatautopk.get(self.namehero, False):
                            return
                        if self.getHPConLai() == 0:
                            time.sleep(1)
                            break
                        skillautoz = self.getSkillAutoZ()
                        # print(skillautoz, self.getSkillActive())
                        if skillautoz != self.getSkillActive():
                            if self.skillautopk:
                                self.mem.write1Byte(baseAutoZ, [0x4, 0x32], self.skillautopk)
                                time.sleep(0.1)
                                continue
                            for z1 in range(250):
                                self.mem.write1Byte(baseAutoZ, [0x4, 0x32], z1)
                                time.sleep(0.5)
                                if skillautoz == self.getSkillActive():
                                    break
                                if not self.skillautopk:
                                    self.skillautopk = z1

                        addressnew = i * 0x6F4

                        namemonters = self.mem.readString(baseListHero, [0x8, 0x38 + addressnew])
                        namemonters = namemonters.replace("(", " ")

                        if " " in namemonters or "111111111111111" in namemonters:
                            break
               
                        if namemonters in listkopk:
                            break

                        id = self.mem.read1Byte(baseListHero, [0x8, 0x224 + addressnew])
                       
                        if id == 255:  # quái vật
                            break

                        if id == 156:  # cô bé bán dạo
                            break
                        # print(dictpk, namemonters, self.namehero)
                        if not namemonters in dictpk.get(self.namehero, ""):
                            break
                        addressnew = i * 0x6F4
                        trangthai1 = self.mem.read1Byte(baseListHero, [0x8, 0x40C + addressnew])
                        if trangthai1 == 0:
                            break
                        trangthai2 = self.mem.read1Byte(baseListHero, [0x8, 0x2A + addressnew])
                        if trangthai2 != 0:
                            break
                        trangthai3_trongthanh = self.mem.read1Byte(baseListHero, [0x8, 0xE + addressnew])
                        if trangthai3_trongthanh == 1:
                            break

                        xmonters = self.mem.read4Byte(baseListHero, [0x8, 0x1A0 + addressnew])
                        ymonters = self.mem.read4Byte(baseListHero, [0x8, 0x1A4 + addressnew])
                        if hstr.triTuyetDoi(xmonters - xhero) > 6 or hstr.triTuyetDoi(ymonters - yhero) > 6:
                            break
                        self.mem.write1Byte(baseListHero, [0x8, 0x20 + addressnew], 6)  # trạng thái quỷ đỏ

                        self.mem.writeByteArray("main.exe+100A8F8", None, self.mem.decimalToHexString(i))
                        self.batAutoZ(False)
                        self.endAuto(1)
                        # print(namemonters, i, zkill)
                        time.sleep(0.1)
                        zkill = zkill + 1
                        if zkill > 30:
                            break
                        
            except Exception as e:
                print(hfile.getError())
            time.sleep(0.1)
    start()
    heroAutoPk[pid] = False
    

def listMap():
    list = []
    list.append((0, "Lorencia"))
    list.append((1, "Dungeon"))
    list.append((2, "Devias"))
    list.append((3, "Noria"))
    list.append((8, "Tarkan2"))
    list.append((4, "LostTower"))
    list.append((6, "Arena"))
    list.append((7, "Atlans2"))
    list.append((10, "Icarus"))
    list.append((21, "Hỗn nguyên lâu"))
    list.append((27, "Kalima4"))
    list.append((34, "CryWolf"))
    list.append((36, "Kalima7"))
    list.append((37, "Kanturu_ruin"))
    list.append((38, "Kanturu_Remain"))
    list.append((40, "Đào ngọc"))
    list.append((41, "Barrack"))
    list.append((42, "Phụ bản Blagass"))
    list.append((51, "Elbeland3"))
    list.append((56, "Swamp_Of_Calmness"))
    list.append((57, "Rakion"))
    list.append((79, "Loren_Market"))
    list.append((80, "Karutan1"))
    list.append((81, "Karutan2"))
    list.append((93, "Màn hình chọn tướng"))
    list.append((94, "Màn hình đăng nhập"))
    return list


listmap = listMap()
def checkAuto247(pid):
    global dictphimbamcuoicung
    try:
        s12 = s12tl(pid)
        s12.namehero = "hero"
        while True:
            abc = s12.getPhimBamCuoiCungMem()
            if abc:
                dictphimbamcuoicung[pid] = abc
            # s12.setPhimBamCuoiCung(112)
            time.sleep(0.1)
    except Exception as e:
        print(hfile.getError())
        pass

class s12tl:
    def __init__(self, pid):
        self.listnameboss = []
        self.pid = pid
        self.lastxoatoi = 0
        self.mem = hmem(pid=pid)
        self.hwnd = hwin.getHandlesByPid(self.pid)
        if self.hwnd:
            self.hwnd = self.hwnd[0]
            self.title = hwin.getTitleByHandle(self.hwnd)
        self.printLevelHero = False
        self.daBatMenuThoatGame = False
        self.daBatMap = False
        self.biPK = 0
        self.config = None
        self.anmain = 0
        self.resetingame = 0
        self.skillautopk = 0
        self.idskillautopk = 0
        
        pass
    
    def fauto(self, indexselectmap):            
            global listpidreset
            global listnvstopgom
            global lastrabai
            self.idskillpc = 0
            self.idskillautopk = 0
            global dangbando
            # global runtelebot
            global listnvautopk

            global tele
            # global telebot
            global TOKEN
            global UserIDTele
            self.indexselectmap = indexselectmap
            global infos
            global infostadiums
            global heropid
            self.namehero = ""
            self.itestmove = 0
            self.lastmove = 0
            self.lastxoatoi = 0
            # mem = self.mem
            # self.addxAutoZ = mem.getPointer(baseAutoZ, [0x44])
            # self.addyAutoZ = mem.getPointer(baseAutoZ, [0x48])
            # self.addAutoZ = mem.getPointer(baseAutoZ, [0x8])
            # self.addTrongThanh = mem.getPointer(0x8150AC4, [0xE])
            
            taikhoanghinho = self.getTaiKhoanGhiNho()
            self.print10 = False
            dadangnhap = False
            hthread.start(checkAuto247, [self.pid])
            
            try:
                self.setKhoangCachNhatDoAutoZ(10)
                dadangnhap = True
            except:
                pass
            print(self.title, dadangnhap)
            if "Nologin" in self.title:
                try:
                    self.namehero = self.title.split("|")[2].strip()
                except:
                    hfile.getError()
            else:
                dadangnhap = True

            if not dadangnhap:
                with lockbando:
                    ilogin = 0
                    logined = False
                    while ilogin < 120:
                        time.sleep(1)
                        try:
                            map = self.getMap(0, 0)
                            if "Màn hình đăng nhập" in map:
                                if not self.getCuaSoNhapNick():
                                    self.clickReloadServer()
                                    time.sleep(0.5)
                                    print(self.namehero, "Sv", "not login 2")
                                    lastserver = self.readServerSave()
                                    print(self.namehero, "Sv", lastserver)
                                    lastserver = getServer(lastserver)
                                    xsv, ysv = listserver[lastserver - 1]
                                    print(self.namehero, "click", lastserver, xsv, ysv)
                                    self.mouseClick(xsv, ysv)
                                    self.sendKey("enter")
                                else:
                                    self.sendKey("enter")
                                    # self.mouseClick(408, 453)
                            elif "Màn hình chọn tướng" in map:
                                self.chonNhanVat(self.namehero)
                            else:
                                try:
                                    self.setKhoangCachNhatDoAutoZ(10)
                                    dadangnhap = True
                                    logined = True
                                    break
                                except:
                                    pass
                            # print(map)
                        except:
                            hfile.getError()
                    if not logined:
                        hwin.closeHwnd(self.hwnd)
                        return
            for i in range(60):
                self.namehero = self.getNameHero()
                if self.namehero != "-1":
                    break
                time.sleep(1)
            if self.namehero == "-1":
                return
            namehero = self.namehero

            self.batMenuThoatGame(False)
            self.batMenuHeThong(False)
            dareset = False
            autoplay = False

            # self.setKhoangCachTrainAutoZ(30)

            # listnhanvatautoreset[self.namehero] = ini.readboolean(self.namehero + "_autoreset")

            # if self.namehero == "Ashe":
            #     self.setViTriMouse(443, 314)
            #     while True:
            #         self.mem.write4Byte('"main.exe"+09A77CE0', [0x24], 13)
            #         time.sleep(0.001)
            # self.mem.write4Byte('"main.exe"+09A77CE0', [0x24], 58)
            #
            # if self.namehero == "Akali":
            # self.callMacroChat()
            # self.printMonter()
            # self.autoSanBoss("Lorencia")
            # time.sleep(1111111)
            # if self.namehero == "Diana":

            #     self.clickHwnd(79, 596)
            # time.sleep(1111111)
            listzen = []
            khongthedangnhap = False
            tongpointsaukhirs = 0
            chuakichhoat = False
            kieurs = -1
            pass2 = ""
            apiAnycaptcha = ""
            self.setIdLanDau = False
            iprintchuadurs = 0
            # print(self.namehero, "Start")
            batbuffcanhan = self.getBuffCaNhan()
            timevevitricu = self.getTimeVeViTriCu()
            batbuffnhom = self.getBuffNhom()
            khoangcachtrainautoz = self.getKhoangCachTrainAutoZ()
            tudongtangmau = self.getTuDongTangMau()
            if khoangcachtrainautoz <= 0:
                khoangcachtrainautoz = ini.readint(self.namehero + "_khoangcachtrainautoz", 0)
                batbuffcanhan = ini.readboolean(self.namehero + "_batbuffcanhan")
                timevevitricu = ini.readint(self.namehero + "_timevevitricu", 0)
                batbuffnhom = ini.readint(self.namehero + "_batbuffnhom", 0)
                tudongtangmau = ini.readboolean(self.namehero + "_tudongtangmau")

            ini.write(self.namehero + "_khoangcachtrainautoz", khoangcachtrainautoz)
            ini.write(self.namehero + "_batbuffcanhan", batbuffcanhan)
            ini.write(self.namehero + "_batbuffnhom", batbuffnhom)
            ini.write(self.namehero + "_timevevitricu", timevevitricu)
            ini.write(self.namehero + "_tudongtangmau", tudongtangmau)

            stoped = False
            ikhongthedangnhapreset = 0

            timequaylaikhibipk = 0
            bipklan1 = True

            self.classs = ""

            self.pktime = []

            self.listclone = hfile.readLines("data/pkclone_save.txt")

            self.tatnhatzen = ini.readboolean(self.namehero + "_tatnhatzen")
            self.tatauto = ini.readboolean(self.namehero + "_tatauto")

            self.rabai = True
            self.timerabai = time.time()
            self.skillautopk = 0
            isettitle = 0
            self.listmapmovekhibipk = []
            self.listmapmovekhibipk.append("Lorencia")
            self.listmapmovekhibipk.append("Noria")
            self.listmapmovekhibipk.append("Devias")
            self.listmapmovekhibipk.append("Elbeland")
            self.listmapmovekhibipk.append("Atlans")
            self.listmapmovekhibipk.append("Tarkan")
            solanbipkmapkarutan2 = 0
            self.timeolot3 = time.time()
            setlandau = False
            self.listnvcomatkhibipk = []
            iquetnv = 0
            iprintheodoi = 0
            self.vemaplientuc = False
            timeratoibai = 0
            self.sogiaycho = 0
            self.toadotrainmap = {}
            laylaihwnd = False
            self.ichonmaychukhac = 0
            self.starttrainstadium = False
            self.listtoadoarenatrain = []
            for zarena in range(11, 0, -1):
                tdy = 10 * zarena
                # td = (hrand.randomInt(88, 92), hrand.randomInt(tdy - 2, tdy + 2))
                td = (90, tdy)
                self.listtoadoarenatrain.append(td)
            self.iarenarunning = 0
            self.quaylaiarena = False
            self.startautogom = False
            self.mapauto = ""
            self.level = 0
            lastservernhandien = 0
            self.chonnv = False
            self.congdiem300lv = ""
            self.dacongdiem300lv = False
            self.ngayhetvip = ""
            self.server = ""
            self.ichonnv = 0

            while True:
                try:
                    taikhoandangnhap = self.getTaiKhoanDangNhap()
                    ngatketnoi = False
                    if self.ichonmaychukhac > 7:
                        # ngatketnoi = True
                        log(f"{namehero} chọn máy chủ khác {self.ichonmaychukhac} lần ko được")
                    if taikhoandangnhap == "-1" or ngatketnoi:
                        listpidreset[self.pid] = False
                        try:
                            infos.pop(self.pid)
                        except:
                            pass
                        try:
                            heropid.pop(namehero)
                        except:
                            pass
                        map = self.getMap(0, 0)
                        log(f"{namehero} bị ngắt kết nối {map}")
                        tele.sendMessage(UserIDTele, f"{namehero} bị ngắt kết nối {map}")
                        try:
                            self.win.kill()
                        except:
                            pass
                        return
                    if not setlandau:
                        print(self.namehero, "Starting...")
                        hpconlai = self.getHPConLai()
                        if hpconlai != 0:
                            self.namehero = self.getNameHero()
                            # if self.namehero != "GaTayBac":
                            #     return
                            self.win = Window.from_pid(ahk, pid=self.pid)

                            self.setNhatTatCa(False)
                            self.setNhatTheoDanhSach(True)
                            self.nhatTatCa = False
                            setlandau = True
                            listnhanvatautoreset.setdefault(self.namehero, ini.readboolean(self.namehero + "_autoreset"))
                            print(self.namehero, "Started", self.tatauto)
                        else:
                            time.sleep(1)
                            continue
                    
                    if taikhoandangnhap != taikhoanghinho:
                        print(self.namehero, "Ghi nhớ tk", taikhoandangnhap)
                        self.setTaiKhoanGhiNho(taikhoandangnhap)
                        taikhoanghinho = self.getTaiKhoanGhiNho()
                    matkhaudangnhap = self.getMatKhauDangNhap()
                    self.setMatKhauGhiNho(matkhaudangnhap)
                    self.namehero = self.getNameHero()
                    # autoReload("function1", self)
                    x, y = self.getPosHero()
                    map = self.getMap(x, y)
                    self.level = self.getLevel()
                    solanrs = self.getSoLanReset()
                    self.server = self.getServer()
                    if isettitle % 20 == 0:
                        titleset = f"{self.server} > {taikhoandangnhap} > {self.namehero} > {self.level} ({solanrs})"
                        self.win.set_title(titleset)
                        if not laylaihwnd:
                            with lockbando:
                                self.hwnd = hwin.getHandleByTitle(titleset, 3)
                                laylaihwnd = True

                    isettitle = isettitle + 1
                    levelrs = 198 + solanrs * 2
                    if levelrs >= 400:
                        levelrs = 400
                    if levelrs < 200:
                        levelrs = 200

                    cayreset = listnhanvatautoreset.get(self.namehero, False)
                    dic = dict()
                    dic["taikhoandangnhap"] = taikhoandangnhap
                    dic["level"] = f"{self.level}/{levelrs}"
                    dic["namehero"] = f"{self.namehero}"
                    dic["map"] = f"{map} ({self.classs})"
                    # dic["autozen"] = cayzen
                    dic["stop"] = herostop.get(self.namehero, False)
                    dic["cayreset"] = cayreset
                    autopknv = listnhanvatautopk.get(self.namehero, False)
                    dic["autopk"] = autopknv
                    infos[self.pid] = dic
                    heropid[self.namehero] = self.pid
                    congdiem = getCongDiem(self.namehero).get("result")
                    if not congdiem:
                        log(f"{htime.getStrTimeNow3()}: {self.namehero} chưa cài đặt cộng điểm")
                        time.sleep(2)
                        continue
                    pass2 = congdiem.get("pass2")
                    sophutrs = hstr.strToInt(congdiem.get("sophutrs", "-1"))
                    self.trainexp = hstr.strToInt(congdiem.get("trainexp", "0"))
                    self.trainstadium = hstr.strToInt(congdiem.get("trainstadium", "0"))
                    self.annv = hstr.strToInt(congdiem.get("annv", "0"))
                    self.anmain = hstr.strToInt(congdiem.get("anmain", "0"))
                    self.resetingame = hstr.strToInt(congdiem.get("resetingame", "0"))

                    if pass2 == "" or sophutrs == -1:
                        log(f"{htime.getStrTimeNow3()}: {self.namehero} chưa cài đặt passweb hoặc sophutrs, kiểm tra lại")
                        time.sleep(1)
                        continue
                    chat = self.getChat()
                    if chat == "/pkclear":
                        solanbipkmapkarutan2 = 0
                        self.setChat("1")
                    if chat == "/ta":
                        log(f"{htime.getStrTimeNow3()}: {self.namehero} tắt auto ra bãi khi bị pk")
                        self.tatauto = True
                        ini.write(self.namehero + "_tatauto", self.tatauto)
                        self.setChat("1")
                    if chat == "/ba":
                        log(f"{htime.getStrTimeNow3()}: {self.namehero} bật auto ra bãi khi bị pk")
                        self.tatauto = False
                        ini.write(self.namehero + "_tatauto", self.tatauto)
                        self.setChat("1")
                    if chat == "/nd":
                        print(self.namehero, "update nhặt đồ")
                        self.updateListNhatDo()
                        self.setChat("1")
                    if chat == "/tz":
                        self.tatnhatzen = True
                        ini.write(self.namehero + "_tatnhatzen", self.tatnhatzen)
                    if chat == "/bz":
                        self.tatnhatzen = False
                        ini.write(self.namehero + "_tatnhatzen", self.tatnhatzen)

                    if hstr.startSwith(chat, "/mv "):

                        chat + "   "
                        xmv = chat.split(" ")[1]
                        ymv = chat.split(" ")[2]
                        print(self.namehero, "move", xmv, ymv)
                        if xmv and ymv:
                            self.autoMoveXY(int(xmv), int(ymv))
                            time.sleep(1)
                            continue
                    self.classs = self.getClass()
                    # print(chat)
                    self.autopkdie = False
                    if autopknv:
                        if not self.namehero in listnvautopk:
                            listnvautopk.append(self.namehero)
                        hthread.start(autoPKThread, [self.pid])
                        # self.autoPKCheckbox()

                    if "/pkt" in chat:
                        while True:
                            self.autoPKTest()
                            chat2 = self.getChat()
                            if chat2 == "z":
                                break
                            time.sleep(0.05)

                    if "/pk" in chat:
                        timesl = 2
                        typez = chat + "_0"
                        timesl = hstr.regex(typez, "(\\d+)")
                        timesl = int(timesl)
                        kieupk = "pk"
                        if "/pkk" in chat:
                            kieupk = "pkk"
                        if "/pkg" in chat:
                            kieupk = "pkg"
                        if len(chat) <= 5:
                            while True:
                                self.autoPK(True, kieupk, timesl)
                                if self.getHPConLai() == 0:
                                    self.autopkdie = True
                                    break
                                chat2 = self.getChat()
                                if chat2 == "z":
                                    break
                                time.sleep(0.1)
                    if chat == "/bv":
                        self.vemaplientuc = True
                    if chat == "/tv":
                        self.vemaplientuc = False
                    if chat == "/gomk":
                        self.gomQuai()
                    if chat == "/tg":
                        if not self.pid in listnvstopgom:
                            listnvstopgom.append(self.pid)
                            self.startautogom = False
                        self.setChat("1")
                    if chat == "/gom":
                        if self.pid in listnvstopgom:
                            listnvstopgom.remove(self.pid)
                        if not self.startautogom:
                            hthread.start(gomQuaiThread, [self.pid, self.mapauto])
                            self.startautogom = True
                        self.setChat("1")
                    if chat == "/gomp":
                        self.gomQuai()
                    if self.namehero in listbuffpc:
                        self.autoBuffPC()
                        pass
                    phimbamcuoicung = self.getPhimBamCuoiCung()
                    # print(self.namehero, "phimbamcuoicung", phimbamcuoicung)
                    if phimbamcuoicung == "F2":
                        self.saveMapF2()
                    if phimbamcuoicung == "F3":
                        log(f"{htime.getStrTimeNow3()}: {self.namehero} đang tạm dừng. Bấm F4 để chạy tiếp")
                        herostop[self.namehero] = True
                        self.setPhimBamCuoiCung(112)

                    if phimbamcuoicung == "F4" or chat == chatAutoSanBot:
                        log(f"{htime.getStrTimeNow3()}: {self.namehero} đã chạy lại")
                        self.setPhimBamCuoiCung(112)
                        herostop[self.namehero] = False

                    if self.getHPConLai() == 0 or self.autopkdie:
                        if self.autopkdie:
                            self.setChat("1")
                        if self.anmain > 0:
                            self.activateHandle()

                        if self.trainstadium > 0 and self.level >= 20:
                            if "LostTower" in map or "Dungeon" in map or "Elbeland" in map or "Loren_Market" in map or ("Lorencia" in map and self.starttrainstadium):
                                self.waitLive()
                                if self.checkDieuKienVaoStadium():
                                    self.trainMapStadium30p()
                                    continue
                        if self.trainexp > 0 and self.level >= 20 and self.checkDieuKienVaoMapExp() < 3:
                            if "LostTower" in map or "Dungeon" in map or "Elbeland" in map:
                                self.waitLive()
                                self.trainMapExp()
                                continue
                        if "Blagass" in map:
                            continue
                        self.listnvcomatkhibipk = self.quetNV()

                        self.setKeepMouseRight(False)

                        if "LostTower7" in map:
                            self.moveMap("LostTower3")
                            self.timeolot3 = time.time()
                            continue

                        printpk = False
                        movemap = False
                        self.waitLive()
                        if "Karutan2" in map and self.vemaplientuc:
                            self.moveMap("Karutan2", boqualandau=True)
                            continue
                        if "Karutan2" in map or "CryWolf" in map:
                            solanbipkmapkarutan2 = solanbipkmapkarutan2 + 1
                            if solanbipkmapkarutan2 % 3 == 0:
                                movemap = True
                                printpk = True
                        else:
                            printpk = True
                        if printpk:
                            self.rabai = False
                            pktime = time.time()
                            self.pktime.append(pktime)
                        printsolan = solanbipkmapkarutan2
                        if printsolan == 0:
                            if self.pktime:
                                printsolan = len(self.pktime)
                        if printsolan:
                            thongbao = "bị pk"
                            if self.server <= 4 or self.server == 10 or self.server == 18 or not self.listnvcomatkhibipk:
                                thongbao = "bị quái cắn"
                            log(f"{htime.getStrTimeNow3()}: {self.namehero} {thongbao} {printsolan} lần map {map}")
                            tele.sendMessage(UserIDTele, f"{self.namehero} {thongbao} {printsolan} lần map {map}")
                            if movemap:
                                maprandom = hrand.randomItemInList(self.listmapmovekhibipk)
                                # log(f"{htime.getStrTimeNow3()}: {self.namehero} move {maprandom}")
                                self.moveMap(maprandom)
                            if not self.tatauto:
                                self.tatauto = ini.readboolean(self.namehero + "_tatauto")
                            if self.tatauto:
                                herostop[self.namehero] = True
                                tele.sendMessage(UserIDTele, f"{self.namehero} đã ngừng auto ra bãi")
                                log(f"{htime.getStrTimeNow3()}: {self.namehero} đã ngừng auto ra bãi")
                        time.sleep(10)
                        continue

                    if not self.rabai:
                        solanbipk = len(self.pktime)
                        timehientai = time.time()
                        gandaynhat = int(timehientai - self.pktime[-1])
                        sogiaycho = solanbipk * 4 * 60
                        solanbipk = solanbipk % 4
                        if solanbipk == 1:
                            sogiaycho = 10 * 60
                        if solanbipk == 2:
                            sogiaycho = 20 * 60
                        if solanbipk == 3:
                            sogiaycho = 40 * 60
                        if solanbipk == 4:
                            sogiaycho = 60 * 60
                        if not self.sogiaycho:
                            phutrabai = phutRaBai()
                            if phutrabai:
                                sogiaycho = phutrabai * 60
                            self.sogiaycho = hrand.randomInt(sogiaycho, sogiaycho + 240)
                        if self.sogiaycho:
                            sogiaycho = self.sogiaycho
                        rabaingay = False
                        if phimbamcuoicung == "F7" or phimbamcuoicung == "F2" or phimbamcuoicung == "F4":
                            herostop[self.namehero] = False
                            sogiaycho = 0
                            self.sogiaycho = 0
                            self.setPhimBamCuoiCung(112)
                            self.setChat("1")
                            rabaingay = True
                        khoangcachrabai = int(time.time() - lastrabai)
                        if gandaynhat < sogiaycho:
                            conlai = sogiaycho - gandaynhat
                            if conlai % 30 == 0:
                                log(f"{htime.getStrTimeNow3()}: {self.namehero} ra bãi sau {conlai}. Số giây chờ {sogiaycho}")
                            time.sleep(1)
                            continue
                        elif khoangcachrabai < 60 and gandaynhat > sogiaycho and not rabaingay:
                            log(f"{htime.getStrTimeNow3()}: {self.namehero} sẽ ra bãi sau {60-khoangcachrabai}")
                        else:

                            stop = herostop.get(self.namehero, False)
                            if stop:
                                stop = "( Đã ngừng auto từ trước) "
                            else:
                                stop = ""
                            log(f"{htime.getStrTimeNow3()}: {self.namehero} ra bãi. {stop}")
                            tele.sendMessage(UserIDTele, f"{self.namehero} ra bãi. {stop}")
                            self.rabai = True
                            self.sogiaycho = 0
                            self.timerabai = time.time()
                            lastrabai = time.time()
                            solanbipkmapkarutan2 = 0
                    else:
                        if self.pktime:
                            timehientai = time.time()
                            gandaynhat = int(timehientai - self.timerabai)
                            sophutrslai = 30
                            sogiaycho = sophutrslai * 60
                            if gandaynhat > sogiaycho:
                                log(f"{htime.getStrTimeNow3()}: {self.namehero} quá {sogiaycho} giây không bị pk. Tính time lại từ đầu")
                                self.pktime = []
                            else:
                                conlai = sogiaycho - gandaynhat
                                if conlai % 30 == 0 and conlai != 0:
                                    log(f"{htime.getStrTimeNow3()}: {self.namehero} nếu {conlai} giây nữa không bị pk. Tính time lại từ đầu")

                    if herostop.get(self.namehero, False):
                        if chat == chatAutoSanBot:
                            herostop[self.namehero] = False
                            dic["stop"] = herostop.get(self.namehero, False)
                            infos[self.pid] = dic
                        else:
                            stoped = True
                            time.sleep(1)
                            continue

                    if self.annv > 0 and not autopknv and not self.getMoRuongDo():
                        self.anNhanVat()

                    if stoped:
                        khoangcachtrainautoz = self.getKhoangCachTrainAutoZ()
                        batbuffcanhan = self.getBuffCaNhan()
                        batbuffnhom = self.getBuffNhom()
                        timevevitricu = self.getTimeVeViTriCu()
                        tudongtangmau = self.getTuDongTangMau()
                        if khoangcachtrainautoz > 0:
                            ini.write(self.namehero + "_khoangcachtrainautoz", khoangcachtrainautoz)
                            ini.write(self.namehero + "_batbuffcanhan", batbuffcanhan)
                            ini.write(self.namehero + "_batbuffnhom", batbuffnhom)
                            ini.write(self.namehero + "_timevevitricu", timevevitricu)
                            ini.write(self.namehero + "_tudongtangmau", tudongtangmau)
                    stoped = False

                    if keystatus["error"]:
                        statuskey = keystatus["status"]
                        if not chuakichhoat:
                            log(f"{htime.getStrTimeNow3()}: {self.namehero} {statuskey}")
                        time.sleep(1)
                        chuakichhoat = True
                        continue
                    if chuakichhoat:
                        statuskey = keystatus["status"]
                        log(f"{htime.getStrTimeNow3()}: {self.namehero} {statuskey}")
                        chuakichhoat = False

                    if len(apiAnycaptcha) != 32 and len(apiAnycaptcha) != 8 and len(apiAnycaptcha) != 82:
                        result_settings = settings.get("result")
                        apiAnycaptchatmp = result_settings.get("apiAnycaptcha")
                        tokenTelegram = result_settings.get("tokenTelegram")
                        if "_" in tokenTelegram:
                            tokenTelegrams = tokenTelegram.split("_")
                            UserIDTele = tokenTelegrams[len(tokenTelegrams) - 1]
                            TOKEN = tokenTelegram.replace("_" + UserIDTele, "")
                            tele = htele(TOKEN)
                            # print(TOKEN, UserIDTele)

                        # print("apiAnycaptchatmp", apiAnycaptchatmp)
                        if len(apiAnycaptchatmp) != 32 and len(apiAnycaptchatmp) != 8 and len(apiAnycaptchatmp) != 2:
                            log(f"{htime.getStrTimeNow3()}: {self.namehero} chưa cài đặt apiAnycaptcha, kiểm tra lại")
                            time.sleep(1)
                            continue
                        apiAnycaptcha = apiAnycaptchatmp

                    self.level = self.getLevel()
                    if self.level == 10:
                        dareset = False

                    if phimbamcuoicung == "F6":
                        log(f"{htime.getStrTimeNow3()}: {self.namehero} save {map} {x} {y}")
                        self.saveMap(map, (x, y))
                        self.saveServer()
                        self.setPhimBamCuoiCung(112)
                    if chat == "/sb":
                        self.autoSanBoss(map)
                        # self.setChat("1")
                    lastsanbos = False
                    if chat == chatAutoSanBot:
                        self.autoSanBoss247()
                        lastsanbos = True
                    if herostop.get(self.namehero, False):
                        if lastsanbos:
                            self.setChat(chatAutoSanBot)
                        continue
                    if not self.setIdLanDau:
                        for izzz in range(10):
                            log(f"{htime.getStrTimeNow3()}: {self.namehero} sẽ chạy sau {10-izzz} giây")
                            time.sleep(1)
                        self.setIdLanDau = True
                    # print(self.namehero, "cayrs", cayreset, "map", map, "khongthedangnhap", khongthedangnhap)
                    if cayreset and not "Kalima" in map and not khongthedangnhap and not autopknv:
                        clicknhamsv = []
                        quaylaigame = False
                        chonmaychukhac = False
                        while True:
                            
                                
                            x, y = self.getPosHero()
                            map = self.getMap(x, y)
                            if self.chonnv:
                                self.ichonnv = self.ichonnv + 1
                                print(self.namehero, "map", map, "self.ichonnv", self.ichonnv)
                            if map == "Màn hình đăng nhập":
                                with lockbando:
                                    self.ichonmaychukhac = 0
                                    print(self.namehero, "lockbando4")
                                    listpidreset[self.pid] = True
                                    if not dareset and self.level >= levelrs:
                                        log(f"{htime.getStrTimeNow3()}: {self.namehero} đăng nhập tài khoản")
                                        self.clickReloadServer()
                                        quanly = muweb()
                                        quanly.apiAnycaptcha = apiAnycaptcha
                                        login = quanly.login(taikhoandangnhap, pass2)
                                        self.clickReloadServer()
                                        if login:
                                            if len(apiAnycaptcha) == 32:
                                                timest = time.time()
                                                while True:
                                                    timeht = time.time()
                                                    timeconlai = int(timeht - timest)
                                                    if timeconlai >= 30:
                                                        break
                                                    if timeconlai % 4 == 0:
                                                        map = self.getMap(x, y)
                                                        if map != "Màn hình đăng nhập":
                                                            quaylaigame = True
                                                            break
                                                        self.clickReloadServer()
                                                        log(f"{htime.getStrTimeNow3()}: {self.namehero} đợi {30 - timeconlai}")
                                                    time.sleep(1)
                                                if quaylaigame:
                                                    continue
                                            while True:
                                                if quaylaigame:
                                                    break
                                                reset = quanly.reset(self.namehero, True)
                                                if reset:
                                                    log(f"{htime.getStrTimeNow3()}: {self.namehero} reset thành công")
                                                    self.saveServer()
                                                    listnhanvatautopk[self.namehero] = False
                                                    dareset = True
                                                    autoplay = False
                                                    tongpointsaukhirs = 0
                                                    log(f"{htime.getStrTimeNow3()}: {self.namehero} reset thành công...")
                                                    break
                                                if quanly.timechors > 0:
                                                    st = time.time()
                                                    icho = 0
                                                    for zrs in range(quanly.timechors):

                                                        map = self.getMap(x, y)
                                                        if map != "Màn hình đăng nhập":
                                                            quaylaigame = True
                                                            break
                                                        if icho % 4 == 0:
                                                            log(f"{htime.getStrTimeNow3()}: {self.namehero} chờ {quanly.timechors-zrs}")
                                                            self.clickReloadServer()
                                                        if time.time() - st > quanly.timechors:
                                                            break
                                                        icho = icho + 1

                                                        time.sleep(1)
                                                    continue
                                                break
                                        else:
                                            khongthedangnhap = True
                                            # dareset = True
                                            # autoplay = False

                                    if not self.getCuaSoNhapNick():
                                        self.clickReloadServer()
                                        time.sleep(0.5)
                                        lastserver = self.readServerSave()
                                        lastservernhandien = lastserver

                                        if lastserver == 10:
                                            lastserver = 9
                                        if lastserver == 18:
                                            lastserver = 10

                                        # if lastserver == 18:
                                        #     lastserver = 11
                                        lastserver = getServer(lastserver)
                                        xsv, ysv = listserver[lastserver - 1]
                                        if len(clicknhamsv) == 1:
                                            xsv, ysv = listserver[lastserver - 2]
                                        # if len(clicknhamsv) == 2:
                                        #     xsv, ysv = listserver[lastserver]
                                        log(f"{htime.getStrTimeNow3()}: {self.namehero} chọn server {lastservernhandien} {xsv} {ysv}")
                                        self.mouseClick(xsv, ysv)
                                        if len(clicknhamsv) <= 2:
                                            time.sleep(1)
                                            serverclick = self.getServer()
                                            if serverclick != lastservernhandien:
                                                log(f"{htime.getStrTimeNow3()}: {self.namehero} click nhầm server {serverclick}")
                                                clicknhamsv.append(1)
                                                self.mouseClick(474, 450)
                                                time.sleep(1)
                                                continue
                                        self.sendKey("enter")
                                    else:
                                        if len(clicknhamsv) <= 2:
                                            if not lastservernhandien:
                                                lastserver = self.readServerSave()
                                                lastservernhandien = lastserver
                                            serverclick = self.getServer()
                                            if serverclick != lastservernhandien:
                                                log(f"{htime.getStrTimeNow3()}: {self.namehero} click nhầm server {serverclick}")
                                                clicknhamsv.append(1)
                                                self.mouseClick(474, 450)
                                                time.sleep(1)
                                                continue
                                        self.sendKey("enter")
                                        # self.mouseClick(408, 453)
                                    time.sleep(0.5)
                            elif map == "Màn hình chọn tướng":
                                with lockbando:
                                    self.chonNhanVat(self.namehero)
                                    self.chonnv = True
                                    self.batMenuThoatGame(False)
                            else:
                                # print(self.namehero, map)

                                break
                            time.sleep(1)
                        if khongthedangnhap:
                            ikhongthedangnhapreset = ikhongthedangnhapreset + 14
                            if ikhongthedangnhapreset > 100:
                                khongthedangnhap = False
                        if not dareset and self.level >= levelrs and not "Màn hình" in map and not khongthedangnhap and not self.webBaoTri():
                            now = datetime.now()
                            hour = now.hour
                            minute = now.minute
                            rsgionay = True
                            if self.server == 5:
                                if hour == 18 or (hour == 19 and minute < 5):
                                    rsgionay = False
                            if self.server == 6:
                                if hour == 19 or (hour == 20 and minute < 5):
                                    rsgionay = False
                            if self.server == 7:
                                if hour == 20 or (hour == 21 and minute < 5):
                                    rsgionay = False
                            if self.server == 8:
                                if hour == 21 or (hour == 22 and minute < 5):
                                    rsgionay = False
                            if rsgionay:
                                dudieukienreset = True
                                dtreseted = 0
                                timetru = 0

                                reseted = ini.read(self.namehero + "_reseted")
                                if not reseted:
                                    ini.write(self.namehero + "_reseted", htime.getStrTimeNowNguyenBan())
                                    reseted = ini.read(self.namehero + "_reseted")

                                # 2022-08-14 13:50:42.435036
                                dtreseted = htime.strTimeNowNguyenBanToDateTime(reseted)
                                dtnow = htime.getTimeNowNguyenBan()
                                timetru = htime.truDateTime(dtnow, dtreseted)
                                if timetru < sophutrs * 60 + 1:
                                    dudieukienreset = False
                                    if iprintchuadurs == 0:
                                        log(f"{htime.getStrTimeNow3()}: {self.namehero} reset lần cuối {dtreseted} chưa đủ {sophutrs} phút để reset")
                                    iprintchuadurs = iprintchuadurs + 1
                                else:
                                    log(f"{htime.getStrTimeNow3()}: {self.namehero} reset lần cuối {dtreseted} đã đủ {sophutrs} phút để reset")
                                    iprintchuadurs = 0
                                    dudieukienreset = True
                                if dudieukienreset and not self.isReseting():
                                    with lockbando:
                                        print(htime.getStrTimeNow3(), self.namehero, "check isReseting")
                                        reseting = self.isReseting()
                                        print(htime.getStrTimeNow3(), self.namehero, "reseting", reseting)
                                        popup = self.getPopupBanDo()
                                        if popup:
                                            self.sendKey("enter")
                                        time.sleep(1)
                                        if not reseting:
                                            if self.resetingame:
                                                log(f"{htime.getStrTimeNow3()}: {self.namehero} reset ingame")
                                                self.autoResetIngame()
                                                continue
                                            print(htime.getStrTimeNow3(), self.namehero, "chọn máy chủ khác. reseting = True")
                                            # print(htime.getStrTimeNow3(), self.namehero, "lockbando5")
                                            listpidreset[self.pid] = True
                                            log(f"{htime.getStrTimeNow3()}: {self.namehero} bấm thoát game")
                                            self.batMenuThoatGame(True)
                                            time.sleep(1)
                                            if self.getMenuThoatGame():
                                                listnhanvatautopk[self.namehero] = False
                                                log(f"{htime.getStrTimeNow3()}: {self.namehero} chọn máy chủ khác")
                                                
                                                self.daBatMenuThoatGame = True
                                                print(self.namehero, self.hwnd, 443, 314)
                                                self.clickHwnd(443, 314)
                                                self.ichonmaychukhac = self.ichonmaychukhac + 1
                                                chonmaychukhac = True
                                                self.sendKey("enter")
                                                time.sleep(6)
                                                continue
                                            else:
                                                self.ichonmaychukhac = self.ichonmaychukhac + 1
                    if chat == "/gom1":
                        self.autoGomQuaiSatViTri()
                        continue
                    if chat == "/kc":
                        self.setKeepMouseRight(True)

                    self.level = self.getLevel()
                    if self.level >= 168 and self.level != 400:
                        point = self.getPoint()
                        if point >= 1000:
                            self.getInfoCongDiem()
                            if self.congdiem300lv:
                                self.setMacroChat(f"/{self.congdiem300lv} {point}")
                                with lockbando:
                                    print(self.namehero, "lockbando7z")
                                    self.callMacroChat()

                    if "Màn hình" in map:
                        time.sleep(1)
                        continue

                    if herostop.get(self.namehero, False):
                        continue
                    if self.level == 10 and not autoplay:
                        # stamina = self.getStaminaAll()
                        # if stamina > 200:
                        #     continue
                        point = self.getPoint()
                        log(f"{htime.getStrTimeNow3()}: {self.namehero} cộng điểm {point} {map} {self.level}")
                        batCOk = False
                        for batC in range(5):
                            if not self.getBatThongTinC():
                                # self.sendKey()
                                with lockbando:
                                    print(self.namehero, "lockbando6")
                                    self.clickHwnd(75, 599)
                                    self.sendKey("enter")
                                    time.sleep(0.5)
                                    self.tatBatChat()
                                    time.sleep(1)
                                continue
                            else:
                                batCOk = True
                                break
                        if not batCOk:
                            continue

                        point = self.getPoint()

                        if tongpointsaukhirs == 0:
                            tongpointsaukhirs = point
                        if point == 0:
                            autoplay = True
                        else:
                            self.chonnv = False
                            self.ichonnv = 0
                            infocongdiem = self.getInfoCongDiem()
                            if not infocongdiem:
                                log(f"{htime.getStrTimeNow3()}: {self.namehero} chưa cài đặt cộng điểm")
                                time.sleep(200)
                                continue
                            pointstr = infocongdiem[0]
                            pointagi = infocongdiem[1]
                            pointvit = infocongdiem[2]
                            pointene = infocongdiem[3]
                            pointcmd = infocongdiem[4]
                            # log(f"{htime.getStrTimeNow3()}: {self.namehero} pointene {pointene}")
                            if pointstr < 0:
                                pointstr = tongpointsaukhirs - pointagi - pointvit - pointene - pointcmd
                            elif pointagi < 0:
                                pointagi = tongpointsaukhirs - pointstr - pointvit - pointene - pointcmd
                            elif pointvit < 0:
                                pointvit = tongpointsaukhirs - pointstr - pointagi - pointene - pointcmd
                            elif pointene < 0:
                                pointene = tongpointsaukhirs - pointstr - pointagi - pointvit - pointcmd
                            elif pointcmd < 0:
                                pointcmd = tongpointsaukhirs - pointstr - pointagi - pointvit - pointene
                            # log(f"{htime.getStrTimeNow3()}: {self.namehero} {pointstr} - {pointagi} - {pointvit} - {pointene} - {pointcmd}")
                            if pointene < 0 or pointcmd < 0 or pointagi < 0 or pointstr < 0 or pointvit < 0:
                                log(f"{htime.getStrTimeNow3()}: {self.namehero} có lỗi khi cộng point, hãy tự cộng nốt")
                                time.sleep(2)
                                continue
                            congok = 0
                            if pointagi == 0:
                                congok = congok + 1
                            if pointstr == 0:
                                congok = congok + 1
                            if pointene == 0:
                                congok = congok + 1
                            if pointvit == 0:
                                congok = congok + 1
                            if pointcmd == 0:
                                congok = congok + 1

                            if pointagi > 0:

                                agidacong = self.getDiemAgi()

                                if agidacong < pointagi:
                                    self.batMenuThoatGame(False)
                                    if pointagi > point:
                                        pointagi = point
                                    print(self.namehero, "addagi", pointagi)
                                    self.setMacroChat(f"/addagi {pointagi}")
                                    with lockbando:
                                        print(self.namehero, "lockbando7")
                                        self.callMacroChat()
                                    time.sleep(4)
                                else:
                                    congok = congok + 1

                            if pointene > 0:

                                enedacong = self.getDiemEne()

                                if enedacong < pointene:
                                    if pointene > point:
                                        pointene = point

                                    print(self.namehero, "addene", pointene)
                                    self.setMacroChat(f"/addene {pointene}")
                                    with lockbando:
                                        print(self.namehero, "lockbando8")
                                        self.callMacroChat()
                                    time.sleep(4)
                                else:
                                    congok = congok + 1
                            if pointstr > 0:

                                strdacong = self.getDiemStr()

                                if strdacong < pointstr:
                                    if pointstr > point:
                                        pointstr = point
                                    # self.sendKey("enter")

                                    # hwin.sendText(f"/addstr {pointstr}")
                                    # self.sendKey("enter")
                                    print(self.namehero, "addstr", pointstr)
                                    self.setMacroChat(f"/addstr {pointstr}")
                                    with lockbando:
                                        print(self.namehero, "lockbando9")
                                        self.callMacroChat()
                                    time.sleep(4)
                                else:
                                    congok = congok + 1
                            if pointvit > 0:

                                vitdacong = self.getDiemVit()

                                if vitdacong < pointvit:
                                    if pointvit > point:
                                        pointvit = point

                                    print(self.namehero, "addvit", pointvit)
                                    self.setMacroChat(f"/addvit {pointvit}")
                                    with lockbando:
                                        print(self.namehero, "lockbando10")
                                        self.callMacroChat()
                                    time.sleep(4)
                                else:
                                    congok = congok + 1
                            if pointcmd > 0:

                                cmddacong = self.getDiemCmd()

                                if cmddacong < pointcmd:
                                    if pointcmd > point:
                                        pointcmd = point

                                    print(self.namehero, "addcmd", pointcmd)
                                    self.setMacroChat(f"/addcmd {pointcmd}")
                                    with lockbando:
                                        print(self.namehero, "lockbando11")
                                        self.callMacroChat()
                                else:
                                    congok = congok + 1
                            if congok >= 5:
                                autoplay = True
                        if autoplay:
                            listpidreset[self.pid] = False
                        continue

                    if map == "Arena" and not self.starttrainstadium:
                        time.sleep(0.5)
                        continue
                    # if self.namehero == "KoThichBuf":
                    #     self.starttrainstadium = True
                    if map != "Arena":
                        self.starttrainstadium = False
                        self.iarenarunning = 0

                    if "Blagass" in map:
                        if self.getIdSkill1() > 0:
                            self.activeSkill3(False)
                        else:
                            self.activeSkill3(True)
                        self.autoMoveXY(97, 186)
                        if not self.nhatTatCa:
                            self.setNhatTatCa(True)
                            self.setNhatTheoDanhSach(False)
                            self.nhatTatCa = True
                        if khoangcachtrainautoz <= 0:
                            khoangcachtrainautoz = ini.readint(self.namehero + "_khoangcachtrainautoz", 0)
                            batbuffcanhan = ini.readboolean(self.namehero + "_batbuffcanhan")
                            batbuffnhom = ini.readboolean(self.namehero + "_batbuffnhom")
                            timevevitricu = ini.readint(self.namehero + "_timevevitricu", 0)
                            tudongtangmau = ini.readboolean(self.namehero + "_tudongtangmau")
                        self.setKhoangCachTrainAutoZ(khoangcachtrainautoz)
                        self.setKhoangCachNhatDoAutoZ(10)
                        self.setBuffCaNhan(batbuffcanhan)
                        self.setBuffNhom(batbuffnhom)
                        self.setTimeVeViTriCu(timevevitricu)
                        self.setTuDongTangMau(tudongtangmau)
                    else:
                        if self.nhatTatCa or self.getNhatTatCa() > 0:
                            self.setNhatTatCa(False)
                            self.setNhatTheoDanhSach(True)
                            self.nhatTatCa = False
                    if "Kalima" in map or "Blagass" in map:
                        time.sleep(0.5)
                        continue
                    mapautoz = self.getMapAuto()
                    mapauto = mapautoz.get("map")
                    self.mapauto = mapauto
                    xauto = mapautoz.get("x")
                    yauto = mapautoz.get("y")

                    if xauto <= 0:
                        time.sleep(0.5)
                        continue
                    classs = self.getClass()
                    self.classs = classs
                    self.hackKhoangCach()
                    xymove = (0, 0)
                    dulv = False
                    kichbanht_map = ""
                    if classs == "dl" or classs == "rf" or classs == "mg" or classs == "gl":
                        if self.level < 26:
                            kichbanht_map = "Elbeland3"
                            dulv = False
                            xauto = 194
                            yauto = 144
                        elif self.level < 46:
                            kichbanht_map = "Dungeon2"
                            dulv = False
                            xauto = 230
                            yauto = 116

                        else:
                            dulv = False
                            if "Tarkan" in mapauto:
                                if self.level >= 93:
                                    dulv = True
                            if "Karutan" in mapauto:
                                if self.level >= 113:
                                    dulv = True
                            if "Kanturu_ruin" in mapauto:
                                if self.level >= 106:
                                    dulv = True
                            if "Kanturu_Remain" in mapauto:
                                if self.level >= 153:
                                    dulv = True
                            if "CryWolf" in mapauto:
                                if self.level >= 10:
                                    dulv = True
                            if "Icarus" in mapauto:
                                if self.level >= 113:
                                    dulv = True
                            if "Atlans" in mapauto:
                                if self.level >= 53:
                                    dulv = True
                            if "LostTower5" in mapauto:
                                if self.level >= 40:
                                    dulv = True
                            if "Dungeon2" in mapauto:
                                if self.level >= 26:
                                    dulv = True
                            if not dulv:
                                if "Karutan" in map or "Kanturu" in map or "LostTower3" in map or "Devias2" in map:
                                    dulv = True
                                    if "LostTower3" in map or "Devias2" in map:
                                        mapauto = map
                                        timedaolot3 = int(time.time() - self.timeolot3)
                                        print(self.namehero, f"Time ở {mapauto} còn lại {300 - timedaolot3}")
                                        if timedaolot3 > 300:
                                            dulv = False

                    else:
                        if self.level < 40:
                            dulv = False
                            kichbanht_map = "Elbeland3"
                            xauto = 194
                            yauto = 144

                        elif self.level < 70:
                            dulv = False
                            kichbanht_map = "Dungeon2"
                            xauto = 230
                            yauto = 116
                        else:
                            dulv = False
                            if "Tarkan" in mapauto:
                                if self.level >= 140:
                                    dulv = True
                            if "Karutan" in mapauto:
                                if self.level >= 170:
                                    dulv = True
                            if "Kanturu_ruin" in mapauto:
                                if self.level >= 160:
                                    dulv = True
                            if "Kanturu_Remain" in mapauto:
                                if self.level >= 230:
                                    dulv = True
                            if "CryWolf" in mapauto:
                                if self.level >= 10:
                                    dulv = True
                            if "Icarus" in mapauto:
                                if self.level >= 170:
                                    dulv = True
                            if "Atlans" in mapauto:
                                if self.level >= 80:
                                    dulv = True
                            if "LostTower5" in mapauto:
                                if self.level >= 60:
                                    dulv = True
                            if "Dungeon2" in mapauto:
                                if self.level >= 40:
                                    dulv = True
                            if not dulv:
                                if "Karutan" in map or "Kanturu" in map or "LostTower3" in map or "Devias2" in map:
                                    dulv = True
                                    if "LostTower3" in map or "Devias2" in map:
                                        mapauto = map
                                        timedaolot3 = int(time.time() - self.timeolot3)
                                        print(self.namehero, f"Time ở {mapauto} còn lại {300 - timedaolot3}")
                                        if timedaolot3 > 300:
                                            dulv = False
                    # print(dulv, "kichbanht_map", kichbanht_map)
                    if "Swamp_Of_Calmness" in mapauto:
                        if self.level >= 400:
                            dulv = True
                    if dulv:
                        if mapauto == "Karutan1":
                            rak2 = False
                            if self.getTrongThanh() or map != "Karutan1":
                                if xauto > 166 and yauto > 146:
                                    rak2 = True
                            if rak2 and map != "Karutan2":
                                self.moveMap("Karutan2")
                                time.sleep(1)
                                continue
                            if map == "Karutan2":
                                x, y = self.getPosHero()
                                if y < 22:
                                    self.autoMoveXY(162, 0)
                                    time.sleep(1)
                                    continue
                        if map != mapauto:
                            self.moveMap(mapauto)
                        xymove = (xauto, yauto)
                    if not dulv and map != "Arena":
                        if not kichbanht_map:
                            kichbanht_map = "LostTower7"
                            xymove = (54, 91)
                        else:
                            xymove = (xauto, yauto)
                        if map != kichbanht_map:
                            self.moveMap(kichbanht_map)

                    if map == "LostTower3":
                        dt = datetime.now()
                        minute = dt.minute
                        movetoadosau = True
                        if minute < 3 or minute > 7:
                            nv = self.quetNV(False)
                            xauto = 91
                            yauto = 171
                            movetoadosau = False
                            if nv:
                                movetoadosau = True
                        if movetoadosau:
                            xauto = 102
                            yauto = 168
                        xymove = (xauto, yauto)
                    if map == "Devias2":
                        dt = datetime.now()
                        giay = dt.second
                        if giay < 30:
                            xauto = 36
                            yauto = 18
                        else:
                            xauto = 37
                            yauto = 34
                        xymove = (xauto, yauto)
                    if map == "Karutan2" and self.vemaplientuc:
                        xauto = 164
                        yauto = 17
                        xymove = (xauto, yauto)
                    if map == "Arena" and self.starttrainstadium:
                        if self.iarenarunning >= len(self.listtoadoarenatrain):
                            self.iarenarunning = 0
                            self.listtoadoarenatrain.reverse()

                        xymove = self.listtoadoarenatrain[self.iarenarunning]
                    if xymove[0] == 0:
                        time.sleep(0.5)
                        continue
                    kichbanht_x = xymove[0]
                    kichbanht_y = xymove[1]
                    x, y = self.getPosHero()
                    xtru = hstr.triTuyetDoi(kichbanht_x - x)
                    ytru = hstr.triTuyetDoi(kichbanht_y - y)
                    if self.listnvcomatkhibipk:
                        iquetnv = iquetnv + 1
                        if iquetnv % 5 == 0:
                            listnvcomatht = self.quetNV()
                            if listnvcomatht:
                                for z123s in listnvcomatht:
                                    if z123s in self.listnvcomatkhibipk:
                                        if iprintheodoi % 5 == 0:
                                            tele.sendMessage(UserIDTele, f"{namehero} đang bị {z123s} theo dõi")
                                            iprintheodoi = iprintheodoi + 1
                    ratoibai = False
                    khoangcachnhandien = 10
                    if map == "Arena":
                        khoangcachnhandien = 5
                    if xtru < khoangcachnhandien and ytru < khoangcachnhandien:
                        # print(self.namehero, self.starttrainstadium, map, "ok")
                        ratoibai = True
                        if not timeratoibai:
                            timeratoibai = time.time()
                        elif time.time() - timeratoibai > 3:
                            if map == "Arena" and self.starttrainstadium:
                                if self.getIdSkill1() > 0:
                                    self.activeSkill3(False)
                                else:
                                    self.activeSkill3(True)
                                if len(self.quetNV()) > 1:
                                    time.sleep(5)
                                    if len(self.quetNV()) > 1:
                                        self.iarenarunning = self.iarenarunning + 1
                                        time.sleep(0.5)
                                        continue
                                self.setNhatZen(False)
                            elif "Devias" in map or "LostTower" in map or "Elbeland" in map or "Dungeon" in map:
                                # if self.classs == "elf":
                                self.activeSkill3(True)
                                self.setNhatZen(False)
                            elif map == mapauto:
                                self.setNhatZen(not self.tatnhatzen)
                            if khoangcachtrainautoz <= 0:
                                khoangcachtrainautoz = ini.readint(self.namehero + "_khoangcachtrainautoz", 0)
                                batbuffcanhan = ini.readboolean(self.namehero + "_batbuffcanhan")
                                batbuffnhom = ini.readboolean(self.namehero + "_batbuffnhom")
                                timevevitricu = ini.readint(self.namehero + "_timevevitricu", 0)
                                tudongtangmau = ini.readboolean(self.namehero + "_tudongtangmau")

                            self.setKhoangCachTrainAutoZ(khoangcachtrainautoz)
                            # self.setNhatSuKien(True)
                            self.setKhoangCachNhatDoAutoZ(khoangcachnhandien)
                            self.setBuffCaNhan(batbuffcanhan)
                            self.setBuffNhom(batbuffnhom)
                            self.setTimeVeViTriCu(timevevitricu)
                            self.autoMoveXY(hrand.randomInt(kichbanht_x - 1, kichbanht_x + 1), hrand.randomInt(kichbanht_y - 1, kichbanht_y + 1))
                            self.setKeepMouseLeft(False)
                            time.sleep(1)
                    trongthanh = self.getTrongThanh()
                    if not ratoibai and (xtru > 20 or ytru > 20):
                        self.setKhoangCachNhatDoAutoZ(0)
                        if testmove:
                            if trongthanh:
                                pass
                            elif map == "Karutan1" and y > 203:
                                pass
                            # hwin.moveMouse(0, 0, 0)
                            elif kichbanht_x < x:
                                self.setZoomMap()
                                if xtru > 15:
                                    if kichbanht_y < y:
                                        print(self.namehero, kichbanht_x, kichbanht_y, x, y, "move 1111")
                                        self.setMousePosition(312, 270)
                                        # self.setMousePosition(396, 201)
                                    elif kichbanht_y > y:
                                        print(self.namehero, kichbanht_x, kichbanht_y, x, y, "move 2222")
                                        self.setMousePosition(324, 134)
                                    else:
                                        print(self.namehero, kichbanht_x, kichbanht_y, x, y, "move 3333")
                                        self.setMousePosition(269, 184)

                                    self.setKeepMouseLeft(True)
                                    time.sleep(0.5)
                                    self.setKeepMouseLeft(False)
                                    # self.win.set_always_on_top("off")
                                else:
                                    if kichbanht_y < y:
                                        print(self.namehero, kichbanht_x, kichbanht_y, x, y, "move aaa")
                                        self.setMousePosition(10, 336)
                                        # self.setMousePosition(248, 263)
                                        # self.setMousePosition(396, 201)
                                    elif kichbanht_y > y:
                                        print(self.namehero, kichbanht_x, kichbanht_y, x, y, "move bbb")
                                        self.setMousePosition(324, 134)
                                    else:
                                        print(self.namehero, kichbanht_x, kichbanht_y, x, y, "move ccc")
                                        self.setMousePosition(269, 184)
                                    self.setKeepMouseLeft(True)
                                    time.sleep(0.5)
                                    self.setKeepMouseLeft(False)
                                    # self.win.set_always_on_top("off")
                            else:
                                self.setZoomMap()
                                if xtru > 15:
                                    if kichbanht_y < y:
                                        print(self.namehero, kichbanht_x, kichbanht_y, x, y, "move 4444")
                                        self.setMousePosition(319, 297)
                                    elif kichbanht_y > y:
                                        print(self.namehero, kichbanht_x, kichbanht_y, x, y, "move 5555")
                                        self.setMousePosition(409, 227)
                                    else:
                                        print(self.namehero, kichbanht_x, kichbanht_y, x, y, "move 6666")
                                        self.setMousePosition(383, 286)
                                    self.setKeepMouseLeft(True)
                                    time.sleep(1)
                                    self.setKeepMouseLeft(False)
                                    # self.win.set_always_on_top("off")
                                else:
                                    if kichbanht_y < y:
                                        print(self.namehero, kichbanht_x, kichbanht_y, x, y, "move xxx")
                                        self.setMousePosition(10, 336)
                                        # self.setMousePosition(248, 263)
                                        # self.setMousePosition(396, 201)
                                    elif kichbanht_y > y:
                                        print(self.namehero, kichbanht_x, kichbanht_y, x, y, "move yyy")
                                        self.setMousePosition(324, 134)
                                    else:
                                        print(self.namehero, kichbanht_x, kichbanht_y, x, y, "move zzz")
                                        self.setMousePosition(269, 184)
                                    self.setKeepMouseLeft(True)
                                    time.sleep(0.5)
                                    self.setKeepMouseLeft(False)
                                    # self.win.set_always_on_top("off")
                    self.moved = False
                    if not ratoibai:
                        if trongthanh:
                            self.setTuDongTangMau(False)
                        else:
                            self.setTuDongTangMau(tudongtangmau)

                        timeratoibai = 0
                        batbuffcanhantmp = self.getBuffCaNhan()
                        if batbuffcanhantmp:
                            batbuffcanhan = batbuffcanhantmp
                        batbuffnhomtmp = self.getBuffNhom()
                        if batbuffnhomtmp:
                            batbuffnhom = batbuffnhomtmp
                        khoangcachtrainautoztmp = self.getKhoangCachTrainAutoZ()
                        if khoangcachtrainautoztmp > 0:
                            khoangcachtrainautoz = khoangcachtrainautoztmp
                        timevevitricutmp = self.getTimeVeViTriCu()
                        if timevevitricutmp > 0:
                            timevevitricu = timevevitricutmp
                        self.setTimeVeViTriCu(0)
                        self.setKhoangCachTrainAutoZ(0)

                        # self.setNhatZen(False)
                        # self.setNhatSuKien(False)
                        self.setBuffCaNhan(False)
                        self.setBuffNhom(False)
                        self.activeSkill3(False)

                        # self.autoMoveXY(kichbanht_x, kichbanht_y)

                        # elif kichbanht_y < y:
                        #     self.setZoomMap()
                        #     self.setMousePosition(248, 261)
                        #     self.setKeepMouseLeft(True)
                        # elif kichbanht_y > y:
                        #     self.setZoomMap()
                        #     self.setMousePosition(401, 160)
                        #     self.setKeepMouseLeft(True)

                        # elif kichbanht_x > x:
                        #     self.setZoomMap()
                        #     self.setMousePosition(360, 246)
                        #     self.setKeepMouseLeft(True)
                        # time.sleep(0.1)
                        # giay = datetime.now().second
                        # if giay % 5 == 0:
                        #     self.setVeViTriCu(False)
                        #     time.sleep(3)
                        # else:
                        #     self.setVeViTriCu(True)
                    # if map == "Karutan2":
                    #     if x > 125 and x < 150 and y > 127 and not autopknv:
                    #         self.autoMoveXY(140, 121)
                    # print(map)
                    if map == "Swamp_Of_Calmness":                    
                        if 150 <= kichbanht_x <= 240 and 6 <= kichbanht_y <= 96:
                            if y > 96:
                                self.autoMoveXY(151, 110) #bên phải
                            elif x < 222 and y < 16:
                                self.autoMoveXY(222, 15) #bên phải
                    if map == "Karutan1":
                        # if x < 90:
                        #     self.setBuffCaNhan(batbuffcanhan)
                        #     self.setBuffNhom(batbuffnhom)
                        # print(kichbanht_x, kichbanht_y)
                        if kichbanht_x > 140 and kichbanht_y < 90:
                            if y > 89:
                                self.autoMoveXY(137, 87)
                        elif kichbanht_y > 150 and kichbanht_x > 140:
                            if y < 152:
                                self.autoMoveXY(136, 153)
                        elif kichbanht_y > 141 and kichbanht_x > 169:
                            if x < 169:
                                self.autoMoveXY(169, 116)
                        # elif kichbanht_x < 70 and y < 100:
                        #     # bên trên
                        #     if trongthanh:
                        #         self.autoMoveXY(102, 117)
                        #     elif x >= 90 and x <= 95 and y >= 107 and y <= 111:
                        #         self.autoMoveXY(67, 123)
                        elif (kichbanht_x > 55 and kichbanht_x < 105 and kichbanht_y < 137) or (kichbanht_x < 70 and kichbanht_y < 100):
                            # bên trên
                            if trongthanh:
                                self.autoMoveXY(102, 117)
                                print("mv1")
                            elif x >= 80 and x <= 95 and y >= 107 and y <= 116:
                                print("mv2")
                                self.autoMoveXY(67, 123)
                            elif x >= 61 and x <= 62 and y >= 107 and y <= 113:
                                print("mv3")
                                self.autoMoveXY(86, 73)
                            elif x >= 67 and x <= 76 and y >= 87 and y <= 95:
                                print("mv3")
                                self.autoMoveXY(86, 73)
                        elif kichbanht_x < 76 and kichbanht_y > 70:
                            # bên phải
                            if trongthanh:
                                self.autoMoveXY(131, 152)
                            elif x >= 87 and x <= 91 and y >= 161 and y <= 164:
                                self.autoMoveXY(82, 173)
                            elif x > 119:
                                self.autoMoveXY(119, 169)
                                # if x > 119 and y < 150:
                                # self.autoMoveXY(119, 169)

                        # elif kichbanht_x < 76 and kichbanht_y < 116:
                        #     if x > 119:
                        #         self.autoMoveXY(119, 169)
                        #     elif x > 70:
                        #         self.autoMoveXY(70, 171)
                    if map == "Icarus":
                        if kichbanht_y > 117:
                            if y < 56:
                                self.autoMoveXY(92, 57)
                            elif y > 56 and y < 89 and x > 45:
                                self.autoMoveXY(39, 76)
                    if map == "Dungeon2":
                        if y > 127:
                            self.moveMap("Lorencia")
                    if map == "Tarkan2":
                        if kichbanht_x > 141:
                            if x < 141:
                                self.autoMoveXY(143, 178)
                    if map == "Devias2":
                        if x > 177:
                            self.autoMoveXY(172, 43)
                        elif x > 100:
                            self.autoMoveXY(95, 24)
                    if map == "Barrack":
                        if kichbanht_y < 124:
                            if y < 124:
                                self.autoMoveXY(61, 124)
                    if map == "Kanturu_Remain":
                        if kichbanht_x < 129 and kichbanht_y > 120:
                            if x < 105 and y < 120:
                                self.autoMoveXY(106, 96)
                            elif x < 152 and y < 111:
                                self.autoMoveXY(152, 111)
                            elif x > 129:
                                self.autoMoveXY(127, 136)
                        elif kichbanht_y > 111:
                            if x < 105:
                                self.autoMoveXY(106, 96)
                            elif x < 152 and y < 111:
                                self.autoMoveXY(152, 111)
                        elif kichbanht_x > 105:
                            if x < 105:
                                self.autoMoveXY(106, 96)

                    if map == "Kanturu_ruin2":
                        if kichbanht_x < 87:
                            if x > 126:
                                self.autoMoveXY(126, 34)
                            elif x > 103:
                                self.autoMoveXY(103, 64)
                            elif x > 46 and y > 37:
                                self.autoMoveXY(46, 37)
                        elif kichbanht_x < 126:
                            if x > 134:
                                self.autoMoveXY(126, 34)
                    if not self.moved:
                        self.autoMoveXY(kichbanht_x, kichbanht_y)
                    time.sleep(0.5)
                    continue
                except Exception as e:
                    fai = hfile.getError()
                    log(f"fauto {fai}")
                time.sleep(0.1)

    def getMap(self, x=0, y=0):
        idmap = self.getIdMap()
        for i in listmap:
            id, name = i
            if id == idmap:
                if name == "LostTower":
                    if x >= 6 and x <= 57 and y >= 85 and y <= 100:
                        return name + "7"
                    if x >= 6 and x <= 57 and y >= 140 and y <= 300:
                        return name + "7"
                    if x >= 80 and x <= 109 and y >= 165 and y <= 300:
                        return name + "3"
                    if x >= 80 and x <= 135 and y >= 5 and y <= 60:
                        return name + "5"
                    if x >= 187 and x <= 250 and y >= 50 and y <= 200:
                        return name + "0"

                if name == "Kanturu_ruin":
                    if x >= 43 and x <= 195 and y >= 82 and y <= 190:
                        return name + "_island"
                    if x >= 101 and x <= 238 and y >= 0 and y <= 100:
                        return name + "2"
                    if y <= 107:
                        return name + "2"
                if name == "Devias":
                    if x < 90 and y < 70:
                        return name + "2"
                if name == "Atlans2":
                    if x < 85 and y < 132:
                        return "Atlans"

                if name == "Elbeland3":
                    if x < 100:
                        return "Elbeland"
                if name == "Dungeon":
                    if x > 200:
                        return "Dungeon2"
                if name == "Tarkan2":
                    if y < 116:
                        return "Tarkan"
                return name
        return str(idmap)
    def autoResetIngame(self):
        
        for i in range(30):
            if not listnhanvatautoreset.get(self.namehero, False):
                return
            map = self.getMap()
            if "Lorencia" not in map:
                self.moveMap("Lorencia")
                time.sleep(1)
                continue
            self.setBuffCaNhan(False)
            x,y = self.getPosHero()
            if x != 131 and y != 126:            
                self.autoMoveXY(131,126)
                time.sleep(1)
                continue
            self.setZoomMap()        
            for z in range(3):
                self.mouseClick(449, 230)
                time.sleep(1)
            self.mouseClick(522,400)
            self.mouseClick(606,472) #606 472
            self.moveMap("Elbeland3")
            if self.getLevel() == 10:
                return True
            time.sleep(1)
        return False
    def getPhimBamCuoiCungMem(self):
        x = self.mem.read4Byte('"main.exe"+09A7C150', [0x1F4, 0x30, 0xC, 0x8, 0x104, 0x10, 0x64])
        if x == 1 or x == 0:  # chuột trái, chuột phải
            return ""
        if x == 113:
            return "F2"
        if x == 114:
            return "F3"
        if x == 115:
            return "F4"
        if x == 116:
            return "F5"
        if x == 117:
            return "F6"
        if x == 118:
            return "F7"
        return str(x)
        
    


    def getPhimBamCuoiCung(self):
        return dictphimbamcuoicung.get(self.pid, False)

    def setPhimBamCuoiCung(self, value):
        self.mem.write4Byte('"main.exe"+09A7C150', [0x1F4, 0x30, 0xC, 0x8, 0x104, 0x10, 0x64], value)

    def getDiemStr(self):
        x = self.mem.read2Byte('"main.exe"+09B563D0', [0xDC, 0x160, 0x104, 0x10, 0x180])
        return x

    def getDiemAgi(self):
        x = self.mem.read2Byte('"main.exe"+09B563D0', [0xDC, 0x160, 0x104, 0x10, 0x180 + 0x4])
        return x

    def getDiemVit(self):
        x = self.mem.read2Byte('"main.exe"+09B563D0', [0xDC, 0x160, 0x104, 0x10, 0x180 + 0x4 + 0x4])
        return x

    def getDiemEne(self):
        x = self.mem.read2Byte('"main.exe"+09B563D0', [0xDC, 0x160, 0x104, 0x10, 0x180 + 0x4 + 0x4 + 0x4])
        return x

    def getDiemCmd(self):
        x = self.mem.read2Byte('"main.exe"+09B563D0', [0xDC, 0x160, 0x104, 0x10, 0x180 + 0x4 + 0x4 + 0x4 + 0x4])
        return x

    def getTongNangLuong(self):
        x = self.mem.read2Byte("XIProject.dll+F311C")
        return x

    def getPoint(self):

        x = self.mem.read4Byte('"main.exe"+09B563D0', [0xDC, 0x160, 0x104, 0x10, 0x78])
        return x

    def getPosHero(self):
        x = self.mem.read4Byte('"main.exe"+09B563D0', [0xDC, 0x178, 0x104, 0xC, 0x70])
        y = self.mem.read4Byte('"main.exe"+09B563D0', [0xDC, 0x178, 0x104, 0xC, 0x74])
        return x, y

    def getPosHeroFloat(self):
        x = self.mem.read4Byte(0x09E77CE0, [0x114 - 0x37C])
        y = self.mem.read4Byte(0x09E77CE0, [0x114 - 0x37C + 0x4])
        return x, y

    def getLevel(self):
        name = self.mem.read4Byte(0x9F50D18, [0x10C])
        return name

    def getTaiKhoanDangNhap(self):
        try:
            name = self.mem.readString(0x09F4CA3C)
            return name
        except:
            return "-1"

    def getMatKhauDangNhap(self):
        name = self.mem.readString("XIProject.dll+F16CD")
        return name

    def setMatKhauGhiNho(self, value):
        name = self.mem.writeString("XIProject.dll+F18DC", None, value, [0x0,0x0])
        
        return name

    def getTaiKhoanGhiNho(self):
        name = self.mem.readString(0x09F4C684)
        return name

    def setTaiKhoanGhiNho(self, value):
        self.mem.writeByteArray(0x09F4C684, None, "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00")
        self.mem.writeString(0x09F4C684, None, value)

    def getNameHero(self):
        try:
            # name = self.mem.readString(0x14477D4, [0xC])
            name = self.mem.readString("XIProject.dll+F16E2")
            # print(name)
            return name
        except:
            return "-1"

    def getIdMap(self):
        # name = self.mem.read4Byte(0x0019B0D0)
        name = self.mem.read4Byte(0x0140AFC4)
        return name

    def getChat(self):
        name = self.mem.readString(0x09F4C920)
        return name

    def setMacroChat(self, value):
        self.mem.writeByteArray("main.exe+83711D0", None, "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00")
        self.mem.writeString("main.exe+83711D0", None, value)

    def callMacroChat(self):
        self.sendKey2("alt", True, "1")
        time.sleep(1)

    def setChat(self, value):
        self.mem.writeString(0x09F4C920, None, value)

    def getItemSelect(self):
        # name = self.mem.readString(0x087F3448)
        name = self.mem.readString(0x087F3510)
        return name

    def setNhatZen(self, enable):
        value = 0
        if enable:
            value = 1
        self.mem.write1Byte(baseAutoZ, [0x147], value)

    def setSkillAutoZ(self, idskill):
        self.mem.write4Byte(baseAutoZ, [0xC8], idskill)

    def setTimeVeViTriCu(self, time):
        self.mem.write4Byte(baseAutoZ, [0xC4], time)

    def getTimeVeViTriCu(self):
        return self.mem.read4Byte(baseAutoZ, [0xC4])

    def setNhatTatCa(self, enable):
        value = 0
        if enable:
            value = 1
        self.mem.write1Byte(baseAutoZ, [0x141], value)

    def getNhatTatCa(self):
        return self.mem.read1Byte(baseAutoZ, [0x141])

    def setNhatTheoDanhSach(self, enable):
        value = 0
        if enable:
            value = 1
        self.mem.write1Byte(baseAutoZ, [0x142], value)

    def setBuffCaNhan(self, enable):
        value = 0
        if enable:
            value = 1
        self.mem.write1Byte(baseAutoZ, [0x110], value)

    def getBuffCaNhan(self):
        value = self.mem.read1Byte(baseAutoZ, [0x110])
        if value == 1:
            return True
        return False

    def setKeepMouseRight(self, enable):
        get = self.mem.read4Byte('"main.exe"+0006B230', [-0xB9])
        value = 0
        if enable:
            value = 1
        if get == value:
            return
        self.mem.write4Byte('"main.exe"+0006B230', [-0xB9], value)

    def setKeepMouseLeft(self, enable):
        get = self.mem.read1Byte('"main.exe"+0006B230', [-0xB6])
        value = 0
        if enable:
            value = 1
            self.itestmove = self.itestmove + 1
            if self.itestmove % 5 == 0:
                hwin.moveMouse(0, 0, 0)
        if get == value:
            return
        self.mem.write1Byte('"main.exe"+0006B230', [-0xB6], value)

    def setViTriMouse(self, x, y):
        self.setViTriXMouse(x)
        self.setViTriYMouse(y)

    def setViTriXMouse(self, value):
        self.mem.write4Byte('"main.exe"+0006B230', [0x0], value)

    def setViTriYMouse(self, value):
        self.mem.write4Byte('"main.exe"+0006B230', [0x4], value)

    def getKhoangCachTrainAutoZ(self):
        return self.mem.read4Byte(baseAutoZ, [0xB4])

    def setKhoangCachTrainAutoZ(self, value):
        self.mem.write4Byte(baseAutoZ, [0xB4], value)

    def setKhoangCachNhatDoAutoZ(self, value):
        self.mem.write4Byte(baseAutoZ, [0x13C], value)

    def getEnableAutoZ(self):
        name = self.mem.read1Byte(baseAutoZ, [0x8])
        if name > 0:
            return True
        return False

    def batAutoZ(self, enable):
        value = 0
        if enable:
            value = 1
        self.mem.write1Byte(baseAutoZ, [0x8], value)

    def setNhatSuKien(self, enable):
        value = 0
        if enable:
            value = 1
        self.mem.write1Byte(baseAutoZ, [0x146], value)

    def getTuDongTangMau(self):
        try:
            if self.mem.read1Byte(baseAutoZ, [0xBA]) > 0:
                return True
        except:
            pass
        return False

    def setTuDongTangMau(self, enable):
        value = 0
        if enable:
            value = 1
        self.mem.write1Byte(baseAutoZ, [0xBA], value)

    def setBuffNhom(self, enable):
        value = 0
        if enable:
            value = 1
        self.mem.write1Byte(baseAutoZ, [0xFD], value)

    def getBuffNhom(self):
        name = self.mem.read1Byte(baseAutoZ, [0xFD])
        if name > 0:
            return True
        return False

    def getTrongThanh(self):
        name = self.mem.read1Byte(0x8150AC4, [0xE])
        if name > 0:
            return True
        return False

    def getZen(self):
        name = self.mem.read4Byte(0x09E7C150, [0x90, 0x30, 0x10, 0xB4])
        return name

    def getCuaSoNhapNick(self):
        try:
            name = self.mem.read4Byte(0x1445198)
            if name == 1:
                return True
        except:
            pass
        return False

    def autoMove(self, listxy):
        xy = hrand.randomItemInList(listxy)
        if self.indexselectmap < len(listxy):
            xy = listxy[self.indexselectmap]
        # print(self.namehero, self.indexselectmap, xy)
        x = xy[0]
        y = xy[1]
        self.mem.write1Byte(baseAutoZ, [0x44], x)
        self.mem.write1Byte(baseAutoZ, [0x48], y)
        self.mem.write1Byte(baseAutoZ, [0x8], 1)
        self.mem.write1Byte(0x8150AC4, [0xE], 0)

    def setVeViTriCu(self, enable):
        value = 1
        if not enable:
            value = 0
        self.mem.write1Byte(baseAutoZ, [0xC0], value)

    def autoMoveXY(self, x, y):
        if not self.lastmove:
            pass
        elif time.time() - self.lastmove < 2:
            return
        self.lastmove = time.time()
        self.moved = True
        # print(self.namehero, "move", x, y)
        self.mem.write1Byte(baseAutoZ, [0x44], x)
        self.mem.write1Byte(baseAutoZ, [0x48], y)
        self.batAutoZ(True)
        # self.mem.write1Byte(baseAutoZ, [0x8], 1)
        self.mem.write1Byte(0x8150AC4, [0xE], 0)

    def getFullHomDo(self):
        value = self.mem.read2Byte('"main.exe"+09B563D0', [0xDC, 0x68, 0x9CC, 0x7C, 0x0, 0x54, 0xDE])

        if value == 32768:
            return True
        value = self.mem.read2Byte('"main.exe"+09B563D0', [0xDC, 0x68, 0x9CC, 0x7C, 0x0, 0x54, 0xDA])
        if value == 32768:
            return True

        return False

    def getMoRuongDo(self):
        try:
            value = self.mem.read4Byte('"main.exe"+09B563D0', [0xDC, 0x68, 0x30, 0xD0, 0x20, 0xA0])
            if value == 200977 or value == 1:
                return True
        except:
            pass
        return False

    def anNhanVat(self, an=True):
        if an:
            an = 1
        else:
            an = 0
        self.mem.write1Byte("XIProject.dll+F167C", None, an)

    def moveMap(self, map, state="min", boqualandau=False):

        log(f"{htime.getStrTimeNow3()}: {self.namehero} move {map}")
        stop = False
        batdautinh = False
        while True:
            phimbamcuoicung = self.getPhimBamCuoiCung()
            if phimbamcuoicung == "F2":
                self.saveMapF2()
                return
            if phimbamcuoicung == "F3":
                stop = True
            if phimbamcuoicung == "F4":
                stop = False
            if stop:
                time.sleep(1)
                continue
            if herostop.get(self.namehero, False):
                return
            x, y = self.getPosHero()
            map2 = self.getMap(x, y)
            print(self.namehero, map2, map)
            if map2 == map:
                if boqualandau == True and not batdautinh:
                    batdautinh = True
                else:
                    if self.anmain > 0:
                        self.win.minimize()
                    self.setMacroChat("")
                    break
            # if testmove:
            #     hwin.moveMouse(0,0,0)
            self.setMacroChat(f"/move {map}")
            if testmove:
                self.clickHwnd(40, 40)
            self.callMacroChat()
            # time.sleep(0.5)

            time.sleep(1)

    def batMenuThoatGame(self, enable):
        if enable:
            if not self.daBatMenuThoatGame:
                self.activateHandle()
                self.sendKey("esc")
                return

        value = 200977
        if not enable:
            value = 200976
        self.mem.write4Byte('"main.exe"+09B563D0', [0xDC, 0x58, 0x30, 0x88, 0x84, 0xA0], value)

    def getMenuThoatGame(self):
        value = self.mem.read4Byte('"main.exe"+09B563D0', [0xDC, 0x58, 0x30, 0x88, 0x84, 0xA0])
        if value == 200977 or value == 1:
            return True
        return False

    def getBatThongTinC(self):
        value = self.mem.read4Byte('"main.exe"+09B563D0', [0xDC, 0x160, 0x24, 0x4, 0x15C, 0xA0])
        if value == 200977 or value == 1:
            return True
        return False

    def batThongTinC(self, enable):
        value = 200977
        if not enable:
            value = 200976
        self.mem.write4Byte('"main.exe"+09B563D0', [0xDC, 0x160, 0x24, 0x4, 0x15C, 0xA0], value)

    def getSoLanReset(self):
        value = self.mem.read2Byte("XIProject.dll+F14A8")
        return value

    def getBatMap(self):
        value = self.mem.read4Byte('"main.exe"+09B563D0', [0xDC, 0xA4, 0x30, 0x88, 0x84, 0xA0])
        if value == 200977 or value == 1:
            return True
        return False

    def batMap(self, enable):
        while True:
            if not self.getBatMap():
                if not enable:
                    return
                self.activateHandle()
                self.sendKey("m")
            else:
                if enable:
                    return
            time.sleep(0.1)

    def batMenuHeThong(self, enable):
        value = 200977
        if not enable:
            value = 200976
        self.mem.write4Byte('"main.exe"+09B563D0', [0xDC, 0x60, 0x30, 0xA0], value)

    def getNangDoLen(self):
        value = self.mem.read4Byte('"main.exe"+09B563D0', [0x110, 0x0, 0xC0, 0x70])
        if value > 0:
            return True
        return False

    def chonNhanVat(self, tennv):
        for i in range(5):
            namemonters = self.mem.readString(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4])
            if namemonters == tennv:
                self.mem.write4Byte(0x1409B88, None, i)
                self.setViTriMouse(0, 0)
                self.mem.write1Byte("main.exe+1045E50", None, 1)  # sáng nút connect
                time.sleep(1)
                self.sendKey("enter")
                self.sendKey("enter")
                self.sendKey("enter")
                time.sleep(3)
                break
        # for i in range(5):
        #     self.mem.write4Byte(0x1409B88, None, i)
        #     time.sleep(0.5)
        #     nvselect = self.mem.readString(0x014477D4, [0xC])
        #     # nvselect = self.mem.readString("XIProject.dll+F16E2")
        #     time.sleep(0.5)
        #     print(nvselect)
        #     if nvselect == tennv:
        #         self.setViTriMouse(0, 0)
        #         self.mem.write1Byte("main.exe+1045E50", None, 1)  # sáng nút connect
        #         # self.mem.write1Byte(0x1445E50, None, 1)  # sáng nút connect
        #         time.sleep(1)
        #         self.sendKey("enter")
        #         self.sendKey("enter")
        #         self.sendKey("enter")
        #         # self.mouseClick(702, 601)
        #         time.sleep(3)
        #         break

    def getPopupBanDo(self):
        value = self.mem.read4Byte('"main.exe"+09B563D0', [0xDC, 0x0, 0x9DC, 0xC4, 0x9CC, 0x88])
        if value == 1:
            return True
        return False

    def moveChuotVaoOTrongCuaHang(self):
        # hwin.moveMouseHwnd(self.hwnd, 199, 405)
        self.clickHwnd(199, 405)

    def activateHandle(self):
        # self.win.restore()
        self.win.activate()
        time.sleep(0.1)

        # hwin.activateHandle(self.hwnd)

    def sendKey(self, key, activehwnd=True, key2=None):
        if activehwnd:
            self.activateHandle()
            time.sleep(0.1)
        hwin.sendKey(key, key2)

    def sendKey2(self, key, activehwnd=True, key2=None):
        if activehwnd:
            self.activateHandle()
            # time.sleep(0.1)
        hwin.sendKey(key, key2)

    def mouseClick(self, x, y, solan=1, activehwnd=True):
        if self.chonnv:
            print(self.namehero, x, y)
        if activehwnd:
            self.activateHandle()
        # hwin.moveMouseHwnd(self.hwnd, x - 50, y)
        
        hwin.mouseClick(self.hwnd, x, y, solan=solan, speed=1)
        
    def mouseMove(self, x, y, activehwnd=True):
        if self.chonnv:
            print(self.namehero, x, y)
        if activehwnd:
            self.activateHandle()
        # hwin.moveMouseHwnd(self.hwnd, x - 50, y)
        
        hwin.moveMouseHwnd(self.hwnd, x, y, speed=1)

    def setZoomMap(self, value=16666):
        oldvalue = self.mem.read4Byte("XIProject.dll+F179E")
        if oldvalue != value:
            self.mem.write4Byte("XIProject.dll+F179E", None, value)

    def setMousePosition(self, x, y):
        self.mem.write4Byte('"main.exe"+0006B230', [0x0], x)
        self.mem.write4Byte('"main.exe"+0006B230', [0x4], y)

    def clickHwnd(self, x, y, activehwnd=True):
        if self.chonnv and y != 599:
            print(self.namehero, x, y)
        # self.setMousePosition(x, y)
        # time.sleep(1)

        if activehwnd:
            self.activateHandle()
        hwin.clickHwnd(self.hwnd, x, y, 30)

    def autoBanDo(self, map):
        while True:
            try:
                time.sleep(1)
                listxy = []
                if self.getTrongThanh():
                    listxy.append((0, 0))
                if not listxy:
                    if map == "Tarkan2":
                        listxy.append((156, 57))
                    else:
                        self.batMap(True)
                        self.clickHwnd(120, 335)
                        continue
                if not listxy:
                    break
                if not self.getTrongThanh():
                    self.autoMove(listxy)
                    continue
                self.batMap(False)
                if not self.getMoRuongDo():
                    self.activateHandle()
                    self.sendKey("s")
                    time.sleep(0.3)
                    # hwin.mouseClick(self.hwnd, 133, 82)
                    self.clickHwnd(629, 269)
                    continue
                listitem = []
                for i in range(64):
                    item = self.mem.read2Byte('"main.exe"+09B563D0', [0xDC, 0x68, 0x9CC, 0x7C, 0x0, 0x54, 0x0 + i * 0x4])
                    listitem.append(item)
                h = -1
                listitemshell = []
                listxyclick = []

                for i in range(8):
                    yclick = 343 + i * 22
                    for j in range(8):
                        h = h + 1

                        item = listitem[h]

                        xclick = 591 + j * 22
                        # print(h, item, xclick, yclick)
                        if item == 0:
                            continue
                        if item in listitemshell:
                            continue
                        print(xclick, yclick, item)
                        xy = (xclick, yclick)
                        listxyclick.append(xy)
                        listitemshell.append(item)

                if not (723, 475) in listxyclick:
                    listxyclick.append((723, 475))
                if not (723, 497) in listxyclick:
                    listxyclick.append((723, 497))
                if not (745, 475) in listxyclick:
                    listxyclick.append((745, 475))
                if not (745, 497) in listxyclick:
                    listxyclick.append((745, 497))
                listxyclick.append((635, 409))
                listxyclickbatbuocban = []
                listxyclickbatbuocban.append((723, 475))
                listxyclickbatbuocban.append((723, 497))
                listxyclickbatbuocban.append((745, 475))
                listxyclickbatbuocban.append((745, 497))
                lastselect = ""
                for i in listxyclick:
                    time.sleep(0.5)
                    x, y = i
                    self.activateHandle()
                    hwin.moveMouseHwnd(self.hwnd, x, y)
                    time.sleep(0.2)
                    itemselect = self.getItemSelect().strip().replace(" ", "")
                    # print(itemselect)
                    # while True:
                    #     time.sleep(1)
                    batbuocban = i in listxyclickbatbuocban
                    if hstr.startSwith(itemselect, "hoanhao") and not batbuocban:
                        continue
                    if hstr.startSwith(itemselect, "Rena") and not batbuocban:
                        continue
                    if itemselect in listitemkhongban and not batbuocban:
                        continue
                    if itemselect == lastselect:
                        continue
                    lastselect = itemselect
                    print(x, y, itemselect)
                    # continue
                    self.clickHwnd(x, y)
                    time.sleep(0.1)
                    if not self.getNangDoLen():
                        continue
                    # daNangDoLen = False
                    # for z in range(6):
                    #     if z % 3 == 0:
                    #         hwin.mouseClick(self.hwnd, x, y)
                    #     if self.getNangDoLen():
                    #         daNangDoLen = True
                    #         break
                    #     time.sleep(0.5)
                    # if not daNangDoLen:
                    #     continue
                    self.moveChuotVaoOTrongCuaHang()
                    # time.sleep(0.5)
                    iwait = 0
                    while True:
                        iwait = iwait + 1
                        if not self.getNangDoLen():
                            break
                        if self.getPopupBanDo():
                            self.clickHwnd(361, 406)
                        else:
                            if iwait % 3 == 0:
                                self.moveChuotVaoOTrongCuaHang()
                        time.sleep(0.1)
                print(self.namehero, "Đợi bán đồ")
                while True:
                    if self.getMoRuongDo():
                        self.activateHandle()
                        self.sendKey("v")

                        if self.getNangDoLen():
                            self.moveChuotVaoOTrongCuaHang()
                    else:
                        break
                    time.sleep(0.1)
                print(self.namehero, "Move map")
                self.moveMap("Kanturu_ruin2")

                return
            except:
                print(hfile.getError())

    def autoSanBoss247(self):

        listmapsb = []
        listmapsb.append("Elbeland3")
        listmapsb.append("Devias")
        listmapsb.append("Noria")
        listmapsb.append("Lorencia")
        self.ngungSanBoss = False
        while True:
            if herostop.get(self.namehero, False):
                print(self.namehero, "Stop săn boss")
                return
            for i in listmapsb:
                if self.ngungSanBoss:
                    print(self.namehero, "Stop săn boss")
                    return
                with lockbando:
                    self.moveMap(i, "")
                    # self.setMacroChat(f"/move {i}")
                    # self.callMacroChat()

                    # time.sleep(3)
                self.autoSanBoss(i)
                time.sleep(1)

    def printMonter(self):
        for i in range(-1, 50):
            namemonters = self.mem.readString(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4])
            print(namemonters)

    def checkDungIm(self, trangthainv):
        if (
            trangthainv == 13
            or trangthainv == 38
            or trangthainv == 5
            or trangthainv == 1
            or trangthainv == 2
            or trangthainv == 9
            or trangthainv == 3
            or trangthainv == 14
            or trangthainv == 4
            or trangthainv == 39
            or trangthainv == 131
            or trangthainv == 85
        ):
            return True
        else:
            return False

    def autoSanBoss(self, map="Noria", printmon=False):
        if not self.listnameboss:
            self.listnameboss = hfile.readLines(f"/data/nameboss-{self.namehero}.txt")
        self.setKhoangCachTrainAutoZ(7)
        self.setNhatZen(False)
        self.setNhatTatCa(False)
        self.setTimeVeViTriCu(0)
        self.setBuffCaNhan(False)
        listmove = []
        if self.namehero != "Akali":
            pass
        #            return
        x, y = self.getPosHero()
        maphientai = self.getMap(x, y)
        if maphientai != map:
            print("Map không khớp")
            return
        namedebug = "Akali"
        if map == "Elbeland3":
            listmove.append((234, 148))
            listmove.append((226, 48))
            listmove.append((172, 31))
            listmove.append((176, 18))
            listmove.append((202, 52))
            listmove.append((192, 32))
            listmove.append((167, 65))
            listmove.append((155, 56))
            listmove.append((163, 77))
            listmove.append((212, 64))
            listmove.append((187, 93))
            listmove.append((207, 128))
            listmove.append((190, 142))
            listmove.append((153, 119))
            listmove.append((144, 106))
            listmove.append((167, 83))
            listmove.append((143, 105))
            listmove.append((99, 64))
            listmove.append((134, 28))
            listmove.append((119, 22))
            listmove.append((90, 44))
            listmove.append((83, 15))
            listmove.append((71, 30))
            listmove.append((29, 30))
            listmove.append((95, 48))
            listmove.append((48, 71))
            listmove.append((54, 91))
            listmove.append((71, 80))
            listmove.append((73, 69))
            # listmove.append((92, 52))
            # listmove.append((74, 81))
            listmove.append((95, 110))
            listmove.append((110, 103))
            listmove.append((113, 111))
            listmove.append((130, 137))
            listmove.append((150, 129))
            listmove.append((150, 158))
            listmove.append((189, 195))
            listmove.append((202, 192))
            listmove.append((187, 169))
            listmove.append((170, 176))
            listmove.append((137, 146))
            listmove.append((124, 159))
            listmove.append((122, 192))
            listmove.append((136, 194))
            listmove.append((127, 229))
            listmove.append((109, 213))
            listmove.append((114, 195))
            listmove.append((97, 188))
            listmove.append((84, 176))
            listmove.append((116, 162))
            listmove.append((95, 137))
            listmove.append((77, 141))
            listmove.append((60, 140))
            listmove.append((34, 133))
            listmove.append((23, 149))
            listmove.append((45, 160))
            listmove.append((50, 144))
            listmove.append((68, 172))
            listmove.append((86, 177))
        elif map == "Lorencia":
            listmove.append((177, 127))
            listmove.append((179, 106))
            listmove.append((164, 87))
            listmove.append((135, 78))
            listmove.append((135, 46))
            listmove.append((100, 54))
            listmove.append((87, 69))
            listmove.append((97, 94))
            listmove.append((89, 127))
            listmove.append((93, 163))
            listmove.append((133, 174))
            listmove.append((172, 177))
            listmove.append((214, 237))
            listmove.append((135, 190))
            listmove.append((81, 177))
            listmove.append((63, 157))
            listmove.append((63, 95))
            listmove.append((85, 44))
            listmove.append((157, 33))
            listmove.append((154, 71))
            listmove.append((200, 76))
            listmove.append((203, 132))
            listmove.append((175, 152))
            listmove.append((226, 213))
            listmove.append((206, 156))
            listmove.append((219, 45))
        elif "Devias" in map:
            listmove.append((223, 84))
            listmove.append((240, 85))
            listmove.append((239, 127))
            listmove.append((215, 116))
            listmove.append((180, 112))
            listmove.append((179, 73))
            listmove.append((161, 49))
            listmove.append((166, 11))
            listmove.append((132, 29))
            listmove.append((115, 12))
            listmove.append((119, 77))
            listmove.append((169, 115))
            listmove.append((203, 120))
            listmove.append((204, 147))
            listmove.append((220, 170))
            listmove.append((237, 194))
            listmove.append((225, 205))
            listmove.append((195, 149))
            listmove.append((199, 234))
            listmove.append((164, 224))
            listmove.append((159, 232))
            listmove.append((158, 202))
            listmove.append((174, 191))
            listmove.append((150, 161))
            listmove.append((159, 124))
            listmove.append((142, 118))
            listmove.append((151, 199))
            listmove.append((136, 233))
            listmove.append((127, 121))
            listmove.append((115, 234))
            listmove.append((108, 89))
            listmove.append((95, 109))
            listmove.append((101, 190))
            listmove.append((91, 179))
            listmove.append((92, 110))
            listmove.append((71, 106))
            listmove.append((99, 193))
            listmove.append((75, 175))
            listmove.append((58, 192))
            listmove.append((62, 208))
            listmove.append((73, 220))
            listmove.append((78, 238))
            listmove.append((15, 237))
            listmove.append((15, 218))
            listmove.append((72, 227))
            listmove.append((71, 216))
            listmove.append((14, 220))
            listmove.append((18, 205))
            listmove.append((70, 214))
            listmove.append((55, 203))
            listmove.append((12, 197))
            listmove.append((14, 183))
            listmove.append((55, 196))
            listmove.append((74, 171))
            listmove.append((54, 150))
            listmove.append((27, 149))
            listmove.append((15, 139))
            listmove.append((18, 106))
            listmove.append((29, 91))
            listmove.append((16, 58))
            listmove.append((41, 57))
            listmove.append((37, 74))
            listmove.append((54, 78))
            listmove.append((65, 67))
            listmove.append((41, 59))
            listmove.append((66, 56))
            listmove.append((52, 43))
            listmove.append((53, 13))
            listmove.append((72, 11))
            listmove.append((81, 24))
            listmove.append((74, 37))
            listmove.append((59, 34))
            listmove.append((57, 22))
            listmove.append((70, 24))
        elif map == "Devias2":
            listmove.append((56, 193))
            listmove.append((11, 184))
            listmove.append((12, 214))
            listmove.append((21, 239))
            listmove.append((22, 193))
            listmove.append((31, 193))
            listmove.append((27, 239))
            listmove.append((37, 239))
            listmove.append((37, 189))
            listmove.append((51, 193))
            listmove.append((47, 239))
            listmove.append((57, 239))
            listmove.append((60, 199))
            listmove.append((68, 236))
            listmove.append((74, 216))
            listmove.append((62, 187))

            listmove.append((75, 174))
            listmove.append((55, 153))
            listmove.append((70, 104))
            listmove.append((84, 110))
            listmove.append((71, 156))
            listmove.append((81, 165))
            listmove.append((81, 110))
            listmove.append((95, 110))
            listmove.append((82, 164))
            listmove.append((91, 187))
            listmove.append((111, 88))
            listmove.append((112, 105))
            listmove.append((100, 98))
            listmove.append((107, 239))
        elif map == "Devias9":
            # xstart = 11
            # ystart = 185
            # xhero, yhero = self.getPosHero()
            # end = False
            # for i in range(11):
            #     j = 0
            #     x1 = xstart + i * 8
            #     if x1 < xhero:
            #         continue
            #     y1 = ystart + j * 57
            #     y2 = ystart + (j + 1) * 57
            #     if (x1, y1) == (67, 185):
            #         x1 = 64
            #         y1 = 210
            #     if (x1, y1) == (75, 185):
            #         x1 = 64
            #         y1 = 210
            #     if (x1, y1) == (91, 185):
            #         x1 = 81
            #         y1 = 225
            #         end = True
            #     if (x1, y2) == (83, 242):
            #         x1 = 81
            #         y2 = 241

            #     if i % 2 == 0:
            #         listmove.append((x1, y1))
            #         listmove.append((x1, y2))
            #     else:
            #         listmove.append((x1, y2))
            #         listmove.append((x1, y1))
            #     print(x1, y1, x1, y2)
            #     if end:
            #         break
            xstart = 58
            ystart = 111
            yadd = 239 - ystart
            xhero, yhero = self.getPosHero()
            end = False
            for i in range(11):
                j = 0
                x1 = xstart + i * 8
                if x1 < xhero:
                    continue
                y1 = ystart + j * yadd
                y2 = ystart + (j + 1) * yadd

                if (x1, y2) == (58, 239):
                    x1 = 58
                    y2 = 157
                if (x1, y2) == (66, 239):
                    x1 = 66
                    y2 = 157
                if (x1, y2) == (74, 239):
                    x1 = 74
                    y2 = 179
                if (x1, y2) == (82, 239):
                    x1 = 82
                    y2 = 182
                if (x1, y2) == (90, 239):
                    x1 = 90
                    y2 = 188
                if (x1, y2) == (114, 239):
                    x1 = 114
                    y2 = 194

                if i % 2 == 0:
                    listmove.append((x1, y1))
                    listmove.append((x1, y2))
                    print(" => ", x1, y1, x1, y2)
                else:
                    listmove.append((x1, y2))
                    listmove.append((x1, y1))
                    print(" <= ", x1, y2, x1, y1)

                if end:
                    break

            # while True:
            #     time.sleep(1)
        elif map == "Noria":
            xhero, yhero = self.getPosHero()
            listmove.append((159, 122))
            for i in range(23):
                j = 0
                x1 = 15 + i * 10
                # if x1 < xhero:
                #     continue
                if i % 2 == 0:
                    y1 = 9 + j * 230
                    y2 = 9 + (j + 1) * 230
                    listmove.append((x1, y1))
                    listmove.append((x1, y2))
                    print(i, x1, y1, x1, y2)
                else:

                    y2 = 9 + j * 230
                    y1 = 9 + (j + 1) * 230
                    listmove.append((x1, y1))
                    listmove.append((x1, y2))
                    print(i, x1, y1, x1, y2)
        else:
            print("Chưa hỗ trợ map này")
            return
            # i = i + 1

        # time.sleep(1111)
        # listmove.append((15, 8))
        # listmove.append((15, 238))
        # listmove.append((21, 238))
        # listmove.append((21, 8))
        # listmove.append((27, 8))
        # listmove.append((27, 238))
        setbuff = False
        # if self.getTongNangLuong() > 2500:
        #     setbuff = True
        listboss = []
        # hwin.setStateHwnd(self.hwnd, "min")
        listdungim = []
        for zmove in listmove:

            print(self.namehero, zmove)
            self.setBuffCaNhan(False)
            # self.setSkillAutoZ(0)
            st = time.time()
            while True:
                if zmove == (15, 9):
                    if time.time() - st > 300:
                        break
                else:
                    if time.time() - st > 100:
                        break
                chat = self.getChat()
                if chat == "/st" or herostop.get(self.namehero, False):
                    self.ngungSanBoss = True
                    return
                listxy = []
                # if zmove == (225, 239):
                #     break
                if zmove == (225, 9):
                    zmove = (230, 9)
                if zmove == (205, 9):
                    zmove = (215, 9)
                if zmove == (165, 9):
                    zmove = (155, 9)
                listxy.append(zmove)

                self.autoMove(listxy)

                if map == "Noria":
                    xwait = 0
                    ywait = 0
                    resettime = False
                    while True:
                        chat = self.getChat()
                        if chat == "/st" or herostop.get(self.namehero, False):
                            self.ngungSanBoss = True
                            return
                        xhero, yhero = self.getPosHero()
                        if xhero == 163 and yhero == 110:
                            list2 = []
                            xwait = 154
                            ywait = 114
                            list2.append((xwait, ywait))
                            self.autoMove(list2)
                            time.sleep(1)
                            continue
                        elif xhero == 174 and yhero == 135:

                            list2 = []
                            xwait = 214
                            ywait = 131
                            list2.append((xwait, ywait))
                            self.autoMove(list2)
                            time.sleep(1)
                            continue
                        elif xhero == 185 and yhero == 137:

                            list2 = []
                            xwait = 214
                            ywait = 131
                            list2.append((xwait, ywait))
                            self.autoMove(list2)
                            time.sleep(1)
                            continue
                        elif xhero == 177 and yhero == 130:
                            list2 = []
                            xwait = 198
                            ywait = 120
                            list2.append((xwait, ywait))
                            self.autoMove(list2)
                            time.sleep(1)
                            continue
                        elif xhero == 165 and yhero == 97:
                            list2 = []
                            xwait = 175
                            ywait = 100
                            list2.append((xwait, ywait))
                            self.autoMove(list2)
                            time.sleep(1)
                            continue
                        elif xhero == 201 and yhero == 105:
                            list2 = []
                            xwait = 175
                            ywait = 100
                            list2.append((xwait, ywait))
                            self.autoMove(list2)
                            time.sleep(1)
                            continue
                        else:
                            if xwait != 0:
                                if xhero == xwait and yhero == ywait:
                                    break
                                else:
                                    if not resettime:
                                        st = time.time()
                                        resettime = True
                                    if time.time() - st > 30:
                                        return
                                    list2 = []
                                    self.setBuffCaNhan(False)
                                    list2.append((xwait, ywait))
                                    self.autoMove(list2)
                                    time.sleep(1)
                                    continue
                            self.autoMove(listxy)
                            break

                xhero, yhero = self.getPosHero()
                trituyetdoix = abs(xhero - zmove[0])
                trituyetdoiy = abs(yhero - zmove[1])
                if (trituyetdoix == 0 or trituyetdoix == 1) and (trituyetdoiy == 0 or trituyetdoiy == 1):
                    break
                # time.sleep(2)
                xhero = xhero - 1
                for i in range(0, 50):
                    timthayboss = False
                    matboss = 0
                    if self.namehero == namedebug:
                        print("scan", i)
                    toivitri = False
                    invdungim = 0
                    nvdungim = False
                    while True:
                        if self.getHPConLai() == 0:
                            return

                        addressnew = i * 0x6F4
                        trangthai1 = self.mem.read1Byte(baseListHero, [0x8, 0x40C + addressnew])
                        if trangthai1 == 0:
                            break
                        trangthai2 = self.mem.read1Byte(baseListHero, [0x8, 0x2A + addressnew])
                        if trangthai2 != 0:
                            break
                        trangthai3_trongthanh = self.mem.read1Byte(baseListHero, [0x8, 0xE + addressnew])
                        if trangthai3_trongthanh == 1:
                            break
                        namemonters = self.mem.readString(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4])
                        trangthainv = self.getTrangThaiNhanVat()
                        trangthai = self.mem.read1Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4 + 0x20])
                        trangthaitancong = self.mem.read1Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4 - 0x10])

                        if printmon or self.namehero == namedebug:
                            print(namemonters, i, trangthai)
                            pass
                        if not " " in namemonters:
                            break
                        if not namemonters in self.listnameboss:
                            self.listnameboss.append(namemonters)
                            hfile.writeLine(f"data/nameboss-{self.namehero}.txt", namemonters)
                        # if namemonters == namehero:
                        #     continue
                        # if trangthai == 1:
                        #     while True:
                        # self.mem.write1Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4 + 0x20], 0)
                        # time.sleep(0.5)
                        coboss = False
                        if (
                            "Rng Vang Con" in namemonters
                            or "Rng Vang" in namemonters
                            or "Phu Thuy Anh sang" in namemonters
                            or "Tho Ngoc Hoang Kim" in namemonters
                            or "Xng T Thn" in namemonters
                            or "Ngi May Vang" in namemonters
                            # or "Lu Vang" in namemonters
                            or "Chin Binh Vang" in namemonters
                            # or "Linh h" in namemonters
                            # or "BOSS" in namemonters
                            or "Kim Thi" in namemonters
                            or namemonters == "Kim Tiu Quy"
                            or namemonters == "Fire Flame Ghost"
                        ):

                            if trangthai == 0 and trangthaitancong == 0:
                                if timthayboss == True:
                                    matboss = matboss + 1
                                    if matboss < 10:
                                        time.sleep(0.5)
                                        continue
                                if self.namehero == namedebug:
                                    print("scan", i, zmove, "thoat 1")
                                break
                            coboss = True
                            xboss = self.mem.read4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x37C])
                            yboss = self.mem.read4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x37C + 0x4])
                            # self.mem.writeFloat(baseListHero, [0x8, 0x51C + i * 0x6F4], xhero * 100 + 50)
                            # self.mem.writeFloat(baseListHero, [0x8, 0x51C + i * 0x6F4 + 0x4], yhero * 100 + 50)
                            # self.mem.write4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x37C], xhero)
                            # self.mem.write4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 + 0x4 - 0x37C], yhero)
                            if not (xboss, yboss) in listboss:
                                if self.namehero == namedebug:
                                    print("scan", i, zmove, "move")
                                listboss.append((xboss, yboss))
                                chat = self.getChat()
                                if chat == "a":
                                    break
                                listxy = []
                                listxy.append((xboss, yboss))
                                if setbuff:
                                    self.setBuffCaNhan(True)
                                # self.setSkillAutoZ(24)
                                self.autoMove(listxy)
                                print(self.namehero, namemonters, i, xboss, yboss)
                                time.sleep(5)
                                timthayboss = True
                                matboss = 0
                        else:
                            # self.mem.writeFloat(baseListHero, [0x8, 0x51C + i * 0x6F4], xhero * 100 + 50)
                            # self.mem.writeFloat(baseListHero, [0x8, 0x51C + i * 0x6F4 + 0x4], yhero * 100 + 50)
                            # self.mem.write4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x37C], xhero)
                            # self.mem.write4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 + 0x4 - 0x37C], yhero)
                            if self.checkDungIm(trangthainv):
                                # self.mem.writeString(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4], "11111")  # sửa lại tên quái
                                invdungim = invdungim + 1
                                if invdungim > 8:
                                    nvdungim = True
                            if self.namehero == namedebug:
                                print(self.namehero, "scan", i, zmove, "thoat 3")
                            break

                        if self.checkDungIm(trangthainv):
                            # self.mem.writeString(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4], "11111")  # sửa lại tên quái
                            xhero, yhero = self.getPosHero()
                            trituyetdoix = abs(xhero - zmove[0])
                            trituyetdoiy = abs(yhero - zmove[1])
                            if (trituyetdoix == 0 or trituyetdoix == 1) and (trituyetdoiy == 0 or trituyetdoiy == 1):
                                if self.namehero == namedebug:
                                    print(self.namehero, "scan", i, zmove, "thoat 4")
                                toivitri = True
                                break
                            matboss = matboss + 1
                            if matboss < 20:
                                time.sleep(0.5)
                                continue
                            else:
                                invdungim = invdungim + 1
                                if invdungim < 10:
                                    time.sleep(0.5)
                                    continue
                                nvdungim = True
                                if self.namehero == namedebug:
                                    print(self.namehero, "scan", i, zmove, "thoat 2")
                                break
                        else:
                            invdungim = 0
                            matboss = 0
                        if not coboss:
                            print(self.namehero, "khong co bosss")
                            break
                    if toivitri:
                        print(self.namehero, "toivitri")
                        break
                    if nvdungim:
                        xhero, yhero = self.getPosHero()
                        adungim = (xhero, yhero)
                        if adungim in listdungim:
                            print(self.namehero, "nvdungim quá lâu, đổi map")
                            return
                        listdungim.append(adungim)
                        print(self.namehero, "nvdungim")
                        break
        print(self.namehero, "Stop")

    def listPT(self):
        lists = []
        for i in range(5):
            nv1 = self.mem.readString('"main.exe"+09B4C6CC', [0x0, 0x8, 0x248, 0x30, 0xC, 0x7C + 0x68 * i])
            if nv1 == self.namehero:
                continue
            if not nv1:
                continue
            if nv1 in lists:
                continue
            lists.append(nv1)
        return lists

    def checkExist(self):
        return hwin.winExistHandle(self.hwnd)

    def getTrangThaiNhanVat(self):
        return self.mem.read4Byte('"main.exe"+09A77CE0', [0x24])

    def getSkillAutoZ(self):
        return self.mem.read4Byte(baseAutoZ, [0xC8])

    def getSkillActive(self):
        return self.mem.read4Byte("main.exe+9A77CE4")

    def autoPKTest(self):
        try:
            xhero, yhero = self.getPosHero()
            # xhero = xhero - 1

            for i in range(0, 50):

                while True:

                    skillautoz = self.getSkillAutoZ()
                    if skillautoz != self.getSkillActive():
                        self.setKeepMouseRight(False)
                        for z1 in range(250):
                            if skillautoz == self.getSkillActive():
                                self.idskillautopk = z1
                                break
                            self.mem.write1Byte(baseAutoZ, [0x4, 0x32], z1)
                            time.sleep(0.5)

                    if self.getMoRuongDo():
                        time.sleep(1)
                        continue

                    namemonters = self.mem.readString(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4])
                    namemonters = namemonters.replace("(", " ")
                    if " " in namemonters or "111111111111111" in namemonters:
                        break
                    if namemonters == self.namehero:
                        break
                    if namemonters in listkopk:
                        break
                    if not namemonters in self.listclone:
                        self.listclone.append(namemonters)
                        hfile.writeLine("data/pkclone_save.txt", namemonters)
                    if listpkclone:
                        if not namemonters in listpkclone:
                            break

                    trangthai1 = self.mem.read1Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4 - 0xE + 0x3E2])
                    if trangthai1 == 0:
                        self.mem.writeString(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4], "111111111111111")
                        # print(i, namemonters, trangthai1)
                        break
                    trangthai2 = self.mem.read1Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4 - 0xE])
                    if trangthai2 != 0:
                        self.mem.writeString(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4], "111111111111111")
                        # print(i, namemonters, trangthai2)
                        break
                    trangthai3_trongthanh = self.mem.read1Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4 - 0xE - 0x1C])
                    if trangthai3_trongthanh == 1:
                        self.mem.writeString(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4], "111111111111111")
                        # print(i, namemonters, trangthai3_trongthanh)
                        break

                    xmonters = self.mem.read4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x37C])
                    ymonters = self.mem.read4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 + 0x4 - 0x37C])
                    if hstr.triTuyetDoi(xmonters - xhero) > 6 or hstr.triTuyetDoi(ymonters - yhero) > 6:
                        break
                    self.mem.write1Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4 - 0x18], 6)  # trạng thái quỷ đỏ
                    # stri = str(i)
                    # if len(stri) == 1:
                    #     stri = "0" + stri

                    # self.mem.writeByteArray("main.exe+100A8F8", None, stri + " 00 00 00")
                    self.mem.writeByteArray("main.exe+100A8F8", None, self.mem.decimalToHexString(i))
                    autoZ = self.getEnableAutoZ()
                    if autoZ:
                        self.setKeepMouseRight(True)
                    print(namemonters)
                    time.sleep(0.05)
                    # self.mem.write1Byte("main.exe+100A900", None, 2)
                    # self.mem.write4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x37C], xhero)
                    # self.mem.write4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 + 0x4 - 0x37C], yhero)
        except Exception as e:
            print(hfile.getError())

    def endAuto(self, value):
        self.mem.write1Byte("XIProject.dll+28D160", None, value)

    def xoaToi(self):
        if not self.lastxoatoi:
            self.lastxoatoi = time.time() - 400
        if time.time() - self.lastxoatoi > 360:
            self.setMacroChat(f"/pkclear")
            self.callMacroChat()
            self.lastxoatoi = time.time()

    def autoPKCheckbox(self):
        try:
            if self.getTrongThanh():
                return
            if self.server == 1 or self.server == 2 or self.server == 3 or self.server == 4 or self.server == 10 or self.server == 18:
                return
            self.xoaToi()
            xhero, yhero = self.getPosHero()

            # xhero = xhero - 1
            self.batAutoZ(True)
            # self.endAuto(0)
            for i in range(0, 50):
                zkill = 0
                while True:
                    if not listnhanvatautopk.get(self.namehero, False):
                        return
                    if self.getHPConLai() == 0:
                        self.autopkdie = True
                        return
                    skillautoz = self.getSkillAutoZ()
                    if skillautoz != self.getSkillActive():
                        if self.skillautopk:
                            self.mem.write1Byte(baseAutoZ, [0x4, 0x32], self.skillautopk)
                            time.sleep(0.1)
                            continue
                        for z1 in range(250):
                            self.mem.write1Byte(baseAutoZ, [0x4, 0x32], z1)
                            time.sleep(0.5)
                            if skillautoz == self.getSkillActive():
                                break
                            if not self.skillautopk:
                                self.skillautopk = z1

                    # id = self.mem.read1Byte(baseListHero, [0x8, 0x260])
                    # if id == 0:  # bản thân hero
                    #     break
                    # id = self.mem.read1Byte(baseListHero, [0x8, 0x248])
                    # if id == 255: #quái vật
                    #     break
                    addressnew = i * 0x6F4

                    namemonters = self.mem.readString(baseListHero, [0x8, 0x38 + addressnew])

                    # break
                    namemonters = namemonters.replace("(", " ")

                    if " " in namemonters or "111111111111111" in namemonters:
                        break
                    # if namemonters == self.namehero:
                    #     break
                    # print(namemonters, id)

                    if namemonters in listkopk:
                        break

                    id = self.mem.read1Byte(baseListHero, [0x8, 0x224 + addressnew])
                    # print(namemonters, id, i)
                    if id == 255:  # quái vật
                        break

                    if id == 156:  # cô bé bán dạo
                        break

                    # if not namemonters in self.listclone:
                    #     self.listclone.append(namemonters)
                    #     hfile.writeLine("data/pkclone_save.txt", namemonters)
                    # if not dictpk[self.namehero]:
                    #     break
                    if not namemonters in dictpk[self.namehero]:
                        break
                    addressnew = i * 0x6F4
                    trangthai1 = self.mem.read1Byte(baseListHero, [0x8, 0x40C + addressnew])
                    if trangthai1 == 0:
                        break
                    trangthai2 = self.mem.read1Byte(baseListHero, [0x8, 0x2A + addressnew])
                    if trangthai2 != 0:
                        break
                    trangthai3_trongthanh = self.mem.read1Byte(baseListHero, [0x8, 0xE + addressnew])
                    if trangthai3_trongthanh == 1:
                        break

                    xmonters = self.mem.read4Byte(baseListHero, [0x8, 0x1A0 + addressnew])
                    ymonters = self.mem.read4Byte(baseListHero, [0x8, 0x1A4 + addressnew])
                    if hstr.triTuyetDoi(xmonters - xhero) > 6 or hstr.triTuyetDoi(ymonters - yhero) > 6:
                        break
                    self.mem.write1Byte(baseListHero, [0x8, 0x20 + addressnew], 6)  # trạng thái quỷ đỏ

                    # stri = str(i)
                    # if len(stri) == 1:
                    #     stri = "0" + stri
                    # self.mem.writeByteArray("main.exe+100A8F8", None, stri + " 00 00 00")
                    self.mem.writeByteArray("main.exe+100A8F8", None, self.mem.decimalToHexString(i))
                    self.batAutoZ(False)
                    self.endAuto(1)
                    print(namemonters, i, zkill)
                    time.sleep(0.1)
                    zkill = zkill + 1
                    if zkill > 30:
                        break
                    # self.mem.write1Byte("main.exe+100A900", None, 2)
                    # self.mem.write4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x37C], xhero)
                    # self.mem.write4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 + 0x4 - 0x37C], yhero)
        except Exception as e:
            print(hfile.getError())

    def autoPKCheckboxCu(self):
        try:
            xhero, yhero = self.getPosHero()
            # xhero = xhero - 1
            self.batAutoZ(True)
            # self.endAuto(0)
            for i in range(-1, 50):
                zkill = 0
                while True:
                    if not listnhanvatautopk.get(self.namehero, False):
                        return
                    if self.getHPConLai() == 0:
                        self.autopkdie = True
                        return
                    skillautoz = self.getSkillAutoZ()
                    if skillautoz != self.getSkillActive():
                        if self.skillautopk:
                            self.mem.write1Byte(baseAutoZ, [0x4, 0x32], self.skillautopk)
                            time.sleep(0.1)
                            continue
                        for z1 in range(250):
                            self.mem.write1Byte(baseAutoZ, [0x4, 0x32], z1)
                            time.sleep(0.5)
                            if skillautoz == self.getSkillActive():
                                break
                            if not self.skillautopk:
                                self.skillautopk = z1
                    namemonters = self.mem.readString(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4])
                    namemonters = namemonters.replace("(", " ")
                    if " " in namemonters or "111111111111111" in namemonters:
                        break
                    if namemonters == self.namehero:
                        break
                    if namemonters in listkopk:
                        break
                    # if not namemonters in self.listclone:
                    #     self.listclone.append(namemonters)
                    #     hfile.writeLine("data/pkclone_save.txt", namemonters)
                    # if not dictpk[self.namehero]:
                    #     break
                    if not namemonters in dictpk[self.namehero]:
                        break

                    trangthai1 = self.mem.read1Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4 - 0xE + 0x3E2])
                    if trangthai1 == 0:
                        # self.mem.writeString(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4], "111111111111111")
                        # print(i, namemonters, trangthai1)
                        break
                    trangthai2 = self.mem.read1Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4 - 0xE])
                    if trangthai2 != 0:
                        # self.mem.writeString(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4], "111111111111111")
                        # print(i, namemonters, trangthai2)
                        break
                    trangthai3_trongthanh = self.mem.read1Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4 - 0xE - 0x1C])
                    if trangthai3_trongthanh == 1:
                        # self.mem.writeString(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4], "111111111111111")
                        # print(i, namemonters, trangthai3_trongthanh)
                        break

                    xmonters = self.mem.read4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x37C])
                    ymonters = self.mem.read4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 + 0x4 - 0x37C])
                    if hstr.triTuyetDoi(xmonters - xhero) > 6 or hstr.triTuyetDoi(ymonters - yhero) > 6:
                        break
                    self.mem.write1Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4 - 0x18], 6)  # trạng thái quỷ đỏ

                    # stri = str(i)
                    # if len(stri) == 1:
                    #     stri = "0" + stri
                    # self.mem.writeByteArray("main.exe+100A8F8", None, stri + " 00 00 00")
                    self.mem.writeByteArray("main.exe+100A8F8", None, self.mem.decimalToHexString(i))
                    self.batAutoZ(False)
                    self.endAuto(1)
                    print(namemonters, i, zkill)
                    time.sleep(0.1)
                    zkill = zkill + 1
                    if zkill > 30:
                        break
                    # self.mem.write1Byte("main.exe+100A900", None, 2)
                    # self.mem.write4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x37C], xhero)
                    # self.mem.write4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 + 0x4 - 0x37C], yhero)
        except Exception as e:
            print(hfile.getError())

    def quetNV(self, quetpt=True, khoangcachquet=8):
        try:
            if quetpt:
                listpt = self.listPT()
            else:
                listpt = []
            lists = []
            xhero, yhero = self.getPosHero()
            # xhero = xhero - 1

            for i in range(-1, 50):
                zkill = 0

                namemonters = self.mem.readString(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4])
                namemonters = namemonters.replace("(", " ")
                if " " in namemonters or "111111111111111" in namemonters:
                    continue
                if namemonters == self.namehero:
                    continue
                if namemonters in listpt:
                    continue

                trangthai1 = self.mem.read1Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4 - 0xE + 0x3E2])
                if trangthai1 == 0:

                    continue
                trangthai2 = self.mem.read1Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4 - 0xE])
                if trangthai2 != 0:

                    continue
                trangthai3_trongthanh = self.mem.read1Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4 - 0xE - 0x1C])
                if trangthai3_trongthanh == 1:
                    continue

                xmonters = self.mem.read4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x37C])
                ymonters = self.mem.read4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 + 0x4 - 0x37C])
                if hstr.triTuyetDoi(xmonters - xhero) > khoangcachquet or hstr.triTuyetDoi(ymonters - yhero) > khoangcachquet:
                    continue
                lists.append(namemonters)

        except Exception as e:
            print(hfile.getError())
        return lists

    def autoBuffPC(self):
        try:
            autoZ = self.getEnableAutoZ()

            if not autoZ:
                return
            listpt = self.listPT()

            # xhero = xhero - 1

            for i in range(-1, 50):
                self.setKeepMouseRight(False)
                while True:
                    # print(self.idskillpc)
                    if self.idskillpc == 0:
                        for z11 in range(200):
                            self.mem.write1Byte(baseAutoZ, [0x4, 0x32], z11)
                            time.sleep(0.1)
                            if self.getSkillActive() == 217:  # skill pc
                                self.idskillpc = z11
                                break
                        break
                    namemonters = self.mem.readString(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4])
                    namemonters = namemonters.replace("(", " ")
                    if " " in namemonters:
                        break
                    if namemonters == self.namehero:
                        break

                    # if not namemonters in listpt:
                    #     break
                    # if (
                    #     namemonters != "KoThichPK"
                    #     and namemonters != "KoThichBuf"
                    #     and namemonters != "Donald"
                    #     and namemonters != "Viktor"
                    #     and namemonters != "MrSoaiCa"
                    #     and namemonters != "NuThanTQ"
                    #     and namemonters != "BoyLangTu"
                    # ):
                    #     break

                    self.setKeepMouseRight(True)
                    self.setMousePosition(319, 208)
                    for z3 in range(10):
                        xhero, yhero = self.getPosHero()
                        self.mem.write1Byte(baseAutoZ, [0x4, 0x32], self.idskillpc)

                        self.mem.writeFloat(baseListHero, [0x8, 0x51C + i * 0x6F4], xhero * 100 + 50)
                        self.mem.writeFloat(baseListHero, [0x8, 0x51C + i * 0x6F4 + 0x4], yhero * 100 + 50)
                        self.mem.write4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x37C], xhero)
                        self.mem.write4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 + 0x4 - 0x37C], yhero)
                        self.mem.write1Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4 + 0x20], 0)
                        time.sleep(0.1)
                    break
                    # self.mem.write1Byte("main.exe+100A900", None, 2)

        except Exception as e:
            print(hfile.getError())

    def autoPK(self, dongbangquai=False, type="pk", timesl=2):

        if self.classs == "rf":
            self.mem.write1Byte(baseAutoZ, [0x4, 0x32], 7)
        xhero, yhero = self.getPosHero()
        # xhero = xhero - 1

        autoZ = self.getEnableAutoZ()
        if type == "pk" or type == "pkk":
            if autoZ:
                if type == "pkk":
                    self.setMousePosition(319, 208)
                self.setKeepMouseRight(True)
        for i in range(-1, 50):
            namemonters = self.mem.readString(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4])
            namemonters = namemonters.replace("(", " ")
            if " " in namemonters:
                continue
            if namemonters == self.namehero:
                continue
            if namemonters in listkopk:
                continue
            # xheroset = xhero

            xmonters = self.mem.read4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x37C])
            ymonters = self.mem.read4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 + 0x4 - 0x37C])
            if hstr.triTuyetDoi(xmonters - xhero) > 5 or hstr.triTuyetDoi(ymonters - yhero) > 5:
                continue
            self.mem.write1Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4 - 0x18], 6)  # trạng thái quỷ đỏ
            # self.mem.writeString(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4], "111111111111111")
            if listpk:
                if not namemonters in listpk:
                    continue

            if autoZ or type == "pkg":
                self.mem.writeFloat(baseListHero, [0x8, 0x51C + i * 0x6F4], xhero * 100 + 50)
                self.mem.writeFloat(baseListHero, [0x8, 0x51C + i * 0x6F4 + 0x4], yhero * 100 + 50)
                time.sleep(timesl)
            # self.mem.write4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x37C], xhero)
            # self.mem.write4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 + 0x4 - 0x37C], yhero)

    def autoPKList(self):
        # print(listpk)
        if not listpk:
            return
        xhero, yhero = self.getPosHero()
        # xhero = xhero - 1
        # self.setMousePosition(319, 208)

        autoZ = self.getEnableAutoZ()

        for i in range(-1, 50):
            namemonters = self.mem.readString(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4])
            namemonters = namemonters.replace("(", " ")
            if " " in namemonters:
                continue
            if namemonters == self.namehero:
                continue
            if namemonters in listkopk:
                continue
            # xheroset = xhero
            if not namemonters in listpk:
                continue
            xmonters = self.mem.read4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x37C])
            ymonters = self.mem.read4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 + 0x4 - 0x37C])
            if hstr.triTuyetDoi(xmonters - xhero) > 5 or hstr.triTuyetDoi(ymonters - yhero) > 5:
                continue

            self.mem.write1Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4 - 0x18], 6)  # trạng thái quỷ đỏ
            # self.mem.writeString(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4], "111111111111111")

            if autoZ:
                if self.classs == "rf":
                    self.mem.write1Byte(baseAutoZ, [0x4, 0x32], 7)
                self.setMousePosition(319, 204)
                self.setKeepMouseRight(True)
                for z in range(30):
                    self.mem.writeFloat(baseListHero, [0x8, 0x51C + i * 0x6F4], xhero * 100 + 50)
                    self.mem.writeFloat(baseListHero, [0x8, 0x51C + i * 0x6F4 + 0x4], yhero * 100 + 50)
                    time.sleep(0.1)

            # self.mem.write4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x37C], xhero)
            # self.mem.write4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 + 0x4 - 0x37C], yhero)

    def autoGomQuai(self, printmon=False, dongbangquai=False, keepmouse=False, khoangcachgom=10):
        try:
            xhero, yhero = self.getPosHero()

            if keepmouse:
                self.setMousePosition(281, 197)
                # self.setMousePosition(319, 208)
                self.setKeepMouseRight(True)
            j = -1
            for i in range(-1, 50):
                namemonters = self.mem.readString(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4])
                namemonters = namemonters.replace("(", " ")
                if not " " in namemonters:
                    continue
                j = j + 1
                # if namemonters == namehero:
                #     continue
                if j > 3:
                    j = 0
                xheroset = xhero - 2
                yheroset = yhero - 1 + j
                # if classs == "elf" or classs == "mg" or classs == "dw":
                xheroset = xhero
                yheroset = yhero
                if printmon:
                    print(namemonters)
                if khoangcachgom > 0:
                    xmonters = self.mem.read4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x37C])
                    ymonters = self.mem.read4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 + 0x4 - 0x37C])

                    if hstr.triTuyetDoi(xmonters - xhero) > 10 or hstr.triTuyetDoi(ymonters - yhero) > 10:
                        continue
                # self.mem.writeString(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4], "111111111111111")
                self.mem.writeFloat(baseListHero, [0x8, 0x51C + i * 0x6F4], xheroset * 100 + 50)
                self.mem.writeFloat(baseListHero, [0x8, 0x51C + i * 0x6F4 + 0x4], yheroset * 100 + 50)
                self.mem.write4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x37C], xheroset)
                self.mem.write4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 + 0x4 - 0x37C], yheroset)
                if dongbangquai:
                    self.mem.write1Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4 + 0x20], 0)
        except Exception as e:
            print(hfile.getError())

    def autoGomQuaiSatViTri(self, printmon=False, dongbangquai=False):
        if not printmon:
            autoZ = self.getEnableAutoZ()
            if not autoZ:
                time.sleep(0.1)
                return
        xhero, yhero = self.getPosHero()
        # xhero = xhero - 1
        keepmouse = True
        if keepmouse:
            self.setMousePosition(281, 197)
            # self.setMousePosition(319, 208)
            self.setKeepMouseRight(True)
        j = -1
        for i in range(-1, 50):
            namemonters = self.mem.readString(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4])
            namemonters = namemonters.replace("(", " ")
            if not " " in namemonters:
                continue
            j = j + 1
            # if namemonters == namehero:
            #     continue
            if j > 3:
                j = 0
            xheroset = xhero - 2
            yheroset = yhero - 1 + j

            if printmon:
                print(namemonters)
            khoangcachgom = 10
            if khoangcachgom > 0:
                xmonters = self.mem.read4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x37C])
                ymonters = self.mem.read4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 + 0x4 - 0x37C])

                if hstr.triTuyetDoi(xmonters - xhero) > khoangcachgom or hstr.triTuyetDoi(ymonters - yhero) > khoangcachgom:
                    continue
            # self.mem.writeString(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4], "111111111111111")
            self.mem.writeFloat(baseListHero, [0x8, 0x51C + i * 0x6F4], xheroset * 100 + 50)
            self.mem.writeFloat(baseListHero, [0x8, 0x51C + i * 0x6F4 + 0x4], yheroset * 100 + 50)
            self.mem.write4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x37C], xheroset)
            self.mem.write4Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 + 0x4 - 0x37C], yheroset)
            if dongbangquai:
                self.mem.write1Byte(baseListHero, [0x8, 0x51C + i * 0x6F4 - 0x4E4 + 0x20], 0)

    def gomQuai(self):
        try:
            while True:
                chat = self.getChat()
                if not "/gom" in chat:
                    break
                if chat == "/gom":
                    self.autoGomQuai()
                if chat == "/gomk":
                    self.autoGomQuai(keepmouse=True)
                if chat == "/gomp":
                    self.autoGomQuai(keepmouse=True, khoangcachgom=0)
                time.sleep(0.05)
        except Exception as e:
            print(hfile.getError())
            pass

    def getClass(self):
        classid = self.mem.read1Byte(0x9F50D18, [0x10C - 0x2])
        if classid == 5 or classid == 21 or classid == 53:
            return "sum"
        elif classid == 18 or classid == 50 or classid == 2:
            return "elf"
        elif classid == 7 or classid == 55:
            return "gl"
        elif classid == 54:
            return "rf"
        elif classid == 3 or classid == 51:
            return "mg"
        elif classid == 4 or classid == 52:
            return "dl"
        elif classid == 0 or classid == 48:
            return "dw"
        elif classid == 1 or classid == 49:
            return "dk"
        else:
            print(self.namehero, "class không khớp", classid)
        return ""

    def getHPConLai(self):
        hp = self.mem.read4Byte("XIProject.dll+F3130")
        return hp

    def getStaminaAll(self):
        stamina = self.mem.read4Byte("XIProject.dll+F3114")
        return stamina

    def getBatChat(self):
        value = self.mem.read4Byte('"main.exe"+09B563D0', [0xDC, 0x28, 0x104, 0x10, 0x1F0])
        if value == 257:
            return True
        else:
            return False

    def tatBatChat(self):
        if self.getBatChat():
            self.sendKey("enter")

    def readMapSave(self, map):
        try:
            return ini.read(map + "_" + self.namehero)
        except:
            return ""

    def readServerSave(self):
        try:
            return ini.readint("server_" + self.namehero, 2)
        except:
            return 1

    def saveMap(self, map, xy):
        print(self.namehero, "Lưu map ok")
        ini.write(map + "_" + self.namehero, xy)

    def saveMapAuto(self, map, xy):
        print(self.namehero, "Lưu map ok")
        ini.write("mapauto_" + self.namehero, map)
        ini.write("xyauto_" + self.namehero, xy)

    def getMapAuto(self):
        map = ini.read("mapauto_" + self.namehero)
        xy = ini.readtuple("xyauto_" + self.namehero)

        dic = dict()
        dic["map"] = map

        dic["x"] = xy[0]
        dic["y"] = xy[1]
        return dic

    def saveServer(self):
        ini.write("server_" + self.namehero, self.getServer())

    def getServer(self):
        return self.mem.read1Byte("main.exe+9B4C420")

    def webBaoTri(self):
        now = datetime.now()
        if now.hour == 23 and now.minute > 50:
            return True
        if now.hour == 00 and now.minute < 16:
            return True
        if now.hour == 5 and now.minute < 22:
            return True
        return False

    def isReseting(self):
        # if self.pid in listpidreset:
        #     return True
        for pid in listpidreset:

            # print(pid, listpidreset.get(pid))
            if listpidreset.get(pid):
                if pid != self.pid:  # phòng trường hợp click chưa được
                    return True
        # print("check web bảo trì")
        return self.webBaoTri()

    def updateListNhatDo(self):
        try:
            # if ini.readboolean(self.namehero + "_nhatdo"):
            #     return
            # ini.write(self.namehero + "_nhatdo", True)
            self.itemcannhat = "52 65 6E 61 00 85 7C BF 93 90 5D B3 CB 3D A6 34 04 00 00 00 0F 00 00 00 93 90 5D B3 48 20 70 20 4B 75 6E 64 75 6E 00 BF 93 90 5D B3 0A 00 00 00 0F 00 00 00 06 85 7C BF 4B 75 6E 64 75 6E 20 34 00 47 28 BE 06 85 7C BF 08 00 00 00 0F 00 00 00 19 47 28 BE 4B 75 6E 64 75 6E 20 35 00 3D A6 34 19 47 28 BE 08 00 00 00 0F 00 00 00 CB 3D A6 34 54 69 EA D2 75 20 51 00 93 90 5D B3 CB 3D A6 34 07 00 00 00 0F 00 00 00 93 90 5D B3 48 75 79 20 68 69 20 48 20 6E 67 20 54 20 63 00 0F 00 00 00 0F 00 00 00 03 85 7C BF 4B 75 6E 64 75 6E 20 36 00 46 28 BE DC 84 7C BF 08 00 00 00 0F 00 00 00 9F 46 28 BE 4B 75 6E 64 75 6E 20 37 00 50 98 3B D4 45 28 BE 08 00 00 00 0F 00 00 00 39 36 F8 3B 54 65 74 72 61 00 7C BF A7 F4 EA BA E7 49 30 3C 05 00 00 00 0F 00 00 00 EC 3E 18 BB 4C 69 6E 68 20 68 20 6E 20 68 75 EC 00 32 38 BB 0C 00 00 00 0F 00 00 00 AD 78 7C BF 70 20 54 EA EC 74 00 3C 6A 3D 28 BE 7D 76 7C BF 06 00 00 00 0F 00 00 00 D9 3C 28 BE 4B 79 CC 20 4C E2 6E 00 95 45 B0 3C F0 3C 28 BE 07 00 00 00"
            self.mem.writeByteArray(baseAutoZ, [0x150], self.itemcannhat)

        except:
            pass

    def clickReloadServer(self):
        self.mouseClick(223, 295)

    def saveMapF2(self):
        x, y = self.getPosHero()
        map = self.getMap(x, y)
        log(f"{htime.getStrTimeNow3()}: {self.namehero} save {map} {x} {y}")
        self.saveMapAuto(map, (x, y))
        self.saveServer()
        self.setPhimBamCuoiCung(112)
        herostop[self.namehero] = False

    def getIdSkill1(self):
        try:
            return self.mem.read4Byte(baseAutoZ, [0xE4])
        except:
            pass
        return 0

    def activeSkill3(self, enable):
        try:
            if enable:
                skill3 = self.mem.read4Byte(baseAutoZ, [0xE4])
                # print(self.namehero, skill3)
                if skill3 > 0:
                    self.mem.write4Byte(baseAutoZ, [0xE8], 1)
            else:
                self.mem.write4Byte(baseAutoZ, [0xE8], 0)
        except:
            pass

    def waitLive(self):
        for z123 in range(10):
            time.sleep(1)
            somau = self.getHPConLai()
            # print(self.namehero, somau)
            if somau != 0:
                break

    def checkDieuKienVaoStadium(self):
        global infostadiums
        date = htime.getNgayThangNam() + "_" + self.namehero
        if not date in infostadiums:
            infostadiums[date] = False
        if infostadiums[date]:
            return False
        return True

    def trainMapStadium30p(self):
        global infostadiums
        date = htime.getNgayThangNam() + "_" + self.namehero
        if not date in infostadiums:
            infostadiums[date] = False
        if infostadiums[date]:
            return False
        infostadiums[date] = False
        for i in range(20):
            map = self.getMap(0, 0)
            if "Arena" in map:
                self.starttrainstadium = True
                return True
            with lockbando:
                self.clickHwnd(133, 88)
            with lockbando:
                self.clickHwnd(390, 268)
            time.sleep(1)
        infostadiums[date] = True
        return False

    def checkDieuKienVaoMapExp(self):
        filedata = "data/trainexp/" + htime.getNgayThangNam() + "_" + self.namehero + "_" + ".txt"
        oldData = hfile.read(filedata)
        if oldData == "":
            oldData = "0"
        oldData = int(oldData)
        return oldData

    def trainMapExp(self):
        filedata = "data/trainexp/" + htime.getNgayThangNam() + "_" + self.namehero + "_" + ".txt"
        oldData = self.checkDieuKienVaoMapExp()
        if oldData >= 3:
            return False
        for i in range(20):
            map = self.getMap(0, 0)
            if "Blagass" in map:
                hfile.write(filedata, oldData + 1, False)
                return True
            with lockbando:
                self.clickHwnd(133, 88)
            with lockbando:
                self.clickHwnd(388, 209)
            time.sleep(1)
        hfile.write(filedata, 3)
        return True

    def hackKhoangCach(self):
        global setskill
        if self.namehero in setskill:
            return
        listskillhack = []
        if self.classs == "mg":
            listskillhack.append(khoangcach["tianangluong"])
            listskillhack.append(khoangcach["muasaobang"])
            listskillhack.append(khoangcach["muasaobangmaster"])
            listskillhack.append(khoangcach["luongnuocxanh"])
        if self.classs == "rf":
            listskillhack.append(khoangcach["bangquyen"])
        if self.classs == "dl":
            listskillhack.append(khoangcach["hoaxichlong"])
            # listskillhack.append(khoangcach["trieuhoiqua"])
        if self.classs == "dw":
            listskillhack.append(khoangcach["muabangtuyet"])
            listskillhack.append(khoangcach["dongbang"])
        if self.classs == "sum":
            listskillhack.append(khoangcach["dongbang"])
        if self.classs == "elf":
            listskillhack.append(khoangcach["tamtien"])
            listskillhack.append(khoangcach["tanconglienhoan"])
            listskillhack.append(khoangcach["tanconglienhoanmaster"])

        for i in listskillhack:
            kc = 8
            if "," in i:
                kc = int(i.split(",")[1])
                i = i.split(",")[0]
            address = self.mem.aobScan(i, False)
            if len(address) > 1:
                for z in address:
                    if z > 1903056216:
                        address.remove(z)
            if len(address) == 1:
                address = address[0] + 0xC
                self.mem.write1Byte(address, None, kc)
        if listskillhack:
            setskill[self.namehero] = True

    def getInfoCongDiem(self):
        congdiem = getCongDiem(self.namehero).get("result")
        if not congdiem:
            return False
        str = congdiem.get("addstr")
        strp = "+"
        if strp in str:
            self.congdiem300lv = "addstr"
        agi = congdiem.get("addagi")
        if strp in agi:
            self.congdiem300lv = "addagi"
        vit = congdiem.get("addvit")
        if strp in vit:
            self.congdiem300lv = "addvit"
        ene = congdiem.get("addene")
        if strp in ene:
            self.congdiem300lv = "addene"
        cmd = congdiem.get("addcmd")
        if strp in cmd:
            self.congdiem300lv = "addcmd"
        pointstr = int(str.replace(strp, ""))
        pointagi = int(agi.replace(strp, ""))
        pointvit = int(vit.replace(strp, ""))
        pointene = int(ene.replace(strp, ""))
        pointcmd = int(cmd.replace(strp, ""))
        return pointstr, pointagi, pointvit, pointene, pointcmd

listnvstopgom = []


def gomQuaiThread(pid, mapauto):
    try:
        s12 = s12tl(pid)
        s12.namehero = "hero"
        while True:
            if pid in listnvstopgom:
                return
            sonv = s12.quetNV(khoangcachquet=20)
            if sonv:
                time.sleep(1)
                continue
            # print("autoGomQuai")
            map = s12.getMap(0, 0)
            if map != mapauto:
                time.sleep(1)
                continue
            s12.autoGomQuai()
            time.sleep(0.1)
    except Exception as e:
        print(hfile.getError())
        pass