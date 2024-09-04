#1.
FoodMenu=["","ต้มยำกุ้ง", "แกงส้ม", "ต้มข่าไก่", "ขนมจีนน้ำยา", "แกงเขียวหวานไก่", "มัสมั่นไก่", "แพนงหมู","แกงจืดหมูสับ" ]

#2.
NameFood=str(input("อาหารที่ต้องการค้นหา:"))
if NameFood in (FoodMenu):
    print("Lucky!!! You found your choice.")
else:
    print("Sorry, you miss your choice.")

#3.
AddFood=str(input("รายการอาหารที่ต้องการเพิ่ม:"))
FoodMenu.append(AddFood)

print("จำนวนอาหารทั้งหมด:",len (FoodMenu))
print("รายการอาหารทั้งหมด:%s" %(FoodMenu))

#4.

FoodMenu[1]='1.ต้มยำกุ้ง';FoodMenu[2]='2.แกงส้ม';FoodMenu[3]='3.ต้มข่าไก่';FoodMenu[4]='4.ขนมจีนน้ำยา';
FoodMenu[5]='5.แกงเขียวหวานไก่';FoodMenu[6]='6.มัสมั่นไก่';FoodMenu[7]='7.แพนงหมู';FoodMenu[8]='8.แกงจืดหมูสับ'
print("รายการอาหารทั้งหมด:%s"%(FoodMenu[1:9]))

DelFood=int(input("อาหารที่ต้องการลบ:"))
FoodMenu.pop(DelFood)
print("รายการอาหารทั้งหมดที่ลบแล้ว:%s"%(FoodMenu[1:8]))

#5.
FoodMenu[1]='1.ต้มยำกุ้ง';FoodMenu[2]='2.แกงส้ม';FoodMenu[3]='3.ต้มข่าไก่';FoodMenu[4]='4.ขนมจีนน้ำยา';
FoodMenu[5]='5.แกงเขียวหวานไก่';FoodMenu[6]='6.มัสมั่นไก่';FoodMenu[7]='7.แพนงหมู';FoodMenu[8]='8.แกงจืดหมูสับ'
print("รายชื่ออาหารทั้งหมด:%s"%(FoodMenu[1:9]))

modifyFood=int(input("ลำดับอาหารที่ต้องการแก้:"))
modifyNameFood=str(input("ชื่ออาหารที่ต้องการแก้:"))
if modifyFood==1:
    FoodMenu[modifyFood]='1.%s'%modifyNameFood
elif modifyFood==2:
    FoodMenu[modifyFood]='2.%s'%modifyNameFood
elif modifyFood==3:
    FoodMenu[modifyFood]='3.%s'%modifyNameFood
elif modifyFood==4:
    FoodMenu[modifyFood]='4.%s'%modifyNameFood
elif modifyFood==5:
    FoodMenu[modifyFood]='5.%s'%modifyNameFood
elif modifyFood==6:
    FoodMenu[modifyFood]='6.%s'%modifyNameFood
elif modifyFood==7:
    FoodMenu[modifyFood]='7.%s'%modifyNameFood
elif modifyFood==8:
    FoodMenu[modifyFood]='8.%s'%modifyNameFood

print("ชื่ออาหารที่แก้ไขแล้ว:%s"%FoodMenu[1:9])



#1. Dictionary
FoodPrice={
    "ต้มยำกุ้ง":90 ,"แกงส้ม":60,"ต้มข่าไก่":60,"มัสมั่นไก่":50,"ขนมจีนน้ำยา":40,"แกงเขียวหวานไก่":40,"แพนงหมู":40,"แกงจืดหมูสับ":30
} 

#2.
NameFood=str(input("อาหารที่ต้องการค้นหา:"))
if NameFood in (FoodPrice):
    FoodPrice1=FoodPrice[NameFood]
    print(f"ชื่ออาหาร:{NameFood} ราคา:{FoodPrice1} บาท.")
