
import discord
import time
import os
import requests
import json
import random 
from discord.ext import commands

client = commands.Bot(command_prefix="/")

go = ["https://imgur.com/t/kyojuro_rengoku/94wOLtZ","https://img.fireden.net/y/image/1461/65/1461658417773.gif", "https://media.tenor.com/images/eb2a5d3665dbcad3f81872e9df694b6e/tenor.gif", "https://img-egc.xvideos-cdn.com/videos/thumbslll/cb/d0/fc/cbd0fc46be9fd823d41c92b20423d37a/cbd0fc46be9fd823d41c92b20423d37a.15.jpg", "https://tenor.com/view/kimetsu-no-yaiba-demon-slayer-oni-akaza-gif-21494126","https://lotus.paheal.net/_images/ccf334ffb7d81245f70224382d494de6/4063501%20-%20Demon_Slayer%3A_Kimetsu_no_Yaiba%20Nezuko_Kamado%20Tanjiro_Kamado%20animated%20ginhaha.gif", "https://peach.paheal.net/_images/31421b6d656d1fdd36a3a27bd813d5d6/4282257%20-%20Demon_Slayer%3A_Kimetsu_no_Yaiba%20DragonEdit%20Nezuko_Kamado%20Sirfy%20animated%20edit.gif", "https://cdn.discordapp.com/attachments/934649292310839396/939657633663709284/ezgif-7-15c43069b3.gif"]

hard=["https://himg.nl/images/sex/56786d7aa30fb2365f6dc7e035ebeef3/original.gif", "https://himg.nl/images/sex/69be88587d5439607ee691cce5db3f33/original.gif", "https://himg.nl/images/sex/070be93a67b5513b7ae94d34dc5f3cf7/original.gif", "https://himg.nl/images/sex/36c85565dde1ba991ec0c2fe79678449/original.gif", "https://porngifs.xxx/wp-content/uploads/2019/08/bounce-porn-gifs-sex-gif.gif", "https://himg.nl/images/sex/61469425ac43e14f6b7763b1312f0a9a/original.gif"]

@client.event
async def on_ready():
  y = 'Bot is Ready'
  print("\033[1m" + y + "\033[0m")

@client.command()
async def hello(ctx):
  await ctx.send('Hello!!')

@client.command()
async def redpanda(ctx):
  r = requests.get("https://some-random-api.ml/img/red_panda", verify = True)

  data = r.text
  parse = json.loads(data)

  image1 = parse['link']
  await ctx.send(image1)

@client.command()
async def wink(ctx):
  r = requests.get("https://some-random-api.ml/animu/wink", verify = True)

  data = r.text
  parse= json.loads(data)

  gif = parse['link']
  await ctx.send(gif)

@client.command()
async def colin(ctx):
  await ctx.send(random.choice(go))

@client.command()
async def clear(ctx, amount=50):
  await ctx.channel.purge(limit = amount)

@client.command()
async def Colin(ctx):
  await ctx.send(random.choice(hard))
  time.sleep(2)
  await ctx.send("https://c.tenor.com/QA6mPKs100UAAAAC/caught-in.gif")
  await ctx.send("Wow!!")

