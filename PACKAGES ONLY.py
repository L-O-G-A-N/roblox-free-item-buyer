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


def cprint(color: str, content: str) -> None:
    console.print(f"[ [bold {color}]>[/] ] {content}")

cookie = input("enter your cookie: ")
os.system('cls')

print(f" Cookie: {cookie}")
print("starting in 10 seconds. restart if something looks wrong")
time.sleep(10)
session = requests.Session()
session.cookies.update({".ROBLOSECURITY": cookie})

console = Console(highlight=False)





def fetch_items() -> None:
    result = {}
    cursor = ""

    while cursor is not None:
        req = session.get(
            f"https://catalog.roblox.com/v1/search/items/details?Category=17&CurrencyType=1&pxMin=0&pxMax=0&salesTypeFilter=1&SortType=3&Limit=30&cursor={cursor}"
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
