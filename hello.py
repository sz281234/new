from com.xebialabs.deployit.util import PasswordEncrypter
username = "admin"
adminPwd = PasswordEncrypter.getInstance().decrypt(releaseVariables['password'])
request = HttpRequest({'url': 'http://localhost:5516/api/v1/config/system-message'}, username, adminPwd)
