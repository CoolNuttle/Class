import os
import discord
import random
from discord.ext import commands, tasks
from itertools import cycle
from keep_alive import keep_alive

client = commands.Bot(command_prefix = '$')
client.remove_command('help')

status = cycle(['$tictactoe', '$help'])

@client.event
async def on_ready():
  change_status.start()
  print('Bismillah, Class is Ready Sir!')

@tasks.loop(seconds=10)
async def change_status():
  await client.change_presence(activity=discord.Game(next(status)))

@client.event
async def on_member_join(member):
  print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
  print(f'{member} has left the server.')

@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! Ping: {round(client.latency * 1000)}ms')

@client.command(pass_context=True)
async def help(ctx):

  embed = discord.Embed(
    title = "Help",
    description = "This is a bot made by CoolNuttle#0001. It is exclusive for SMP Muhammadiyah PK, especially for 11'th generation. Go read below, to see more features!",
    colour = discord.Colour.blue()
  )

  embed.add_field(name='$schedule/sched <class>', value='See ur Schedule!', inline=False)
  embed.add_field(name='$zoom', value='See zoom links!', inline=False)
  embed.add_field(name='$invite', value='Invite bot to your server!', inline=False)
  embed.add_field(name='$tictactoe <@player 1> <@player 2>', value='Play tictactoe game with your friend!')
  embed.set_footer(text='CoolNuttle#0001 | Feel free to ask!')

  await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=2):
  await ctx.channel.purge(limit=amount)

#@client.command()
#async def kick(ctx, member : discord.Member, *, reason=None):
#  await member.kick(reason=reason)
#  await ctx.send(f'Kicked {member.mention}')

#@client.command()
#async def ban(ctx, member : discord.Member, *, reason=None):
#  await member.ban(reason=reason)
#  await ctx.send(f'Banned {member.mention}')

#@client.command()
#async def unban(ctx, *, member):
#  banned_users = await ctx.guild.bans()
#  member_name, member_discriminator = member.split('#')

#  for ban_entry in banned_users:
#    user = ban_entry.user
#
#    if (user.name, user.discriminator) == (member_name, member_discriminator):
#      await ctx.guild.unban(user)
#      await ctx.send(f'Unbanned {user.mention}')
#      return

@client.command(pass_context=True)
async def invite(ctx, arg=None):
    if arg == 'Tas':
      embed = discord.Embed(
        title = 'Tas',
        colour = discord.Colour.blue()
      )

      embed.set_footer(text='CoolNuttle#0001 | Feel free to ask!')
      embed.add_field(name='Link', value='https://discord.com/api/oauth2/authorize?client_id=841155881054765066&permissions=8&scope=bot')
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/852913207193370665/882508479678545920/menggokil.png')

      await ctx.send(embed=embed)
      return

    if arg == 'tas':
      embed = discord.Embed(
        title = 'Tas',
        colour = discord.Colour.blue()
      )

      embed.set_footer(text='CoolNuttle#0001 | Feel free to ask!')
      embed.add_field(name='Link', value='https://discord.com/api/oauth2/authorize?client_id=841155881054765066&permissions=8&scope=bot')
      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/852913207193370665/882508479678545920/menggokil.png')

      await ctx.send(embed=embed)
      return

    if arg == 'Class':
      embed = discord.Embed(
        title = 'Class',
        colour = discord.Colour.blue()
      )

      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/859234833774936084/882489176036093982/download.png')
      embed.set_footer(text='CoolNuttle#0001 | Feel free to ask!')
      embed.add_field(name='Link', value='https://discord.com/api/oauth2/authorize?client_id=864783083777949697&permissions=8&scope=bot')

      await ctx.send(embed=embed)
      return

    if arg == 'class':
      embed = discord.Embed(
        title = 'Class',
        colour = discord.Colour.blue()
      )

      embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/859234833774936084/882489176036093982/download.png')
      embed.set_footer(text='CoolNuttle#0001 | Feel free to ask!')
      embed.add_field(name='Link', value='https://discord.com/api/oauth2/authorize?client_id=864783083777949697&permissions=8&scope=bot')

      await ctx.send(embed=embed)

    if arg == None:
      embed = discord.Embed(
        title = 'Invite',
        colour = discord.Colour.blue()
      )

      embed.add_field(name='Class', value='$invite Class', inline=False)
      embed.add_field(name='Tas', value='$invite Tas', inline=False)
      embed.set_footer(text='CoolNuttle#0001 | Feel free to ask!')

      await ctx.send(embed=embed)
    
    else:
      await ctx.send('Please Type a Specific Command!')

