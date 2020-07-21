import json

import qiniu
from flask import Blueprint, request, make_response, jsonify

from utils import restful, zlcache
from utils.alidayu import send_sms
from .forms import SmsCaptchaForm
from io import BytesIO
from utils.captcha import Captcha
from tasks import send_sms_captcha
bp = Blueprint("common", __name__, url_prefix="/c")


# @bp.route('/sms_captcha/', methods=['POST'])
# def sms_captcha():
#     form = SmsCaptchaForm(request.form)
#     if form.validate():
#         telephone = form.telephone.data
#         captcha = Captcha.gene_text(number=4)
#         template = {
#             'code': captcha
#         }
#         res = send_sms_captcha(template, telephone)
#         res_dict = json.loads(res)
#         if res_dict.get('Message') == 'OK' and res_dict.get('Code') == 'OK':
#             print("短信验证码是%s" % captcha)
#             zlcache.set(telephone, captcha)
#             return restful.success()
#         else:
#             return restful.server_error()
#     else:
#         return restful.params_error(form.get_error())


# @bp.route('/sms_captcha/', methods=['POST'])
# def sms_captcha():
#     telephone = request.form.get("telephone")
#     captcha = Captcha.gene_text(number=4)
#     template = {
#         'code': captcha
#     }
#     print(captcha)
#     res = send_sms_captcha(template, telephone)
#     res_dict = json.loads(res)
#     if res_dict.get('Message') == 'OK' and res_dict.get('Code') == 'OK':
#
#         print("短信验证码是%s" % captcha)
#         zlcache.set(telephone, captcha)
#         return restful.success()
#     else:
#         return restful.params_error()

@bp.route('/sms_captcha/', methods=['POST'])
def sms_captcha():
    form = SmsCaptchaForm(request.form)
    if form.validate():
        telephone = form.telephone.data
        captcha = Captcha.gene_text(number=4)
        template = {
            'code': captcha
        }
        print(captcha)
        zlcache.set(telephone, captcha)
        print(zlcache.get(telephone))
        res = send_sms(template, telephone)
        res_dict = json.loads(res)
        if res_dict.get('Message') == 'OK' and res_dict.get('Code') == 'OK':

            print("短信验证码是%s" % captcha)
            zlcache.set(telephone, captcha)
            return restful.success()
        else:
            return restful.params_error()
    else:
        return restful.params_error(form.get_error())

@bp.route('/captcha/')
def graph_captcha():
    text, image = Captcha.gene_graph_captcha()
    zlcache.set(text.lower(), text.lower())
    out = BytesIO()
    image.save(out, 'png')
    out.seek(0)
    resp = make_response(out.read())
    resp.content_type = 'image/png'
    return resp


@bp.route('/uptoken/')
def uptoken():
    access_key = 'M4zCEW4f9XPanbMN-Lb9O0S8j893f0e1ezAohFVL'
    secret_key = '7BKV7HeEKM3NDJk8_l_C89JI3SMmeUlAIatzl9d4'
    q = qiniu.Auth(access_key, secret_key)

    bucket = 'hyvideo'
    token = q.upload_token(bucket)
    return jsonify({'uptoken': token})
