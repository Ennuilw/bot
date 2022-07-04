import discord
import dateutil.parser
import random
import asyncio
import json
import ndjson
from discord.ext import commands
from discord.ui import View, Button
intents=discord.Intents.all()
bot=commands.Bot(command_prefix=".", intents=intents)
bot.remove_command("help")



#async with channel.typing():

@bot.command()
@commands.has_role(991009276946419714)
async def help_(ctx):
    e=discord.Embed(
        title="深夜祭-コマンド",
        description=
        f"<@&991009276946419714>限定コマンド\n"
        "`help_` **:** このコマンド\n"
        "`register[reg] *(id)` **:** 憤死者リストに**登録**\n"
        "`sh` **:** Jsonファイルの中身を見る\n"
        "`show` **:** 憤死者リストを表示\n"

    )
    e.add_field(name="*(id)", value="-id or mention it bot to target")
    e.set_footer(text=f"By: {ctx.author}")
    await ctx.send(embed=e)


@bot.command()
async def setting_list_f(ctx):
    if ctx.author.id != 956042267221721119:return
    _data_list = {"person":[]}
    with open("memberlist.json", "w", encoding="utf-8") as f:
        json.dump(_data_list, f, indent=2)
    msg = await ctx.send("EXECUTING")
    await asyncio.sleep(0.1)
    await msg.edit("EXECUTING.")
    await asyncio.sleep(0.1)
    await msg.edit("EXECUTING..")
    await asyncio.sleep(0.1)
    await msg.edit("EXECUTING...")
    await asyncio.sleep(0.5)
    await msg.edit("リストのフォーマットが終了しました。")

@bot.command(aliases=["reg"])
@commands.has_role(991009276946419714)
async def register(ctx, user:discord.Member, reason = None):
    if not user:await ctx.send(("登録するユーザーが指定されていません"))
    data = {
        "name":f"{user.name}#{user.discriminator}",
        "id":user.id,
        "reason": reason
    }
    with open("memberlist.json", "r") as f:
        info = json.load(f)
    info["person"].append(data)
    with open("memberlist.json", "w", encoding="utf-8") as f:
        json.dump(info, f, indent=2)# ensure_ascii=False,
    await ctx.send("追加しました")

@bot.command(aliases=["add"])
@commands.has_role(991009276946419714)
async def additional(ctx, user:discord.Member):
    if not user:await ctx.send(("登録するユーザーが指定されていません"))
    data = {
        "name":f"{user.name}#{user.discriminator}",
        "id":user.id
    }
    with open("memberlist.json", "r") as f:
        info = json.load(f)
    info["person"].append(data)
    with open("memberlist.json", "w", encoding="utf-8") as f:
        json.dump(info, f, indent=2)# ensure_ascii=False,
    await ctx.send("追加しました。")


@bot.command(aliases=["s"])
async def search(ctx, name:discord.Member):
    with open("memberlist.json", "r") as f:
        info=json.load(f)
    print(info.get("person").get("name"))

@bot.command()
async def json_setup(ctx):
    data_format = {
        
    }
"""
@bot.command()
async def hunshi(ctx):
    pass
        e.add_field(
            name="> ",
            value=jsn["person"][i]["reason"],inline=False
        )
"""


@bot.command()
@commands.has_role(991009276946419714)
async def sh(ctx):
    with open("memberlist.json", "r") as f:
        info = f.read()
    e=discord.Embed(
        title="memberlist.json",
        description=f"```json{info}```")
    await ctx.send(embed=e)


@bot.command()
@commands.has_role(991009276946419714)
async def print(ctx):
    with open("memberlist.json", "r") as f:jsn = (json.load(f))
    e=discord.Embed(color=0xff0000)
    i = 0
    for i in range(len(jsn["person"])):  
        e.add_field(
            name= (jsn["person"][i]["name"]), value= 'ID: {}'.format(jsn["person"][i]["id"]),inline=False)
        i += 1
    e.title="リスト [{}]".format(len(jsn["person"]))
    await ctx.send(embed=e)

@bot.command()
async def text(ctx):
    text = """
典型的憤死ワード集

・荒らしで時間無駄にしてて草
・しょうもないことして楽しい？
・BANすればいいだけ 残念だったな
・ムカつくから黙れ
・学歴しか誇れないゴミで草
・楽しんでて哀れ
・暇つぶし楽しかったよ
・学歴と頭脳は比例しない
・あーもうこいつうるさいから蹴ろう
・誤字してて草
・十字軍はくだらない組織
・あそんでいるだけなんだが？
"""
    await ctx.send(text)


