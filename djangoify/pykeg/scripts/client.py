import xmlrpclib
s = xmlrpclib.ServerProxy('http://localhost:9966')
while 1:
  user = raw_input('start flow: drinker? ').strip()
  s.AuthUser(user)
  raw_input('stop flow by hitting enter...')
  s.StopFlow()
  print ''