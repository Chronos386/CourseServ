from DBHelper.DBClass import DBClass
from DBHelper.AllModels import *


class Answerer:
    def __init__(self):
        self.HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: application/json; charset=utf-8\r\n\r\n'
        self.content = ""
        self.dbHelper = DBClass()

    def default(self, cl_sock):
        self.HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
        self.content = '<title>Error Python HTTP Server</title>\n<div><center><h1><br><br><br>ERROR 404</h1>' \
                       '</center>\n</div><div><center><br><br>This page wasn\'t found.</center></div>'.encode('utf-8')
        cl_sock.send(self.HDRS.encode('utf-8') + self.content)
        self.HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: application/json; charset=utf-8\r\n\r\n'

    def firstHTML(self, cl_sock):
        self.HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
        self.content = '<title>Test Python HTTP Server</title>\n<p><center><img ' \
                       'src="https://i.pinimg.com/564x/ae/74/56/ae74569e3905410204dd9ac2b236c33d.jpg"></center></p>\n' \
                       '<center><br><big>Where is my SSL certificate?</big></center>'.encode('utf-8')
        cl_sock.send(self.HDRS.encode('utf-8') + self.content)
        self.HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: application/json; charset=utf-8\r\n\r\n'

    def sendRaseTable(self, cl_sock):
        self.content = self.dbHelper.tableToJSON(Races)
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))

    def sendRase(self, cl_sock, race_id):
        self.content = self.dbHelper.findRaceByID(race_id)
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))

    def sendWeapTypeTable(self, cl_sock):
        self.content = self.dbHelper.tableToJSON(weapon_types)
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))

    def sendArmorTypeTable(self, cl_sock):
        self.content = self.dbHelper.tableToJSON(armor_types)
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))

    def sendClassTable(self, cl_sock):
        self.content = self.dbHelper.tableToJSON(Classes)
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))

    def sendVarRase(self, cl_sock, race_id):
        self.content = self.dbHelper.findVarRacesByID(int(race_id))
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))

    def sendVarRaseByRace(self, cl_sock, race):
        self.content = self.dbHelper.findVarRacesByRace(int(race))
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))

    def sendWeapon(self, cl_sock, weap_id):
        self.content = self.dbHelper.findWeaponByID(int(weap_id))
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))

    def sendWeaponByType(self, cl_sock, type_weap):
        self.content = self.dbHelper.findWeaponByType(int(type_weap))
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))

    def sendArmor(self, cl_sock, armor_id):
        self.content = self.dbHelper.findArmorByID(int(armor_id))
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))

    def sendArmorByType(self, cl_sock, type_armor):
        self.content = self.dbHelper.findArmorByType(int(type_armor))
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))

    def sendSpell(self, cl_sock, spell_id):
        self.content = self.dbHelper.findSpellByID(int(spell_id))
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))

    def sendWeapByClass(self, cl_sock, class_id):
        self.content = self.dbHelper.findWeaponByClass(int(class_id))
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))

    def sendArmByClass(self, cl_sock, class_id):
        self.content = self.dbHelper.findArmorByClass(int(class_id))
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))

    def sendSpellByClass(self, cl_sock, class_id):
        self.content = self.dbHelper.findSpellByClass(int(class_id))
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))

    def sendDescr(self, cl_sock, descr_id):
        self.content = self.dbHelper.findDescrByID(int(descr_id))
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))

    def sendAcc(self, cl_sock, acc_id):
        self.content = self.dbHelper.findAccByID(int(acc_id))
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))

    def sendExistAccByLog(self, cl_sock, acc_log):
        self.HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
        self.content = self.dbHelper.findAccByLog(acc_log)
        if len(self.content) == 2:
            cl_sock.send(self.HDRS.encode('utf-8') + 'No'.encode('utf-8'))
        else:
            cl_sock.send(self.HDRS.encode('utf-8') + 'Yes'.encode('utf-8'))
        self.HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: application/json; charset=utf-8\r\n\r\n'

    def sendAccByLogPasw(self, cl_sock, acc_log, acc_pasw):
        self.content = self.dbHelper.findAccByLogPassword(acc_log, acc_pasw)
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))

    def sendPict(self, cl_sock, pict_id):
        self.content = self.dbHelper.findPictByID(int(pict_id))
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))

    def sendDamBuffByCher(self, cl_sock, ch_id):
        self.content = self.dbHelper.findDamBuffByCherID(int(ch_id))
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))

    def sendHealthBuffByCher(self, cl_sock, ch_id):
        self.content = self.dbHelper.findHealthBuffByCherID(int(ch_id))
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))

    def sendExistGameByName(self, cl_sock, name):
        self.HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
        self.content = self.dbHelper.findGameByName(name)
        if len(self.content) == 2:
            cl_sock.send(self.HDRS.encode('utf-8') + 'No'.encode('utf-8'))
        else:
            cl_sock.send(self.HDRS.encode('utf-8') + 'Yes'.encode('utf-8'))
        self.HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: application/json; charset=utf-8\r\n\r\n'

    def sendGameByNamePasw(self, cl_sock, name, acc_pasw):
        self.content = self.dbHelper.findGameByNamePassword(name, acc_pasw)
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))

    def sendCharByAccGame(self, cl_sock, acc_id, game_id):
        self.content = self.dbHelper.findCharByAccGame(int(acc_id), int(game_id))
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))

    def sendGamesByAcc(self, cl_sock, acc_id):
        self.content = self.dbHelper.findGameByAcc(int(acc_id))
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))

    def sendCharactersByAcc(self, cl_sock, acc_id):
        self.content = self.dbHelper.findCharactersByAcc(int(acc_id))
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))

    def sendOk(self, cl_sock):
        self.HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
        self.content = "Ok\0"
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))
        self.HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: application/json; charset=utf-8\r\n\r\n'

    def sendOnlineAccByGame(self, cl_sock, game_id):
        self.content = self.dbHelper.findOnlineAccByGame(int(game_id))
        cl_sock.send(self.HDRS.encode('utf-8') + self.content.encode('utf-8'))
