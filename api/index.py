# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# import json

# app = FastAPI()

# # Enable CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# Load the marks data
# with open("marks.json", "r") as f:
#     marks_data = json.load(f)
# marks_data = [{"gBGt":6},{"M":16},{"x":46},{"Jla9g":54},{"OOqx7Df":46},{"wquNLDwsB":15},{"2rVioTy":77},{"n9YQCUS2":73},{"f4YQF":10},{"zcGvdlDF":69},{"Z":58},{"m":72},{"9hLY6":60},{"yGEaGyY":82},{"q5JF54twU":96},{"hMkH":73},{"k":64},{"GlxFQ":70},{"eEw":90},{"gfS4c":79},{"WHo":19},{"Griw":17},{"W490":17},{"0y9Lul5Ms":11},{"imTUZ":11},{"5Gf2":27},{"u9U3":68},{"AA":48},{"vUXHflCpNE":80},{"hMeoEVbYf":76},{"bL":65},{"BC":48},{"hZXPbA":60},{"k":52},{"iD":80},{"mdmtJxEmIe":78},{"W3UFcOfh":46},{"eQOS8YQ":97},{"uosdAx":41},{"lXX":43},{"G5Tq5":67},{"itr9C07A":47},{"ryyp8hT":24},{"zGjECP":43},{"MBLlacY":89},{"9U":20},{"el38nmEdF":26},{"a":91},{"cmI":7},{"k9Utuq":32},{"YUv":66},{"NQx7ySlinD":51},{"TKrZCJKN":23},{"nCr6P":4},{"p2":96},{"f21N6":62},{"itNq":67},{"Zq8VgRQUs":12},{"pRWelRzNPS":9},{"G7VlnH":2},{"VAK":66},{"LXjhhl8H":28},{"maOfuW":59},{"B":58},{"2RIZ9s2s":21},{"rGo2oKy7":38},{"R4ZaOonUUF":16},{"8t":36},{"hN83xkhrlf":42},{"iYCQ8":29},{"w5Ab0C":94},{"Z0mtEGNAEL":8},{"b0":63},{"qrSA":51},{"CUI":81},{"JMf4mlS4":11},{"ciPyjd":45},{"cUFVlzwf":97},{"v":30},{"Nt9x":86},{"Dn":57},{"H3kTR":24},{"CyzyCcy":90},{"pwprxV":77},{"GOni":49},{"l1":28},{"VpVdSXAR":34},{"8U":7},{"BaEiK43L":6},{"U7s12":36},{"EpTr":69},{"kTLWVbkkv5":60},{"QNHHHF":22},{"Qk7DE":97},{"gumg4IC1sZ":90},{"mSuCc720Jj":70},{"1":62},{"kHJ8WD":18},{"xs1Ji":63},{"1GRy1WK":19}]
# marks_data = {"gBGt":6,"M":16,"x":46,"Jla9g":54,"OOqx7Df":46,"wquNLDwsB":15,"2rVioTy":77,"n9YQCUS2":73,"f4YQF":10,"zcGvdlDF":69,"Z":58,"m":72,"9hLY6":60,"yGEaGyY":82,"q5JF54twU":96,"hMkH":73,"k":64,"GlxFQ":70,"eEw":90,"gfS4c":79,"WHo":19,"Griw":17,"W490":17,"0y9Lul5Ms":11,"imTUZ":11,"5Gf2":27,"u9U3":68,"AA":48,"vUXHflCpNE":80,"hMeoEVbYf":76,"bL":65,"BC":48,"hZXPbA":60,"k":52,"iD":80,"mdmtJxEmIe":78,"W3UFcOfh":46,"eQOS8YQ":97,"uosdAx":41,"lXX":43,"G5Tq5":67,"itr9C07A":47,"ryyp8hT":24,"zGjECP":43,"MBLlacY":89,"9U":20,"el38nmEdF":26,"a":91,"cmI":7,"k9Utuq":32,"YUv":66,"NQx7ySlinD":51,"TKrZCJKN":23,"nCr6P":4,"p2":96,"f21N6":62,"itNq":67,"Zq8VgRQUs":12,"pRWelRzNPS":9,"G7VlnH":2,"VAK":66,"LXjhhl8H":28,"maOfuW":59,"B":58,"2RIZ9s2s":21,"rGo2oKy7":38,"R4ZaOonUUF":16,"8t":36,"hN83xkhrlf":42,"iYCQ8":29,"w5Ab0C":94,"Z0mtEGNAEL":8,"b0":63,"qrSA":51,"CUI":81,"JMf4mlS4":11,"ciPyjd":45,"cUFVlzwf":97,"v":30,"Nt9x":86,"Dn":57,"H3kTR":24,"CyzyCcy":90,"pwprxV":77,"GOni":49,"l1":28,"VpVdSXAR":34,"8U":7,"BaEiK43L":6,"U7s12":36,"EpTr":69,"kTLWVbkkv5":60,"QNHHHF":22,"Qk7DE":97,"gumg4IC1sZ":90,"mSuCc720Jj":70,"1":62,"kHJ8WD":18,"xs1Ji":63,"1GRy1WK":19}

