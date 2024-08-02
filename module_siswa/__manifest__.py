# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Siswa Management',
    'author': 'Michael',
    'version': '1.0',
    'description': """
       Manage students, teachers, classes, and subjects
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/siswa_views.xml',
        'views/guru_views.xml',
        'views/mata_pelajaran_views.xml',
        'views/kelas_views.xml',
        'report/siswa_report_template.xml',
    ],
    'depends': [
                'base'

                ],
    'installable': True,
    "images":['static/logo.png'],
}
