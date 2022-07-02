import discord
import json
import asyncio
from discord.ext import commands
from discord.ui import View, Button, Select
intents=discord.Intents.all()
bot=commands.Bot(command_prefix=",", intents=intents)
bot.remove_command("help")

@bot.command()
@commands.has_role(991009276946419714)
async def help_(ctx):
    e=discord.Embed(
        title="深夜祭-コマンド",
        description=
        f"<@&991009276946419714>限定コマンド\n\n"
        "`help_` **:** このコマンド\n"
        "`register[reg] *(id)` **:** 憤死者リストに**登録**\n"
        "`additional[add]` **:** 憤死メンバーの情報を追加\n"
        "`show[sh]` **:** Jsonファイルの中身を表示\n"
        "`print[p]` **:** 憤死者リストを表示\n"
        "`setup_json` **:** Jsonファイルを初期化\n" 
    )
    e.add_field(name="*(id)", value="-id or mention it bot to target")
    e.set_footer(text=f"By: {ctx.author}")
    await ctx.send(embed=e)


def _load():
    with open("memberlist.json", "r") as f:info = json.load(f)
    return info

"""
def _search(keyword):
    with open("memberlist.json", "r") as f:info=json.load(f)
    return info
"""



"""Jsonファイルの初期化"""
@bot.command()
async def setup_json(ctx):
    if not ctx.author.id == 959142919573491722:return
    data_list = {"person":[]}
    with open("memberlist.json", "w", encoding="utf-8") as f:
        json.dump(data_list, f, indent=2)
    await ctx.send("ファイルのフォーマットが終了しました。")



"""Jsonファイルの中身の全体出力"""
@bot.command()
@commands.has_role(991009276946419714)
async def sh(ctx):
    with open("memberlist.json", "r") as f:
        info = f.read()
    e=discord.Embed(
        title="memberlist.json",
        description=
f"""```json
{info}```""")
    await ctx.send(embed=e)


"""Jsonにまとめられたメンバーを総出力"""
@bot.command(aliases=["p"])
@commands.has_role(991009276946419714)
async def print(ctx):
    info = _load()
    i = 0
    for i in range(len(info["person"])):
        e=discord.Embed(color=0xff0000)
        e.add_field(name= (info["person"][i]["name"]), value= 'ID: {}'.format(info["person"][i]["id"]),inline=False)
        e.add_field(name="REASON:",value="```{}```".format(info["person"][i]["reason"]),inline=True)
        e.title=f"憤死者リスト [{i+1}]"
        i += 1
        await ctx.send(embed=e)
        
"""memberlist.jsonに登録（初出力）"""
@bot.command(aliases=["reg"])
@commands.has_role(991009276946419714)
async def register(ctx, user:discord.Member, reason = None):
    if not user:await ctx.send(("登録するユーザーが指定されていません"))
    data = {
        "name":f"{user.name}#{user.discriminator}",
        "id":user.id,
        "reason": reason
    }
    info = _load()
    info["person"].append(data)
    with open("memberlist.json", "w", encoding="utf-8") as f:
        json.dump(info, f, indent=2)
        #,ensure_ascii=False
    await ctx.send("追加しました")



"""memberlist.jsonにすでにある辞書型の中から情報を追加"""
@bot.command(aliases=["add"])
@commands.has_role(991009276946419714)
async def additional(ctx, user:discord.Member):
    if not user:await ctx.send(("登録するユーザーが指定されていません"))
    with open("memberlist.json", "r") as f:
        info = json.load(f)
    data = {
        "name":f"{user.name}#{user.discriminator}",
        "id":user.id
    }
    info["person"].append(data)
    with open("memberlist.json", "w", encoding="utf-8") as f:
        json.dump(info, f, indent=2)
        #,ensure_ascii=False
    await ctx.send("追加しました。")


@bot.command(aliases=["s"])
async def search(ctx, name:discord.Member):
    info = _load()
    i = 0
    #_info = [info["person"][i] for "person" in ]



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

bot.run