else:
    print("เสียใจ ไม่มมีอาหารที่คุณต้องการ")  

#3.
AddFood=str(input("รายการอาหารที่ต้องการเพิ่ม:"))
PriceFood=int(input("ราคาอาหารที่ต้องการเพิ่ม:"))
FoodPrice.update({AddFood:PriceFood})

print("จำนวนอาหารทั้งหมด:",len (FoodPrice))
print("รายการอาหาร/ราคาทั้งหมด:%s" %(FoodPrice))  

FoodPrice.clear()
FoodPrice.update({"1.ต้มยำกุ้ง":90,"2.แกงส้ม":60,"3.ต้มข่าไก่":60,"4.มัสมั่นไก่":50,"5.ขนมจีนน้ำยา":40,"6.แกงเขียวหวานไก่":40,"7.แพนงหมู":40,"8.แกงจืดหมูสับ":30})
print(f"รายการอาหารทั้งหมด:{FoodPrice}")

DelFood=int(input("อาหารที่ต้องการลบ:"))
if DelFood==1:
    FoodPrice.pop("1.ต้มยำกุ้ง")
elif DelFood==2:
    FoodPrice.pop("2.แกงส้ม")
elif DelFood==3:
    FoodPrice.pop("3.ต้มข่าไก่")
elif DelFood==4:
    FoodPrice.pop("4.มัสมั่นไก่")
elif DelFood==5:
    FoodPrice.pop("5.ขนมจีนน้ำยา")
elif DelFood==6:
    FoodPrice.pop("6.แกงเขียวหวานไก่")
elif DelFood==7:
    FoodPrice.pop("7.แพนงหมู")
elif DelFood==8:
    FoodPrice.pop("8.แกงจืดหมูสับ")

print("รายการอาหารทั้งหมดที่ลบแล้ว:%s"%(FoodPrice)) 


#7.
KUSRC = {"Management", "Engineering","Science", "Marine", "Economics"}
KUBKK = {"Agriculture", "Business", "Fisheries", "Humanities", "Science", "Engineering", "Education", "Economics"}

#8
#7.1
KUALL=KUSRC.union(KUBKK)
print("คณะทั้งหมดของทั้งสองวิทยาเขต:",KUALL)
#7.2
KUALL=KUSRC.intersection(KUBKK)
print("คณะที่มีอยู่ทั้งสองวิทยาเขต:",KUALL)
#7.3
KUALL=KUSRC.difference(KUBKK)
print("คณะที่มีอยู่ในวิทยาเขตศรีราชาแต่ไม่มีในวิทยาเขตบางเขน:",KUALL)



#9.
KUfaculty=str(input("ชื่อคณะที่ต้องการ:"))

if KUfaculty in KUSRC.intersection(KUBKK):
    print("คุณมีโอกาสได้ทั้งสองวิทยาเขต")
elif KUfaculty in KUSRC.difference(KUBKK) :
    print("คุณเรียนที่วิทยาเขตศรีราชา")
elif KUfaculty in KUBKK.difference(KUSRC):
    print("คุณเรียนที่วิทยาเขตบางเขน")
else:
    print("เสียใจด้วย คุณไม่ได้เรียนที่วิทยาเขตบางเขนหรือศรีราชา")


#6.
Faculty=("Management", "Engineering", "Science", "Marine", "Economic")

#7.
print("จำนวนข้อมูลทั้งหมด:",len(Faculty[1:6]))
Start=int(input("ค่าเริ่มต้น:"))
Stop=int(input("ค่าสิ้นสุด(จะไม่ถูกอ่านค่า):"))
print("ข้อมูลที่ต้องการ:",Faculty[Start:Stop])


#8.
KuFaculty=str(input("เชื่อคณะที่ศึกษาอยู่:"))

if KuFaculty in Faculty:
    print("You are studying at KU Sriracha campus.")

else:
    print("Sorry, you aren’t studying there.")

