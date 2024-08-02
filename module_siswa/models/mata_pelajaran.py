from odoo import models, fields

class MataPelajaran(models.Model):
    _name = 'siswa.mata_pelajaran'
    _description = 'Mata Pelajaran'

    name = fields.Char(string='Name', required=True)