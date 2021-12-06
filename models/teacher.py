from odoo import models, fields, api, _
import re


class UniversityTeacher(models.Model):
    _name = 'university.teacher'
    _description = 'Teacher management'
    _rec_name = 'f_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    f_name = fields.Char(string="Prenom", required=True)
    l_name = fields.Char(string='Nom', tracking=True, required=True)
    date_of_birth = fields.Date(string='Date de Naissance', required=True)
    e_mail = fields.Char('E-mail', tracking=True, required=True)
    identity_card = fields.Char(string='Carte Identité', required=True, tracking=True)
    phone = fields.Char(string='Téléphone', required=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    rue = fields.Char('Rue')
    ville = fields.Char('Ville')
    code_postale = fields.Char('Code postale')
    date_inscription = fields.Datetime(string='Date Inscription', default=fields.Datetime.now, readonly=True)
    date_start = fields.Datetime('Date of start', default=fields.Datetime.now, readonly=True)



    teacher_id = fields.Many2one('res.users', ondelete='set null', string="User", index=True)
    suggestions = fields.Text('Suggestions')
    subject_id = fields.Many2one(comodel_name='university.subject', string='Matiere')
    class_ids = fields.Many2many('university.class', 'prof_class_rel', 'f_name', 'class_name', string='Classe')


    @api.model
    def create(self, values):
        if self.env['res.users'].sudo().search([('login', '=', values.get('e_mail'))]):
            user_id = self.env['res.users'].search([('login', '=', values.get('e_mail'))])
            values.update(teacher_id=user_id.id)
        else:
            vals_user = {
                'name': values.get('f_name'),
                'login': values.get('e_mail'),
                # 'password': values.get('mot_passe'),
                # other required field
            }
            user_id = self.env['res.users'].sudo().create(vals_user)
            values.update(teacher_id=user_id.id)
            res = super(UniversityTeacher, self).create(values)

            return res


