import discord
import asyncio
import random
from discord.utils import get
from discord.voice_client import VoiceClient
from discord.ext import commands
import translate
import re
import time
from urllib import parse, request
from translate import Translator
#from os import listdir
import os
import youtube_dl
#from os.path import isfile, join
bot = commands.Bot(command_prefix = '-', help_command = None)
token = 'NzExNjc1NjA0MDI5ODAwNDY4.Xs9zAQ.L5zEQwgoqtgTkBFohCKXG1m5q7M'
stat = 'SMOKING WEED'
list_music = []
@bot.event
async def on_ready():
	print("Hello i'm {}".format(bot.user))
	await bot.change_presence(activity=discord.Game(stat), status= discord.Status.online , afk = False)
#		if not discord.opus.is_loaded():
#		discord.opus.load_opus()
@bot.event
async def on_message(message):
	print(message.author, "says :", message.content)
	await bot.process_commands(message)
	if message.content == '<@711675604029800468>':
		await message.channel.send("QUE QUIERES PUTA?")

@bot.command(pass_context = True, aliases = ["Help", "Ayuda", "ayuda"])
async def help(ctx):
	await ctx.send("ingles + texto")

@bot.command()
async def ingles(ctx,*, arg):
	print(arg)
	idioma = Translator(from_lang = "spanish", to_lang = "english")
	end = idioma.translate(arg)
	await ctx.send(end)

@bot.command()

async def youtube(ctx, *, arg):

	string = parse.urlencode({'search_query': arg })
	contenido = request.urlopen('http://youtube.com/results?' + string)
	resultado = re.findall('href=\"\\/watch\\?v=(.{11})', contenido.read().decode())
	rest = "http://youtube.com/watch?v=" + resultado[0]
	return rest
	await ctx.send(rest)


'''
@bot.command(aliases = ['j', 'Join', 'enter', 'in'])

async def join(ctx):
	try:
		pj = ctx.message.author
		channel = pj.voice.channel
		vc = await channel.connect()
	#	musica = join("./song.mp3")
		await ctx.send("```SUCCESSFULLY CONNECTED TO {}```".format(channel))
	#	vc.play(discord.FFmpegPCMAudio('./song.mp3'), after=lambda e: print('done', e))

	except discord.errors.ClientException:
		await ctx.send("```ALREADY IN A VOICE CHANNEL```")

	except AttributeError:
		await ctx.send("``NOT IN A VOICE CHANNEL``")
'''
@bot.command(aliases = ['salir', 'Leave', 'Exit', 'exit', 'l'])

async def leave(ctx):

	author = ctx.message.author
#	channel = author.voice.channel
	try:
		channel = ctx.message.author.voice.channel
		voice = get(bot.voice_clients, guild = ctx.guild)
		await voice.disconnect()
		await ctx.send("```SUCCESSFULLY DISCONNECTED OF {}```".format(channel))
	except AttributeError:
		await ctx.send("```IM NOT IN A CHANNEL```")
@bot.command(aliases = ['Play', 'p', 'P'])

async def play(ctx, *, name):
#	if not discord.opus.is_loaded():
#song = os.path.isfile('./song.mp3')
#		raise RunTimeError('Opus failed to load')
	canal = ctx.message.author.voice.channel
	voz  = get(bot.voice_clients, guild = ctx.guild)
	name = name
	url = get_link(name)
	if voz == None or voz != None:
		try:

			await canal.connect()
			embed_cn = discord.Embed(title = "Info", color = 0x07ca00)
			embed_cn.add_field(name ="STATUS", value = "SUCCESSFULLY CONNECTED TO {} CHANNEL".format(canal), inline = True)
			await ctx.send(embed = embed_cn)
			voz = get(bot.voice_clients, guild = ctx.guild)
		except:
			print("YA ESTABA EN VOZ")
		if not voz.is_playing() and not voz.is_paused():
			song = os.path.isfile('./song.mp3')
			url = get_link(name)
			if song:
				print("Eliminando")
				os.remove('./song.mp3')
			vc = ctx.message.author.voice.channel
			voice = get(bot.voice_clients, guild = ctx.guild)
			if voice == None:
				await vc.connect()
				embed_c = discord.Embed(title = "INFO", color = 0x07ca00)
				embed_c.add_field(name = "Status", value ="SUCCESFULLY CONNECTED TO {} CHANNEL".format(vc))
				await ctx.send(embed=embed_c)
				voice = get(bot.voice_clients, guild = ctx.guild)
			else:
				print("Se intento conectar a un canal , pero ya estaba coenctado")
#	if not discord.opus.is_loaded():
#		discord.opus.load_opus()
			#	await ctx.send("I WILL PLAY THE SONG IN A FEW SECONDS")