@client.command()
async def test(ctx):
  await ctx.send('https://cdn.discordapp.com/attachments/865401732934270996/882156147954581535/unknown.png')

@client.command(pass_context=True)
async def sched(ctx, arg=None):
  if arg == '8a':
    await ctx.send('https://cdn.discordapp.com/attachments/859234833774936084/864701872731586620/unknown.png')
    return

  if arg == '8b':
    await ctx.send('https://cdn.discordapp.com/attachments/859234833774936084/864701956575723530/unknown.png')
    return

  if arg == '8c':
    await ctx.send('https://cdn.discordapp.com/attachments/859234833774936084/864702035545817138/unknown.png')

  if arg == None:
    embed = discord.Embed(
      title = 'Schedule',
      colour = discord.Colour.blue()
    )

    embed.add_field(name='8A', value='$sched/schedule 8a', inline=False)
    embed.add_field(name='8B', value='$sched/schedule 8b', inline=False)
    embed.add_field(name='8C', value='$sched/schedule 8c', inline=False)
    embed.set_footer(text='CoolNuttle#0001 | Feel free to ask!')

    await ctx.send(embed=embed)

  else:
    await ctx.send('Please Type a Specific Command!')

@client.command(pass_context=True)
async def schedule(ctx, arg=None):
  if arg == '8a':
    await ctx.send('https://cdn.discordapp.com/attachments/859234833774936084/864701872731586620/unknown.png')
    return

  if arg == '8b':
    await ctx.send('https://cdn.discordapp.com/attachments/859234833774936084/864701956575723530/unknown.png')
    return

  if arg == '8c':
    await ctx.send('https://cdn.discordapp.com/attachments/859234833774936084/864702035545817138/unknown.png')

  if arg == None:
    embed = discord.Embed(
      title = 'Schedule',
      colour = discord.Colour.blue()
    )

    embed.add_field(name='8A', value='$sched/schedule 8a', inline=False)
    embed.add_field(name='8B', value='$sched/schedule 8b', inline=False)
    embed.add_field(name='8C', value='$sched/schedule 8c', inline=False)
    embed.set_footer(text='CoolNuttle#0001 | Feel free to ask!')

    await ctx.send(embed=embed)

  else:
    await ctx.send('Please Type a Specific Command!')