@client.command()
async def translate(ctx, *, word):
  import requests

  url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
  url_2 = "https://google-translate1.p.rapidapi.com/language/translate/v2/detect"

  payload = "q={}&target=tr&source=en".format(word)
  headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com",
    'x-rapidapi-key': "1fa99094damsh2e8b6d5553191d0p167141jsn1c04d132e346"
    }
  headers_2 = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com",
    'x-rapidapi-key': "1fa99094damsh2e8b6d5553191d0p167141jsn1c04d132e346"
    }

  response = requests.request("POST", url, data=payload, headers=headers)
  data = response.text
  trans = json.loads(data)
  x = "q={}".format(trans['data']['translations'][0]['translatedText'])
  detect = requests.request("POST", url_2, data=x, headers=headers_2)
  data_2 = detect.text
  detect_2 = json.loads(data_2)
  language = trans['data']['translations'][0]['translatedText']
  translated = (detect_2['data']['detections'][0][0]['language'])
  embed = discord.Embed(
    title = 'Inputed phrase/word.',
    description = f'Initial input: {word}',
    colour = discord.Color.lighter_grey()
    )
  embed.set_image(url = 'https://adrenalineboots.files.wordpress.com/2014/11/symbol_talk.png')
  embed.set_thumbnail(url = 'https://assets.materialup.com/uploads/06a17548-98d7-4537-bea3-9c59b64628dc/attachment.jpg')
  embed.add_field(name = 'Translation', value = language, inline = False)
  embed.add_field(name = 'Language', value = translated, inline = False)
  embed.set_footer(text = 'Made by Astroid45#9086')
  await ctx.send(embed=embed)

