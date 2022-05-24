import socket
from threading import Thread
from NetHelper.Answerer import *
from DBHelper.Sawer import *


class HTTPReq:
    RequestType = ""
    RequestBody = ""


class NetClass:
    def __init__(self):
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Request = HTTPReq()
        self.answ = Answerer()
        self.postBody = ''
        self.save = Saver()

    def reqAnalysis(self, data):
        counter = 3
        try:
            txt = data.decode('utf-8')
        except socket.error:
            return
        print(txt)
        while txt[counter - 2:counter] != ' /' and counter < len(txt):
            counter += 1
        if txt[counter - 2:counter] != ' /':
            return
        self.Request.RequestType = txt[0:counter - 2]
        start = counter
        counter += 1
        findSymb = ''
        while findSymb != 'HTTP/':
            if txt[counter - 1:counter] == 'H':
                if txt[counter - 1:counter + 4] == 'HTTP/':
                    findSymb = txt[counter - 1:counter + 4]
                    counter -= 2
                else:
                    counter += 1
            else:
                counter += 1
        self.Request.RequestBody = txt[start:counter]
        self.Request.RequestBody = self.Request.RequestBody.replace("%20", " ")

    def postReqAnalyse(self, data):
        try:
            txt = data.decode('utf-8')
        except TypeError:
            return
        self.postBody = ""
        partsBody = txt.split("\n")
        if len(partsBody) >= 9:
            for i in range(8, len(partsBody)):
                if i != 8:
                    self.postBody += "\n"
                self.postBody += partsBody[i]

    def sendAnswer(self, cl_sock):
        partsBody = self.Request.RequestBody.split("/")
        match partsBody[0]:
            case "":
                self.answ.firstHTML(cl_sock)
            case "table":
                match len(partsBody):
                    case 2:
                        match partsBody[1]:
                            case "race":
                                self.answ.sendRaseTable(cl_sock)
                            case "weap_type":
                                self.answ.sendWeapTypeTable(cl_sock)
                            case "armor_type":
                                self.answ.sendArmorTypeTable(cl_sock)
                            case "class":
                                self.answ.sendClassTable(cl_sock)
                            case _:
                                self.answ.default(cl_sock)
                    case 3:
                        match partsBody[1]:
                            case "class":
                                self.answ.sendClass(cl_sock, partsBody[2])
                            case "race":
                                self.answ.sendRase(cl_sock, partsBody[2])
                            case "var_race":
                                self.answ.sendVarRase(cl_sock, partsBody[2])
                            case "weap":
                                self.answ.sendWeapon(cl_sock, partsBody[2])
                            case "armor":
                                self.answ.sendArmor(cl_sock, partsBody[2])
                            case "spell":
                                self.answ.sendSpell(cl_sock, partsBody[2])
                            case "descript":
                                self.answ.sendDescr(cl_sock, partsBody[2])
                            case "account":
                                self.answ.sendAcc(cl_sock, partsBody[2])
                            case "picture":
                                self.answ.sendPicture(cl_sock, partsBody[2])
                            case _:
                                self.answ.default(cl_sock)
                    case 4:
                        match partsBody[1]:
                            case "account":
                                self.answ.sendAccByLogPasw(cl_sock, partsBody[2], partsBody[3])
                            case "game":
                                self.answ.sendGameByNamePasw(cl_sock, partsBody[2], partsBody[3])
                            case "character":
                                self.answ.sendCharByAccGame(cl_sock, partsBody[2], partsBody[3])
                            case _:
                                self.answ.default(cl_sock)
                    case _:
                        self.answ.default(cl_sock)
            case "types":
                if len(partsBody) == 3:
                    match partsBody[1]:
                        case "var_race":
                            self.answ.sendVarRaseByRace(cl_sock, partsBody[2])
                        case "weap":
                            self.answ.sendWeaponByType(cl_sock, partsBody[2])
                        case "armor":
                            self.answ.sendArmorByType(cl_sock, partsBody[2])
                        case _:
                            self.answ.default(cl_sock)
                else:
                    self.answ.default(cl_sock)
            case "class":
                if len(partsBody) == 3:
                    match partsBody[1]:
                        case "weapon":
                            self.answ.sendWeapByClass(cl_sock, partsBody[2])
                        case "armor":
                            self.answ.sendArmByClass(cl_sock, partsBody[2])
                        case "spell":
                            self.answ.sendSpellByClass(cl_sock, partsBody[2])
                        case _:
                            self.answ.default(cl_sock)
                else:
                    self.answ.default(cl_sock)
            case "account":
                if len(partsBody) == 3:
                    match partsBody[1]:
                        case "dammBuff":
                            self.answ.sendDamBuffByCher(cl_sock, partsBody[2])
                        case "hpBuff":
                            self.answ.sendHealthBuffByCher(cl_sock, partsBody[2])
                        case "games":
                            self.answ.sendGamesByAcc(cl_sock, partsBody[2])
                        case "characters":
                            self.answ.sendCharactersByAcc(cl_sock, partsBody[2])
                        case _:
                            self.answ.default(cl_sock)
                else:
                    self.answ.default(cl_sock)
            case "game":
                if len(partsBody) == 2:
                    self.answ.sendOnlineAccByGame(cl_sock, partsBody[1])
                elif len(partsBody) == 3:
                    if partsBody[1] == "accounts":
                        self.answ.sendAccByGame(cl_sock, partsBody[2])
                    else:
                        self.answ.default(cl_sock)
                else:
                    self.answ.default(cl_sock)
            case "exist":
                if len(partsBody) == 3:
                    match partsBody[1]:
                        case "account":
                            self.answ.sendExistAccByLog(cl_sock, partsBody[2])
                        case "game":
                            self.answ.sendExistGameByName(cl_sock, partsBody[2])
                        case _:
                            self.answ.default(cl_sock)
                else:
                    self.answ.default(cl_sock)
            case _:
                self.answ.default(cl_sock)
        cl_sock.close()

    def saveData(self):
        partsBody = self.Request.RequestBody.split("/")
        match partsBody[0]:
            case "new":
                match partsBody[1]:
                    case "account":
                        self.save.addNewAccount(self.postBody)
                    case "game":
                        self.save.addNewGame(self.postBody)
                    case "character":
                        self.save.addNewCharacter(self.postBody)

            case "update":
                match partsBody[1]:
                    case "account":
                        self.save.updAccountPsw(self.postBody)
                    case "game":
                        self.save.updGameByDelCh(partsBody[2], self.postBody)
                    case "character":
                        self.save.updCharacter(self.postBody)

            case "delete":
                match partsBody[1]:
                    case "account":
                        self.save.dellAccount(self.postBody)
                    case "game":
                        self.save.dellGame(self.postBody)
                    case "character":
                        self.save.dellCharacter(self.postBody)
            case _:
                print("Попытка запостить кринж")

    def give_inf(self, cl_sock):
        data = cl_sock.recv(1024)
        self.reqAnalysis(data)
        if self.Request.RequestType == 'GET':
            self.sendAnswer(cl_sock)
        elif self.Request.RequestType == 'POST':
            self.answ.sendOk(cl_sock)
            self.postReqAnalyse(data)
            self.saveData()

    def listenWebServ(self):
        self.serv.bind(('192.168.100.3', 80))
        self.serv.listen(1000)
        while True:
            try:
                client_sock, adder = self.serv.accept()
            except socket.error:
                pass
            else:
                thr = Thread(target=self.give_inf, args=(client_sock,))
                thr.start()