@client.command()
async def zoom(ctx, arg=None):
  if arg == None:
    embed = discord.Embed(
      title = 'Zoom Links',
      colour = discord.Colour.blue()
  )

    embed.add_field(name='UST SUKMA', value='$zoom sukma', inline=False)
    embed.add_field(name='PAI', value='$zoom pai', inline=False)
    embed.add_field(name='BAHASA INGGRIS', value='$zoom bing', inline=False)
    embed.add_field(name='KEMUHAMMADIYAHAN', value='$zoom kemuh', inline=False)
    embed.add_field(name='PRAKARYA', value='$zoom prakar', inline=False)
    embed.add_field(name='MATEMATIKA', value='$zoom mat', inline=False)
    embed.add_field(name='BAHASA INDONESIA', value='$zoom bindo', inline=False)
    embed.add_field(name='SAINS RISET', value='$zoom saset', inline=False)
    embed.add_field(name='PJOK', value='$zoom pjok', inline=False)
    embed.add_field(name='PKN', value='$zoom pkn', inline=False)
    embed.add_field(name='BIMBINGAN KONSELING', value='$zoom bk', inline=False)
    embed.add_field(name='BAHASA JAWA', value='$zoom bjawa', inline=False)
    embed.add_field(name='BIOLOGI', value='$zoom bio', inline=False)
    embed.add_field(name='SENI BUDAYA', value='$zoom pai', inline=False)
    embed.add_field(name='FISIKA', value='$zoom fis', inline=False)
    embed.add_field(name='INFORMATIKA', value='$zoom infor', inline=False)
    embed.add_field(name='IPS', value='$zoom ips', inline=False)
    embed.set_footer(text='CoolNuttle#0001 | Feel free to ask!')

    await ctx.send(embed=embed)
    return

  if arg == 'sukma':
    embed = discord.Embed(
      colour = discord.Colour.blue(),
      title = 'Ust Sukma',
      description = 'Sukma (IPA Fisika)\nJoin Zoom Meeting\nhttps://zoom.us/j/3392044063?pwd=WlJsTkJuUFZPWHl4WjMvRHpUQ3ZHdz09\nMeeting ID: 339 204 4063\nPasscode: Sainsklub'
    )

    embed.set_footer(text='CoolNuttle#0001 | Feel free to ask!')

    await ctx.send(embed=embed)
    return

  if arg == 'pai':
    embed = discord.Embed(
      colour = discord.Colour.blue(),
      title = 'PAI',
      description = 'Ustadz. Muhammad Arif Wicagsono (PAI)\n🏷️ Join Zoom Meeting\nhttps://us04web.zoom.us/j/9461348187?pwd=MzZETTJrWENZeEQzYWI5MzdlZ2xUQT09\nMeeting ID: 946 134 8187\nPasscode: bismillah'
    )

    embed.set_footer(text='CoolNuttle#0001 | Feel free to ask!')

    await ctx.send(embed=embed)
    return

  if arg == 'bing':
    embed = discord.Embed(
      colour = discord.Colour.blue(),
      title = 'BAHASA INGGRIS',
      description = 'Muhammad Dafit Pitoyo (B. Inggris)\nJoin Zoom Meeting\nhttps://zoom.us/j/2486822599?pwd=TldvREhBN2NDZW1rdTM1Q3Y1dDNIZz09\nMeeting ID: 248 682 2599\nPasscode: BigBang'
    )

    embed.set_footer(text='CoolNuttle#0001 | Feel free to ask!')

    await ctx.send(embed=embed)
    return

  if arg == 'kemuh':
    embed = discord.Embed(
      colour = discord.Colour.blue(),
      title = 'KEMHUAMMADIYAHAN',
      description = 'Heru Hadiyono is inviting you to a scheduled Zoom meeting\nTopic: Kemuhammadiyahan\nTime: Jul 25, 2021 06:00 AM Jakarta\nJoin Zoom Meeting\nhttps://zoom.us/j/3603125218?pwd=cEJPZzBKTFhFQUtJVWRpTDB2WVFOdz09\nMeeting ID: 360 312 5218\nPasscode: bismillah'
    )

    embed.set_footer(text='CoolNuttle#0001 | Feel free to ask!')

    await ctx.send(embed=embed)
    return

  if arg == 'prakar':
    embed = discord.Embed(
      colour = discord.Colour.blue(),
      title = 'PRAKARYA',
      description = 'Heru Hadiyono is inviting you to a scheduled Zoom meeting\nTopic: Kemuhammadiyahan\nTime: Jul 25, 2021 06:00 AM Jakarta\nJoin Zoom Meeting\nhttps://zoom.us/j/3603125218?pwd=cEJPZzBKTFhFQUtJVWRpTDB2WVFOdz09\nMeeting ID: 360 312 5218\nPasscode: bismillah'
  )

    embed.set_footer(text='CoolNuttle#0001 | Feel free to ask!')

    await ctx.send(embed=embed)
    return

  if arg == 'mat':
    embed = discord.Embed(
      colour = discord.Colour.blue(),
      title = 'MATEMATIKA',
      description = 'Assalamualaikum wr.wb anak-anak, untuk pembelajaran matematika kelas 8B hari ini menggunakan link berikut yaa SMP Muh PK 027 is inviting you to a scheduled Zoom meeting\nJoin Zoom Meeting\nhttps://zoom.us/j/94942382002?pwd=SENpNng5RWJTL0ZudnVWZlQ3dTNCdz09\nMeeting ID: 949 4238 2002\nPasscode: mathasik\nterimakasih☺️'
    )

    embed.set_footer(text='CoolNuttle#0001 | Feel free to ask!')

    await ctx.send(embed=embed)
    return

  if arg == 'bindo':
    embed = discord.Embed(
      colour = discord.Colour.blue(),
      title = 'BAHASA INDONESIA',
      description = 'Dyah Ayu Fajar Utami (Bahasa Indonesia) \nJoin Zoom Meeting\nhttps://us05web.zoom.us/j/2816072839?pwd=T0Y4SVNGcXpUTDB2dnhOQmF2Y05ZZz09\nMeeting ID: 281 607 2839\nPasscode: BINDO8'
    )

    embed.set_footer(text='CoolNuttle#0001 | Feel free to ask!')

    await ctx.send(embed=embed)
    return

  if arg == 'saset':
    embed = discord.Embed(
      colour = discord.Colour.blue(),
      title = 'SAINS RISET',
      description = 'Us Puji Harmisih (Sains Riset)\nJoin Zoom Meeting\nhttps://zoom.us/j/5197260159?pwd=dlFwYVBSNE0veDJnQ3lQNlg1TW03dz09\nMeeting ID: 519 726 0159\nPasscode: smppk'
    )

    embed.set_footer(text='CoolNuttle#0001 | Feel free to ask!')

    await ctx.send(embed=embed)
    return

  if arg == 'pjok':
    embed = discord.Embed(
      colour = discord.Colour.blue(),
      title = 'PJOK',
      description = 'Us Cahya (PJOK)\nJoin Zoom Meeting\nhttps://us04web.zoom.us/j/7616841193?pwd=eE1vNGo3dlY1ZllkQ2RxRTV5RW9vZz09\nMeeting ID: 761 684 1193\nPasscode: pjokasik'
    )

    embed.set_footer(text='CoolNuttle#0001 | Feel free to ask!')

    await ctx.send(embed=embed)
    return

  if arg == 'pkn':
    embed = discord.Embed(
      colour = discord.Colour.blue(),
      title = 'PKN',
      description = 'Us solikhin PKn\nTopic: pembelajaran pkn kelas 8\nTime: This is a recurring meeting Meet anytime\nJoin Zoom Meeting\nhttps://us04web.zoom.us/j/73843566081?pwd=SUZYM0RCU2JydlVMdkJaUnJUSSsrdz09\nMeeting ID: 738 4356 6081\nPasscode: bismillah'
    )

    embed.set_footer(text='CoolNuttle#0001 | Feel free to ask!')

    await ctx.send(embed=embed)
    return

  if arg == 'bk':
    embed = discord.Embed(
      colour = discord.Colour.blue(),
      title = 'BIMBINGAN KONSELING',
      description = 'Us. Sofi Maharani BK\nJoin Zoom Meeting\nhttps://us04web.zoom.us/j/5811585847?pwd=T0NxbEdaN2JpOG5hYXVKV2RtTHF0dz09\nMeeting ID: 581 158 5847\nPasscode: kelasBK'
    )

    embed.set_footer(text='CoolNuttle#0001 | Feel free to ask!')

    await ctx.send(embed=embed)
    return

  if arg == 'bjawa':
    embed = discord.Embed(
      colour = discord.Colour.blue(),
      title = 'BAHASA JAWA',
      description = 'Us Laili (Bahasa Jawa)\nJoin Zoom Meeting\nhttps://zoom.us/j/4109520827?pwd=VnVpVnNGeTA0TVJDUVhCSUFPaVl4dz09\nMeeting ID: 410 952 0827\nPasscode: d1jp39'
    )

    embed.set_footer(text='CoolNuttle#0001 | Feel free to ask!')

    await ctx.send(embed=embed)
    return

  if arg == 'bio':
    embed = discord.Embed(
      colour = discord.Colour.blue(),
      title = 'BIOLOGI',
      description = 'Ichsan Widayanto( biologi\nJoin Zoom Meeting\nhttps://us04web.zoom.us/j/8957446941?pwd=YzhzdmcxRkE0ZmJNS2JLSDNPbnZPQT0\nMeeting ID: 895 744 6941\nPasscode: bismillah'
    )

    embed.set_footer(text='CoolNuttle#0001 | Feel free to ask!')

    await ctx.send(embed=embed)
    return

  if arg == 'senbud':
    embed = discord.Embed(
      colour = discord.Colour.blue(),
      title = 'SENI BUDAYA',
      description = 'Topic: Seni Budaya 8B\nTime: Jul 15, 2021 08:45 AM Jakarta\nJoin Zoom Meeting\nhttps://us04web.zoom.us/j/71643830613?pwd=Um91dHB0eGlJSUR6bkM2K1V1VGhtQT09\nMeeting ID: 716 4383 0613\nPasscode: senbud'
    )

    embed.set_footer(text='CoolNuttle#0001 | Feel free to ask!')

    await ctx.send(embed=embed)
    return

  if arg == 'fis':
    embed = discord.Embed(
      colour = discord.Colour.blue(),
      title = 'FISIKA',
      description = 'Us Nurul (Fisika)\nhttps://zoom.us/j/4204454709?pwd=cEF0YTltWEZzRFJMMFQrK2NrUzhFZz09\nMeeting ID: 420 445 4709\nPasscode: PKCERDAS'
    )

    embed.set_footer(text='CoolNuttle#0001 | Feel free to ask!')

    await ctx.send(embed=embed)
    return

  if arg == 'infor':
    embed = discord.Embed(
      colour = discord.Colour.blue(),
      title = 'INFORMATIKA',
      description = 'Informatika pak.zul\nJoin Zoom Meeting\nhttps://zoom.us/j/7455032585?pwd=azRzUXk1STBJR0Q0L1Q0djVVTVVqdz09\nMeeting ID: 745 503 2585\nPasscode: muhpk'
    )

    embed.set_footer(text='CoolNuttle#0001 | Feel free to ask!')

    await ctx.send(embed=embed)
    return

  if arg == 'ips':
    embed = discord.Embed(
      colour = discord.Colour.blue(),
      title = 'IPS',
      description = 'Ust Rozak (Ips)\nJoin zoom meeting\nhttps://us04web.zoom.us/j/9309963049?pwd=cU1GYXNYMlJUQXh2VGlIMEl3T3FOZz09\nMeeting ID : 930 996 3049\nPasscode : bismillah'
    )

    embed.set_footer(text='CoolNuttle#0001 | Feel free to ask!')

    await ctx.send(embed=embed)

  else:
    await ctx.send('Please Type a Specific Command!')