@client.command()
async def price(ctx, *, shoe):
  url = "https://stockx.com/api/browse"


  #change name to get different shoe
  querystring = {"_search":f"{shoe}","dataType":"product"}

  payload = ""
  headers = {
    "cookie": "_ga=GA1.2.556695976.1596899981; tracker_device=82cd8894-013e-45b3-b63c-73bcd3130e16; _px_f394gi7Fvmc43dfg_user_id=OTg1NWRlNjAtZDk4YS0xMWVhLWExODQtNGY5NzExNTEwZDI1; rskxRunCookie=0; rCookie=w5yac4182gb2oa4n6co71hkdlt0shx; QuantumMetricUserID=99edfa4da90767d202b5f8c4b5a637db; mfaLogin=err; _rdt_uuid=1621001185735.89bf88dc-4ee5-4c69-877b-aefc56f476a4; __pdst=89e42f430b464acc9f167ef47725f739; ajs_user_id=0489a8f2-d02d-11e8-8028-12f926a2c6c6; __pxvid=bc93acb3-fecd-11eb-a91a-0242ac110003; __ssid=3675417db90105205a11ba902b79d14; _ts_yjad=1629829199389; _scid=b31c240f-2378-4f2f-bf3b-c5bd007b7532; _pin_unauth=dWlkPU5HSmhZakpsTVRVdFlqRmpPUzAwTURWaUxUZzVPREl0WXpobU1qTmhZMlF5TXpBeg; _ga=GA1.2.556695976.1596899981; _pxvid=f2bef9a3-306e-11ec-8e33-5461505a5573; ajs_group_id=ab_3ds_messaging_eu_web.false%2Cab_aia_pricing_visibility_web.novariant%2Cab_chk_germany_returns_cta_web.true%2Cab_chk_order_status_reskin_web.true%2Cab_chk_place_order_verbage_web.false%2Cab_chk_remove_affirm_bid_entry_web.true%2Cab_chk_remove_fees_bid_entry_web.false%2Cab_citcon_psp_web.true%2Cab_desktop_home_hero_section_web.control%2Cab_home_contentstack_modules_web.variant%2Cab_home_dynamic_content_targeting_web.control%2Cab_low_inventory_badge_pdp_web.control%2Cab_pirate_recently_viewed_browse_web.false%2Cab_product_page_refactor_web.true%2Cab_recently_viewed_pdp_web.variant_1%2Cab_test_korean_language_web.true%2Cab_web_aa_1103.true; ajs_anonymous_id=bf3a499f-78af-4a9e-80a6-032fa768e644; stockx_seen_ask_new_info=true; ab_one_buy_now_button=variant_1; rbuid=rbos-97db2135-5a72-4334-a347-9a633f09fdcf; _gcl_au=1.1.864405280.1642432403; stockx_device_id=web-d94a8efe-1798-4143-95b4-eb44278d2de3; __lt__cid=7e74511d-47ca-443f-b103-8989d26125c4; language_code=en; _gid=GA1.2.675827628.1645128299; pxcts=e22341f2-902c-11ec-a83c-434564467145; riskified_recover_updated_verbiage=true; ops_banner_id=blt055adcbc7c9ad752; IR_gbd=stockx.com; stockx_preferred_market_activity=sales; NA_SAC=dT1odHRwcyUzQSUyRiUyRnN0b2NreC5jb20lMkZidXklMkZhZGlkYXMtbm1kLXIxLXRyaXBsZS1ibGFjay0yMDE5JTNGc2l6ZSUzRDEwLjV8cj0=; _gac_UA-67038415-1=1.1645134631.EAIaIQobChMIi9m4tMmH9gIVBLrICh1H8AVOEAQYAiABEgIWr_D_BwE; _gcl_aw=GCL.1645134632.EAIaIQobChMIi9m4tMmH9gIVBLrICh1H8AVOEAQYAiABEgIWr_D_BwE; _gcl_dc=GCL.1645134632.EAIaIQobChMIi9m4tMmH9gIVBLrICh1H8AVOEAQYAiABEgIWr_D_BwE; _clck=a596t3|1|ez3|0; token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5USkNNVVEyUmpBd1JUQXdORFk0TURRelF6SkZRelV4TWpneU5qSTNNRFJGTkRZME0wSTNSQSJ9.eyJodHRwczovL3N0b2NreC5jb20vY3VzdG9tZXJfdXVpZCI6IjA0ODlhOGYyLWQwMmQtMTFlOC04MDI4LTEyZjkyNmEyYzZjNiIsImh0dHBzOi8vc3RvY2t4LmNvbS9nYV9ldmVudCI6IkxvZ2dlZCBJbiIsImlzcyI6Imh0dHBzOi8vYWNjb3VudHMuc3RvY2t4LmNvbS8iLCJzdWIiOiJhdXRoMHwwNDg5YThmMi1kMDJkLTExZTgtODAyOC0xMmY5MjZhMmM2YzYiLCJhdWQiOiJnYXRld2F5LnN0b2NreC5jb20iLCJpYXQiOjE2NDUyMDY3MDgsImV4cCI6MTY0NTI0OTkwOCwiYXpwIjoiT1Z4cnQ0VkpxVHg3TElVS2Q2NjFXMER1Vk1wY0ZCeUQiLCJzY29wZSI6Im9mZmxpbmVfYWNjZXNzIn0.XqQR1rFRc-lQ1KVq4MJxG6uq_DSbN9D55gLb9yLkdUnLiRJb3gpiUzDKwSC-aw4pFFmKrGK1yUZ-TiK_E1w7ZOfgqXuGUoVtYXdad6S3OW0SVdzxK0OzfpbiMT4l4oznHWiZBiIYEssH-bLuVe_kysSwlVceplWTOmlGOtM4wj_TwKXbaTI1g2XhD5N2yqAjh5_0vfbmTSrjonC0MsTfDku2d68k-JPcsLZIwAg3adBNS-auWgrtMXgF281zK6g9vGLUUFTx0s8E6Y4QOK2FoTltNX-Sn_N85RmdJjSosY4RKi_ndjWl3C_Xp0AG4j42tdLOF5vA5kWnV2OS_2G9mw; QuantumMetricSessionID=5b23f3a4308a50a270e4bbd12b29071c; stockx_default_sneakers_size=10.5; stockx_session=%22ac626673-3cb2-4492-9a38-0a23a3b11272%22; forterToken=58e78fe801ec423d80a155ed146f9097_1645212049084__UDF43_13ck; _derived_epik=dj0yJnU9QURMc2hwQWIyTkFaYzM0NnE4NkdXNjFjRWQ5M0ZzQlEmbj0yV2tWTjhYLXAwZ1dMQW5UQUltRTFnJm09NCZ0PUFBQUFBR0lQOFpFJnJtPTQmcnQ9QUFBQUFHSVA4WkU; stockx_product_visits=11; lastRskxRun=1645212053596; _uetsid=e34e7c70902c11ec972061c9a5c05a33; _uetvid=5ba4a250bcb211eb95b135163fb1471a; IR_9060=1645212054763%7C0%7C1645212054763%7C%7C; IR_PI=97803f72-d98a-11ea-a165-42010a246cc2%7C1645298454763; _px3=da5ce042870d1780c381d51ae0454c37d7559082c7d06c8433b21f433cca2d5e:txbZg/8wltgIevv1AqN4XwBogfG+rDEMBFN18VMO2G4i8h7RMiRP9Ls5qknIFaKYgR8BT5Dft8l/vzAzWynn0g==:1000:RGrnAazgHj1boEGOu57jD5DnG4ruMGfA6kunSIXYsPlbsRr8m3dBFPn2b1uFRk9wYm5hsduiSbflKhJbe2BdhypnreYWBuTP4rYHkJqlRgEp8e6G7WRnqwOvyQQS/DvwFBhQarHSru/WX+PAl4ctZh4C3s30vxb9aQ5KHdmYrF0F2TdmE/N76y68ohTV27acDJF35q+nBoYEEsIdLSuxZQ==; _clsk=166vz9t|1645212157057|35|0|l.clarity.ms/collect; _gat=1; stockx_selected_currency=USD; _dd_s=rum=0&expire=1645213091613; stockx_homepage=browseverticals; loggedIn=0489a8f2-d02d-11e8-8028-12f926a2c6c6; _pxff_tm=1",
    "authority": "stockx.com",
    "sec-ch-ua": '"Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    "appos": "web",
    "sec-ch-ua-mobile": "?0",
    "authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5USkNNVVEyUmpBd1JUQXdORFk0TURRelF6SkZRelV4TWpneU5qSTNNRFJGTkRZME0wSTNSQSJ9.eyJodHRwczovL3N0b2NreC5jb20vY3VzdG9tZXJfdXVpZCI6IjA0ODlhOGYyLWQwMmQtMTFlOC04MDI4LTEyZjkyNmEyYzZjNiIsImh0dHBzOi8vc3RvY2t4LmNvbS9nYV9ldmVudCI6IkxvZ2dlZCBJbiIsImlzcyI6Imh0dHBzOi8vYWNjb3VudHMuc3RvY2t4LmNvbS8iLCJzdWIiOiJhdXRoMHwwNDg5YThmMi1kMDJkLTExZTgtODAyOC0xMmY5MjZhMmM2YzYiLCJhdWQiOiJnYXRld2F5LnN0b2NreC5jb20iLCJpYXQiOjE2NDUyMDY3MDgsImV4cCI6MTY0NTI0OTkwOCwiYXpwIjoiT1Z4cnQ0VkpxVHg3TElVS2Q2NjFXMER1Vk1wY0ZCeUQiLCJzY29wZSI6Im9mZmxpbmVfYWNjZXNzIn0.XqQR1rFRc-lQ1KVq4MJxG6uq_DSbN9D55gLb9yLkdUnLiRJb3gpiUzDKwSC-aw4pFFmKrGK1yUZ-TiK_E1w7ZOfgqXuGUoVtYXdad6S3OW0SVdzxK0OzfpbiMT4l4oznHWiZBiIYEssH-bLuVe_kysSwlVceplWTOmlGOtM4wj_TwKXbaTI1g2XhD5N2yqAjh5_0vfbmTSrjonC0MsTfDku2d68k-JPcsLZIwAg3adBNS-auWgrtMXgF281zK6g9vGLUUFTx0s8E6Y4QOK2FoTltNX-Sn_N85RmdJjSosY4RKi_ndjWl3C_Xp0AG4j42tdLOF5vA5kWnV2OS_2G9mw",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-platform": '"Windows"',
    "appversion": "0.1",
    "accept": "*/*",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://stockx.com/search?s=JORDAN%201%20MARINA",
    "accept-language": "en-US,en;q=0.9",
    "if-none-match": 'W/"30b2f-emQKcIXLmie+tIB3yD99wvBm4FY"'
  }

  r = requests.request("GET", url, data=payload, headers=headers, params=querystring)
  data = r.json()
  shoe_name = data["Products"][0]["shortDescription"].replace('-', ' ')
  shoe_retail = data["Products"][0]["retailPrice"]
  shoe_id = data["Products"][0]["styleId"]
  lowest_ask = data["Products"][0]["market"]["lowestAsk"]
  lowest_ask_size = data["Products"][0]["market"]["lowestAskSize"]
  highest_bid = data["Products"] [0]["market"]["highestBid"]
  highest_bid_size = data["Products"] [0]["market"]["highestBidSize"]

  embed = discord.Embed(
    title = shoe_name,
    description = f'Retail: ${shoe_retail}  ||  SKU: {shoe_id}',
    colour = discord.Color.lighter_grey()
    )
  embed.set_image(url = data["Products"][0]["media"]["smallImageUrl"])
  embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/934649292310839396/944423331162124308/StockX-New-Logo.png')
  embed.add_field(name = 'Asks', value = f'Lowest Ask: ${lowest_ask}  ||  Size: {lowest_ask_size}', inline = False)
  embed.add_field(name = 'Bids', value = f'Highest Bid: ${highest_bid}  ||  Size: {highest_bid_size}', inline = False)
  embed.set_footer(text = 'Made by jah#1544 and Portgas#8946')
  await ctx.send(embed=embed)


