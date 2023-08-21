import pathlib
import time
import os
import requests
from rich.console import Console
# pov: you get rate limited
pensive = """
                                     &&&&&&&                                    
                          &&&&&&&&&&&&&&&&&&&&&&&&&&&&&                         
                     &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&                    
                 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&                
              &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&             
           &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&          
         &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&        
       &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&      
      &&&&&&&&&&&&&&&&&&&&*,,,,/&&&&&&&&&&&&&&&&&,,,,,(&&&&&&&&&&&&&&&&&&&&     
    &&&&&&&&&&&&&&&&&&&%,,,,,,&&&&&&&&&&&&&&&&&&&&&,,,,,,&&&&&&&&&&&&&&&&&&&(   
   &&&&&&&&&&&&&&&&%,,,,,,,,&&&&&&&&&&&&&&&&&&&&&&&&&,,,,,,,,&&&&&&&&&&&&&&&&&  
  &&&&&&&&&&,,,,,,,,,,,,#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&/,,,,,,,,,,,,&&&&&&&&&% 
 *&&&&&&&&&&,,,,,,,%&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%,,,,,,,&&&&&&&&&& 
 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&,,,,&&&&&&&&&&&&#,,,&&#,,,%&&&&&&&&&&&%,,,/&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&,,,,,,,,,,,,,,,,,&&&&&,,,,,,,,,,,,,,,,,&&&&&&&&&&&&&&&&&&&&
 &&&&&&&&&&&&&&&&&&&&&&,,,,,,,,,,,,,&&&&&&&&&,,,,,,,,,,,,,&&&&&&&&&&&&&&&&&&&&&&
 &&&&&&&&&&&&&&&&&&&&&&&&&&/,,,%&&&&&&&&&&&&&&&&&#,,,#&&&&&&&&&&&&&&&&&&&&&&&&&&
  &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&& 
  &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&% 
   &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%  
    &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&(   
      &&&&&&&&&&&&&&&&&&&&&&&,,,,,,,,,,,,,,,,,,,,,,/&&&&&&&&&&&&&&&&&&&&&&&     
       &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&%      
         &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&        
           &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&/          
              &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&             
                 &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&                
                     &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&                    
                          &&&&&&&&&&&&&&&&&&&&&&&&&&&&/                         
                          """

catagories = """
All: 1
Collectibles: 2
Clothing: 3
BodyParts: 4 -- use this for dynamic heads too
Gear: 5
Models: 6
Plugins: 7
Decals: 8
Audio: 9
Meshes: 10
Accessories: 11
AvatarAnimations: 12 -- emotes
CommunityCreations: 13 -- ugc, i'm not sure if this works anymore
Video: 14 -- I don't think this does anything
Recommended: 15 -- don't use
LayeredClothing: 16
Characters: 17 -- DONT USE, USE OTHER FILE
"""
subcatagories = """
Featured: 0
All: 1
Collectibles: 2
Clothing: 3
BodyParts: 4
Gear: 5
Models: 6
Plugins: 7
Decals: 8
Hats: 9
Faces: 10
Packages: 11
Shirts: 12
Tshirts: 13
Pants: 14
Heads: 15
Audio: 16
RobloxCreated: 17
Meshes: 18
Accessories: 19
HairAccessories: 20
FaceAccessories: 21
NeckAccessories: 22
ShoulderAccessories: 23
FrontAccessories: 24
BackAccessories: 25
WaistAccessories: 26
AvatarAnimations: 27
ClimbAnimations: 28
FallAnimations: 30
IdleAnimations: 31
JumpAnimations: 32
RunAnimations: 33
SwimAnimations: 34
WalkAnimations: 35
AnimationPackage: 36
BodyPartsBundles: 37
AnimationBundles: 38
EmoteAnimations: 39
CommunityCreations: 40
Video: 41
Recommended: 51
LayeredClothing: 52
AllBundles: 53
HeadAccessories: 54
ClassicTShirts: 55
ClassicShirts: 56
ClassicPants: 57
TShirtAccessories: 58
ShirtAccessories: 59
PantsAccessories: 60
JacketAccessories: 61
SweaterAccessories: 62
ShortsAccessories: 63
ShoesBundles: 64
DressSkirtAccessories: 65
DynamicHeads: 66

i'm too lazy to explain these all but you can probably make out what most of these do
"""
def cprint(color: str, content: str) -> None:
    console.print(f"[ [bold {color}]>[/] ] {content}")

cookie = input("enter your cookie: ")
os.system('cls')

print(catagories)
catagory = input("Enter the number from which catagory you would like to buy from: ")
os.system('cls')
print(subcatagories)
subcatagory = input("Enter the number from which subcatagory you would like to buy from: ")
os.system('cls')
print(f" Cookie: {cookie} \n Catagory: {catagory} \n Subcatagory: {subcatagory}")
print("starting in 10 seconds. restart if something looks wrong")
time.sleep(10)
os.system('cls')
session = requests.Session()
session.cookies.update({".ROBLOSECURITY": cookie})

console = Console(highlight=False)





def fetch_items() -> None:
    result = {}
    cursor = ""

    while cursor is not None:
        req = session.get(
            f"https://catalog.roblox.com/v1/search/items/details?Category={catagory}&Subcategory={subcatagory}&CurrencyType=1&pxMin=0&pxMax=0&salesTypeFilter=1&SortType=3&Limit=30&cursor={cursor}"
        )
        res = req.json()

        if req.status_code == 429:
            print(pensive)
            cprint("red", "Rate limited. Waiting 120 seconds")
            time.sleep(120)
            continue

        for item in res.get("data", []):
            item_name = item.get("name")
            result[item.get("creatorTargetId")] = item.get("productId")
            cprint("blue", f"Found {item_name}")
        cursor = res.get("nextPageCursor")

    return result


def purchase(name: str, product_id: int) -> None:
    req = session.post("https://auth.roblox.com/v2/login")
    csrf_token = req.headers["x-csrf-token"]

    while True:

        req = session.post(
            f"https://economy.roblox.com/v1/purchases/products/{product_id}",
            json={"expectedCurrency": 1, "expectedPrice": 0, "expectedSellerId": name},
            headers={"X-CSRF-TOKEN": csrf_token},
        )

        if req.status_code == 429:
            print(pensive)
            cprint("red", "Rate limited. Waiting 120 seconds")
            time.sleep(120)
            continue

        res = req.json()
        if "reason" in res and res.get("reason") == "AlreadyOwned":
            cprint("yellow", f"Product from {name} is already owned")
            return

        cprint("green", f"Successfully purchased product from: {name}")
        return


def main() -> None:
    free_items = fetch_items()
    for name, product_id, in free_items.items():
        purchase(name, product_id)
while True:
 main()
