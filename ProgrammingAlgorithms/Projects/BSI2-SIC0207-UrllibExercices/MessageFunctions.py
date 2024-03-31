# módulos e-mail
import smtplib
import email.message  # coloquei no lugar de email.mime.text

# Função finalizada
def send_email(receiver, better_price, site):
    msg = email.message.Message()
    text = f"""
    Olá, funcionário do Starbuzz. O café está ${better_price}
    Agora é um bom momento para comprar café!
    Acesse: {site}
    
    Obrigado por usar este programa,
    Starbuzz"""

    # Definir parâmetros da mensagem
    msg["Subject"] = "Teste do Starbuzz"
    msg["From"] = "nanda.caetano2018@gmail.com"
    msg["To"] = receiver
    password = "xevnfxxrwyxwdwch"
    msg.set_payload(text)

    # Criar o servidor
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    # server.starttls()

    # Fazer login com as credenciais previamente informadas
    server.login(msg["From"], password)

    # Enivar a mensagem via server
    server.sendmail(msg["From"], [receiver], msg.as_string().encode("utf8"))
    server.close()
    
# Função não finalizada (em processo)
def send_telegram():

    # mensagem = "teste do starbuzz"

    api_key = "5641942650:AAGUMZ7HdsG5ZUrD_Mld-kSfR-Kypl-blUI"
    # api_id = "10667654"
    # api_hash = "1e31a13e7ede91580bf666e2b3f96c91"
    # bot_name = "starbuzzz_bot"

    # Criar o bot
    import telebot
    bot = telebot.TeleBot(api_key)

    # Enviar a mensagem
    # bot.send_message(receiver, message)

    api_key = "5641942650:AAGUMZ7HdsG5ZUrD_Mld-kSfR-Kypl-blUI"

    @bot.message_handler(commands="oi")
    def response(mensagem):
        bot.reply_to(mensagem, "oi")
        print(mensagem)

    bot.polling()


