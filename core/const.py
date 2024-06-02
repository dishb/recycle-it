from os.path import dirname

PADX = 10
PADY = 10
STICKY = "nsew"

FONT_SIZE = 17

SCRIPT_PATH = dirname(__file__).removesuffix("/core")

IMG_PATH = F"{SCRIPT_PATH}/images/object.png"

RECYCLE = ["cardboard",
           "glass",
           "metal",
           "paper",
           "plastic",
           ]
TRASH = ["clothes",
         "shoes",
         "trash"
         ]
COMPOST = ["biological"]
EWASTE = ["battery"]
