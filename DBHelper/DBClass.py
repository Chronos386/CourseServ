from sqlalchemy.orm import sessionmaker
from DBHelper.AllModels import *
from DBHelper.Encoder import *
import json


class DBClass:
    def __init__(self):
        self.engine = create_engine("postgresql+psycopg2://postgres:Chronos386@localhost/game_app")
        self.conn = self.engine.connect()
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def getCountWeapType(self):
        return self.session.query(weapon_types).count()

    def getCountArmType(self):
        return self.session.query(armor_types).count()

    def getCountUsrSt(self):
        return self.session.query(user_status).count()

    def getCountAcc(self):
        return self.session.query(Accounts).count()

    def getCountDescr(self):
        return self.session.query(descriptions).count()

    def getCountRace(self):
        return self.session.query(Races).count()

    def getCountVarRace(self):
        return self.session.query(var_races).count()

    def getCountClass(self):
        return self.session.query(Classes).count()

    def getCountWeap(self):
        return self.session.query(Weapon).count()

    def getCountArm(self):
        return self.session.query(Armor).count()

    def getCountSpell(self):
        return self.session.query(Spell_table).count()

    def getCountWeapCl(self):
        return self.session.query(Relat_table_t_weap_t_cl).count()

    def getCountArmCl(self):
        return self.session.query(Relat_table_t_arm_t_cl).count()

    def getCountSpellCl(self):
        return self.session.query(Relat_table_t_spell_cl).count()

    def getCountGame(self):
        return self.session.query(Games).count()

    def getCountChar(self):
        return self.session.query(Character).count()

    def getCountDammBuff(self):
        return self.session.query(damage_buff).count()

    def getCountHealBuff(self):
        return self.session.query(health_buff).count()

    def tableToJSON(self, tabl):
        c = self.session.query(tabl).all()
        dataTable = json.dumps(c, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        return dataTable

    def findRaceByID(self, race_id):
        c = self.session.query(Races).filter_by(id=race_id).all()
        dataTable = json.dumps(c, cls=AlchemyEncoder, ensure_ascii=False)
        return dataTable

    def findVarRacesByID(self, vrace_id):
        c = self.session.query(var_races).filter_by(id=vrace_id).all()
        dataTable = json.dumps(c, cls=AlchemyEncoder, ensure_ascii=False)
        return dataTable

    def findVarRacesByRace(self, race_id):
        c = self.session.query(var_races).filter_by(rac_id=race_id).all()
        dataTable = json.dumps(c, cls=AlchemyEncoder, ensure_ascii=False)
        return dataTable

    def findWeaponByID(self, this_id):
        c = self.session.query(Weapon).filter_by(id=this_id).all()
        dataTable = json.dumps(c, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        return dataTable

    def findWeaponByType(self, type_id):
        c = self.session.query(Weapon).filter_by(weap_t_id=type_id).all()
        dataTable = json.dumps(c, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        return dataTable

    def findWeaponByClass(self, cl_id):
        a = self.session.query(Relat_table_t_weap_t_cl).filter_by(class_id=cl_id).all()
        b = self.session.query(weapon_types).filter_by(id=a[0].weap_t_id).all()
        b.clear()
        for i in a:
            b += self.session.query(weapon_types).filter_by(id=i.weap_t_id).all()
        c = self.session.query(Weapon).filter_by(weap_t_id=b[0].id).all()
        c.clear()
        for i in b:
            c += self.session.query(Weapon).filter_by(weap_t_id=i.id).all()
        dataTable = json.dumps(c, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        return dataTable

    def findArmorByID(self, this_id):
        c = self.session.query(Armor).filter_by(id=this_id).all()
        dataTable = json.dumps(c, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        return dataTable

    def findArmorByType(self, type_id):
        c = self.session.query(Armor).filter_by(arm_t_id=type_id).all()
        dataTable = json.dumps(c, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        return dataTable

    def findArmorByClass(self, cl_id):
        a = self.session.query(Relat_table_t_arm_t_cl).filter_by(class_id=cl_id).all()
        b = self.session.query(armor_types).filter_by(id=a[0].arm_t_id).all()
        b.clear()
        for i in a:
            b += self.session.query(armor_types).filter_by(id=i.arm_t_id).all()
        c = self.session.query(Armor).filter_by(arm_t_id=b[0].id).all()
        c.clear()
        for i in b:
            c += self.session.query(Armor).filter_by(arm_t_id=i.id).all()
        dataTable = json.dumps(c, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        return dataTable

    def findSpellByID(self, spell_id):
        c = self.session.query(Spell_table).filter_by(id=spell_id).all()
        dataTable = json.dumps(c, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        return dataTable

    def findSpellByClass(self, cl_id):
        a = self.session.query(Relat_table_t_spell_cl).filter_by(class_id=cl_id).all()
        if len(a) != 0:
            c = self.session.query(Spell_table).filter_by(id=a[0].spell_id).all()
            c.clear()
            for i in a:
                c += self.session.query(Spell_table).filter_by(id=i.spell_id).all()
            dataTable = json.dumps(c, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        else:
            dataTable = json.dumps(a, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        return dataTable

    def findDescrByID(self, descr_id):
        c = self.session.query(descriptions).filter_by(id=descr_id).all()
        dataTable = json.dumps(c, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        return dataTable

    def findAccByID(self, acc_id):
        c = self.session.query(Accounts).filter_by(id=acc_id).all()
        dataTable = json.dumps(c, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        return dataTable

    def findAccByLog(self, acc_log):
        c = self.session.query(Accounts).filter_by(login=acc_log).all()
        dataTable = json.dumps(c, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        return dataTable

    def findAccByLogPassword(self, acc_log, acc_pasw):
        c = self.session.query(Accounts).filter_by(login=acc_log, password=acc_pasw).all()
        dataTable = json.dumps(c, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        return dataTable

    def findPictByID(self, pict_id):
        c = self.session.query(pict_avatar).filter_by(id=pict_id).all()
        dataTable = json.dumps(c, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        return dataTable

    def findDamBuffByCherID(self, ch_id):
        c = self.session.query(damage_buff).filter_by(ch_id=ch_id).all()
        dataTable = json.dumps(c, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        return dataTable

    def findHealthBuffByCherID(self, ch_id):
        c = self.session.query(health_buff).filter_by(ch_id=ch_id).all()
        dataTable = json.dumps(c, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        return dataTable

    def findGameByName(self, name):
        c = self.session.query(Games).filter_by(game_name=name).all()
        dataTable = json.dumps(c, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        return dataTable

    def findGameByNamePassword(self, name, acc_pasw):
        c = self.session.query(Games).filter_by(game_name=name, password=acc_pasw).first()
        dataTable = json.dumps(c, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        data = json.loads(dataTable)
        acc = self.session.query(Accounts).filter_by(id=int(data["master_id"])).first()
        data["master_id"] = acc.login
        dataTable = json.dumps(data, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        return dataTable

    def findGameByAcc(self, acc_id):
        a = self.session.query(Character).filter_by(acc_id=acc_id).all()
        if len(a) != 0:
            c = self.session.query(Games).filter_by(id=a[0].game_id).all()
            first_id = [a[0].game_id]
            for i in a:
                if i.game_id not in first_id:
                    c += self.session.query(Games).filter_by(id=i.game_id).all()
                    first_id.append(i.game_id)
        b = self.session.query(Games).filter_by(master_id=acc_id).all()
        if len(a) != 0:
            for i in b:
                if i.id not in first_id:
                    c += i
            dataTable = json.dumps(c, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        else:
            dataTable = json.dumps(b, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        data = json.loads(dataTable)
        for i in data:
            acc = self.session.query(Accounts).filter_by(id=int(i["master_id"])).first()
            i["master_id"] = acc.login
        dataTable = json.dumps(data, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        return dataTable

    def findCharactersByAcc(self, acc_id):
        a = self.session.query(Character).filter_by(acc_id=acc_id).all()
        dataTable = json.dumps(a, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        data = json.loads(dataTable)
        for i in data:
            url = self.session.query(pict_avatar).filter_by(id=int(i["pict_id"])).first()
            i["pict_id"] = url.url
        dataTable = json.dumps(data, ensure_ascii=False, sort_keys=True)
        return dataTable

    def findCharByAccGame(self, acc_id, game_id):
        c = self.session.query(Character).filter_by(acc_id=acc_id, game_id=game_id).all()
        dataTable = json.dumps(c, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        return dataTable

    def findOnlineAccByGame(self, game_id):
        c = self.session.query(online_gamers).filter_by(game_id=game_id).all()
        dataTable = json.dumps(c, cls=AlchemyEncoder, ensure_ascii=False, sort_keys=True)
        return dataTable
