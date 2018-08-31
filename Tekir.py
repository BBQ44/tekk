#Tekir by Haso
import discord
import asyncio
import logging
import random
from discord.ext.commands import Bot
from discord.ext import commands

BOT_PREFIX = "tk!"
TOKEN = "NDIzODIyMjYyNjY4NjIzODcy.DZ--vQ.IKcVC8NiqlZbLVIxOCz7btxaUsg"


@client.event
async def on_ready():
    print ("Hazırım!!!")
    print ("Başlıyorum!!! " + client.user.name)
    print ("ID: " + client.user.id) 
    await client.change_presence(game=discord.Game(name='tk!yardım'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('tk!zar'):
        possible_responses = [
            '`1`Düştü',
            '`6`Düştü',
            '`5`Düştü',
            '`4`Düştü',
            '`3`Düştü',
            '`2`Düştü',
        ]
        await client.send_message(message.channel, random.choice(possible_responses))



    if message.content.startswith('tk!yardım'):
        await client.send_message(message.author, ' **tk!zar=Zar**\n**tk!espri=Espri Yapar**\n**tk!Avatar @ = Etiketlenen Kullanıcının Avatarını Gösterir.**\n**tk!foto = Benim Fotoğraflarımı Gösterir**\n**tk!kill @=Etiketlenen Kişiyi Öldürür.**\n**tk!hizmet = Hizmetten Memnun Kalıp Kalmadığımı Söyler**\n**tk!baliktut = Balık Tutar (*Banada Verirsiniz Bir Balık :stuck_out_tongue_winking_eye:*)**\n**tk!balıktut = Balıkları Gerçek Resimleriyle Tutar.**')
    if message.content.startswith('tk!help'):
        await client.send_message(message.author, ' **tk!zar=Zar**\n**tk!espri=Espri Yapar**\n**tk!Avatar @ = Etiketlenen Kullanıcının Avatarını Gösterir.**\n**tk!foto = Benim Fotoğraflarımı Gösterir**\n**tk!kill @=Etiketlenen Kişiyi Öldürür.**\n**tk!hizmet = Hizmetten Memnun Kalıp Kalmadığımı Söyler**\n**tk!baliktut = Balık Tutar (*Banada Verirsiniz Bir Balık :stuck_out_tongue_winking_eye:*)**\n**tk!balıktut = Balıkları Gerçek Resimleriyle Tutar.**')
    if message.content.startswith('tk!foto'):
        possible_responses = [
            'https://thumb.ibb.co/km79VS/Foto_raf0228.jpg',
            'https://thumb.ibb.co/k17hjn/Foto_raf0222.jpg',
            'https://thumb.ibb.co/du7nH7/Foto_raf0253.jpg',
            'https://thumb.ibb.co/n2LMS7/Foto_raf0258.jpg',
            'https://thumb.ibb.co/eVCoc7/Foto_raf0232.jpg',
            'https://thumb.ibb.co/nQ30qS/Foto_raf0253.jpg',
            'https://thumb.ibb.co/e0GQPn/Foto_raf0245.jpg',
            'https://thumb.ibb.co/mPo0qS/Foto_raf0246.jpg',
            'https://thumb.ibb.co/bx69jn/Foto_raf0237.jpg',
        ]
        await client.send_message(message.channel, random.choice(possible_responses))

    if message.content.startswith('tk!espri'):
        possible_responses = [
            'Kar üzerinde yürüyen adama ne denir. Karabasan.',
            'Yıkanan Ton’a ne denir? Washington!',
            'Adamın biri yarın öleceğim demiş. Yarmışlar ölmüş.',
            'Hadi oyun oynayalım. Vazgeçtim, oymadan oynayalım!',
            'Bir adamın ayakları kokmuş kolları linyit.',
            'Oğlumun adını mafya koydum, artık bi mafya babasıyım!',
            'Geçen gün bir taksi çevirdim; hala dönüyor!',
            '– Sözlüme neden 50 verdiniz hocam? +Sözlün kim evladım?',
            'Fransızların nesi eksiktir? “FRAN”ları tabi ki!',
            'Soru: Yangın dolabını açarsan ne olur? Cevap: Yang kızar.',
            '-Abi sizin araba ne malı? -Alman malı! Bizimki de klimalı!',
            'Geçen gün kamyonu sürdüm, Leonardo da Vinci.',
            'Kitabım evde kalmış, çünkü onun bir kocası yok!',
            'İyi ki İtalya da doğmamışız! Neden? Çünkü İtalyanca bilmiyoruz!',
            ' İphone alıcam. + 6 mı 7 mi? – Bitane yeter kanka.',
            '+Okeyde kıza elin nasıl dedim. -Ojeli dedi. +Ben Şoka girdim. -O Migrosa',
        ]
        await client.send_message(message.channel, random.choice(possible_responses))

    if message.content.startswith('tk!hizmet'):
        possible_responses = [
            'Gayet İyiydi',
            'İyiydi',
            'Normal',
            'Daha İyi Olabilirdi',
            'Kötü',
            'Çok Kötü',
        ]
        await client.send_message(message.channel, random.choice(possible_responses))
    if message.content.startswith('tk!balıktut'):
        possible_responses = [
            'https://thumb.ibb.co/j01Y9S/upra.jpg \n Çupra Tuttun',
            'Balık Tutamadın',
            'Balık Tutamadın',
            'Balık Tutamadın',
            'Balık Tutamadın',
            'Balık Tutamadın',
            'https://thumb.ibb.co/cOHvOn/alabal_k.jpg \n Alabalık Tuttun',
            'https://thumb.ibb.co/nCZLpS/hamsi.jpg \n Hamsi Tuttun',
            'https://thumb.ibb.co/d8gpin/istavrit.jpg \n İstavrit Tuttun',
            'https://thumb.ibb.co/cj2Jb7/l_fer.jpg \n Lüfer Balığı Tuttun',
            'https://thumb.ibb.co/deDwUS/palamut.jpg \n Palamut Tuttun',
            'https://thumb.ibb.co/naUOb7/uskumru.jpg \n Uskumru Tuttun',
        ]
        await client.send_message(message.channel, random.choice(possible_responses))
    if message.content.startswith('tk!baliktut'):
        possible_responses = [
            ':fish: Çupra Tuttun',
            'Balık Tutamadın',
            'Balık Tutamadın',
            'Balık Tutamadın',
            'Balık Tutamadın',
            'Balık Tutamadın',
            ':blowfish: Alabalık Tuttun',
            ':blowfish: Hamsi Tuttun',
            ':fish: İstavrit Tuttun',
            ':tropical_fish: Lüfer Balığı Tuttun',
            ':fish: Palamut Tuttun',
            ':blowfish: Uskumru Tuttun',
        ]
        await client.send_message(message.channel, random.choice(possible_responses))
client.run(TOKEN) 
