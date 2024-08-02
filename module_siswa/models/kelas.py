from odoo import models, fields

class Kelas(models.Model):
    _name = 'siswa.kelas'
    _description = 'Kelas'

    name = fields.Char(string='Name', required=True)