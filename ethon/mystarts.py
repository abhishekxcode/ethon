#ignore this file

from telethon import events, Button


async def start_srb(event, st):
    await event.reply(st, 
                      buttons=[
                              [Button.inline(" 📸 Set Thumbnail ", data="set"),
                               Button.inline(" 🗑️ Remove Thumbnail ", data="rem")]])
                              
    
async def vc_menu(event):
    await event.edit("**VIDEO Trimmer v2.0**", 
                    buttons=[
                        [Button.inline(" ℹ️ Info", data="info"),
                         Button.inline(" 📦 Source", data="source")],
                        [Button.inline(" 📢 Notice", data="notice"),
                         Button.inline(" 🏠 Main Menu", data="help")]])
    