#vc.play(discord.FFmpegPCMAudio('testing.mp3'), after=lambda e: print('done', e))
			ydl_opts = {
       			 'format': 'bestaudio/best',
			 'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
                         'noplaylist': True,
    			 'nocheckcertificate': True, # 'postprocessors': [{
    		         'ignoreerrors': False, # 'key': 'FFmpegExtractAudio',
   			 'logtostderr': False, # 'preferredcodec': 'mp3',
  			 'quiet': True, # 'preferredquality': '192',	
 			 'no_warnings': True,
    			 'key': 'FFmpegMetadata',
  			 'default_search': 'auto', # 'quiet': True,
   			 'source_address': '0.0.0.0', # }],
  			 'usenetrc': True
			 }
			with youtube_dl.YoutubeDL(ydl_opts) as ydl:
				print("Downloading audio now\n")
				ydl.download([url])
				info_dict = ydl.extract_info(url, download=False)
				video_title = info_dict.get('title', None)
			for file in os.listdir("./"):
				if file.endswith(".m4a") or file.endswith(".webm"):
					name = file
					print(f"Renamed File: {file}\n")
					os.rename(file, "song.mp3")
			fin = bot.get_cog(end)
			next = 0
			def final():
				print(len(list_music))
				if len(list_music) > 0:

					voice.play(discord.FFmpegPCMAudio("{}.mp3".format(list_music[0])), after = lambda e: final())
					voice.source = discord.PCMVolumeTransformer(voice.source)
					voice.source.volume = 00.100
				#	await bot.change_presence(activity=discord.Game(list_music[0]), status = discord.Status.online, afk = False)
				#	ctx.send("PLAYING NEXT QUEUE SONG: {}".format(list_music[0]))
#				del list_music[0]
				#	try:
					#	for file in os.listdir("./"):
					#	os.remove("{}.mp3".format(list_music[0]))
			#	except PermissionError:
			#		print("STILL PLAYING")
					del list_music[0]
				else:
				#	await bot.change_presence(activity=discord.Game("SMOKING WEED"), status = discord.Status.online, afk = False)
					for file in os.listdir("./"):
						if file.endswith(".mp3"):
							os.remove(file)
							print("SE REMOVIO TODAA QUEUE")
			voice.play(discord.FFmpegPCMAudio("song.mp3"), after=lambda e: final())
			voice.source = discord.PCMVolumeTransformer(voice.source)
			voice.source.volume = 00.100
			nname = name.rsplit("-", 2)
			embed_playing = discord.Embed(title = "Status", color = 0x07ca00)
			embed_playing.add_field(name ="Playing", value = "[{}]({})".format(video_title, url), inline = True)
			await ctx.send(embed=embed_playing)
			print("playing\n")
			stat = video_title
		#	await bot.change_presence(activity=discord.Game(stat), status= discord.Status.online, afk = False)

		elif  voz.is_playing() or voz.is_paused():
			maxima = len(list_music)
			total = maxima -1
			embed_q = discord.Embed(title = "QUEUE", color = 0xDF0101)
			embed_q.add_field(name = "Info", value = "ALREADY PLAYNG A SONG , ADDING TO QUEUE", inline = True)
			ydl_opts = {
				'format': 'bestaudio/best',
				'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
				'noplaylist': True,
				'nocheckcertificate': True,
				'ignoreerrors': False,
				'logtostderr': False,
				'quiet': True,
				'no_warnings': True,
				'key': 'FFmpegMetaData',
				'default_search': 'auto',
				'source_address': '0.0.0.0',
				'usenetrc': True
			}
			with youtube_dl.YoutubeDL(ydl_opts) as ydl:
				print("DOWNLOADING TO QUEUE NOW")
				ydl.download([url])
				info_dict = ydl.extract_info(url, download = False)
				titulo =  info_dict.get('title', None)
			for file in os.listdir('./'):
				if file.endswith('.m4a') or file.endswith('.webm'):
					os.rename(file, '{}.mp3'.format(titulo))
					list_music.append(titulo)
					n = 0
					for i in list_music:
						n += 1
						print("{}: {}".format(n, i))
						msg = "{}: {}".format(n, i)
						i = msg
						await ctx.send("QUEUE : {}".format(msg))
			embed_q.add_field(name = "Song", value = "[{}]({})".format(titulo, url))
			await ctx.send(embed = embed_q)
@bot.command()
async def queue(ctx, url):
	channel = ctx.message.author.voice.channel
	voice = get(bot.voice_clients, guild = ctx.guild)
	if voice !=  None:
		if vc.is_playing():
			pass



@bot.command(aliases = ['pausa', 'Pause', 'paus'])

async def pause(ctx):

	vc = get(bot.voice_clients, guild =ctx.guild)
	if vc.is_playing():
		vc.pause()
		await ctx.send("Paused")

	elif vc.is_paused():
		await ctx.send("ALREADY IN PAUSE")

@bot.command()

async def resume(ctx):

	vc = get(bot.voice_clients, guild = ctx.guild)
	if vc.is_paused():
		vc.resume()
		await ctx.send("Playing Again")
	else:
		await ctx.send("NOT IN PAUSE")


@bot.command(aliases = ['Stop', 'alto', 'parar'])

