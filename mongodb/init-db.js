db = db.getSiblingDB("image_db");
db.image_tb.drop();
db.image_tb.insertMany([
    {"id": "1x1.png", "path": "data/database/1x1.png", "is_valid": true, "width": 1, "height": 1}
])