from fastapi import APIRouter

router = APIRouter(
    prefix = "/ร้านอาหาร",
    tags = ["Restaurant"],
    responses = {404: {"message" : "Not found"}}
)

# Restaurant 
res_db = [
    {   #1
        "ชื่อร้าน" : "น้าไก่ไข่นุ่ม",
        "ที่ตั้ง" : "ซอยเกกี 1",
        "ประเภทอาหาร" : "อาหารญี่ปุ่น",
        "เมนูแนะนำ" : "ข้าวหมูทอดไข่นุ่ม , ข้าวห่อสาหร่าย",
        "เวลาเปิด-ปิด" : "17:00 – 22:00",
        "เบอร์โทรติดต่อ"  : "087 673 3844"
    },
    {   #2
        "ชื่อร้าน" : "chefcommady",
        "ที่ตั้ง" : "ซอยเกกี 2",
        "ประเภทอาหาร" : "อาหารจานเดียว",
        "เมนูแนะนำ" : "เบอร์เกอร์, แกงกะหรี่, สปาเก็ตตี้",
        "เวลาเปิด-ปิด" : "8:30 – 24:00",
        "เบอร์โทรติดต่อ"  : "090 699 4636"
    },
    {   #3
        "ชื่อร้าน" : "กะเพราบิลเลี่ยน",
        "ที่ตั้ง" : "Billion Park",
        "ประเภทอาหาร" : "อาหารไทย",
        "เมนูแนะนำ" : "กะเพรา",
        "เวลาเปิด-ปิด" : "16:30 – 4:00",
        "เบอร์โทรติดต่อ"  : "082 998 9405"
    },
    {   #4
        "ชื่อร้าน" : "ข้าวมันไก่ป้าน้อย",
        "ที่ตั้ง" : "Billion Park",
        "ประเภทอาหาร" : "อาหารตามสั่ง",
        "เมนูแนะนำ" : "ข้าวหมกไก่",
        "เวลาเปิด-ปิด" : "10:00 – 2:00",
        "เบอร์โทรติดต่อ"  : "088 623 9575, 063 676 7335"
    },
    {   #5
        "ชื่อร้าน" : "ไก่ทอดไฮโซ",
        "ที่ตั้ง" : "499 ซอยฉลองกรุง 1",
        "ประเภทอาหาร" : "Street food, Fast food",
        "เมนูแนะนำ" : "ไก่ทอด",
        "เวลาเปิด-ปิด" : "10:00 – 17:30",
        "เบอร์โทรติดต่อ"  : "088 918 2062"
    },
    {   #6
        "ชื่อร้าน" : "นมมหาลัย",
        "ที่ตั้ง" : "Billion Park",
        "ประเภทอาหาร" : "ขนมหวาน, เครื่องดื่ม",
        "เมนูแนะนำ" : "โกโก้นมสดปั่น, ไอติมทอด",
        "เวลาเปิด-ปิด" : "17:00 – 23:30",
        "เบอร์โทรติดต่อ"  : "098 829 8780"
    },
    {   #7
        "ชื่อร้าน" : "Dimple coffee",
        "ที่ตั้ง" : "ซอยRNP",
        "ประเภทอาหาร" : "Coffee shop",
        "เมนูแนะนำ" : "นมสดคาราเมล, ปังปิ้ง",
        "เวลาเปิด-ปิด" : "10:00 – 19:00",
        "เบอร์โทรติดต่อ"  : "090 699 4636"
    },
    {   #8
        "ชื่อร้าน" : "ไข่หวานบ้านซูชิ",
        "ที่ตั้ง" : "College Town",
        "ประเภทอาหาร" : "อาหารญี่ปุ่น",
        "เมนูแนะนำ" : "ซูชิ, แซลม่อน",
        "เวลาเปิด-ปิด" : "12:00 – 22:00",
        "เบอร์โทรติดต่อ"  : "083 788 4380"
    },
    {   #9
        "ชื่อร้าน" : "Long-Kin (กะเพราไข่ข้นชีสลาวา)",
        "ที่ตั้ง" : "ซอยเกกี 4",
        "ประเภทอาหาร" : "อาหารไทย",
        "เมนูแนะนำ" : "กะเพราไข่ข้นชีสลาวา",
        "เวลาเปิด-ปิด" : "12:00 - 21:00",
        "เบอร์โทรติดต่อ"  : "085 727 7702 "
    },
    {   #10
        "ชื่อร้าน" : "หอมมนต์ (เตี๋ยวเรือต่อชาม)",
        "ที่ตั้ง" : "ซอยเกกี 4",
        "ประเภทอาหาร" : "ก๋วยเตี๋ยว",
        "เมนูแนะนำ" : "ก๋วยเตี๋ยวเรือ",
        "เวลาเปิด-ปิด" : "09:30 - 22:00",
        "เบอร์โทรติดต่อ"  : "090 969 0502"
    }
]

#all restaurant
@router.get("/")
async def get_res():
    return res_db

#restaurant id sort by list
@router.get("/{res_id}/")
async def get_res_id(res_id : int):
    return res_db[res_id]

#Make a lot of effort
#search about restaurant
@router.get("/{about_res}/")
async def get_about_res(about_res : str):
    res_list = res_db.split(":") 
    for i in res_list:
        if about_res in res_list:
            return res_db.index(i)