@client.command()
async def rate(ctx, *, coin):
  import requests

  url = "https://alpha-vantage.p.rapidapi.com/query"

  querystring = {"market":"CNY","symbol":"BTC","function":"DIGITAL_CURRENCY_DAILY"}
  querystring["symbol"] = coin
  headers = {
    'x-rapidapi-host': "alpha-vantage.p.rapidapi.com",
    'x-rapidapi-key': "74054fb7fdmshbf82f26a2285e4dp1f58cdjsn532a23962644"
    }

  response = requests.request("GET", url, headers=headers, params=querystring)

  await ctx.send(response.text)


@client.command()
async def ip(ctx, *, domain):
  import requests

  url = "https://find-any-ip-address-or-domain-location-world-wide.p.rapidapi.com/iplocation"

  querystring = {"ip":"godaddy.com","apikey":"873dbe322aea47f89dcf729dcc8f60e8"}
  querystring["ip"] = domain
  headers = {
    'x-rapidapi-host': "find-any-ip-address-or-domain-location-world-wide.p.rapidapi.com",
    'x-rapidapi-key': "74054fb7fdmshbf82f26a2285e4dp1f58cdjsn532a23962644"
    }

  response = requests.request("GET", url, headers=headers, params=querystring)
  data = response.text
  ip_2= json.loads(data)
  # revit = ip_2[]
  await ctx.send(response.text)

# @client.command()
# async def money(ctx, *, value, cur1, cur2):
#   import requests

#   url = "https://community-neutrino-currency-conversion.p.rapidapi.com/convert"

#   payload = "from-value={}&from-type={}&to-type={}".format(value, cur1, cur2)
#   headers = {
# 	  "content-type": "application/x-www-form-urlencoded",
# 	  "X-RapidAPI-Host": "community-neutrino-currency-conversion.p.rapidapi.com",
# 	  "X-RapidAPI-Key": "74054fb7fdmshbf82f26a2285e4dp1f58cdjsn532a23962644"
#   }
#   response = requests.request("POST", url, data=payload, headers=headers)
#   data = response.text
#   trans = json.loads(data)
#   x = "q={}".format()
#   await ctx.send(data)


# client.run(os.getenv('token'))
TOKEN ='OTM0NjQ0NTEwODc5ODA1NTAw.YezFiA.KoWpwyrOzRmzYt1tMqAA2gpJGVc' 

client.run(TOKEN)

