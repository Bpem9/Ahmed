URL = 'https://***/real-estate/houses-and-villas-rent/lemesos-district-limassol/?type_view=line&ordering=newest&price_max=1500'
HEADERS={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.53',
    'accept':'*/*'
}
ID_REG = r'/adv/([0-9]{7})(\_)(.*)'
HOUSE_TYPE_REG = r'(\s?)(.*)(\s)to rent$'
HOST = 'https://***'
tg_bot_token = '5330936569:AAFDerX7DkfrmcAZZhKenPCYcrec13RqAdw'