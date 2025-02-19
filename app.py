import datetime
from flask import Flask, render_template, flash, redirect, url_for, session, request
from passlib.handlers.sha2_crypt import sha256_crypt
from log import Log
from dbs.foldersdb import FoldersDb
from dbs.userdb import UserDb
from schema_forms.patient_history import PatientHistoryForm
from schema_forms.medical_history_form import MedicalHistoryForm, PatientCancerHistoryForm, FamilyCancerHistoryForm
from schema_forms.clinical_exam import ClinicalExamForm
from schema_forms.type_of_surgery import SurgeryReportForm
from schema_forms.nodes_surgery import NodesFrozenSectionForm
from schema_forms.post_surgery_complication_surgery import PostSurgeryComplicationForm
from schema_forms.pathological_reports import BiopsyForm
from schema_forms.mammo_form import MammographyForm, MammoMassForm, MammoCalcificationForm
from schema_forms.nact import NeoAdjuvantChemoDrugForm, NeoAdjuvantChemoToxicityForm, NeoAdjuvantChemoTherapyForm
from schema_forms.usg import SonoMammographyForm, SonoMammoMassForm
from schema_forms.folder_form import FoldersForm
from wtforms import Form, StringField, PasswordField, validators
from schema_forms.models import FolderSection
from flask_bootstrap import Bootstrap
from isloggedin import is_logged_in
from crudprint import construct_crudprint
from crudprint_folder import construct_crudprint_folder
from dbs.sectiondb import SectionDb
import os

# Initialize logging
log = Log()
# Initialize DB
# url = os.getenv('BCDB_URL')
url = None
if url is None:
    url = 'mongodb+srv://admin:zT2SfgLN6Efr6NmG@pccm.rddjc.mongodb.net/pccm_db?retryWrites=true&w=majority'
url = url.replace('"', '')
print('Using db at: ' + url)

port = os.getenv('PORT')
port = None
if port is None:
    port = 5666

db = FoldersDb(log, FoldersForm)
db.connect(url)

# Initialize User DB
users_db = UserDb(log)

users_db.connect(url)

# Initialize section DBs
app = Flask(__name__)
bootstrap = Bootstrap(app)

folder_db = FoldersDb(log, FoldersForm)
folder_db.connect(url)
folder_crudprint = construct_crudprint_folder(folder_db)
app.register_blueprint(folder_crudprint, url_prefix="/folder")

nact_db = SectionDb(log, NeoAdjuvantChemoTherapyForm, 'nact')
nact_db.connect(url)
nact_crudprint = construct_crudprint('nact', nact_db, folder_db)
app.register_blueprint(nact_crudprint, url_prefix="/nact")

nact_drug_db = SectionDb(log, NeoAdjuvantChemoDrugForm, 'nact_drug')
nact_drug_db.connect(url)
nact_drug_crudprint = construct_crudprint('nact_drug', nact_drug_db, folder_db)
app.register_blueprint(nact_drug_crudprint, url_prefix="/nact_drug")

nact_toxicity_db = SectionDb(log, NeoAdjuvantChemoToxicityForm, 'mammography')
nact_toxicity_db.connect(url)
nact_toxicity_crudprint = construct_crudprint(
    'nact_toxicity', nact_toxicity_db, folder_db)
app.register_blueprint(nact_toxicity_crudprint, url_prefix="/nact_toxicity")

mammo_db = SectionDb(log, MammographyForm, 'mammography')
mammo_db.connect(url)
mammo_crudprint = construct_crudprint('mammography', mammo_db, folder_db)
app.register_blueprint(mammo_crudprint, url_prefix="/mammo")

mammo_mass_db = SectionDb(log, MammoMassForm, 'mammo_mass')
mammo_mass_db.connect(url)
mammo_mass_crudprint = construct_crudprint(
    'mammography_mass', mammo_mass_db, folder_db)
app.register_blueprint(mammo_mass_crudprint, url_prefix="/mammo_mass")

mammo_calcification_db = SectionDb(
    log, MammoCalcificationForm, 'mammo_calcification')
mammo_calcification_db.connect(url)
mammo_calcification_crudprint = construct_crudprint(
    'mammo_calcification', mammo_calcification_db, folder_db)
app.register_blueprint(mammo_calcification_crudprint,
                       url_prefix="/mammo_calcification")

usg_db = SectionDb(log, SonoMammographyForm, 'sono_mammography')
usg_db.connect(url)
usg_crudprint = construct_crudprint('sonomammography', usg_db, folder_db)
app.register_blueprint(usg_crudprint, url_prefix="/usg")

usg_mass_db = SectionDb(log, SonoMammoMassForm, 'sonomammography_mass')
usg_mass_db.connect(url)
usg_mass_crudprint = construct_crudprint(
    'sonomammography_mass', usg_mass_db, folder_db)
