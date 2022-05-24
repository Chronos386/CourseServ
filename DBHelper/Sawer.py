import json
from DBHelper.DBClass import DBClass
from DBHelper.AllModels import *


def findFirstFreeID(table_db):
    stmt = DBClass().session.query(table_db).order_by(table_db.id.asc()).all()
    count = DBClass().session.query(table_db).count()
    mass = []
    for i in range(1, count+1):
        if i != stmt[i-1].id:
            mass.append(i)
    if len(mass) != 0:
        count = mass[0]
    else:
        count += 1
    return count


class Saver:
    def __init__(self):
        self.dbHelper = DBClass()

    def addNewAccount(self, new_str):
        count = findFirstFreeID(Accounts)
        data = json.loads(new_str)
        user_new = Accounts(id=count, login=data["login"], password=data["password"], stat_id=int(data["stat_id"]))
        self.dbHelper.session.add(user_new)
        self.dbHelper.session.commit()

    def updAccountPsw(self, new_psw):
        data = json.loads(new_psw)
        query = self.dbHelper.session.query(Accounts).filter(Accounts.id == data["id"]).first()
        query.password = data["password"]
        self.dbHelper.session.commit()

    def dellAccount(self, dell_str):
        data = json.loads(dell_str)
        all_games = self.dbHelper.session.query(Games).filter_by(master_id=data["id"]).all()
        for i in all_games:
            characters = self.dbHelper.session.query(Character).filter_by(game_id=i.id).all()
            for j in characters:
                self.dbHelper.session.query(damage_buff).filter_by(ch_id=j.id).delete(synchronize_session=False)
                self.dbHelper.session.query(health_buff).filter_by(ch_id=j.id).delete(synchronize_session=False)
            self.dbHelper.session.query(Character).filter_by(game_id=i.id).delete(synchronize_session=False)
            self.dbHelper.session.query(online_gamers).filter_by(game_id=i.id).delete(synchronize_session=False)
        self.dbHelper.session.query(Games).filter_by(master_id=data["id"]).delete(synchronize_session=False)
        all_char = self.dbHelper.session.query(Character).filter_by(acc_id=data["id"]).all()
        for i in all_char:
            self.dbHelper.session.query(damage_buff).filter_by(ch_id=i.id).delete(synchronize_session=False)
            self.dbHelper.session.query(health_buff).filter_by(ch_id=i.id).delete(synchronize_session=False)
        self.dbHelper.session.query(Character).filter_by(acc_id=data["id"]).delete(synchronize_session=False)
        self.dbHelper.session.query(online_gamers).filter_by(acc_id=data["id"]).delete(synchronize_session=False)
        self.dbHelper.session.query(Accounts).filter_by(id=data["id"]).delete(synchronize_session=False)
        self.dbHelper.session.commit()

    def addNewGame(self, new_str):
        count = findFirstFreeID(Games)
        data = json.loads(new_str)
        game_new = Games(id=count, game_name=data["game_name"], world_name=data["world_name"],
                         password=data["password"], master_id=int(data["master_id"]))
        self.dbHelper.session.add(game_new)
        self.dbHelper.session.commit()

    def addNewCharacter(self, new_str):
        count = findFirstFreeID(Character)
        pict_id = findFirstFreeID(pict_avatar)
        data = json.loads(new_str)
        find_class = self.dbHelper.session.query(Classes).filter_by(id=data["class_id"]).first()
        if len(data["pict_id"]) != 0:
            pict = self.dbHelper.session.query(pict_avatar).filter_by(url=data["pict_id"]).all()
            if len(pict) == 0:
                new_pict = pict_avatar(id=pict_id, url=data["pict_id"])
                self.dbHelper.session.add(new_pict)
                self.dbHelper.session.commit()
            else:
                pict_id = pict.id
        else:
            find_pict = self.dbHelper.session.query(pict_avatar).filter_by(id=find_class.pict_id).first()
            pict_id = find_pict.id
        new_character = Character(id=count, name=data["name"], hp=data["hp"], notes=data["notes"], power=data["power"],
                                  agility=data["agility"], body_type=data["body_type"], intellect=data["intellect"],
                                  wisdom=data["wisdom"], charisma=data["charisma"], dmg_buff=data["dmg_buff"],
                                  hp_buff=data["hp_buff"], acc_id=data["acc_id"], var_races_id=data["var_races_id"],
                                  class_id=data["class_id"], weap_id=data["weap_id"], arm_id=data["arm_id"], pict_id=
                                  pict_id, game_id=data["game_id"])
        self.dbHelper.session.add(new_character)
        self.dbHelper.session.commit()

    def updGameByDelCh(self, game_id, acc_id):
        a = self.dbHelper.session.query(Character).filter_by(game_id=int(game_id), acc_id=int(acc_id)).all()
        for i in a:
            self.dbHelper.session.query(damage_buff).filter_by(ch_id=i.id).delete(synchronize_session=False)
            self.dbHelper.session.query(health_buff).filter_by(ch_id=i.id).delete(synchronize_session=False)
        self.dbHelper.session.query(Character).filter_by(game_id=int(game_id), acc_id=int(acc_id)) \
            .delete(synchronize_session=False)
        self.dbHelper.session.commit()

    def dellGame(self, dell_str):
        data = json.loads(dell_str)
        all_games = self.dbHelper.session.query(Games).filter_by(id=data["id"]).all()
        for i in all_games:
            characters = self.dbHelper.session.query(Character).filter_by(game_id=i.id).all()
            for j in characters:
                self.dbHelper.session.query(damage_buff).filter_by(ch_id=j.id).delete(synchronize_session=False)
                self.dbHelper.session.query(health_buff).filter_by(ch_id=j.id).delete(synchronize_session=False)
            self.dbHelper.session.query(Character).filter_by(game_id=i.id).delete(synchronize_session=False)
            self.dbHelper.session.query(online_gamers).filter_by(game_id=i.id).delete(synchronize_session=False)
        self.dbHelper.session.query(Games).filter_by(id=data["id"]).delete(synchronize_session=False)
        self.dbHelper.session.commit()

    def dellCharacter(self, dell_str):
        data = json.loads(dell_str)
        self.dbHelper.session.query(damage_buff).filter_by(ch_id=data["id"]).delete(synchronize_session=False)
        self.dbHelper.session.query(health_buff).filter_by(ch_id=data["id"]).delete(synchronize_session=False)
        self.dbHelper.session.query(Character).filter_by(id=data["id"]).delete(synchronize_session=False)
        self.dbHelper.session.commit()

    def updCharacter(self, new_ch):
        data = json.loads(new_ch)
        pict_id = findFirstFreeID(pict_avatar)
        query = self.dbHelper.session.query(Character).filter(Character.id == data["id"]).first()
        query.name = data["name"]
        query.hp = data["hp"]
        query.notes = data["notes"]
        query.power = data["power"]
        query.agility = data["agility"]
        query.body_type = data["body_type"]
        query.intellect = data["intellect"]
        query.wisdom = data["wisdom"]
        query.charisma = data["charisma"]
        query.var_races_id = data["var_races_id"]
        query.class_id = data["class_id"]
        query.weap_id = data["weap_id"]
        query.arm_id = data["arm_id"]
        pict = self.dbHelper.session.query(pict_avatar).filter_by(url=data["pict_id"]).all()
        if len(pict) == 0:
            new_pict = pict_avatar(id=pict_id, url=data["pict_id"])
            self.dbHelper.session.add(new_pict)
            self.dbHelper.session.commit()
        else:
            pict_id = pict[0].id
        query.pict_id = pict_id
        self.dbHelper.session.commit()