async def stop(ctx):
	vc = get(bot.voice_clients, guild = ctx.guild)
	if vc != None:
		list_music.clear()
		vc.stop()
		await ctx.send("SI EXISTE UNA QUEUE , SERÁ ELIMINADA")
		await ctx.send("```SUCCESSFULLY STOPPED```")
	else:
		await ctx.send("NOT PLAYING MUSIC")



@bot.command(aliases = ['nepis', 'Nepis', 'verga', 'Verga', 'pene', 'culebra', 'snake'])

async def nepe(ctx, arg=None):
#	if arg == None:
	size = random.randint(0, 25)
	veces = 0
	if size > 12:
		color = 0x07ca0
	else:
		color = 0xdd0900
	largo = '='
	if arg == None:
		mention = ctx.message.author.mention
	else:
		all =[]
		for i in  arg:
			all.append(i)
		print(all)
		del all[0]
		del all[0]
		del all[18]
		fil = ' '
		for k in all:
			fil += k
		print (all)
		print("id ==== ", fil)
		mention = arg
	#	await ctx.send(arg)
	for i in range(size):
		largo +=  '='
	cm = len(largo)
	msg = "8{}D   {} cm".format( largo, cm)
	embed = discord.Embed(title = "Nepe Machine", color = color, description = mention)
	embed.add_field(name = "Nepe Size", value = msg)
	await ctx.send(embed = embed)
@bot.event
async def end(ctx):
	await ctx.send("MUSIC ENDS")
	for file in os.listdir("./"):
		if file.endswith(".mp3"):
			os.remove(file)
			print("SE REMOVIO: {}".format(file))

@bot.command(aliases = ['borrar', 'delete', 'Delete', 'Clear', 'Clean', 'clean'])

async def clear(ctx, msg):
	if msg != None:
#		async for x in bot.logs_from(ctx.message.channel, limit =msg):
		await ctx.message.channel.purge(limit =int( msg))
		await ctx.send('```{} MESSAGES WAS DELETED SUCCESSFULLY```'.format(msg))

@bot.command(aliases = ['next', 'siguiente', 'Skip', 'Next', 'saltar', 'Siguiente'])

async def skip(ctx):
	#voice = ctx.message.author.voice.channel
	vc = get(bot.voice_clients, guild = ctx.guild)
	if len(list_music) > 0:
		embed_sk = discord.Embed(title = "Skipped", color = 0x07ca00)
		embed_sk.add_field(name = "Playing", value = list_music[0], inline = True)
		await ctx.send(embed = embed_sk)
		vc.stop()
	elif len(list_music) == 0:
		embed_not = discord.Embed(title = "INFO", color = 0x07ca00)
		embed_not.add_field(name = "ERROR", value = "NOT SONGS IN QUEUE, STOPPING", inline = True)
		await ctx.send(embed = embed_not)
		vc.stop()
	elif vc == None:
		print("NOTNIN A VOICE CHANNEL")
		embed_error = discord.Embed(title = "Error", color =  0xdd0900)
		embed_error.add_field(name = "SORRY", value = "NOT IN A VOICE CHANNEL",  inline = True)
		await ctx.send(embed = embed_error)

def  get_link(two):
	if True:
		string = parse.urlencode({'search_query': str(two) })
		contenido = request.urlopen('http://youtube.com/results?' + string)
              #  if len(contenido) > 0:
		resultado = re.findall('href=\"\\/watch\\?v=(.{11})', contenido.read().decode())
		if len(resultado) > 0:
			rest = "http://youtube.com/watch?v=" + resultado[0]
			return rest
		else:
			get_link(str(two))
			print("****************** HACIENDO DE NUEVO LA BUSQUEDA****")
def borrar():
	for file in os.listdir("./"):
		if file.endswith(".mp3"):
			name = file
			os.remove(file)
			print(f"Removes File: {file}\n")

@bot.command(aliases = ['entrar', 'Join', 'meterse', 'Entrar'])
async def join(ctx):
        channel = ctx.message.author.voice.channel
        voice = get(bot.voice_clients, guild = ctx.guild)
        if voice == None and channel != None: # bot.run(token)
                pj = ctx.message.author
                channel = pj.voice.channel
                vc = await channel.connect()
        #       musica = join("./song.mp3")
                color = 0x12c400
                titulo = "Info"
                name = "Status:"
                msg = "SUCCESSFULLY CONNECTED TO {}".format(channel)
        #       vc.play(discord.FFmpegPCMAudio('./song.mp3'), 
        #           
        elif voice != None:
                msg = "ALREADY IN A VOICE CHANNEL"
                color = 0xdb0300
                titulo = "Info"
                name = "ERROR:"
        elif channel == None:
                msg = "NOT IN A VOICE CHANNEL"
                color = 0xdb0300
                titulo = "Info"
                name = "ERROR:"
                                                                                
        embed = discord.Embed(title = titulo, color = color)
        embed.add_field(name = name, value = msg)
        await ctx.send(embed = embed)
bot.run(token)
