from odoo import models, fields

class Siswa(models.Model):
    _name = 'siswa.siswa'
    _description = 'Siswa'

    name = fields.Char(string='Name', required=True)
    date_of_birth = fields.Date(string='Date of Birth')
    kelas_id = fields.Many2one('siswa.kelas', string='Kelas')
    guru_id = fields.Many2one('siswa.guru', string='Guru') ### Sebaiknya Many2many karena 1 siswa bisa diajar banyak guru 
    mata_pelajaran_id = fields.Many2one(related='guru_id.mapel_id', string='Mata Pelajaran', store=True) ### Sebbaiknya model Many2many di onchange input ke mata_pelajaran_ids 
