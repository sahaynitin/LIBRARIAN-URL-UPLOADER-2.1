class Translation(object):

    START_TEXT = """**Hello User
This is a Telegram URL Upload Bot! Powered By Team Librarian™️ ** 

**Please send me any Direct download URL link, I can upload to telegram as File/Video**

__/help for more details..__

**Specially designed for** : **@Team_Librarian**
    """

    HELP_USER = """Hi 🍃 I'am a URL Uploader bot😍

1} Send url (Link | New Name with Extension)
2} Send Custom Thumbnail (Optional)
3} Select the desired format 
    🎞  - Stream format (left side)
    📁  - File format (right side)

If you want to set custom thumbnail, send photo or Use auto-generated 📸 Thumbnail

Specially Designed For : @Team_Librarian
"""

    FORMAT_SELECTION = """Select the desired format
 "<a herf='{}'> File Sizs Might Be approximate</a>"
   🎞  - Stream format (left side)
   📁  - File format (right side)
   
If you want to set custom thumbnail, send photo or Use auto-generated 📸 Thumbnail

You can use ```/deletethumbnail``` to delete the auto-generated thumbnail.

Powered By @Team_Librarian™️
"""
    
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""


    UPGRADE_TEXT = "If you need it's source code, Dm @Purushottam_Mahajan & @AniMesH941 Made with 🐍♥ by Team Librarian"
    
    DOWNLOAD_START = "```Trying to download your file...😘🤦```"
    
    UPLOAD_START = "🙈Uploading now.."
    
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \n\nUploaded in {} seconds."

    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."

    SAVED_CUSTOM_THUMB_NAIL = "Custom thumbnail saved. This will be permanent.\n\nUse /deletethumbnail to clear it."

    DEL_ETED_CUSTOM_THUMB_NAIL = "🤦Custom thumbnail cleared succesfully.( BC )"

    CUSTOM_CAPTION_UL_FILE = " "

    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."

    NO_VOID_FORMAT_FOUND = "🥺ERROR...\n<b>YouTubeDL</b> said: {}"
    
    SHOW_THUMB = "Use /deletethumbnail to clear this thumbnail.🤦🙈"
    
    NO_THUMB = "No saved thumbnails Found!!\n\nSend an image to save it as your thumbnail permanently."    