@bot.command()
async def help(ctx):
    e=discord.Embed(title="Help command",description=
    f"Example\n"
    "`command[aliase]` **:** 見方\n"
    "\n:partying_face: **バラエティ**\n"
    "`fortune[kuji]` **:** 占い\n"
    "`soviet` **:** ソヴィエトアスキーアート\n"
    "`yn` **:** yesかno\n"
    "\n:tools: **ツール**\n"
    "`help` **:** このコマンド\n"
    "`about` **:** このボットについて\n"
    "`avatar[a]` **:** アイコンを表示\n"
    "`banner[b]` **:** バナーを表示。もしあればｗ\n"
    "`track` **:** アクティビティからSpotifyのurlを\n"
    "`spotify[sp]` **:** Information on the Spotify song you are listening to\n"
    "`userinfo[ui]` **:** Get info about user\n"
    "`serverinfo[si]` **:** Get info about server\n"
    "`invite *2(id)` **:** Create bot invite url",color=0x6dc1d1)
    e.add_field(name="*(reason)", value=f"-Reason to use command(Possible without)", inline=False)
    e.add_field(name="*2(id)", value = "-id or mention it bot to target")
    e.set_footer(text=f"By: {ctx.author}")
    await ctx.send(embed=e)



    #await ctx.send((jsn["person"][0]["name"]))


@bot.command()
async def soviet(ctx):
    await ctx.send("""```fix
                !#########      
            !########!           !\\
         !########!               #!\\
      !##########                 \###!
    ##############                 ####!
     !###!     !####!             .#####!
       '          #####            ######!
                    !####!         #######
                       #####      ,#######
                         !####!  ,#######!
                            ####!########
          ##                  ,##########
        ,######!,          ,############
   ,!##### ########################!####!
 ,######'     ##################!'    #####
 ,######'           ########"           !####!
#####'                                     #####!
~##                                          ####
```
""")

@bot.command()
async def yn(ctx):
    await ctx.send(random.choice(("Yes","No")))

@bot.command()
async def about(ctx):
    user= bot.get_user(956042267221721119)
    members= 0
    for guild in bot.guilds:members += guild.member_count - 1
    embed= discord.Embed(title= "Server URL",color= 0x6dc1d1, url ="https://discord.gg/owen")
    embed.add_field(name= "Customers",value= f"Servers **:** `{str(len(bot.guilds))}`\nMembers **:** `{str(members)}`", inline= False)
    embed.add_field(name= "Dev", value= f"{user.mention}", inline= False)
    embed.set_author(name= "About this bot")
    embed.set_thumbnail(url=user.avatar.url)
    embed.set_footer(text=f"By: {str(ctx.author)}")
    await ctx.send(embed=embed)

@bot.command(aliases=["kuji"])
async def fortune(ctx):
    result = [":clap: 大吉", ":wink: 吉", ":sweat_smile: 中吉", ":smirk: 小吉", ":sweat: 凶", ":joy::thumbsup: 大凶"]
    embed= discord.Embed(title=f"{random.choice(result)}", color= 0x6dc1d1)
    embed.set_footer(text= f"By: {str(ctx.author)}")
    await ctx.reply(embed=embed, mention_author= False)


@bot.command(aliases=["a"])
async def avatar(ctx, user:discord.Member=None):
    if not user: user= ctx.author
    avatar= user.display_avatar
    embed= discord.Embed(title= "Avatar Link", description= f"{user.mention}'s Avatar",  color= 0x6dc1d1, url= avatar)
    embed.set_author(name= str(user), icon_url= avatar)
    embed.set_image(url= avatar)
    embed.set_footer(text= f"By: {str(ctx.author)}")
    await ctx.send(embed= embed)

@bot.command(aliases=["b"])
async def banner(ctx, user:discord.Member=None):
    if not user:user=ctx.author
    user = await bot.fetch_user(user.id)
    banner_url = user.banner.url
    avatar=user.display_avatar
    e=discord.Embed(title= "Banner Link", description= f"{user.mention}'s Banner",  color= 0x6dc1d1, url= banner_url)
    e.set_author(name= str(user), icon_url= avatar)
    e.set_image(url= banner_url)
    e.set_footer(text= f"By: {str(ctx.author)}")
    await ctx.send(embed=e)