#======================================================
# Game

player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
  [0, 1, 2],
  [3, 4, 5],
  [6, 7, 8],
  [0, 3, 6],
  [1, 4, 7],
  [2, 5, 8],
  [0, 4, 8],
  [2, 4, 6]
]

@client.command()
async def tictactoe(ctx, p1 : discord.Member, p2 : discord.Member):
  global player1
  global player2
  global turn
  global gameOver
  global count

  if gameOver:
    global board
    board = [":white_large_square:", ":white_large_square:",":white_large_square:", 
    ":white_large_square:", ":white_large_square:",":white_large_square:", 
    ":white_large_square:", ":white_large_square:", ":white_large_square:"]
    turn = ""
    gameOver = False
    count = 0

    player1 = p1
    player2 = p2

    #print the board
    line = ""
    for x in range(len(board)):
      if x == 2 or x == 5 or x == 8:
        line += " " + board[x]
        await ctx.send(line)
        line = ""
      else:
          line += " " + board[x]

    #determine who goes first
    num = random.randint(1, 2)
    if num == 1:
      turn = player1
      await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
    if num == 2:
      turn = player2
      await ctx.send("It is <@" + str(player2.id) + ">'s turn.")

  else:
    await ctx.send("A game was already in progress! Finish it before starting a new game.")

