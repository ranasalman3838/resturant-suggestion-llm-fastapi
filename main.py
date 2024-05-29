from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from resturant_idea_suggestion import get_name


app = FastAPI()

orgins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=orgins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/resturant_idea_suggestion/{resturant_type}")
async def get_resturant_idea(resturant_type: str):
    name = get_name(resturant_type)
    resturant_name = name['resturant_name'].strip().replace('\n', '').replace('"', '')
    menu_items = name['menu_items'].replace('\n','').split(',')

    return {"resturant_name":resturant_name, "menu_items":menu_items}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)