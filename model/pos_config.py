# -*- coding: utf-8 -*-

from odoo import api, models, fields


class PosConfig(models.Model):
    """Inherit pos configuration and add new fields."""
    _inherit = 'pos.config'

    refund_security = fields.Integer(string='Contraseña de seguridad de reembolso', help="Contraseña de seguridad de reembolso, utilizada para esa tienda especificada")
    image = fields.Binary(string='Image', help="Imagen para el Punto de Venta")
    
    @api.model
    def fetch_global_refund_security(self):
        param = self.env['ir.config_parameter'].sudo().get_param('pos_refund_password.global_refund_security')
        return param