@client.command()
async def place(ctx, pos : int):
  global turn
  global player1
  global player2
  global board
  global count

  if not gameOver:
      mark = ""
      if turn == ctx.author:
        if turn == player1:
          mark = ":regional_indicator_x:"
        elif turn == player2:
          mark = ":o2:"
        if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
          board[pos - 1] = mark
          count += 1

          # Print Board
          line = ""
          for x in range(len(board)):
              if x == 2 or x == 5 or x == 8:
                  line += " " + board[x]
                  await ctx.send(line)
                  line = ""
              else:
                  line += " " + board[x]

          checkWinner(winningConditions, mark)
          if gameOver:
            await ctx.send(mark + "wins!")
          elif count >= 9:
            await ctx.send("It's a tie!")

          # switch turns
          if turn == player1:
            turn = player2
          elif turn == player2:
            turn = player1

        else:
          await ctx.send("Be sure to chose an integer between 1 and 9 (inclusive) and an unmarked tile.")
      else:
          await ctx.send("It is not your turn.")
  else:
    await ctx.send("Please start a new game with $tictactoe command.")

def checkWinner(winningConditions, mark):
  global gameOver
  for condition in winningConditions:
    if board[condition[0]] == mark and board [condition[1]] == mark and board[condition[2]] == mark:
      gameOver = True

@tictactoe.error
async def tictactoe_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Please mention 2 players for this command.")
  elif isinstance(error, commands.BadArgument):
    await ctx.send("Please make sure to mention/ping players (ie. <@841847405988020244>).")

@place.error
async def place_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("Please enter a position you would like to mark.")
  elif isinstance(error, commands.BadArgument):
    await ctx.send("Please make sure to enter an integer.")

@client.command()
async def end(ctx):
  global gameOver
  if not gameOver:
    gameOver = True
    await ctx.send("Stopping current game...")
  else:
    await ctx.send("There is currently no game running!")

        
keep_alive ()
client.run(os.getenv('TOKEN'))
