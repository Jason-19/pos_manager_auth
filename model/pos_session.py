# -*- coding: utf-8 -*-
from odoo import models


class PosSession(models.Model):
    """Inherited model POS Session for loading field in hr.employee into
       pos session.
       
       Methods:
           _pos_ui_models_to_load(self):
              to load model hr employee to pos session.
              
           _loader_params_hr_employee(self):
              loads field limited_discount to pos session.

       """
    _inherit = "pos.session"

    def _pos_ui_models_to_load(self):
        """Load hr.employee model into pos session"""
        result = super()._pos_ui_models_to_load()
        result += ['hr.employee']
        return result

    def _loader_params_hr_employee(self):
        """load hr.employee parameters"""
        result = super()._loader_params_hr_employee()
        result['search_params']['fields'].extend(['limited_discount'])
        return result
