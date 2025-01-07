# -*- coding: utf-8 -*-
from odoo import fields, models

class HrEmployee(models.Model):
    """Add field into hr employee"""
    _inherit = 'hr.employee'

    limited_discount = fields.Integer(string="Discuento Limite", help="Proporcionar límite de descuento para cada " "empleado")
