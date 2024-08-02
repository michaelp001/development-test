
from odoo import api, models

class SiswaReport(models.AbstractModel):
    _name = 'report.siswa_report_template'
    _description = 'Siswa Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['siswa.siswa'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'siswa.siswa',
            'docs': docs,
        }