app.register_blueprint(usg_mass_crudprint, url_prefix="/usg_mass")

pathological_reports_db = SectionDb(log, BiopsyForm, 'pathological_reports')
pathological_reports_db.connect(url)
pathological_reports_crudprint = construct_crudprint(
    'pathological_reports', pathological_reports_db, folder_db)
app.register_blueprint(pathological_reports_crudprint,
                       url_prefix="/pathological_reports")

patient_history_db = SectionDb(log, PatientHistoryForm, 'patient_history')
patient_history_db.connect(url)
patient_history_crudprint = construct_crudprint(
    'patient_history', patient_history_db, folder_db)
app.register_blueprint(patient_history_crudprint,
                       url_prefix="/patient_history")

patient_cancer_history_db = SectionDb(
    log, PatientCancerHistoryForm, 'patient_cancer_history')
patient_cancer_history_db.connect(url)
patient_cancer_history_crudprint = construct_crudprint(
    'patient_cancer_history', patient_cancer_history_db, folder_db)
app.register_blueprint(patient_cancer_history_crudprint,
                       url_prefix="/patient_cancer_history")

medical_history_db = SectionDb(log, MedicalHistoryForm, 'medical_history')
medical_history_db.connect(url)
medical_history_crudprint = construct_crudprint(
    'medical_history', medical_history_db, folder_db)
app.register_blueprint(medical_history_crudprint,
                       url_prefix="/medical_history")

family_cancer_history_db = SectionDb(
    log, FamilyCancerHistoryForm, 'family_cancer_history')
family_cancer_history_db.connect(url)
family_cancer_history_crudprint = construct_crudprint(
    'family_history', family_cancer_history_db, folder_db)
app.register_blueprint(family_cancer_history_crudprint,
                       url_prefix="/family_cancer_history")

clinical_exam_db = SectionDb(log, ClinicalExamForm, 'clinical_exam')
clinical_exam_db.connect(url)
clinical_exam_crudprint = construct_crudprint(
    'clinical_exam', clinical_exam_db, folder_db)
app.register_blueprint(clinical_exam_crudprint, url_prefix="/clinical_exam")

type_of_surgery_db = SectionDb(log, SurgeryReportForm, 'type_of_surgery')
type_of_surgery_db.connect(url)
type_of_surgery_crudprint = construct_crudprint(
    'type_of_surgery', type_of_surgery_db, folder_db)
app.register_blueprint(type_of_surgery_crudprint,
                       url_prefix="/type_of_surgery")

nodes_surgery_db = SectionDb(log, NodesFrozenSectionForm, 'nodes_surgery')
nodes_surgery_db.connect(url)
nodes_surgery_crudprint = construct_crudprint(
    'nodes_surgery', nodes_surgery_db, folder_db)
app.register_blueprint(nodes_surgery_crudprint, url_prefix="/nodes_surgery")

post_surgery_complication_surgery_db = SectionDb(
    log, PostSurgeryComplicationForm, 'post_surgery_complication_surgery')
post_surgery_complication_surgery_db.connect(url)
post_surgery_complication_surgery_crudprint = construct_crudprint(
    'post_surgery_complication_surgery', post_surgery_complication_surgery_db, folder_db)
app.register_blueprint(post_surgery_complication_surgery_crudprint,
                       url_prefix="/post_surgery_complication_surgery")
#
#########################################################
# Login, registration and index


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


class RegisterForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.hash(str(form.password.data))
        print(name, email, username, password)
        # print(name + 'entered')
        if users_db.add_user(name, email, username, password):
            flash('You are now registered and can log in', 'success')
        else:
            flash('Error adding user to database', 'error')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password_candidate = request.form['password']
        encrypted, name = users_db.get_password(username)
        if encrypted is not None:
            if sha256_crypt.verify(password_candidate, encrypted):
                session['logged_in'] = True
                session['username'] = username
                session['name'] = name
                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)
        return name
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))


#########################################################
# Main dashboard
@app.route('/dashboard')
@is_logged_in
def dashboard():
    folder_list = db.get_folders()
    if folder_list:
        return render_template('dashboard.html', folders=folder_list)
    else:
        msg = 'No data found'
        return render_template('dashboard.html', msg=msg)

#########################################################
    # Folder CRUD


######################
# Folder
@app.route('/search', methods=['POST'])
@is_logged_in
def search_folder():
    folder_number = request.form['query']
    folder = folder_db.get_folder_by_number(folder_number, is_delete=False)
    if folder is None:
        flash(folder_number + ' not found', 'danger')
        return redirect(url_for('dashboard'))
    return redirect(url_for('view_folder', folder_pk=folder.fld_folder_pk.data))


@app.route('/folder/<folder_pk>', methods=['GET'])
@is_logged_in
def view_folder(folder_pk):
    folder_number = folder_db.folder_check(folder_pk)

    if folder_number is None:
        flash(folder_pk + ' not found', 'danger')
        return redirect(url_for('dashboard'))

