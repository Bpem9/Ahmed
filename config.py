URL = 'https://www.bazaraki.com/real-estate/houses-and-villas-rent/lemesos-district-limassol/?type_view=line&ordering=newest&price_max=1500'
HEADERS={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36 OPR/88.0.4412.53',
    'accept':'*/*'
}
ID_REG = r'/adv/([0-9]{7})(\_)(.*)'
HOUSE_TYPE_REG = r'(\s?)(.*)(\s)to rent$'
SITE = 'https://www.bazaraki.com'
HOST = 'ec2-34-247-172-149.eu-west-1.compute.amazonaws.com'
USER = 'ppsswfihmmxibr'
PASSWORD = 'f9f83210f506fc0660ad8c48d8b55897757fb8eb957647d1429d0026ce54ef38'
DATABASE = 'd5na09jr7u8pef'
PORT = '5432'
