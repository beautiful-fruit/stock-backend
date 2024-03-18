from pydantic import BaseModel

class DiscordUserBase(BaseModel):
#     {
#     "id": "625302301313073192",
#     "username": "happypotato_0415",
#     "avatar": "76158dd300380ef5cc76f5b8bd05e753",
#     "discriminator": "0",
#     "public_flags": 0,
#     "premium_type": 0,
#     "flags": 0,
#     "banner": null,
#     "accent_color": null,
#     "global_name": "一顆悠閒的貓麻糬",
#     "avatar_decoration_data": null,
#     "banner_color": null,
#     "mfa_enabled": true,
#     "locale": "zh-TW"
# }

    id: int
    username: str
    avatar: str
    global_name: str
    email: str
    verified: bool