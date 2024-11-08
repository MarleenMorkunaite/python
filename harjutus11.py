# Harjutus 11
# 08.11.24 Marleen

def pikim_sona(*sonad):
    pikim = 0
    for i in sonad:
        if len(i)>pikim:
            pikim=len(i)
    print(f"Pikim sõna on: {pikim} märki!")


pikim_sona("üks", "kaks", "kolmkümmend", "kaheksa", "hgjhgjsjfsfsdgfdfddfdfd")