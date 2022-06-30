from utils.db import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    terr = db.Column(db.String(100))
    reg = db.Column(db.String(100))
    pdvnum = db.Column(db.String(100))
    pdvname = db.Column(db.String(100))
    manager = db.Column(db.String(100))
    managerPhone = db.Column(db.String(100))
    leader = db.Column(db.String(100))
    leaderPhone = db.Column(db.String(100))

    def __init__(self, terr, reg, pdvnum, pdvname, manager, managerPhone, leader, leaderPhone):
        self.terr = terr
        self.reg = reg
        self.pdvnum = pdvnum
        self.pdvname = pdvname
        self.manager = manager
        self.managerPhone = managerPhone
        self.leader = leader
        self.leaderPhone = leaderPhone