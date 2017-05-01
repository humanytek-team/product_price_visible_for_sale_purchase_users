# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'

    lst_price = fields.Float(
        groups='purchase.group_purchase_user,sales_team.group_sale_salesman')
    standard_price = fields.Float(
        groups='purchase.group_purchase_user,sales_team.group_sale_salesman')