"""
@bot.command(aliases=["b"])
async def banner(ctx, user:discord.Member=None):
    if not user:user=ctx.author
    try:
        req = await bot.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
        banner_id = req["banner"]
    except:
        embed= discord.Embed(title= "Have you set banner?")
        embed.set_footer(text=str(f"By: {ctx.author}"))
        await ctx.send(embed= embed)

    if banner_id:
        banner_url_png= f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
        banner_url_gif= f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}.gif?size=1024"
        _embed= discord.Embed(title= "Banner Link", description= f"{user.mention}'s banner", color= 0x6dc1d1, url= banner_url_png)
        _embed.set_image(url= banner_url_png)
        _embed.set_footer(text= str(f"By : {ctx.author}"))
        b= Button(label="Gif",style=discord.ButtonStyle.green)
    async def button_callback(interaction):
        embed= discord.Embed(title= "Banner Link", description= f"{user.mention}'s banner", color= 0x6dc1d1, url= banner_url_gif)
        embed.set_image(url= banner_url_gif)        
        embed.set_footer(text= str(f"By : {ctx.author}"))
        await interaction.response.edit_message(embed=embed, view=None)
    b.callback= button_callback
    view=View()
    view.add_item(b)
    await ctx.send(embed=_embed, view=view)
"""


@bot.command()
async def track(ctx, user:discord.Member=None):
    if not user: user=ctx.author
    spotify_result = next((activity for activity in user.activities if isinstance(activity, discord.Spotify)), None)
    if spotify_result is None:await ctx.send(f"{user.name} is not listening to Spotify!")
    if spotify_result:await ctx.send(f"https://open.spotify.com/track/{spotify_result.track_id}")


@bot.command(aliases=["sp"])
async def spotify(ctx, user:discord.Member=None):
    if not user:user=ctx.author
    spotify_result= next((activity for activity in user.activities if isinstance(activity, discord.Spotify)), None)
    if spotify_result is None:await ctx.send(f"{user.name} is not listening to Spotify!")
    if spotify_result:
        embed=discord.Embed(title=f"{spotify_result.title}",
        color=spotify_result.color,url=f"https://open.spotify.com/track/{spotify_result.track_id}")
        embed.set_thumbnail(url=spotify_result.album_cover_url)
        embed.add_field(name="Song Title", value=f"```{spotify_result.title}```")
        artists = spotify_result.artists
        if not artists[0]: re_result=spotify_result.artist
        else: re_result = ', '.join(artists)
        embed.add_field(name="Artist[s]", value=f"```{re_result}```")
        embed.add_field(name="Album", value=f"```{spotify_result.album}```", inline=False)
        embed.add_field(name="Time", value=f"```{dateutil.parser.parse(str(spotify_result.duration)).strftime('%M:%S')}```")
        embed.add_field(name="URL", value=f"```https://open.spotify.com/track/{spotify_result.track_id}```", inline=False)
        embed.set_footer(text=f"By: {str(ctx.author)}")
        await ctx.send(embed=embed)


@bot.command()
async def test(ctx, user:discord.ClientUser=None):
    if not user:user=ctx.author
    #await ctx.send(user.)

@bot.command()
async def test_usre(ctx, user:discord.Member=None):
    if not user:user==ctx.author
    await ctx.send(user.system)

@bot.command()
async def mutual(ctx, user:discord.Member=None):
    if not user:user=ctx.author
    info = user.mutual_guilds
    for i in range(len(info)):
        await ctx.send()

@bot.command()
async def invite(ctx, id:discord.Member = None):
    if not id: id = bot.user
    #else:
        #id = str(id.replace("<@", '').strip())
        #id = str(id.replace(">", '').strip())
    b = Button(label="No permissions", url= f"https://discord.com/oauth2/authorize?client_id={id.id}&permissions=0&scope=bot%20applications.commands")
    b_2 = Button(label="Administrator", url= f"https://discord.com/oauth2/authorize?client_id={id.id}&permissions=8&scope=bot%20applications.commands")
    b_3 = Button(label="Make yourself",  url= f"https://discord.com/oauth2/authorize?client_id={id.id}&permissions=1644971949559&scope=bot%20applications.commands")
    view=View()
    view.add_item(b)
    view.add_item(b_2)
    view.add_item(b_3)
    e=discord.Embed(description=id.mention,color=0xfff87a)
    date_format="%Y/%m/%d %H:%M:%S"
    e.add_field(name=f"アカウント作成日", value=f"**`{id.joined_at.strftime(date_format)}`**")
    e.add_field(name="サーバー参加日", value= f"**`{id.joined_at.strftime(date_format)}`**")
    await ctx.send(embed=e, view=view)

