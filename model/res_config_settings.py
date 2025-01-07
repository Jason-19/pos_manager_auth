# -*- coding: utf-8 -*-

from odoo import models, fields

class ResConfigSettings(models.TransientModel):
    """Adding a new field to res_config_settings model."""
    _inherit = 'res.config.settings'

    global_refund_security = fields.Integer(
        string='Contraseña de reembolso global',
        config_parameter='pos_refund_password.global_refund_security',
        help="Contraseña de seguridad de reembolso global, común para todas las tiendas")
