class script(object):
    START_TXT = """SALUTπ  {},
πΌπΎπ½ π½πΎπΌ π΄ππ <a href=https://t.me/flaurabot>πBelle flaura</a>, πΉπ΄ πΏπ΄ππ ππ΄ π΅πΎπππ½πΈπ π³π΄π π΅πΈπ»πΌπ π΄π π³π΄π ππ΄ππΈπ΄π, πΈπ» πππ΅π΅πΈπ π³π΄ πΌβπ°πΉπΎπππ΄π Γ ππΎπ½ πΆππΎππΏπ΄ π΄π π³π΄ πΏππΎπ΅πΈππ΄π π"""
    HELP_TXT = """π·π΄π {}
ππΎπΈπ²πΈ π»βπ°πΈπ³π΄ πΏπΎππ πΌπ΄π π²πΎπΌπΌπ°π½π³π΄π."""
    ABOUT_TXT = """β― πΌπΎπ½ π½πΎπΌ: {}
β― π²ππ΄π°ππ΄ππ: <a href=https://t.me/soprasoppy><b><i>πΏπ MR SOPRA ππΏ</i></b></a>
β― π»πΈπ±ππ°ππ: πΏπππΎπΆππ°πΌ
β― π»π°π½πΆππ°πΆπ΄: πΏπππ·πΎπ½ πΉ
β― π³π°ππ° π±π°ππ΄: πΌπΎπ½πΆπΎ π³π±
β― π±πΎπ ππ΄πππ΄π: π·π΄ππΎπΊπ
β― π±ππΈπ»π³ πππ°πππ: v1.0.1 [ π±π΄ππ° ]"""
    SOURCE_TXT = """<b>NOTE:</b>
- Bα΄ΚΚα΄ Flaura est un Projet Open Source. 
- Vous pouvez demandez le lien de prise en charge gratuitement ci-dessous ππ
- Source - <a href=https://t.me/filmserieshoww><b><i>FILMS SERIES SHOW</i></b></a>  

<b>DEVS:</b>
- <a href=https://t.me/soprasoppy><b><i>πΏ π MR SOPRA ππΏ</i></b></a>"""
    MANUELFILTER_TXT = """Aide: <b>Filtres</b>

- Le filtre est ma fonctionnalitΓ© oΓΉ vous pouvez dΓ©finir des rΓ©ponses automatisΓ©es pour un mot-clΓ© particulier et Moi Belle Flaura rΓ©pondra Γ  chaque fois que ce mot-clΓ© est employΓ© dans le message

<b>NOTE:</b>
1. Bα΄ΚΚα΄ Flaura devrait avoir un privilΓ¨ge dβadministrateur.
2. Seuls les administrateurs peuvent ajouter des filtres dans un chat.
3. Les boutons dβalerte ont une limite de 64 caractΓ¨res.

<b>Commandes et Utilisation:</b>
β’ /filter - <code>ajouter un filtre dans le chat</code>
β’ /filters - <code>lister tous les filtres dβun chat</code>
β’ /del - <code>supprimer un filtre spΓ©cifique dans le chat</code>
β’ /delall - <code>supprimer tous les filtres dans un chat (chat owner only)</code>"""
    BUTTON_TXT = """Aide: <b>Bouttons</b>

- Bα΄ΚΚα΄ Flaura prends en charge les Boutons en ligne dβURL et dβalerte.

<b>NOTE:</b>
1. Telegram ne vous permettra pas dβenvoyer des boutons sans aucun contenu, le contenu est donc obligatoire.
2. Bα΄ΚΚα΄ Flaura prend en charge les boutons avec nβimporte quel type de mΓ©dia de tΓ©lΓ©gramme.
3. Les boutons doivent Γͺtre correctement AnalysΓ©s

<b>URL Buttons:</b>
<code>Bα΄ΚΚα΄ Flaura votre meilleure amie π</code>

<b>Boutons d'alerte:</b>
<code>Un petit secretπ€« : Je suis la soeur de Katnice</code>"""
    AUTOFILTER_TXT = """Aide: <b>Filtre Auto</b>

<b>NOTE:</b>
1. Faites de moi un administratrice de votre chaΓ?ne mΓͺme si elle est privΓ©e.
2. Assurez-vous que votre chaΓ?ne ne contient pas de porno, des fichiers soumis aux droits d'auteurs ou Γ  caractΓ¨res businness.
3. TransfΓ©rez-moi le dernier message avec citations.
 Jβajouterai tous les fichiers de ce canal Γ  ma Base de DonnΓ©e."""
    CONNECTION_TXT = """Aide: <b>Connections</b>

- Utilisez la connexion en PM pour la gestion des filtres 
- Il permet dβΓ©viter le spamming dans les groupes.

<b>NOTE:</b>
1. Seuls les administrateurs peuvent ajouter une connexion.
2. Envoyer <code>/connect</code> pour me connectΓ© Γ  votre PM

<b>Commandes et utilisation:</b>
β’ /connect  - <code>connecter un chat particulier Γ  votre PM</code>
β’ /disconnect  - <code>se dΓ©connecter dβun chat</code>
β’ /connections - <code>Listes de toutes vos connexions</code>"""
    EXTRAMOD_TXT = """Aide: <b>Modules Extra</b>

<b>NOTE:</b>
Ce sont les caractΓ©ristiques supplΓ©mentaires de la Bα΄ΚΚα΄ AΚΙͺα΄α΄

<b>Commandes et utilisation:</b>
β’ /id - <code>obtenir lβID dβun utilisateur SpΓ©cifiΓ©.</code>
β’ /info  - <code>Obtenir des informations sur un utilisateur.</code>
β’ /imdb  - <code>Obtenir les informations sur le film Γ  partir de source IMDb.</code>
β’ /search  - <code>Obtenir les informations sur le film Γ  partir de diverses sources.</code>"""
    ADMIN_TXT = """Aide: <b>Admin Mods</b>

<b>NOTE:</b>
Ce module ne fonctionne que pour mes administrateurs

<b>Commandes et utilisation:</b>
β’ /logs - <code>to get the rescent errors</code>
β’ /stats - <code>to get status of files in db.</code>
β’ /delete - <code>to delete a specific file from db.</code>
β’ /users - <code>to get list of my users and ids.</code>
β’ /chats - <code>to get list of the my chats and ids </code>
β’ /leave  - <code>to leave from a chat.</code>
β’ /disable  -  <code>do disable a chat.</code>
β’ /ban  - <code>to ban a user.</code>
β’ /unban  - <code>to unban a user.</code>
β’ /channel - <code>to get list of total connected channels</code>
β’ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """β ππΎππ°π» π΅πΈπ»π΄π: <code>{}</code>
β ππΎππ°π» πππ΄ππ: <code>{}</code>
β ππΎππ°π» π²π·π°ππ: <code>{}</code>
β πππ΄π³ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±
β π΅ππ΄π΄ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±"""
    LOG_TEXT_G = """#Nα΄α΄α΄ α΄α΄α΄_GΚα΄α΄α΄α΄
Groupe = {}(<code>{}</code>)
Nombre Total de membres = <code>{}</code>
AjoutΓ© Par - {}
"""
    LOG_TEXT_P = """#Nα΄α΄α΄ α΄α΄α΄_α΄α΄ΙͺΚΙͺsα΄α΄α΄α΄Κ
ID - <code>{}</code>
Nom - {} Γ  dΓ©marrΓ© Bα΄ΚΚα΄ Flaura
"""