@bot.command()
async def invite_(ctx, id:str):    
    b = Button(label="No permissions", url= f"https://discord.com/oauth2/authorize?client_id={id}&permissions=0&scope=bot%20applications.commands")
    b_2 = Button(label="Administrator", url= f"https://discord.com/oauth2/authorize?client_id={id}&permissions=8&scope=bot%20applications.commands")
    b_3 = Button(label="Make yourself",  url= f"https://discord.com/oauth2/authorize?client_id={id}&permissions=1644971949559&scope=bot%20applications.commands")
    view=View()
    view.add_item(b)
    view.add_item(b_2)
    view.add_item(b_3)
    await ctx.send("a", view=view)

@bot.command(aliases=["acc"])
async def account(ctx, user:discord.Member=None):
    if not user:user=ctx.author
    date_format="%Y/%m/%d %H:%M:%S"
    e = discord.Embed()
    e.set_author(name=ctx.author, url=user.avatar.url)
    e.add_field(name=f"アカウント作成日", value=f"**`{user.joined_at.strftime(date_format)}`**")
    e.add_field(name="サーバー参加日", value= f"**`{user.joined_at.strftime(date_format)}`**")
    e.set_thumbnail(url=user.avatar.url)
    e.set_footer(text= f"By: {str(ctx.author)}")
    await ctx.send(embed=e)

@bot.command(aliases=["ui"])
async def userinfo(ctx, user:discord.Member= None):
    if not user: user= ctx.author
    date_format="%Y/%m/%d"
    embed= discord.Embed(title= f"{user}", description= f"**ID : `{user.id}`**", color= 0x6dc1d1)
    embed.set_thumbnail(url=user.display_avatar)
    embed.add_field(name= "Name", value= f"> `{user}`",inline= True)
    embed.add_field(name= "Nickname", value= f"> `{user.display_name}`", inline= True)
    embed.add_field(name= "Bot...?", value= f"> `{user.bot}`", inline= True)
    
    if len(user.roles) >= 1:
        role_string = " ".join([r.mention for r in user.roles][1:])
        #role_string = " ".join([r.mention for r in user.roles])
        embed.add_field(name= f"Roles `{len(user.roles)-1}`", value= role_string, inline=False)
    embed.add_field(name= "Createion Account", value= f"> `{user.created_at.strftime(date_format)}`", inline= True)
    embed.add_field(name= "Joined Server", value= f"> `{user.joined_at.strftime(date_format)}`", inline= True)
    try:
        req= await bot.http.request(discord.http.Route("GET", "/users/{uid}", uid= user.id))
        banner_id= req["banner"]
        if banner_id:
            banner_url= f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
            embed.set_image(url=banner_url)
            embed.set_footer(text= f"By: {str(ctx.author)}  [Banner is png file]")
    except:
        embed.set_footer(text= f"By: {str(ctx.author)}")    
    await ctx.send(embed= embed)


@bot.command(aliases=["si"])
async def serverinfo(ctx):
    guild= ctx.guild
    date_f= "%Y/%m/%d"
    region= str(guild.region)
    mcount= str(guild.member_count)
    ucount= str(sum(1 for member in guild.members if not member.bot))
    bcount= str(sum(1 for member in guild.members if member.bot))
    tchannels= len(guild.text_channels)
    vchannels= len(guild.voice_channels)
    categories= len(guild.categories)
    roles= [role for role in guild.roles]
    emojis= [emoji for emoji in guild.emojis]
    embed= discord.Embed(title=f"{guild.name} information", description= f"**Server id : `{guild.id}`**", color= 0x6dc1d1)
    embed.set_thumbnail(url= guild.icon.url)
    embed.add_field(name= "Owner", value= f"> {guild.owner.mention}")
    embed.add_field(name= "Region", value= f"> `{region}`")
    embed.add_field(name= "Emojis", value= f"> Emojis: `{len(emojis)}`")
    embed.add_field(name= "Boost", 
                    value= f"> boost **:** `{guild.premium_subscription_count}`\n> Tier **:** `{guild.premium_tier}`")
    embed.add_field(name= "Roles", value= f"> Role **:** `{len(roles)}`", inline= True)
    embed.add_field(name= "Createion", value= f"> `{guild.created_at.strftime(date_f)}`", inline=True)
    embed.add_field(name= "Members", value= f"> Member **:** `{mcount}`\n> User: `{ucount}`\n> Bot: `{bcount}`")
    embed.add_field(name= "Channels", 
                    value= f"> Channel **:** `{tchannels+vchannels}`\n> Text **:** `{tchannels}`\n> Voice **:** `{vchannels}`\n> Category **:** `{categories}`",inline= True)
    try:
        req= await bot.http.request(discord.http.Route("GET", "/guilds/{sid}", sid= guild.id))
        banner_id= req["banner"]
        if banner_id:
            banner_url= f"https://cdn.discordapp.com/banners/{guild.id}/{banner_id}.png?size=1024"
            embed.set_image(url= banner_url)
            embed.set_footer(text= f"By: {str(ctx.author)} ・Banner is png file")
    except:
        embed.set_footer(text= f"By: {str(ctx.author)}")
    await ctx.send(embed= embed)

