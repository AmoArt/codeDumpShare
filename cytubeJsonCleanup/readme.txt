tool created in converting the cytube json archive comments into an somehow usefull dataset for training emote predition text models.

Example of what the text in datset will look like:
[
  {
    "msg": "I love them :excite:  :excite:  :excite:  :excite:",
    "text_": "I love them",
    "tags_": ":excite: :excite: :excite: :excite:"
  },
  {
    "msg": "PonyLover123: :mlp_heart: Check out this awesome artwork! :mlp_heart: :art:",
    "text_": "PonyLover123: Check out this awesome artwork!",
    "tags_": ":mlp_heart: :mlp_heart: :art:"
  }
]


To operate the scripts, place the zip json files in the 'json_raw_zip' folder, than fun the nummered python code.

source of json files:
https://mare.pages.dev