# @app.get("/api")
# async def get_marks(name: str):
#     names = name.split(',')
#     marks = []
#     # marks = [marks_data.get(name, 0) for name in names]
#     for n in names:
#         student = next(student for student in marks_data if student["name"] == n), None
#         if student:
#             marks.append(student["marks"])
#         else:
#             marks.append(None)  # Or handle as you prefer
#     return {"marks": marks }
import json
import os
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler

# Sample data for 100 imaginary students
students_marks = {"gBGt":6,"M":16,"x":46,"Jla9g":54,"OOqx7Df":46,"wquNLDwsB":15,"2rVioTy":77,"n9YQCUS2":73,"f4YQF":10,"zcGvdlDF":69,"Z":58,"m":72,"9hLY6":60,"yGEaGyY":82,"q5JF54twU":96,"hMkH":73,"k":64,"GlxFQ":70,"eEw":90,"gfS4c":79,"WHo":19,"Griw":17,"W490":17,"0y9Lul5Ms":11,"imTUZ":11,"5Gf2":27,"u9U3":68,"AA":48,"vUXHflCpNE":80,"hMeoEVbYf":76,"bL":65,"BC":48,"hZXPbA":60,"k":52,"iD":80,"mdmtJxEmIe":78,"W3UFcOfh":46,"eQOS8YQ":97,"uosdAx":41,"lXX":43,"G5Tq5":67,"itr9C07A":47,"ryyp8hT":24,"zGjECP":43,"MBLlacY":89,"9U":20,"el38nmEdF":26,"a":91,"cmI":7,"k9Utuq":32,"YUv":66,"NQx7ySlinD":51,"TKrZCJKN":23,"nCr6P":4,"p2":96,"f21N6":62,"itNq":67,"Zq8VgRQUs":12,"pRWelRzNPS":9,"G7VlnH":2,"VAK":66,"LXjhhl8H":28,"maOfuW":59,"B":58,"2RIZ9s2s":21,"rGo2oKy7":38,"R4ZaOonUUF":16,"8t":36,"hN83xkhrlf":42,"iYCQ8":29,"w5Ab0C":94,"Z0mtEGNAEL":8,"b0":63,"qrSA":51,"CUI":81,"JMf4mlS4":11,"ciPyjd":45,"cUFVlzwf":97,"v":30,"Nt9x":86,"Dn":57,"H3kTR":24,"CyzyCcy":90,"pwprxV":77,"GOni":49,"l1":28,"VpVdSXAR":34,"8U":7,"BaEiK43L":6,"U7s12":36,"EpTr":69,"kTLWVbkkv5":60,"QNHHHF":22,"Qk7DE":97,"gumg4IC1sZ":90,"mSuCc720Jj":70,"1":62,"kHJ8WD":18,"xs1Ji":63,"1GRy1WK":19}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Enable CORS
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header['Access-Control-Allow-Methods'] = 'GET, POST, PUT, PATCH, DELETE, OPTIONS'
        self.send_header['Access-Control-Allow-Headers'] = 'Content-Type'
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Parse query parameters
        query_components = parse_qs(urlparse(self.path).query)

        # Get the names from the query parameters (handling multiple name parameters)
        names = query_components.get('name', [])

        # Retrieve marks for the requested names
        marks = [students_marks.get(name, 0) for name in names]

        # Send the JSON response
        self.wfile.write(json.dumps({"marks": marks}).encode('utf-8'))
        return
