# -*- coding: cp1252 -*-
class Version:
    ConnectionKey = "iwixnunsnoayy161"
    Version = "1.96"
    
class Tokens:
    oldprotocol = "\r\r"

    #Token Catapult
    catapult = "\x05\x14"
    
    #Tokens do Modopwet
    Manipule = ")\x10"
    MainModo = '\x1d\x15'
    CloseReport = "#U"
    Watch = "#Q"
    BanHack = "#\x01"

    #Tokens de mapa
    Particule = "\x1a\x08"
    UserPosition = "\x1a\x1a"
    PositionMobile = "\x1a/"
    Mort = "\x1aJ"

    #Tokens do Rato
    HoleCheese = "Jf"
    gotCheese = "J6"
    placeObject = "J`"
    IceCube = "J\x0b"  	
    gotTicket = "J\x1f"
    Destruction = "J!"
    Saydamlastirma = "J\x14"
    Yikimiscisi = "J\x06"
    Yansitici = "J\x1b"

    #Tokens do chat
    Chat = "44" #Chat Message
    Whisper = "4h" #Sent Whisper
    Tribemsg = "4V" #Tribe Message
    Silence = "4\x05" #Silence
    scommand = "4b" #Sent Command

    #Tokens do client
    report = "V\x1f"
    idioma = "Vl" #Select Idioma
    useremote = "V\r"
    shoplist = "<;"
    Puan = "V\x0b"
    lo = "  "
    ping = "V\x04"
    zombie = "V\x06"
    shoplist2 = "V`"
    skills = "V\x01"
    meep = "V&"
    present = ",S"
    rpresent = ",_"
    spresent = ",\x05"
    cday = "V\x19"

    #Tokens da Tribo
    entertribe = '\x1b\r'
    tribecode = '\x1bl'

    #Tokens compra de morangos
    buyfraises = "\x07b"

    #Tokens da loja
    sendfraises = "`\x06"
    equipitem = "`f"
    buyitem = "`6"
    custombuy = "``"
    custom = "`\x0b"

    # Tokens não definidos #
    typechamane = "\x02b" 
    coleurchamane = "\x02f"

    #Trocar de senha (In-game)
    sentemailaddress = "\x02H"  # Digita o Email
    sentvalidatecode = "\x02\x07" # Valida o código
    codechangepass = "\x02\x1b" # Envia o código para mudar de senha
    changepass = "\x02\x14" # Digitar nova senha 

    #Trocar de senha (Index)
    recoverysend = "\x02\x05" # Digita o Usuário e o Email
    recoverysendvalidation = "\x02\x19" # Valida o código
    recoverychangepassword = "\x02\x1c" # Digite a nova senha

    #Stats
    gamelog = "\x02\x1a"
    stats = "\x02\x10"

    #vbig
    vbig = '\x03H'

    #lua
    lua = '$\r'
    presskey = "$l"

    idk = '\x04l'
    
    def __init__(self):
        self.data = []
