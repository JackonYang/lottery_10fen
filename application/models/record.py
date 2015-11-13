# -*- Encoding: utf-8 -*-
from _base import db


class Record(db.Model):
    """快乐十分开奖记录"""
    __tablename__ = 'lottery_record'

    day = db.Column(db.String(10), primary_key=True)  # YYYY-mm-dd
    seq = db.Column(db.Integer,  # last 3bit of kjIssue
                    autoincrement=False, primary_key=True)
    timestamp = db.Column(db.String(64))  # HH:MM:SS kai jiang time
    win_str = db.Column(db.String(64))  # list dumped by json

    __mapper_args__ = {
        'order_by': (day, seq)
    }

    def __init__(self, kjIssue, kjDate, kjZNum, **kwargs):
        self.seq = int(kjIssue[-3:])
        self.day, self.timestamp = kjDate.split()
        self.win_str = kjZNum

    @property
    def win(self):
        """开奖号码"""
        return map(int, self.win_str.split())

    @property
    def issue(self):
        """开奖期号"""
        return '{}{:0>3d}'.format(''.join(self.day.split('-')), self.seq)

    @property
    def time(self):
        """开奖时间"""
        return '{} {}'.format(self.day, self.timestamp)

    def __repr__(self):
        return '{}~No.{:0>2d}'.format(self.day, self.seq)
