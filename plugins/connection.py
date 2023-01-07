from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.connections_mdb import add_connection, all_connections, if_active, delete_connection
from info import ADMINS
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


@Client.on_message((filters.private | filters.group) & filters.command('connect'))
async def addconnection(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply(f"Vous êtes administrateur anonyme. Utilisez /connect {message.chat.id} en PM")
    chat_type = message.chat.type

    if chat_type == "private":
        try:
            cmd, group_id = message.text.split(" ", 1)
        except:
            await message.reply_text(
                "<b>Enter in correct format!</b>\n\n"
                "<code>/connect groupid</code>\n\n"
                "<i>Obtenez votre ID de groupe en ajoutant ce bot à votre groupe et utilisez  <code>/id</code></i>",
                quote=True
            )
            return

    elif chat_type in ["group", "supergroup"]:
        group_id = message.chat.id

    try:
        st = await client.get_chat_member(group_id, userid)
        if (
                st.status != "administrator"
                and st.status != "creator"
                and userid not in ADMINS
        ):
            await message.reply_text("Vous devez être administrateur dans le groupe donné!", quote=True)
            return
    except Exception as e:
        logger.exception(e)
        await message.reply_text(
            "Invalide Group ID!\n\nSi c’est correct, Assurez-vous que je suis présent dans votre groupe!!",
            quote=True,
        )

        return
    try:
        st = await client.get_chat_member(group_id, "me")
        if st.status == "administrator":
            ttl = await client.get_chat(group_id)
            title = ttl.title

            addcon = await add_connection(str(group_id), str(userid))
            if addcon:
                await message.reply_text(
                    f"Connexion réussie à **{title}**\nGérez maintenant votre groupe à partir de mon pm !",
                    quote=True,
                    parse_mode="md"
                )
                if chat_type in ["group", "supergroup"]:
                    await client.send_message(
                        userid,
                        f"Connecté à **{title}** !",
                        parse_mode="md"
                    )
            else:
                await message.reply_text(
                    "Vous êtes déjà connecté à ce chat!",
                    quote=True
                )
        else:
            await message.reply_text("Ajouter Moi en tant qu’administrateur dans le groupe", quote=True)
    except Exception as e:
        logger.exception(e)
        await message.reply_text('Une erreur s’est produite! Réessayez plus tard.', quote=True)
        return


@Client.on_message((filters.private | filters.group) & filters.command('disconnect'))
async def deleteconnection(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply(f"Vous êtes administrateur anonyme. Utilisez /connect {message.chat.id} en PM")
    chat_type = message.chat.type

    if chat_type == "private":
        await message.reply_text("Exécuter /connections pour afficher ou déconnecter des groupes!", quote=True)

    elif chat_type in ["group", "supergroup"]:
        group_id = message.chat.id

        st = await client.get_chat_member(group_id, userid)
        if (
                st.status != "administrator"
                and st.status != "creator"
                and str(userid) not in ADMINS
        ):
            return

        delcon = await delete_connection(str(userid), str(group_id))
        if delcon:
            await message.reply_text("Déconnexion réussie de ce chat", quote=True)
        else:
            await message.reply_text("Ce chat n’est pas connecté à moi!\nFaire /connect pour le connecter.", quote=True)


@Client.on_message(filters.private & filters.command(["connections"]))
async def connections(client, message):
    userid = message.from_user.id

    groupids = await all_connections(str(userid))
    if groupids is None:
        await message.reply_text(
            "Il n’y a pas de connexions actives !! Connectez-vous d’abord à certains groupes.",
            quote=True
        )
        return
    buttons = []
    for groupid in groupids:
        try:
            ttl = await client.get_chat(int(groupid))
            title = ttl.title
            active = await if_active(str(userid), str(groupid))
            act = " - ACTIVE" if active else ""
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=f"{title}{act}", callback_data=f"groupcb:{groupid}:{act}"
                    )
                ]
            )
        except:
            pass
    if buttons:
        await message.reply_text(
            "Détails de votre groupe connecté ;\n\n",
            reply_markup=InlineKeyboardMarkup(buttons),
            quote=True
        )
    else:
        await message.reply_text(
            "Il n’y a pas de connexions actives !! Connectez-vous d’abord à certains groupes.",
            quote=True
        )
