"""
Test flask_app to return an HL7 message via HTTP

Derek Delpero
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__)+"/flask")
#sys.path.append('..')
#print __file__

from flask import Flask, abort
from flask import request

app = Flask(__name__)


@app.route('/ORU_R01/<id>')
def oru_r01(id):

    sample_hl7 = u'\r'.join([
    'MSH|^~\&|GHH LAB|ELAB-3|GHH OE|BLDG4|200202150930||ORU^R01|CNTRL-3456|P|2.4',
    'PID|||555-44-4444||EVERYWOMAN^EVE^E^^^^L|JONES|196203520|F|||153 FERNWOOD DR.^^STATESVILLE^OH^35292||(206)3345232|(206)752-121||||AC555444444||67-A4335^OH^20030520',
    'OBR|1|845439^GHH OE|1045813^GHH LAB|1554-5^GLUCOSE|||200202150730||||||||555-55-5555^PRIMARY^PATRICIA P^^^^MD^^LEVEL SEVEN HEALTHCARE, INC.|||||||||F||||||444-44-4444^HIPPOCRATES^HOWARD H^^^^MD',
    'OBX|1|SN|1554-5^GLUCOSE^POST 12H CFST:MCNC:PT:SER/PLAS:QN||^182|mg/dl|70_105|H|||F',
    'OBX|2|FN|1553-5^GLUCOSE^POST 12H CFST:MCNC:PT:SER/PLAS:QN||^182|mg/dl|70_105|H|||F\r'
])
    if request.headers['Content-Type'] == '':
        sample_hl7 = "<html><body><pre>" + sample_hl7 + "</pre></body></html>"
    return sample_hl7

if __name__=="__main__":
   app.debug = True
   app.run()
