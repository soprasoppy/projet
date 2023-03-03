class script(object):
    START_TXT = """SALUT🖐  {},
𝙼𝙾𝙽 𝙽𝙾𝙼 𝙴𝚂𝚃 <a href=https://t.me/flaurabot>😍Belle flaura</a>, 𝙹𝙴 𝙿𝙴𝚄𝚇 𝚃𝙴 𝙵𝙾𝚄𝚁𝙽𝙸𝚁 𝙳𝙴𝚂 𝙵𝙸𝙻𝙼𝚂 𝙴𝚃 𝙳𝙴𝚂 𝚂𝙴𝚁𝙸𝙴𝚂, 𝙸𝙻 𝚂𝚄𝙵𝙵𝙸𝚃 𝙳𝙴 𝙼’𝙰𝙹𝙾𝚄𝚃𝙴𝚁 À 𝚃𝙾𝙽 𝙶𝚁𝙾𝚄𝙿𝙴 𝙴𝚃 𝙳𝙴 𝙿𝚁𝙾𝙵𝙸𝚃𝙴𝚁 😍"""
    HELP_TXT = """𝙷𝙴𝚈 {}
𝚅𝙾𝙸𝙲𝙸 𝙻’𝙰𝙸𝙳𝙴 𝙿𝙾𝚄𝚁 𝙼𝙴𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝙴𝚂."""
    ABOUT_TXT = """✯ 𝙼𝙾𝙽 𝙽𝙾𝙼: {}
✯ 𝙲𝚁𝙴𝙰𝚃𝙴𝚄𝚁: <a href=https://t.me/soprasoppy><b><i>🐿💈 MR SOPRA 💈🐿</i></b></a>
✯ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼
✯ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹
✯ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾 𝙳𝙱
✯ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: 𝙷𝙴𝚁𝙾𝙺𝚄
✯ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: v1.0.1 [ 𝙱𝙴𝚃𝙰 ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- Bᴇʟʟᴇ Flaura est un Projet Open Source. 
- Vous pouvez demandez le lien de prise en charge gratuitement ci-dessous 👇👇
- Source - <a href=https://t.me/filmserieshoww><b><i>FILMS SERIES SHOW</i></b></a>  

<b>DEVS:</b>
- <a href=https://t.me/soprasoppy><b><i>🐿 💈 MR SOPRA 💈🐿</i></b></a>"""
    MANUELFILTER_TXT = """Aide: <b>Filtres</b>

- Le filtre est ma fonctionnalité où vous pouvez définir des réponses automatisées pour un mot-clé particulier et Moi Belle Flaura répondra à chaque fois que ce mot-clé est employé dans le message

<b>NOTE:</b>
1. Bᴇʟʟᴇ Flaura devrait avoir un privilège d’administrateur.
2. Seuls les administrateurs peuvent ajouter des filtres dans un chat.
3. Les boutons d’alerte ont une limite de 64 caractères.

<b>Commandes et Utilisation:</b>
• /filter - <code>ajouter un filtre dans le chat</code>
• /filters - <code>lister tous les filtres d’un chat</code>
• /del - <code>supprimer un filtre spécifique dans le chat</code>
• /delall - <code>supprimer tous les filtres dans un chat (chat owner only)</code>"""
    BUTTON_TXT = """Aide: <b>Bouttons</b>

- Bᴇʟʟᴇ Flaura prends en charge les Boutons en ligne d’URL et d’alerte.

<b>NOTE:</b>
1. Telegram ne vous permettra pas d’envoyer des boutons sans aucun contenu, le contenu est donc obligatoire.
2. Bᴇʟʟᴇ Flaura prend en charge les boutons avec n’importe quel type de média de télégramme.
3. Les boutons doivent être correctement Analysés

<b>URL Buttons:</b>
<code>Bᴇʟʟᴇ Flaura votre meilleure amie 😘</code>

<b>Boutons d'alerte:</b>
<code>Un petit secret🤫 : Je suis la soeur de Katnice</code>"""
    AUTOFILTER_TXT = """Aide: <b>Filtre Auto</b>

<b>NOTE:</b>
1. Faites de moi un administratrice de votre chaîne même si elle est privée.
2. Assurez-vous que votre chaîne ne contient pas de porno, des fichiers soumis aux droits d'auteurs ou à caractères businness.
3. Transférez-moi le dernier message avec citations.
 J’ajouterai tous les fichiers de ce canal à ma Base de Donnée."""
    CONNECTION_TXT = """Aide: <b>Connections</b>

- Utilisez la connexion en PM pour la gestion des filtres 
- Il permet d’éviter le spamming dans les groupes.

<b>NOTE:</b>
1. Seuls les administrateurs peuvent ajouter une connexion.
2. Envoyer <code>/connect</code> pour me connecté à votre PM

<b>Commandes et utilisation:</b>
• /connect  - <code>connecter un chat particulier à votre PM</code>
• /disconnect  - <code>se déconnecter d’un chat</code>
• /connections - <code>Listes de toutes vos connexions</code>"""
    EXTRAMOD_TXT = """Aide: <b>Modules Extra</b>

<b>NOTE:</b>
Ce sont les caractéristiques supplémentaires de la Bᴇʟʟᴇ Aʟɪᴄᴇ

<b>Commandes et utilisation:</b>
• /id - <code>obtenir l’ID d’un utilisateur Spécifié.</code>
• /info  - <code>Obtenir des informations sur un utilisateur.</code>
• /imdb  - <code>Obtenir les informations sur le film à partir de source IMDb.</code>
• /search  - <code>Obtenir les informations sur le film à partir de diverses sources.</code>"""
    ADMIN_TXT = """Aide: <b>Admin Mods</b>

<b>NOTE:</b>
Ce module ne fonctionne que pour mes administrateurs

<b>Commandes et utilisation:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#Nᴏᴜᴠᴇᴀᴜ_Gʀᴏᴜᴘᴇ
Groupe = {}(<code>{}</code>)
Nombre Total de membres = <code>{}</code>
Ajouté Par - {}
"""
    LOG_TEXT_P = """#Nᴏᴜᴠᴇᴀᴜ_ᴜᴛɪʟɪsᴀᴛᴇᴜʀ
ID - <code>{}</code>
Nom - {} à démarré Bᴇʟʟᴇ Flaura
"""