# select active tab
    active_tab_id = request.args.get('active_tab')
    if active_tab_id is None:
        if 'active_tab' in session:
            active_tab_id = session['active_tab']
    if active_tab_id is None:
        active_tab_id = "PatientHistory"
    session['active_tab'] = active_tab_id

    # set up sections
    folder_sections = []
    if active_tab_id == "Radiology":
        folder_sections = [
            create_folder_section(folder_pk, "mammo",
                                  "mammo", mammo_db.get_folder_items),
            create_folder_section(folder_pk,  "mammo_mass", "mammo_mass",
                                  mammo_mass_db.get_folder_items, is_list=True),
            create_folder_section(folder_pk,  "mammo_calcification", "mammo_calcification",
                                  mammo_calcification_db.get_folder_items, is_list=True),
            create_folder_section(folder_pk,  "usg", "usg",
                                  usg_db.get_folder_items),
            create_folder_section(folder_pk,  "usg_mass", "usg_mass", usg_mass_db.get_folder_items, is_list=True), ]
    elif active_tab_id == "PathologicalReports":
        folder_sections = [create_folder_section(folder_pk=folder_pk, id="pathological_reports", section_name="pathological_reports",
                                                 db_get=pathological_reports_db.get_folder_items, is_list=False), ]
    elif active_tab_id == "PatientHistory":
        folder_sections = [
            create_folder_section(folder_pk, "patient_history",
                                  "patient_history", patient_history_db.get_folder_items),
            create_folder_section(folder_pk, "patient_cancer_history", "patient_cancer_history",
                                  patient_cancer_history_db.get_folder_items, is_list=True),
            create_folder_section(folder_pk, "medical_history", "medical_history",
                                  medical_history_db.get_folder_items, is_list=True),
            create_folder_section(folder_pk, "family_cancer_history", "family_cancer_history",
                                  family_cancer_history_db.get_folder_items, is_list=True),

        ]
    elif active_tab_id == "ClinicalExam":
        folder_sections = [
            create_folder_section(
                folder_pk, "clinical_exam", "clinical_exam", clinical_exam_db.get_folder_items),
        ]
    elif active_tab_id == "NACT":
        folder_sections = [
            create_folder_section(folder_pk, "nact", "nact",
                                  nact_db.get_folder_items),
            create_folder_section(
                folder_pk, "nact_drug", "nact_drug", nact_drug_db.get_folder_items, is_list=True),
            create_folder_section(folder_pk, "nact_toxicity", "nact_toxicity", nact_toxicity_db.get_folder_items,
                                  is_list=True), ]
    elif active_tab_id == "Surgery":
        folder_sections = [
            create_folder_section(folder_pk, "type_of_surgery", "type_of_surgery",
                                  type_of_surgery_db.get_folder_items, is_list=True),
            create_folder_section(folder_pk, "nodes_surgery", "nodes_surgery",
                                  nodes_surgery_db.get_folder_items, is_list=True),
            create_folder_section(folder_pk, "post_surgery_complication_surgery", "post_surgery_complication_surgery",
                                  post_surgery_complication_surgery_db.get_folder_items, is_list=True)
        ]

    folder_tabs = [
        ("PatientHistory", "Patient History"),
        ("ClinicalExam", "Clinical Exam"),
        ("Radiology", "Radiology"),
        ("PathologicalReports", "Pathological Reports"),
        ("NACT", "NeoAdjuvant Chemotherapy"),
        ("Surgery", "Surgery"),
        ("AdjuvantChemo", "Adjuvant Chemotherapy"),
        ("Radiotherapy", "Radiotherapy"),
        ("LongTermTherapy", "LongTerm Therapy"),
        ("FollowUp", "Follow-up"),
    ]

    key = folder_pk
    return render_template('folder_tabs.html', folder_number=folder_number, key=folder_pk, folder_sections=folder_sections,
                           folder_tabs=folder_tabs, active_tab_id=active_tab_id)


def create_folder_section(folder_pk, id, section_name, db_get, is_list=False):
    forms = db_get(folder_pk)
    action = "add"
    status = ["To be filled"]
    last_modified_on = [datetime.datetime.today().strftime('%Y-%m-%d')]
    update_by = [""]
    pks = None
    if forms is not None and len(forms) > 0:
        action = "edit"
        status = [x.fld_form_status.data for x in forms]
        last_modified_on = [x.last_update.data for x in forms]
        pks = [(x.fld_pk.data, x.get_summary()) for x in forms]
        update_by = [x.update_by.data for x in forms]

    section = FolderSection(id, section_name, action, status, forms, folder_pk, last_modified_on=last_modified_on,
                            last_modified_by=update_by, pks=pks, is_list=is_list)
    return section


# MAIN
if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run(host='0.0.0.0', port=port, debug=True)