@bot.command(aliases=["sb"])
async def serverbanner(ctx):
    try:
        guild=ctx.guild
        req= await bot.http.request(discord.http.Route("GET", "/guilds/{sid}", sid= guild.id))
        banner_id= req["banner"]
        if banner_id:
            banner_url_png= f"https://cdn.discordapp.com/banners/{guild.id}/{banner_id}.png?size=1024"
            banner_url_gif= f"https://cdn.discordapp.com/banners/{guild.id}/{banner_id}.gif?size=1024"
            _embed= discord.Embed(title= "Banner Link", description= f"{guild.name} banner", color= 0x6dc1d1, url= banner_url_png)
            _embed.set_image(url= banner_url_png)
            _embed.set_footer(text= f"By: {str(ctx.author)} ・Banner is png file")
            b= Button(label="Gif",style=discord.ButtonStyle.green)
        
        async def button_callback(interaction):
            embed= discord.Embed(title= "Banner Link", description= f"{guild.name} banner", color= 0x6dc1d1, url= banner_url_gif)
            embed.set_image(url= banner_url_gif)        
            embed.set_footer(text= str(f"By : {ctx.author}"))
            await interaction.response.edit_message(embed=embed, view=None)
        b.callback= button_callback
        view=View()
        view.add_item(b)
        await ctx.send(embed=_embed, view=view)
    except:
        embed= discord.Embed(title= "Have you set banner?")
        embed.set_footer(text=str(f"By: {ctx.author}"))
        await ctx.send(embed= embed)

@bot.command()
async def register_(ctx, user:discord.Member, reason=None):
    register_json = {
        "name":user,
        "id":user.id,
        "reason":reason
    }
    with open("person.json", "a"):
        txt = json.dump()

@bot.event
async def on_command_error(ctx, error):
        if isinstance(error, discord.ext.commands.errors.MissingPermissions):
            embed = discord.Embed(title="-MissingPermissions", \
                description=f"権限不足ですよ。出直せバカ", timestamp=ctx.message.created_at, color=0xff0000)
            await ctx.send(embed=embed)
        elif isinstance(error, discord.ext.commands.errors.BotMissingPermissions):
            embed = discord.Embed(title="-BotMissingPermissions", \
            description=f"当botの権限が不当に制限されています。信用ないならなぜ入れたんです？", timestamp=ctx.message.created_at, color=0xff0000)
            await ctx.send(embed=embed)
        #elif isinstance(error, discord.ext.commands.errors.CommandNotFound):
        #    embed = discord.Embed(title="-CommandNotFound", \
        #    description=f"コマンドが見つかりませんでした。今一度`.help`で確認なさってください。", timestamp=ctx.message.created_at, color=0xff0000)
        #    await ctx.send(embed=embed)
        elif isinstance(error, discord.ext.commands.errors.MemberNotFound):
            embed = discord.Embed(title="-MemberNotFound", \
                description=f"指定されたユーザーが発見されませんでした。", timestamp=ctx.message.created_at, color=0xff0000)
            await ctx.send(embed=embed)
        elif isinstance(error, discord.ext.commands.errors.BadArgument):
            embed = discord.Embed(title="-BadArgument", \
            description=f"指定された引数がエラーを起こしているため実行出来ません。", timestamp=ctx.message.created_at, color=0xff0000)
            await ctx.send(embed=embed) 
        elif isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            embed = discord.Embed(title="-BadArgument", \
            description=f"必要な引数が足りません。", timestamp=ctx.message.created_at, color=0xff0000)
            await ctx.send(embed=embed)
        elif isinstance(error,discord.ext.commands.errors.MissingRole):
            embed = discord.Embed(title="-MissingRole", \
            description=f"ロール持ってないからだめよ", timestamp=ctx.message.created_at, color=0xff0000)
            await ctx.send(embed=embed)
        elif isinstance(error, discord.ext.commands.errors.CheckFailure):
            embed = discord.Embed(title="-CheckFailure", \
            description=f"Something error: \ndm only or Dev only command", timestamp=ctx.message.created_at, color=0xff0000)
            await ctx.send(embed=embed)
        else:raise error


bot.run()
