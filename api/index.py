from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the marks data
# with open("marks.json", "r") as f:
#     marks_data = json.load(f)
marks_data = [{"name":"gBGt","marks":6},{"name":"M","marks":16},{"name":"x","marks":46},{"name":"Jla9g","marks":54},{"name":"OOqx7Df","marks":46},{"name":"wquNLDwsB","marks":15},{"name":"2rVioTy","marks":77},{"name":"n9YQCUS2","marks":73},{"name":"f4YQF","marks":10},{"name":"zcGvdlDF","marks":69},{"name":"Z","marks":58},{"name":"m","marks":72},{"name":"9hLY6","marks":60},{"name":"yGEaGyY","marks":82},{"name":"q5JF54twU","marks":96},{"name":"hMkH","marks":73},{"name":"k","marks":64},{"name":"GlxFQ","marks":70},{"name":"eEw","marks":90},{"name":"gfS4c","marks":79},{"name":"WHo","marks":19},{"name":"Griw","marks":17},{"name":"W490","marks":17},{"name":"0y9Lul5Ms","marks":11},{"name":"imTUZ","marks":11},{"name":"5Gf2","marks":27},{"name":"u9U3","marks":68},{"name":"AA","marks":48},{"name":"vUXHflCpNE","marks":80},{"name":"hMeoEVbYf","marks":76},{"name":"bL","marks":65},{"name":"BC","marks":48},{"name":"hZXPbA","marks":60},{"name":"k","marks":52},{"name":"iD","marks":80},{"name":"mdmtJxEmIe","marks":78},{"name":"W3UFcOfh","marks":46},{"name":"eQOS8YQ","marks":97},{"name":"uosdAx","marks":41},{"name":"lXX","marks":43},{"name":"G5Tq5","marks":67},{"name":"itr9C07A","marks":47},{"name":"ryyp8hT","marks":24},{"name":"zGjECP","marks":43},{"name":"MBLlacY","marks":89},{"name":"9U","marks":20},{"name":"el38nmEdF","marks":26},{"name":"a","marks":91},{"name":"cmI","marks":7},{"name":"k9Utuq","marks":32},{"name":"YUv","marks":66},{"name":"NQx7ySlinD","marks":51},{"name":"TKrZCJKN","marks":23},{"name":"nCr6P","marks":4},{"name":"p2","marks":96},{"name":"f21N6","marks":62},{"name":"itNq","marks":67},{"name":"Zq8VgRQUs","marks":12},{"name":"pRWelRzNPS","marks":9},{"name":"G7VlnH","marks":2},{"name":"VAK","marks":66},{"name":"LXjhhl8H","marks":28},{"name":"maOfuW","marks":59},{"name":"B","marks":58},{"name":"2RIZ9s2s","marks":21},{"name":"rGo2oKy7","marks":38},{"name":"R4ZaOonUUF","marks":16},{"name":"8t","marks":36},{"name":"hN83xkhrlf","marks":42},{"name":"iYCQ8","marks":29},{"name":"w5Ab0C","marks":94},{"name":"Z0mtEGNAEL","marks":8},{"name":"b0","marks":63},{"name":"qrSA","marks":51},{"name":"CUI","marks":81},{"name":"JMf4mlS4","marks":11},{"name":"ciPyjd","marks":45},{"name":"cUFVlzwf","marks":97},{"name":"v","marks":30},{"name":"Nt9x","marks":86},{"name":"Dn","marks":57},{"name":"H3kTR","marks":24},{"name":"CyzyCcy","marks":90},{"name":"pwprxV","marks":77},{"name":"GOni","marks":49},{"name":"l1","marks":28},{"name":"VpVdSXAR","marks":34},{"name":"8U","marks":7},{"name":"BaEiK43L","marks":6},{"name":"U7s12","marks":36},{"name":"EpTr","marks":69},{"name":"kTLWVbkkv5","marks":60},{"name":"QNHHHF","marks":22},{"name":"Qk7DE","marks":97},{"name":"gumg4IC1sZ","marks":90},{"name":"mSuCc720Jj","marks":70},{"name":"1","marks":62},{"name":"kHJ8WD","marks":18},{"name":"xs1Ji","marks":63},{"name":"1GRy1WK","marks":19}]

@app.get("/api")
async def get_marks(name: str):
    names = name.split(',')
    marks = []
    marks = [marks_data.get(name, 0) for name in names]
    # for n in names:
    #     # student = next(student for student in marks_data if student["name"] == n), None
    #     # if student:
    #     #     marks.append(student["marks"])
    #     else:
    #         marks.append(None)  # Or handle as you prefer
    return {"marks": marks}