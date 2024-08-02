from odoo import models, fields

class Guru(models.Model):
    _name = 'siswa.guru'
    _description = 'Guru'

    name = fields.Char(string='Name', required=True)
    mapel_id = fields.Many2one('siswa.mata_pelajaran', string='Mata Pelajaran')