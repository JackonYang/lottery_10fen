# -*- Encoding: utf-8 -*-
from flask_restful import Resource, fields, marshal_with
from models import Record

live_fields = {
    'issue': fields.String,
    'seq': fields.Integer,
    'time': fields.String,
    'win': fields.List(fields.Integer),
}


class LiveWin(Resource):
    @marshal_with(live_fields)
    def get(self, count):
        return Record.query.all()[-count:]
