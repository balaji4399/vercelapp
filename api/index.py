from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample data for 100 imaginary students
students_marks = {"gBGt":6,"M":16,"x":46,"Jla9g":54,"OOqx7Df":46,"wquNLDwsB":15,"2rVioTy":77,"n9YQCUS2":73,"f4YQF":10,"zcGvdlDF":69,"Z":58,"m":72,"9hLY6":60,"yGEaGyY":82,"q5JF54twU":96,"hMkH":73,"k":6, ...}

@app.get("/api")
async def get_marks(request: Request):
    # Parse query parameters
    query_components = request.query_params

    # Get the names from the query parameters (handling multiple name parameters)
    names = query_components.getlist('name')

    # Retrieve marks for the requested names
    marks = [students_marks.get(name, 0) for name in names]

    # Send the JSON response
    return JSONResponse(content={"marks": marks}
