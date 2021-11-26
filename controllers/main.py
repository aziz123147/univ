from odoo import http
from odoo.http import request


class University(http.Controller):
    # Sample Controller Created
    @http.route('/university/student/', website=True, auth='public')
    def university_student(self, **kw):
        # return "Thanks for watching"
        print("aziz")
        # http.request.env['university.student'].sudo().create(kw)
        return http.request.render("university_managment.student_page", {

        })\

    @http.route('/university/teacher/', website=True, auth='public')
    def university_student(self, **kw):
        # return "Thanks for watching"
        print("aziz")
        # http.request.env['university.student'].sudo().create(kw)
        return http.request.render("university_managment.teacher_page", {

        })

    # creation dans la base de données
    @http.route('/creer/teacher', type="http", auth='public', website=True)
    def creeruser(self, **kw):
        print("aziz")
        http.request.env['university.teacher'].sudo().create(kw)
        return http.request.render('university_managment.student_page_thanks', {})
    #
    #
    #
    # @http.route('/update_patient', type='json', auth='user')
    # def update_patient(self, **rec):
    #     if request.jsonrequest:
    #         if rec['id']:
    #             print("rec...", rec)
    #             patient = request.env['hospital.patient'].sudo().search([('id', '=', rec['id'])])
    #             if patient:
    #                 patient.sudo().write(rec)
    #             args = {'success': True, 'message': 'Patient Updated'}
    #     return args
    #
    # @http.route('/create_patient', type='json', auth='user')
    # def create_patient(self, **rec):
    #     if request.jsonrequest:
    #         print("rec", rec)
    #         if rec['name']:
    #             vals = {
    #                 'patient_name': rec['name'],
    #                 'email_id': rec['email_id']
    #             }
    #             new_patient = request.env['hospital.patient'].sudo().create(vals)
    #             print("New Patient Is", new_patient)
    #             args = {'success': True, 'message': 'Success', 'id': new_patient.id}
    #     return args
    #
    # @http.route('/get_patients', type='json', auth='user')
    # def get_patients(self):
    #     print("Yes here entered")
    #     patients_rec = request.env['hospital.patient'].search([])
    #     patients = []
    #     for rec in patients_rec:
    #         vals = {
    #             'id': rec.id,
    #             'name': rec.patient_name,
    #             'sequence': rec.name_seq,
    #         }
    #         patients.append(vals)
    #     print("Patient List--->", patients)
    #     data = {'status': 200, 'response': patients, 'message': 'Done All Patients Returned'}
    #     return data
