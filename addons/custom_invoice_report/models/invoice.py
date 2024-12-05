from odoo import models, fields

class CustomInvoice(models.Model):
    _name = 'custom.invoice'
    _description = 'Custom Invoice'

    name = fields.Char(string='Invoice Reference', required=True)
    date = fields.Date(string='Invoice Date', required=True)
    partner_id = fields.Many2one('res.partner', string='Customer', required=True)
    amount_total = fields.Float(string='Total Amount', required=True)