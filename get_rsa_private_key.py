from Crypto.PublicKey import RSA

n = 26179751854087331402331071604988485626982836276798177195222446151071273439780592994270737435017138406631242790569709
e = 65537

# valores obtidos com coda-nfs
p = 5146951772184269300025961189405010212772342675599485312661
q = 5086457579721431558131968975470302984140630429995118930169
#

phi_n = (p - 1) * (q - 1)
d = pow(e, -1, phi_n)

private_key = RSA.construct((n, e, d, p, q))
pem = private_key.export_key(format='PEM')

pem_file = open('private_key.pem', 'wb')
pem_file.write(pem)

print("Private Key =", pem.decode('utf-8'))
